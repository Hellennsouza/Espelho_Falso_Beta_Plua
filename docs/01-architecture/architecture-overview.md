# 01. Arquitetura do Sistema e Execucao em Borda (Edge-AI)

## Visao Geral
A **Operacao Espelho Falso v8.2.1 Beta Plus** adota uma arquitetura descentralizada de alto desempenho, executando inferencia de Inteligencia Artificial diretamente no dispositivo do cliente (*on-device*) via **ONNX Runtime WebAssembly (WASM) Int8**.

## Componentes Chaves da Borda
1. **Engine ONNX Runtime WASM Int8**:
   - Quantizacao Int8 para reduzir a pegada de memoria a <15 MB.
   - Compilacao WebAssembly habilitando aceleracao de hardware via WebGL / WebGPU e SIMD no navegador/SuperApp.
   - **Latencia media**: 41,8 ms por frame.
   - **Throughput do cluster**: 1.420 transacoes por segundo (TPS).

2. **Mecanismo de Fallback Adaptativo**:
   - Para dispositivos com limitacoes de hardware (*low-end*), a pipeline alterna dinamicamente entre WebGL, WebAssembly multi-thread e inferencia leve por CPU sem degradacao do Score de Risco.

3. **Garantias de Desempenho e Disponibilidade**:
   - **SLA Operacional**: Reducao do tempo de retencao cautelar Pix de 120h para **3,8 horas**.
   - **Disponibilidade**: 99,99% Uptime com resiliencia local a desconexoes temporarias de rede.
