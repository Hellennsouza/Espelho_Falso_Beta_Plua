# 🛡️ Operação Espelho Falso v8.2.1 Beta Plus

 **Plataforma de Perícia Biométrica &amp; Inteligência Financeira Antifraude no Pix**  
 *Detecção de Deepfakes, Assinatura de Silício (PRNU), Identity Graph e Explicabilidade Regulatória (XAI / LGPD Art. 20)*

### ⚠️ Aviso Legal / Disclaimer 

Este repositório possui caráter estritamente acadêmico, científico e de Pesquisa &amp; Desenvolvimento (P&amp;D). Este projeto **não possui vínculo formal, patrocínio, representação, endosso ou chancela oficial** de nenhuma instituição financeira, órgão de governo ou agência de inteligência/segurança citada (incluindo Itaú Unibanco, Banco Central do Brasil, CMN, ANPD, ABIN, INTERPOL, FATF/GAFI, FBI ou UNODC). Todas as análises, modelos técnicos, simulações e métricas apresentadas baseiam-se exclusivamente em dados sintéticos, literatura científica aberta, regulamentações públicas e dados de domínio público.

## 📌 Visão Geral

A **Operação Espelho Falso v8.2.1 Beta Plus** é um ecossistema de P&amp;D em Engenharia de Software e Perícia Financeira projetado para conter a nova onda de **Deepfakes**, **Virtual Camera Injections** e **Contas Mulas** em transações Pix e *onboarding* bancário.

Combinando **Edge-AI em ONNX Runtime WASM Int8 (&lt;50ms)**, **análise de ruído óptico no hardware (PRNU)**, **análise de grafos em streaming** e **Laudos Periciais XAI (FastTreeSHAP v2)**, o sistema automatiza a retenção cautelar do Pix (**Resolução BCB nº 142/2021**) reduzindo o SLA médio de análise da Lacuna L-02 de **120 horas para 3,8 horas**, mantendo conformidade com o **Art. 20 da LGPD** e a **Resolução CMN nº 4.966/21**.

---

## 🗂️ Estrutura do Repositório

```
espelho-falso-poc/
├── .gitlab-ci.yml                   # Pipeline de Integração e Deploy Contínuo (CI/CD)
├── .gitignore                       # Proteção contra vazamento acidental de chaves, PII e mídia local
├── LICENSE                          # Licença de Uso Institucional / P&amp;D
├── README.md                        # Documentação principal do repositório
├── requirements.txt                 # Dependências (OpenCV, MediaPipe, SciPy, SHAP, NetworkX, Streamlit, PyYAML)
│
├── src/                             # Código-fonte dos Módulos e Pipeline
│   ├── main_pipeline.py             # Pipeline Orquestrador Integrado com Telemetria SHA-256
│   ├── app_dashboard_p1.py          # Painel SOC Antifraude em Tempo Real (Streamlit / Plotly)
│   ├── onnx_wasm_liveness.js        # Engine de Borda ONNX Runtime WASM Int8 (Zero-Disk Persistence)
│   ├── kafka_event_producer.py      # Produtor de eventos de streaming para simulação do Pix
│   ├── module1_ocular_liveness.py   # Mód 1: Liveness Ocular Espectral, Sobel &amp; FFT (ISO/IEC 30107-3)
│   ├── module2_prnu_silicon.py      # Mód 2: Ruído de Silício PRNU &amp; Anti-Virtual Camera Injection
│   ├── module3_identity_graph.py    # Mód 3: Identity Graph (Algoritmo de Louvain &amp; PageRank)
│   └── module4_scib_xai.py          # Mód 4: Score SCIB, Trava BCB 142/21 &amp; Laudo XAI (LGPD Art. 20)
│
├── docs/                            # Repositório Central de Governança, Engenharia e Dossiês
│   ├── 01-architecture/            # Arquitetura de Software e Telemetria
│   │   ├── architecture-overview.md # Arquitetura ONNX WASM Int8 &amp; Edge-AI
│   │   ├── telemetry-and-audit.md   # Coletor de Telemetria Auditável SHA-256
│   │   └── zero-disk-persistence.md # Especificação de Processamento 100% Volátil em RAM (LGPD)
│   │
│   ├── 02-technical-modules/        # Especificações Técnicas dos 4 Módulos
│   │   ├── module1-ocular-liveness.md # Perícia Corneal e Micro-cintilação PWM
│   │   ├── module2-prnu-silicon.md    # Assinatura de Silício do Sensor Óptico
│   │   ├── module3-identity-graph.md  # Detecção de Enxames de Mulas em Streaming
│   │   └── module4-scib-xai.md        # Explicabilidade Algorítmica e FastTreeSHAP v2
│   │
│   ├── 03-compliance-and-dossiers/ # Dossiês Oficiais de Protocolo
│   │   ├── bacen-cmn-compliance.md  # Dossiê de Conformidade BCB Res. 142/21 e CMN 4.966/21
│   │   ├── anpd-lgpd-governance.md  # Dossiê de Governança ANPD / LGPD (Arts. 11 e 20)
│   │   ├── abin-sisbin-security.md  # Dossiê de Proteção de Infraestrutura Crítica (ABIN/SISBIN)
│   │   └── global-agencies-alignment.md # Alinhamento INTERPOL, FATF/GAFI, FBI e UNODC
│   │
│   ├── 04-api-and-schemas/          # Contratos de Integração e Schemas
│   │   ├── openapi-spec.yaml        # Especificação OpenAPI v3 das APIs Antifraude
│   │   └── laudo-xai-schema.json    # Schema JSON do Laudo Pericial de Explicabilidade
│   │
│   └── 05-operations-and-soc/       # Guias de Operação e Deploy
│       ├── deploy-production-checklist.md # Runbook e Checklist CI/CD para Produção
│       └── soc-dashboard-guide.md   # Manual de Operação do Painel SOC Streamlit
│
└── data/                            # Datasets Sintéticos e Telemetria
    ├── synthetic_sample.csv         # Dataset de transações sintéticas (0% dados reais)
    └── telemetry_runtime_state.json # Estado da telemetria em tempo real gerada pelo pipeline
    ├── README.md                    # Documentação da pasta data

```

