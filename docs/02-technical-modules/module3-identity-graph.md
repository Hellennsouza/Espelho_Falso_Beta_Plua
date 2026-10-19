# Modulo 3: Identity Graph Multimodal & Comunidades de Mulas

## Visao Geral
O **Modulo 3** analisa os relacionamentos e grafos de vinculacao em tempo real para identificar **redes de contas mulas**, enxames de transacoes suspeitas e estruturas organizadas de pulverizacao de recursos ilicitos no Pix.

## Algoritmos e Processamento em Streaming
1. **Algoritmo de Detensao de Comunidades de Louvain**:
   - Executado em memoria volatil sobre grafos de relacionamentos (CPF, dispositivo, IP, chave Pix, biometria).
   - Agrupa nos altamente densos indicando redes de contas laranjas operadas pelo mesmo grupo criminoso.

2. **PageRank em Streaming Micro-Batch**:
   - Calcula em tempo real a relevancia e centralidade de contas recebedoras de recursos no Pix.
   - Identifica contas concentradoras projetadas para drenar valores retidos ou fracionados.
