# FFmpeg

**FFmpeg** es una colección de software libre que puede grabar, convertir y hacer streaming de audio y vídeo. Incluye libavcodec, una biblioteca de códecs. FFmpeg está desarrollado en GNU/Linux, pero puede ser compilado en la mayoría de los sistemas operativos, incluyendo Windows. [Wikipedia](https://es.wikipedia.org/wiki/FFmpeg).  


# Unir audio y video convirtiendo el codec.

```
$  ffmpeg -i video.mp4 -i audio.wav -c:v copy -c:a aac output.mp4
```

Asumiendo que el video no tiene ningún audio y el codec del audio se traducirá a otro codec.



# Unir audio y video sin convertir el codec.

```
$  ffmpeg -i video.mp4 -i audio.wav -c copy output.mp4
```


[superuser-solucion](https://superuser.com/questions/277642/how-to-merge-audio-and-video-file-in-ffmpeg)


# Convertir audio multicanal a stéreo

```
$  ffmpeg -hide_banner -i video.mp4 -vcodec copy -acodec aac -strict -2 -ab 320K -ac 2 output.mp4
```

En el caso de 5.1, el .1 indica el subwoofer y en este caso se descarta.


# Convertir los subtítulos con formato vtt a srt

```
$  ffmpeg -i subtitle.en.vtt subtitle.srt
```

Este es opcional porque ffmpeg permite los subtítulos *.vtt*.



# Insertar subtítulos en el video.

```
$  ffmpeg -hide_banner -i video.mp4 -i subtitulo.vtt -c copy -c:s mov_text -metadata:s:s:0 language=eng out.mp4
```

* -c:v o -codec copy
Set the video codec. This is an alias for -codec

-c:s mov_text
Set the subtitle codec. This is an alias for `-codec:s`.

* -metadata [key]
Set a metadata key/value pair.
```bash
-metadata s:s:0          # subtitlulo 1<br>
-metadata s:s:1          # subtitlulo 2<br>
-metadata s:s:2          # subtitlulo 3<br>
-metadata s:s:X          # subtitlulo X<br>
```

* language=en
Set language, in this case for language for subtitle.
	

[Source](https://bernd.dev/2020/04/adding-subtitles/)



# Insertar capítulos en el video y preservar todas los metadatos que contenga.

Acá es importante saber qué metadata contiene el video, para ello:

```
$  ffprobe -hide_banner -i video.mp4
```


Así obtendremos información del fichero y sabremos que mantener.

En este ejemplo de comando, se preservará la metadata de video 1, audio 1, subtítulos 1, se agregará los capítulos del fichero de entrada y se copiarán los codecs para el video final.

```    
$  ffmpeg -i video.mp4 -f ffmetadata -i metadataFile.txt -map 0:v -map 0:a -map 0:s -map_metadata 1 -map_chapters 1 -c copy outVideo.mp4
```

* -map 0:v - mantiene metadata de video.
* -map 0:a - mantiene metadata de audio.
* -map 0:s - mantiene metadata de subtitulo.
* -map_metadata - usa el fichero de entrada "metadataFile.txt".
* -c copy - solo copia el codec.


[Source](https://stackoverflow.com/questions/70280531/problems-adding-chapters-ffmpeg)


---

# Script ffmetadata

**`transformChapters.py`** es un script que transforma los capítulos.


El formato de los capítulos deben ser:

* Sin titulo para el grupo de capítulos.

```
00:00:00 - texto
```

```
00:00:00 texto
```

* Con titulo para el grupo de capítulos.
```
Titulo capítulos
00:00:00 - texto
```

```
Titulo capítulos
00:00:00 texto
```



## Ejemplo de conversión

Un ejemplo del fichero final en cada caso de formato de subtítulos.

1. Sin título para el grupo de capítulos, genera titulo por defecto:

```	
;FFMETADATA1
title=Chapters
	
[CHAPTER]
TIMEBASE=1/1000
START=0000000
END=1000000
title=Chapter 10
	
[STREAM]
title=Chapters
```

2. Con título para el grupo de capítulos.
```
;FFMETADATA1
title=Introduccion Materia
	
[CHAPTER]
TIMEBASE=1/1000
START=0000000
END=1000000
title=Chapter 10
	
[STREAM]
title=Introduccion Materia	
```



# End

Con esta información se podrá unir fichero de video, audio, subtítulo, y capítulo.

El tiempo que tarde en completar cada tarea dependerá de la potencia del procesador.




