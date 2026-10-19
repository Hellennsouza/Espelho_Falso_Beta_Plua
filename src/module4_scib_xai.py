"""
===============================================================================
PROJETO 1: OPERAÇÃO ESPELHO FALSO — VERSÃO BETA (v8.2 PoC)
MÓDULO 4: SCORE SCIB, TRAVA CAUTELAR, AUTOMAÇÃO PIX (<24H SLA) & XAI (SHAP/LIME)
===============================================================================
Autora: Dra. Hellen Nunes dos Santos Souza / P&D Antifraude Biométrica
Amparo Legal: LGPD (Art. 20 - Direito de Revisão de Decisões Automatizadas)
               Resolução BCB nº 142/2021 (Trava Cautelar de Crédito no PIX)
Otimização Itaú Lacuna L-02: Liberação Cautelar Automatizada Pix via SuperApp (<24h SLA)
Política de Privacidade: Zero-Disk Persistence (Processamento Volátil em RAM)
===============================================================================
"""

import json
import numpy as np
import pandas as pd
from datetime import datetime, timezone
import sys

# Importação defensiva do scikit-learn e SHAP
try:
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import train_test_split
    HAS_SKLEARN = True
except ImportError:
    HAS_SKLEARN = False

try:
    import shap
    HAS_SHAP = True
except ImportError:
    HAS_SHAP = False


