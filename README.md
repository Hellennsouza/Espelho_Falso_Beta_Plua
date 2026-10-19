# 🛡️ Operação Espelho Falso — Versão Beta (PoC Autônoma)

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Computer_Vision-OpenCV%20%7C%20MediaPipe-green.svg)](https://opencv.org/)
[![XAI](https://img.shields.io/badge/Explainable_AI-SHAP%20%7C%20LIME-orange.svg)](https://shap.readthedocs.io/)
[![Graph Analytics](https://img.shields.io/badge/Network_Science-NetworkX-purple.svg)](https://networkx.org/)
[![Compliance](https://img.shields.io/badge/LGPD-Art._11%2C_II%2C_'g'-brightgreen.svg)](http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm)
[![ISO Benchmark](https://img.shields.io/badge/ISO%2FIEC-30107--3-blueviolet.svg)](https://www.iso.org/standard/67381.html)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📌 Visão Geral do Projeto

A **Operação Espelho Falso (Versão Beta PoC)** é uma arquitetura de Prova de Conceito (PoC) autônoma em **Visão Computacional, Biometria Espectral, Análise de Grafos e Explicabilidade de IA (XAI)** desenvolvida para combate a fraudes de identidade, injeção virtual de vídeo, ataques por *deepfakes* 4K e enxames de contas mulas no onboarding de instituições financeiras.

Desenvolvida sob os princípios de **Privacy by Design**, a solução opera com processamento em memória RAM volátil (**Zero-Disk Persistence**), garantindo conformidade absoluta com o **Art. 11, II, "g" da LGPD** (prevenção à fraude na identificação e autenticação do titular).

---

## 🏗️ Arquitetura dos Módulos Técnicos

O sistema é composto por 4 módulos autônomos integrados em uma esteira de avaliação em tempo real:

```
[ FRAME DA CÂMERA / TRANSAÇÃO ]
              │
              ├──► [ MÓDULO 1: Visão Computacional & Liveness ] 
              │     └─► Gradiente Corneal (Sobel), Decomposição HSV/CIELAB, FFT Temporal (PWM 60-240Hz)
              │
              ├──► [ MÓDULO 2: Assinatura de Silício & Hardware ]
              │     └─► Extração de Ruído PRNU de Sensor, Validação TEE/Secure Enclave & Bloqueio de Câmeras Virtuais
              │
              ├──► [ MÓDULO 3: Identity Graph Analytics ]
              │     └─► Mapeamento de Redes Multimodais em NetworkX, Algoritmo de Louvain & PageRank de Risco
              │
              └──► [ MÓDULO 4: Score SCIB, Trava Cautelar & XAI ]
                    ├─► Consolidação do Score SCIB (0 a 1000) via RandomForest Quantizado
                    ├─► Disparo da Trava Cautelar de Crédito/PIX (Resolução BCB nº 142/2021) se SCIB >= 750
                    └─► Geração do Laudo Pericial de Explicabilidade Algorítmica (LGPD Art. 20 via SHAP/LIME)
```

---

## 📂 Estrutura do Repositório

```text
espelho-falso-poc/
├── .gitignore                   # Proteção contra vazamento acidental de imagens/vídeos locais
├── LICENSE                      # Licença Open Source MIT
├── README.md                    # Documentação principal do projeto
├── requirements.txt             # Dependências de execução (OpenCV, MediaPipe, SciPy, SHAP, NetworkX)
├── docs/
│   ├── projeto_1_operacao_espelho_falso_beta_poc.pdf   # Relatório Técnico Estrutural (10 Páginas)
│   └── projeto_1_espelho_falso_beta_poc_checklist.xlsx # Planilha de Acompanhamento de Bancada
├── src/
│   ├── module1_ocular_liveness.py # Mód 1: Gradiente Corneal, HSV e FFT Temporal
│   ├── module2_prnu_silicon.py    # Mód 2: Ruído de Silício PRNU & Câmeras Virtuais
│   ├── module3_identity_graph.py  # Mód 3: Identity Graph & Algoritmo de Louvain
│   ├── module4_scib_xai.py        # Mód 4: Score SCIB, Trava BCB 142/21 & XAI SHAP/LIME
│   └── main_pipeline.py           # Pipeline Orquestrador Integrado (End-to-End)
└── data/
    └── synthetic_sample.csv       # Dataset sintético de transações (0% dados pessoais reais)
```

---

## 🔒 Privacidade & Governança (LGPD & BACEN)

* **Zero-Disk Persistence:** Nenhum frame de vídeo ou imagem biométrica é gravado no disco rígido. Todo o cálculo ocorre no *buffer* volátil da memória RAM (`io.BytesIO`), descartando os quadros imediatamente após a extração dos vetores numéricos.
* **Vetorização Irreversível:** Biometria convertida em tensores matemáticos unidirecionais.
* **Resolução BCB nº 142/2021:** Disparo automatizado de retenção cautelar de limites e transações PIX/Crédito quando o Score SCIB ultrapassa 750 pontos.
* **Art. 20 da LGPD (Explicabilidade Algorítmica):** Geração automática de Laudos Periciais de XAI legíveis em linguagem natural contendo a justificativa motivadora dos pesos matemáticos para auditorias e defesas jurídicas.

---

## 🚀 Como Executar no Seu Ambiente Local

### 1. Clonar o Repositório e Criar o Ambiente Virtual
```bash
git clone https://github.com/seu-usuario/espelho-falso-poc.git
cd espelho-falso-poc

# Criar ambiente virtual
python -m venv venv

# Ativar no Linux/Mac:
source venv/bin/activate
# Ativar no Windows:
venv\Scripts\activate
```

### 2. Instalar as Dependências
```bash
pip install -r requirements.txt
```

### 3. Executar o Pipeline Integrado (Todos os Módulos)
```bash
python src/main_pipeline.py
```

### 4. Executar Módulos Individuais em Bancada
```bash
# Teste do Módulo 1 (Liveness Ocular ao vivo na webcam ou vídeo sintético)
python src/module1_ocular_liveness.py 0

# Teste do Módulo 2 (Assinatura PRNU de Câmera)
python src/module2_prnu_silicon.py test

# Teste do Módulo 3 (Grafo de Contas Mulas)
python src/module3_identity_graph.py

# Teste do Módulo 4 (Score SCIB & Laudo XAI)
python src/module4_scib_xai.py
```

---

## 📊 Exemplo de Saída do Laudo Pericial de XAI (LGPD Art. 20)

Quando uma transação suspeita é retida, o Módulo 4 gera a seguinte auditoria explicável:

```text
=======================================================================
LAUDO PERICIAL DE EXPLICABILIDADE ALGORÍTMICA (XAI) — LGPD ART. 20
PROJETO 1: OPERAÇÃO ESPELHO FALSO (v8.0)
=======================================================================
ID Transação: TX_FRAUD_9909
Data/Hora UTC: 2026-10-07T00:46:55.636509+00:00
Score SCIB Calculado: 1000 / 1000 pontos
Decisão Automatizada: 🔴 REJEITADO / RETIDO
Ação no Core Bancário: LOCK_ACCOUNTS_TRAVA_CAUTELAR
Respaldo Legal: Resolução BCB nº 142/2021 & Art. 11, II, 'g' da LGPD
-----------------------------------------------------------------------
JUSTIFICATIVA TÉCNICA MOTIVADORA (AUDITORIA DE DECISÃO IA):
• Ausência de ruído físico de silício do sensor de câmera (Injeção Virtual por Software). (Peso: +0.194)
• Superfície óptica reflexiva incompatível com curvatura corneal humana (Ataque por Tela Digital). (Peso: +0.142)
• Frequência de cintilação temporal detectada (Modulação PWM de Tela de Display). (Peso: +0.110)
=======================================================================
```

---

## 🎯 Benchmarks de Teste em Bancada (ISO/IEC 30107-3)

A PoC é avaliada contra 5 categorias de ataque utilizando métricas internacionais:
* **APCER (Attack Presentation Classification Error Rate):** Target `< 0,1%`
* **BPCER (Bona Fide Presentation Classification Error Rate):** Target `< 1,0%`

---

## 👩‍💻 Autoria e Pesquisa

* **Autora & Desenvolvedora:** Dra. Hellen Nunes dos Santos Souza
* **Foco:** Pesquisa & Desenvolvimento em Visão Computacional, Biometria Antifraude, Graph Analytics e Explicabilidade de IA (XAI).
* **Contato / LinkedIn:** [Meu Perfil no LinkedIn](https://www.linkedin.com/)

---
*Isenção de Responsabilidade: Este repositório é um projeto de Pesquisa e Desenvolvimento (P&D) focado em Prova de Conceito (PoC) utilizando exclusivamente dados sintéticos e simulações de bancada.*
