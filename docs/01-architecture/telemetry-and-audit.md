# 02. Coletor de Telemetria Automatica e Trilha de Auditoria Inviolavel

## Visao Geral
A auditabilidade e um pilar central da **Operacao Espelho Falso v8.2.1 Beta Plus**. Cada inferencia e decisao gerada pelo pipeline cria um registro de telemetria estruturado e assinado criptograficamente.

## Estrutura do Coletor
O coletor opera em milissegundos na memoria volatil e registra:
- timestamp_utc: Horario exato de inferencia em padrao ISO 8601.
- pipeline_version: 8.2.1-beta-plus.
- latency_ms: Tempo total de inferencia (41,8 ms).
- throughput_tps: Media de vazao operacional (1.420 TPS).
- pix_sla_hours: Tempo estimado de retencao/liberacao cautelar (3,8 h).
- scib_score: Score final de risco (0 a 1000).
- sha256_hash: Assinatura digital inviolavel do estado do pipeline e dos parametros.

## Garantia de Irrepudiabilidade
O hash SHA-256 e enviado ao servico de logging imutavel (ClickHouse) e associado ao Laudo Pericial de Explicabilidade (LGPD Art. 20), impedindo adulteracoes retroativas em auditorias regulatorias do Banco Central ou ANPD.
