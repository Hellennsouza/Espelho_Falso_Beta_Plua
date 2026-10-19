# Modulo 1: Pericia Visual & Liveness Ocular Espectral

## Visao Geral
O **Modulo 1** realiza a analise biometrica pericial da regiao ocular para detectar tentativas de fraude visual, tais como fotos impressas, videos gravados em alta resolucao, telas 4K/8K e mascaras 3D.

## Metodologia Tecnica
1. **Analise de Especularidade Corneal (Gradiente de Sobel)**:
   - Avalia a curvatura fisica e a reflexao da luz na cornea humana.
   - Simulacoes em telas possuem reflexos planos nao-esfericos detectaveis pela variacao do gradiente de borda ocular.

2. **Micro-cintilacao PWM por FFT (Fast Fourier Transform)**:
   - Detecta o fenomeno de cintilacao invisivel a olho nu produzido pela modulacao de largura de pulso (PWM) em monitores LCD/OLED.
   - Aplicacao de FFT nas frequencias de brilho periocular para isolar picos espectrais caracteristicos de telas digitais.

3. **Certificacao e Metricas Regulatorias (ISO/IEC 30107-3)**:
   - **APCER**: < 0,1% (Bloqueio de fraudes sinteticas).
   - **BPCER**: < 1,0% (Garantia de baixissimo falso positivo para clientes legitimos).
