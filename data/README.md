# 📂 Data Directory — Operação Espelho Falso (v8.2.1 Beta Plus)

Esta pasta contém o dataset sintético de testes e o arquivo de estado de telemetria em tempo real gerado pelo pipeline de execução.

---

### 📄 Arquivos do Diretório:

1. **`synthetic_sample.csv`**:
   - Dataset sintético de 500 transações Pix simuladas.
   - **Garantia LGPD (Art. 11, II, 'g'):** 0% de dados pessoais reais ou PII.
   - Contém métricas de Liveness Ocular, Assinatura PRNU de Silício, Identity Graph e Score SCIB.

2. **`telemetry_runtime_state.json`**:
   - Estado de telemetria em tempo real exportado pelo orquestrador `main_pipeline.py`.
   - Registra indicadores de desempenho da borda (41.8 ms, 1.420 TPS), médias de SLA (3.8h) e assinatura digital imutável com **Hash SHA-256**.
