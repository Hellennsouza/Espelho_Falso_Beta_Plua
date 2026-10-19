"""
===============================================================================
PROJETO 1: OPERAÇÃO ESPELHO FALSO (v8.2.1 Beta Plus)
SUÍTE DE TESTES UNITÁRIOS AUTOMATIZADOS (UNITTEST / PYTEST)
===============================================================================
Autora: Dra. Hellen Nunes dos Santos Souza
===============================================================================
"""

import sys
import os
import unittest
import numpy as np

# Adiciona diretórios de busca de módulos ao sys.path
for path in ["/workspace/artifacts", "/workspace/scratch", "/workspace/src", "/workspace"]:
    if os.path.exists(path) and path not in sys.path:
        sys.path.insert(0, path)

# Importações dos Módulos do Projeto 1
try:
    from module1_ocular_liveness import OcularLivenessModule
    from module2_prnu_silicon import PRNUCameraSignatureModule
    from module3_identity_graph import IdentityGraphAnalytics
    from module4_scib_xai import SCIBScoreAndXAIModule
    from main_pipeline import EspelhoFalsoUnifiedPipeline
except ImportError:
    from src.module1_ocular_liveness import OcularLivenessModule
    from src.module2_prnu_silicon import PRNUCameraSignatureModule
    from src.module3_identity_graph import IdentityGraphAnalytics
    from src.module4_scib_xai import SCIBScoreAndXAIModule
    from src.main_pipeline import EspelhoFalsoUnifiedPipeline


class TestModule1OcularLiveness(unittest.TestCase):
    """Testes unitários para o Módulo 1 (Visão Computacional e Liveness Ocular)."""

    def setUp(self):
        self.mod1 = OcularLivenessModule(fps=30, buffer_size=15)

    def test_init(self):
        self.assertIsNotNone(self.mod1)
        self.assertEqual(self.mod1.buffer_size, 15)

    def test_process_frame(self):
        dummy_frame = np.random.randint(50, 200, (480, 640, 3), dtype=np.uint8)
        metrics, annotated = self.mod1.process_frame(dummy_frame)
        
        self.assertIsInstance(metrics, dict)
        self.assertIsNotNone(annotated)
        self.assertEqual(annotated.shape, dummy_frame.shape)


class TestModule2PRNUSilicon(unittest.TestCase):
    """Testes unitários para o Módulo 2 (PRNU de Silício e Anti-Virtual Camera)."""

    def setUp(self):
        self.mod2 = PRNUCameraSignatureModule()

    def test_init(self):
        self.assertIsNotNone(self.mod2)

    def test_extract_and_correlate(self):
        dummy_frame = np.random.randint(0, 255, (480, 640, 3), dtype=np.uint8)
        metrics, _, _ = self.mod2.process_frame(dummy_frame)
        
        self.assertIsInstance(metrics, dict)


class TestModule3IdentityGraph(unittest.TestCase):
    """Testes unitários para o Módulo 3 (Graph Analytics e Comunidades de Mulas)."""

    def setUp(self):
        self.mod3 = IdentityGraphAnalytics()

    def test_graph_pipeline(self):
        results = self.mod3.run_pipeline()
        self.assertIsInstance(results, dict)


class TestModule4SCIBXAI(unittest.TestCase):
    """Testes unitários para o Módulo 4 (Score SCIB, Trava Pix e XAI FastTreeSHAP v2)."""

    def setUp(self):
        self.mod4 = SCIBScoreAndXAIModule()

    def test_process_transaction_legit(self):
        feature_vector = {
            "f1_corneal_gradient": 12.0,
            "f2_spectral_saturation": 25.0,
            "f3_fft_power": 15.0,
            "f4_prnu_correlation": 0.85,
            "f5_device_integrity": 1.0,
            "f6_graph_mule_risk": 0.05,
            "f7_behavioral_score": 0.05
        }
        res = self.mod4.process_transaction(feature_vector, "TX_TEST_LEGIT")
        self.assertIsInstance(res, dict)
        self.assertIn("scib_score", res)
        self.assertLess(res["scib_score"], 750)

    def test_process_transaction_fraud(self):
        feature_vector = {
            "f1_corneal_gradient": 58.5,
            "f2_spectral_saturation": 145.2,
            "f3_fft_power": 210.0,
            "f4_prnu_correlation": 0.02,
            "f5_device_integrity": 0.0,
            "f6_graph_mule_risk": 0.95,
            "f7_behavioral_score": 0.95
        }
        res = self.mod4.process_transaction(feature_vector, "TX_TEST_FRAUD")
        self.assertIsInstance(res, dict)
        self.assertIn("scib_score", res)
        self.assertGreaterEqual(res["scib_score"], 750)
        self.assertIn("laudo_pericial_lgpd_text", res)


class TestEspelhoFalsoUnifiedPipeline(unittest.TestCase):
    """Testes unitários de Integração End-to-End no Pipeline Unificado."""

    def setUp(self):
        self.pipeline = EspelhoFalsoUnifiedPipeline()

    def test_execute_transaction_check_legit(self):
        frame = np.random.randint(40, 200, (480, 640, 3), dtype=np.uint8)
        meta = {
            "transaction_id": "TX_TEST_INTEG_01",
            "account_id": "ACC_LEGIT_99",
            "device_id": "DEV_REAL_IPHONE",
            "ip_address": "189.10.20.30",
            "is_emulator": False,
            "behavioral_score": 0.02
        }
        report, annotated = self.pipeline.execute_transaction_check(frame, meta)
        
        self.assertIsNotNone(report)
        self.assertEqual(report["zero_disk_ram_status"], "VERIFIED_VOLATILE")
        self.assertLess(report["module_4_final_decision"]["scib_score"], 750)

    def test_execute_transaction_check_fraud(self):
        frame = np.random.randint(0, 255, (480, 640, 3), dtype=np.uint8)
        meta = {
            "transaction_id": "TX_TEST_INTEG_FRAUD",
            "account_id": "ACC_MULE_88",
            "device_id": "DEV_MULE_EMULATOR",
            "ip_address": "185.220.101.10",
            "is_emulator": True,
            "behavioral_score": 0.95,
            "override_f1_grad": 60.0,
            "override_f2_sat": 150.0,
            "override_f3_fft": 220.0,
            "override_f4_prnu": 0.01,
            "is_mule_cluster_override": True
        }
        report, annotated = self.pipeline.execute_transaction_check(frame, meta)
        
        self.assertIsNotNone(report)
        self.assertGreaterEqual(report["module_4_final_decision"]["scib_score"], 750)
        self.assertIn("LAUDO PERICIAL DE EXPLICABILIDADE", report["module_4_final_decision"]["laudo_pericial_lgpd_text"])


if __name__ == "__main__":
    unittest.main()
