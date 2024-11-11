# FFmpeg

**FFmpeg** es una colección de software libre que puede grabar, convertir y hacer streaming de audio y vídeo. Incluye libavcodec, una biblioteca de códecs. FFmpeg está desarrollado en GNU/Linux, pero puede ser compilado en la mayoría de los sistemas operativos, incluyendo Windows. [Wikipedia](https://es.wikipedia.org/wiki/FFmpeg). 


# Unir audio y video convirtiendo el codec.

Asumiendo que el video no tiene ningún audio y el codec del audio se traducirá a otro codec.

```bash
$  ffmpeg -i video.mp4 -i audio.wav -c:v copy -c:a aac output.mp4
```


# Unir audio y video sin convertir el codec.

```bash
$  ffmpeg -i video.mp4 -i audio.wav -c copy output.mp4
```

[superuser-solucion](https://superuser.com/questions/277642/how-to-merge-audio-and-video-file-in-ffmpeg)


# Unir audio en un tiempo determinado

El parámetro `-itsoffset [tiempo]` determina el tiempo en que la pista (audio o video) se debe inicializar.

```bash
ffmpeg -i video.mp4 -itsoffset 00:01:30 -i audio.aac -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 output.mp4
```

# Convertir formato de audio y mantener 5.1

```bash
ffmpeg -i audio.flac -c:a ac3 -b:a 640k -ac 6 output.ac3
```

Tabla de Byterate en formatos de audio.

| Formato | Byterate |
|-|-|
| MP3 (MPEG-1 Audio Layer III) |128 kbps, 192 kbps, 256 kbps, 320 kbps |
| AAC (Advanced Audio Coding) | 128 kbps, 256 kbps |
| FLAC (Free Lossless Audio Codec) | entre 700 - 1.100 kbps |
| WAV (Waveform Audio File Format) | 1,411 kbps aprox. (CD - 16 bits, 44.1 kHz) |
| OGG Vorbis | 160 kbps, 192 kbps |
| Opus | 64 kbps a 128 kbps |
| M4A (MPEG-4 Audio) | 128 kbps, 256 kbps |
| ALAC (Apple Lossless Audio Codec) | entre 700 - 1,100 kbps |


# Convertir audio multicanal a stéreo

```bash
$  ffmpeg -hide_banner -i video.mp4 -vcodec copy -acodec aac -strict -2 -ab 320K -ac 2 output.mp4
```

En el caso de 5.1, el .1 indica el subwoofer y en este caso se descarta.


# Convertir los subtítulos con formato vtt a srt

```bash
$  ffmpeg -i subtitle.en.vtt subtitle.srt
```

Este es opcional porque ffmpeg permite los subtítulos *.vtt*.



# Insertar subtítulos

Agrega subtítulos a un stream del fichero, no "quema" los subtítulos en la imagen de video.

```bash
ffmpeg -hide_banner -i video.mp4 -i subtitulo.vtt -i sub.ass \
    -c:v copy -c:a copy -c:s mov_text \
    -map 0:v -map 0:a -map 1 -map 2 \
    -metadata:s:s:0 language=eng \
    -metadata:s:s:1 language=spa out.mp4
```

* `-c:v copy -c:a copy` : copia codec video y audio.
* `-c:s mov_text` : establece codec para subtítulos.
* `-map 0:v -map 0:a -map 1 -map 2` : establece el mapeo de los elementos, dependiendo de la disposición del video original.
* `-metadata [key]` : establece valor para el subtítulo, `-metadata:s:s:X language=[LANG]`, reemplazar `X` por el índice correcto, y `[LANG]` por el lenguaje en *ISO 639-2*.
	

[Source](https://bernd.dev/2020/04/adding-subtitles/)


# Establecer subtítulo por defecto

Usar `-disposition:s:0 default`, dependiendo del subtítulo y `-metadata` estén en la posición correcta.

```bash
ffmpeg -i input_video.mkv -c copy -disposition:s:0 default output_video.mkv
```

```bash
ffmpeg -hide_banner -i video.mp4 -i subtitulo.vtt -c copy -c:s mov_text -metadata:s:s:0 language=eng -disposition:s:0 default  out.mp4
```



# Insertar subtítulos ASS

Conservando los codec de video, audio, incoporando subtítulos en formato ASS.

```bash
$ ffmpeg -hide_banner -i in_video.mp4 -i subs.ass -c copy -scodec mov_text -map 0 -map 1 out_video.mp4
```

Estableciendo la metadata "language" al video.

```bash
ffmpeg -hide_banner -i in_video.mp4 -i subtitle.ass -c copy -scodec mov_text -metadata:s:s:0 -language=esp out_video.mp4
```


# Insertar capítulos en el video y preservar todas los metadatos que contenga.

Acá es importante saber qué metadata contiene el video, para ello se usa `ffprobe`:

```bash
$  ffprobe -hide_banner -i video.mp4
```

Así obtendremos información del fichero y sabremos que mantener.

En este ejemplo de comando, se preservará la metadata de video 1, audio 1, subtítulos 1, se agregará los capítulos del fichero de entrada y se copiarán los codecs para el video final.

```bash
$  ffmpeg -i video.mp4 -f ffmetadata -i metadataFile.txt -map 0:v -map 0:a -map 0:s -map_metadata 1 -map_chapters 1 -c copy outVideo.mp4
```

* -map 0:v - mantiene metadata de video.
* -map 0:a - mantiene metadata de audio.
* -map 0:s - mantiene metadata de subtitulo.
* -map_metadata - usa el fichero de entrada "metadataFile.txt".
* -c copy - solo copia el codec.


[Source](https://stackoverflow.com/questions/70280531/problems-adding-chapters-ffmpeg)



# Quemar subtitulos en video

Se debe usar la opción `-vf` y el argumento debe ir entre comillas dobles, si está en otra ruta, se debe deben escapar los carácteres especiales, ejemplo bash Linux: `FILE_PATH=$(printf "%q" $DIRECTORY/subass_final.ass")`

```bash
fmpeg -hide_banner -i MOVIE.mp4 -acodec copy -vf "ass=file_sub.ass" FINAL_MOVIE.mp4
```

