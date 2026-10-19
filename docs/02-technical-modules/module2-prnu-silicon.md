# Modulo 2: Assinatura de Silicio PRNU e Protecao no Nivel de Hardware

## Visao Geral
O **Modulo 2** atua na camada de hardware do dispositivo do usuario para combater injeçoes de camera virtual, emuladores e substituicao de stream de midia antes da captura.

## Principios Tecnicos de PRNU (Photo-Response Non-Uniformity)
1. **Digital Fisica do Sensor Optico**:
   - Imperfeicoes microscopicas no processo de fabricacao do silicio (wafers dos sensores CMOS) geram um padrao de ruido unico e irrepetivel para cada camera fisica de smartphone.
   - O Modulo 2 extrai o ruido de alta frequencia do sensor optico e valida se a imagem provem de uma camera fisica real.

2. **Injecao de Camera Virtual**:
   - Cameras virtuais e injetores de software transmitem imagens sinteticas limpas de ruido de silicio.
   - A ausencia do PRNU genuino dispara bloqueio imediato na camada HAL (Hardware Abstraction Layer) do aplicativo.
