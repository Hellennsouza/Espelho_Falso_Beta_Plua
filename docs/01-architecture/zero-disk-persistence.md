# 03. Protocolo Zero-Disk Persistence (Conformidade LGPD Art. 11)

## Visao Geral
O protocolo **Zero-Disk Persistence** assegura que nenhum dado biometrico sensivel (vetores faciais, frames de camera, imagens brutas) ou PII do cliente seja armazenado em disco rigido, SSD ou armazenamento nao-volatil no dispositivo ou nos servidores de borda.

## Principios de Funcionamento
1. **Captura e Processamento em Memoria Volatil (RAM)**:
   - Os frames de video sao capturados no elemento HTML5 Canvas diretamente na memoria RAM do navegador/SuperApp.
   - Os vetores de inferencia biometrica e PRNU sao mantidos estritamente como matrizes binarias Float32Array em memoria efemera.

2. **Descarte Instantaneo (Zero-Trace Lifecycle)**:
   - Apos o calculo do Liveness Ocular (Modulo 1) e Assinatura PRNU (Modulo 2), os buffers de imagem sao sobrescritos com zeros e liberados pelo Garbage Collector.
   - **Tempo de vida dos dados biometricos em RAM**: < 100 ms.

3. **Enquadramento Legal (LGPD)**:
   - Cumprimento rigoroso do **Art. 11, II, 'g' da LGPD** (prevencao a fraude e seguranca do titular no processo de identificacao e autenticacao de cadastro em sistemas eletronicos).
