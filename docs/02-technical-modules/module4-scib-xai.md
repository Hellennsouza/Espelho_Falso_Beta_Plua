# Modulo 4: Motor de Pontuacao SCIB e Explicabilidade XAI (FastTreeSHAP v2)

## Visao Geral
O **Modulo 4** consolida os sinais de risco dos Modulos 1, 2 e 3 em um valor unificado de risco — o **Score SCIB** (0 a 1000) — e gera o **Laudo Pericial de Explicabilidade (XAI)** exigido pelo **Art. 20 da LGPD** e pela **Resolucao CMN no 4.966/21**.

## Escala do Score SCIB
- **0 a 200 (Baixo Risco / Bona Fide)**: Aprovacao automatica instantanea (<50 ms). SLA do Pix < 1 min.
- **201 a 600 (Risco Medio / Analise Cautelar)**: Retencao cautelar automatica (**Resolucao BCB no 142/2021**). Tempo medio de analise: **3,8 horas** (Lacuna L-02 Itau).
- **601 a 1000 (Risco Critico / Fraude Confirmada)**: Bloqueio imediato da transacao e notificacao de seguranca.

## Explicabilidade Algoritmica com FastTreeSHAP v2
- Utiliza o **FastTreeSHAP v2** acelerado por GPU para calcular os valores SHAP de cada variavel da decisao em tempo real.
- Emissao do Laudo Pericial XAI (LGPD Art. 20) contendo as 5 variaveis de maior peso para a decisao.
