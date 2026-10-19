# Checklist Operacional de Deploy em Producao (Runbook)

## Pre-Requisitos de Infraestrutura
- Cluster Kubernetes / OpenShift configurado com suporte a GPU/SIMD.
- Topicos Kafka e tabelas ClickHouse provisionados para ingestao streaming sem PII.
- Runtime ONNX WASM Int8 validado em navegadores Chrome, Safari e Android/iOS WebViews.

## Passos da Esteira CI/CD (.gitlab-ci.yml)
1. Estagio Test: Executar testes unitarios nos 4 modulos (pytest test_pipeline.py).
2. Estagio Build: Compilar artefatos WASM Int8 e empacotar conteineres.
3. Estagio Compliance Check: Validar esquemas JSON e integridade de hashes SHA-256.
4. Estagio Deploy: Promover para o ambiente de producao com estrategia Canary.
