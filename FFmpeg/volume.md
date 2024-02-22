# Manipulación del volumen

> [volume doc](https://trac.ffmpeg.org/wiki/AudioVolume)

Solo ajusta al volumen no establece el volumen.

Establecer a la mitad el nivel de volumen de entrada:

```bash
ffmpeg -i input.wav -filter:a "volume=0.5" output.wav
```

Aumentar a 150% el nivel del volumen de entrada:

```bash
ffmpeg -i input.wav -filter:a "volume=1.5" output.wav
```

Incrementar el volumen usando *decibel* (`dB`):

```bash
ffmpeg -i input.wav -filter:a "volume=10dB" output.wav
```

Reducir el volumen se usa valores negativos:

```bash
ffmpeg -i input.wav -filter:a "volume=-5dB" output.wav
```


# Normalización

Para detectar el volumen, se debe analizar con `volumedetect`:

```bash
ffmpeg -i input.wav -filter:a volumedetect -f null /dev/null
```

Obteniendo una salida similar a:

```bash
[Parsed_volumedetect_0 @ 0x7f8ba1c121a0] mean_volume: -16.0 dB
[Parsed_volumedetect_0 @ 0x7f8ba1c121a0] max_volume: -5.0 dB
...
```

## Normalización de volumen

Es recomendado, ejecutar la normalización en dos etapas:

1. Extraer la medida de volumen desde la primera ejecución.
2. Usar los valores obtenidos anteriormente y compararlos con una segunda ejecución de medida de volumen.

Para normalizar el volumen de un fichero, se debe usar un fichero `loudnorm` que implementa algoritmo EBU R128:

```bash
ffmpeg -i input.wav -filter:a loudnorm output.wav
```

## `ffmpeg-nomalize`

Para automatizar el proceso de automatización se puede usar `pip install ffmpeg-nomalize`.

```bash
ffmpeg-normalize 1.wav 2.wav -o 1-normalized.m4a 2-normalized.m4a -c:a aac -b:a 192k
```
