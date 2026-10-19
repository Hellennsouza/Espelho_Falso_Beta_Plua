/**
 * PROJETO 1: OPERAÇÃO ESPELHO FALSO (v8.2 Beta Plus)
 * CLIENT-SIDE ONNX RUNTIME WEBASSEMBLY (WASM) INFERENCE ENGINE
 * 
 * Autora: Dra. Hellen Nunes dos Santos Souza
 * Execução On-Device: Captura de quadros da câmera, pré-processamento e
 * inferência biométrica em <50ms no navegador/SuperApp bancário.
 * Política: Zero-Disk Persistence (Processamento exclusivamente em memória volátil).
 */

class OnnxWasmLivenessEngine {
    constructor(config = {}) {
        this.modelPath = config.modelPath || './models/liveness_quant_int8.onnx';
        this.inputWidth = config.inputWidth || 128;
        this.inputHeight = config.inputHeight || 128;
        this.lowEndDevice = config.isLowEndDevice || false;
        this.session = null;
    }

    async initialize() {
        try {
            console.log('[WASM] Inicializando ONNX Runtime WebAssembly...');
            ort.env.wasm.numThreads = this.lowEndDevice ? 1 : 2;
            ort.env.wasm.simd = true;

            this.session = await ort.InferenceSession.create(this.modelPath, {
                executionProviders: ['wasm', 'webgl'],
                graphOptimizationLevel: 'all'
            });
            console.log('[WASM] Modelo Int8 carregado com sucesso on-device.');
            return true;
        } catch (error) {
            console.error('[WASM] Falha na inicialização do ONNX WASM:', error);
            return false;
        }
    }

    preprocessImageData(imageBuffer) {
        const float32Data = new Float32Array(3 * this.inputWidth * this.inputHeight);
        for (let i = 0; i < imageBuffer.length / 4; i++) {
            float32Data[i] = (imageBuffer[i * 4] / 127.5) - 1.0;
            float32Data[i + 16384] = (imageBuffer[i * 4 + 1] / 127.5) - 1.0;
            float32Data[i + 32768] = (imageBuffer[i * 4 + 2] / 127.5) - 1.0;
        }
        return new ort.Tensor('float32', float32Data, [1, 3, this.inputHeight, this.inputWidth]);
    }

    async inferLiveness(imageBuffer) {
        const startTime = performance.now();
        if (!this.session) {
            await this.initialize();
        }

        const inputTensor = this.preprocessImageData(imageBuffer);
        const feeds = { input_tensor: inputTensor };
        
        const results = await this.session.run(feeds);
        const output = results.output_scores.data;
        const latencyMs = performance.now() - startTime;

        return {
            livenessScore: output[0],
            isSpoof: output[0] < 0.35,
            latencyMs: latencyMs,
            deviceMode: this.lowEndDevice ? 'LOW_END_FALLBACK' : 'HIGH_PERFORMANCE_WASM'
        };
    }
}

if (typeof module !== 'undefined' && module.exports) {
    module.exports = { OnnxWasmLivenessEngine };
}