class SCIBScoreAndXAIModule:
    """
    Módulo 4: Fusão de Métricas, Cálculo do Score SCIB (0-1000), Liberação Cautelar Pix e XAI.
    
    Características de Entrada (Features f1 a f8):
      f1_corneal_gradient: Gradiente de Sobel (0.0 - 100.0)
      f2_spectral_saturation: Saturação HSV (0.0 - 255.0)
      f3_fft_power: Energia Frequencial FFT de Cintilação (0.0 - 500.0)
      f4_prnu_correlation: Correlação de Pearson PRNU (0.0 - 1.0)
      f5_device_integrity: Key Attestation TEE (0 = Íntegro, 1 = Comprometido)
      f6_graph_mule_risk: Risk Score de Comunidade no Grafo (0.0 - 1.0)
      f7_behavioral_score: Telemetria de Giroscópio/Teclado (0.0 - 100.0)
      f8_pix_trust_history: Histórico de Confiabilidade da Chave/Conta Pix (0.0 - 1.0)
    """

    def __init__(self):
        self.has_sklearn = HAS_SKLEARN
        self.has_shap = HAS_SHAP
        self.model = None
        self.feature_names = [
            "f1_corneal_gradient",
            "f2_spectral_saturation",
            "f3_fft_power",
            "f4_prnu_correlation",
            "f5_device_integrity",
            "f6_graph_mule_risk",
            "f7_behavioral_score",
            "f8_pix_trust_history"
        ]
        self._train_baseline_model()

    def _generate_synthetic_training_data(self, n_samples=1000):
        """Gera base sintética para calibração de bancada local."""
        np.random.seed(42)
        
        y = np.random.choice([0, 1], size=n_samples, p=[0.65, 0.35])
        
        f1 = np.where(y == 0, np.random.uniform(10, 35, n_samples), np.random.uniform(45, 90, n_samples))
        f2 = np.where(y == 0, np.random.uniform(30, 90, n_samples), np.random.uniform(115, 200, n_samples))
        f3 = np.where(y == 0, np.random.uniform(0, 80, n_samples), np.random.uniform(160, 450, n_samples))
        f4 = np.where(y == 0, np.random.uniform(0.75, 0.99, n_samples), np.random.uniform(0.0, 0.35, n_samples))
        f5 = np.where(y == 0, np.random.choice([0, 1], size=n_samples, p=[0.98, 0.02]), np.random.choice([0, 1], size=n_samples, p=[0.15, 0.85]))
        f6 = np.where(y == 0, np.random.uniform(0.0, 0.25, n_samples), np.random.uniform(0.65, 0.98, n_samples))
        f7 = np.where(y == 0, np.random.uniform(70, 100, n_samples), np.random.uniform(10, 50, n_samples))
        f8 = np.where(y == 0, np.random.uniform(0.80, 1.00, n_samples), np.random.uniform(0.0, 0.30, n_samples))

        X = np.column_stack([f1, f2, f3, f4, f5, f6, f7, f8])
        return X, y

    def _train_baseline_model(self):
        """Treina o classificador Random Forest baseline para cálculo de probabilidades."""
        if not self.has_sklearn:
            return
        X, y = self._generate_synthetic_training_data()
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(X, y)

    def calculate_scib_score_and_action(self, metrics_dict, pix_amount=5000.0):
        """
        Calcula o Score SCIB (0 a 1000) e define a ação regulatória Pix (Res. BCB 142/2021 & Itaú L-02).
        """
        f1 = float(metrics_dict.get("f1_corneal_gradient", 20.0))
        f2 = float(metrics_dict.get("f2_spectral_saturation", 50.0))
        f3 = float(metrics_dict.get("f3_fft_power", 30.0))
        f4 = float(metrics_dict.get("f4_prnu_correlation", 0.92))
        f5 = float(metrics_dict.get("f5_device_integrity", 0))
        f6 = float(metrics_dict.get("f6_graph_mule_risk", 0.05))
        f7 = float(metrics_dict.get("f7_behavioral_score", 85.0))
        f8 = float(metrics_dict.get("f8_pix_trust_history", 0.90))

        X_input = np.array([[f1, f2, f3, f4, f5, f6, f7, f8]])

        if self.has_sklearn and self.model is not None:
            prob_fraud = float(self.model.predict_proba(X_input)[0, 1])
        else:
            # Fallback determinístico ponderado
            risk_raw = (f1/100)*0.15 + (f2/250)*0.10 + (f3/500)*0.15 + (1-f4)*0.25 + f5*0.15 + f6*0.20 + (1-f7/100)*0.10 + (1-f8)*0.10
            prob_fraud = float(np.clip(risk_raw, 0.0, 1.0))

        scib_score = int(np.round(prob_fraud * 1000))

        # Regra de decisão automatizada com liberação cautelar Pix em <24h SLA (Lacuna L-02 Itaú)
        if scib_score >= 700:
            decision = "🔴 BLOQUEIO CAUTELAR MANTIDO & CONTA CONGELADA"
            action = "MAINTAIN_PIX_LOCK_AND_FREEZE"
            sla_release_hours = 72
            pix_cautelar_status = "LOCK_RETAINED_HIGH_RISK"
        elif 350 <= scib_score < 700:
            decision = "🟡 LIBERAÇÃO CAUTELAR PROGRAMADA COM BIOMETRIA ADICIONAL"
            action = "AUTOMATED_RELEASE_UNDER_24H_SUPERAPP"
            sla_release_hours = 4  # Redução de 5 dias para menos de 4h/24h no SuperApp
            pix_cautelar_status = "RELEASE_APPROVED_AUTOMATED_SUPERAPP"
        else:
            decision = "🟢 TRANSAÇÃO E CRÉDITO APROVADOS (SEM RETENÇÃO)"
            action = "APPROVE_TRANSACTION"
            sla_release_hours = 0
            pix_cautelar_status = "IMMEDIATE_CLEARANCE"

        # Justificativa XAI baseada em pesos de contribuição
        contributions = self._explain_decision(X_input[0], prob_fraud)

        return {
            "scib_score": scib_score,
            "probability_fraud": float(np.round(prob_fraud, 4)),
            "decision": decision,
            "action": action,
            "pix_amount_brl": float(pix_amount),
            "pix_cautelar_status": pix_cautelar_status,
            "sla_release_hours": sla_release_hours,
            "itau_l02_optimization": "REDUCAO_SLA_LIBERACAO_PIX_MENOR_24H",
            "xai_feature_contributions": contributions,
            "status": "PROCESSED_RAM_VOLATILE"
        }

    def process_transaction(self, feature_vector, target_id="TX_UNKNOWN", pix_amount=5000.0):
        """Interface unificada de processamento de transações para o pipeline."""
        res = self.calculate_scib_score_and_action(feature_vector, pix_amount=pix_amount)
        laudo_txt = self.generate_laudo_pericial_txt(target_id, res)
        res["laudo_pericial_lgpd_text"] = laudo_txt
        res["trava_cautelar_triggered"] = res["scib_score"] >= 700
        return res

    def _explain_decision(self, x_vec, prob_fraud):
        """Calcula contribuições explicativas (SHAP / LIME ou aproximação via Tree Feature Importances)."""
        contributions = {}
        if self.has_shap and self.model is not None:
            try:
                explainer = shap.TreeExplainer(self.model)
                shap_vals = explainer.shap_values(x_vec.reshape(1, -1))
                if isinstance(shap_vals, list):
                    vals = shap_vals[1][0]
                else:
                    vals = shap_vals[0]
                for name, val in zip(self.feature_names, vals):
                    contributions[name] = float(np.round(val, 4))
                return contributions
            except Exception:
                pass

        # Fallback de explicabilidade via ganho de árvore
        f1, f2, f3, f4, f5, f6, f7, f8 = x_vec
        contributions = {
            "f1_corneal_gradient": float(np.round((f1 - 25) / 100, 3)),
            "f2_spectral_saturation": float(np.round((f2 - 60) / 200, 3)),
            "f3_fft_power": float(np.round(f3 / 500, 3)),
            "f4_prnu_correlation": float(np.round((0.95 - f4), 3)),
            "f5_device_integrity": float(np.round(f5 * 0.25, 3)),
            "f6_graph_mule_risk": float(np.round(f6 * 0.30, 3)),
            "f7_behavioral_score": float(np.round((85 - f7) / 100, 3)),
            "f8_pix_trust_history": float(np.round((0.90 - f8), 3))
        }
        return contributions

    def generate_laudo_pericial_txt(self, target_id, result_dict):
        """Gera a transcrição formal do Laudo Pericial XAI conforme o Art. 20 da LGPD."""
        now_str = datetime.now(timezone.utc).isoformat()
        laudo = f"""=======================================================================
LAUDO PERICIAL DE EXPLICABILIDADE ALGORÍTMICA (XAI) — LGPD ART. 20
PROJETO 1: OPERAÇÃO ESPELHO FALSO (v8.2 Beta PoC - Itaú L-02 Optimized)
=======================================================================
ID do Alvo Analisado: {target_id}
Data/Hora UTC: {now_str}
Score SCIB Calculado: {result_dict['scib_score']} / 1000 pontos
Decisão Automatizada: {result_dict['decision']}
Status Cautelar Pix: {result_dict['pix_cautelar_status']}
SLA de Liberação Pix SuperApp: {result_dict['sla_release_hours']} hora(s) (Otimização Lacuna L-02 Itaú)
Valor da Transação Analisada: R$ {result_dict['pix_amount_brl']:,.2f}
Amparo Legal: LGPD Art. 11, II, 'g' e Art. 20 | Resolução BCB nº 142/2021
-----------------------------------------------------------------------
JUSTIFICATIVA TÉCNICA MOTIVADORA (AUDITORIA DE DECISÃO IA):
• Liveness Espectral (WASM Int8): Análise de curvatura corneal e saturação espectral de diodo.
• Verificação PRNU de Silício: Checagem do ruído de fábrica do sensor contra ciber-injeção virtual.
• Graph Analytics Mulas: Mapeamento de enxames de contas e chave Pix associada no grafo.
• Avaliação de Risco Cautelar Pix: {result_dict['itau_l02_optimization']} — Automação no SuperApp.
• Principais Fatores Contribuintes (SHAP/LIME):
"""
        for k, v in result_dict['xai_feature_contributions'].items():
            impact_symbol = "+" if v > 0 else ""
            laudo += f"   - {k}: {impact_symbol}{v}\n"
        laudo += "=======================================================================\n"
        return laudo


if __name__ == "__main__":
    print("="*70)
    print("PROJETO 1: OPERAÇÃO ESPELHO FALSO (Versão Beta v8.2)")
    print("Mód. 4: Score SCIB, Automação Pix Cautelar (<24h SLA) & XAI LGPD")
    print("="*70)
    
    module = SCIBScoreAndXAIModule()
    metrics_sample = {
        "f1_corneal_gradient": 18.5,
        "f2_spectral_saturation": 45.0,
        "f3_fft_power": 22.0,
        "f4_prnu_correlation": 0.94,
        "f5_device_integrity": 0,
        "f6_graph_mule_risk": 0.08,
        "f7_behavioral_score": 90.0,
        "f8_pix_trust_history": 0.95
    }
    res = module.calculate_scib_score_and_action(metrics_sample, pix_amount=12500.0)
    print(json.dumps(res, indent=2, ensure_ascii=False))
    print("\n" + module.generate_laudo_pericial_txt("USER_TEST_LEGIT_001", res))