---

## 🔬 Os 4 Pilares Técnicos

1. **Liveness Ocular Espectral (Módulo 1):** Inspeciona a especularidade corneal via gradiente de Sobel e a micro-cintilação PWM por FFT em telas digitais, atendendo à norma **ISO/IEC 30107-3** (APCER &lt; 0,1%, BPCER &lt; 1,0%).
2. **Assinatura de Silício PRNU (Módulo 2):** Valida a "digital física" única do sensor de imagem do dispositivo na camada HAL, bloqueando *Virtual Camera Injections*, emuladores e hooks de DLL.
3. **Identity Graph &amp; Comunidades de Mulas (Módulo 3):** Processamento em streaming via algoritmo de Louvain e PageRank em RAM, identificando e congelando enxames de contas mulas em milissegundos.
4. **Score SCIB &amp; Explicabilidade XAI (Módulo 4):** Unificação do score de risco (0 a 1000) com automação da trava cautelar do Pix (**Resolução BCB nº 142/2021**) e geração instantânea de **Laudos Periciais XAI** (**LGPD Art. 20**) via FastTreeSHAP v2.

---

## 📊 Métricas Chave de Desempenho

| Métrica                              | Valor Apurado        | Benefício Operacional                                               |
| ------------------------------------ | -------------------- | ------------------------------------------------------------------- |
| **Latência Média On-Device**         | **41,8 ms**          | Execução ultra-rápida sem impacto na UX do usuário no SuperApp      |
| **Throughput Processamento**         | **1.420 TPS**        | Suporta picos de volumetria do Pix em datas comemorativas           |
| **Otimização SLA Pix (Lacuna L-02)** | **3,8 horas**        | Redução drástica frente ao teto regulatório do Bacen (120 horas)    |
| **Persistência em Disco**            | **0% (RAM Volátil)** | Garantia de *Privacy by Design* conforme o Art. 11, II, 'g' da LGPD |
| **Integridade de Execução**          | **SHA-256**          | Assinatura imutável por transação para auditoria técnica            |

---

## 🏛️ Governança e Dossiês Institucionais

O repositório inclui dossiês completos em `docs/03-compliance-and-dossiers/` e relatórios em PDF formatados para protocolo direto perante os seguintes órgãos:

* 🏦 **Banco Central do Brasil (BCB) &amp; CMN:** Atendimento à Res. BCB nº 142/2021 e Res. CMN nº 4.966/21.
* 🔒 **ANPD / LGPD:** Garantia de ausência de vazamento (*Zero-Disk Persistence*) e direito de explicação automatizada (Art. 20).
* 🛡️ **ABIN &amp; SISBIN:** Proteção contra ataques à Infraestrutura Crítica do Sistema Financeiro Nacional (SFN).
* 🚓 **Organismos Internacionais (INTERPOL, FATF/GAFI, FBI):** Alinhamento aos relatórios globais sobre *Agentic AI* e *Cyber-Enabled Fraud*.

---

## 🚀 Quickstart: Como Executar

### 1\. Instalação das Dependências

```
pip install -r requirements.txt

```

### 2\. Execução do Pipeline Completo

```
python src/main_pipeline.py

```

### 3\. Inicialização do Painel SOC Antifraude

```
streamlit run src/app_dashboard_p1.py

```

---

## 📄 Licença e Autoria

* **Projeto:** Operação Espelho Falso v8.2.1 Beta Plus
* **Autoria &amp; P&amp;D:** Hellen Nunes dos Santos Souza
* **Licença:** MIT License / Propriedade Intelectual P&amp;D FinCrimes
