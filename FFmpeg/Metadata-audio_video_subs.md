# FFmpeg

Hace unos días, se me presentó un problema, y al investigar el asunto, me encontré con las siguientes soluciones.

El software usado es:

	* yt-dlp
	* ffmpeg

En un sistema operativo, Fedora 34.




# Unir audio y video convirtiendo el codec.

	$  ffmpeg -hide_banner -i video.mp4 -i audio.wav -c:v copy -c:a aac output.mp4

Asumiendo que el video no tiene ningún audio y el codec del audio se traducirá a otro codec.



# Unir audio y video sin convertir el codec.

	$  ffmpeg -hide_banner -i video.mp4 -i audio.wav -c copy output.mp4



[superuser-solucion](https://superuser.com/questions/277642/how-to-merge-audio-and-video-file-in-ffmpeg)



# La maravillosa herramienta, yt-dlp


# Descargar los subtítulos.

	$  yt-dlp --write-subs --sub-langs en --skip-download url_Video


  Este comando funciona solamente para subtítulos en la plataforma de la caja roja con triangulo blanco.

	$  yt-dlp --write-auto-subs --sub-langs en --skip-download url_Video




# Convertir los subtítulos con formato vtt a srt

	$  ffmpeg -hide_banner -i subtitle.en.vtt subtitle.srt


Este es opcional porque ffmpeg permite los subtítulos vtt.



# Insertar subtítulos en el video.

	$  ffmpeg -hide_banner -i video.mp4 -i subtitulo.vtt -c copy -c:s mov_text -metadata:s:s:0 language=eng out.mp4


-c:v o -codec copy
	Set the video codec. This is an alias for -code
-c:s mov_text
	Set the subtitle codec. This is an alias for -codec:s.
-metadata
	Set a metadata key/value pair.
		s:s:0 -- subtítulo 1
		s:s:1 -- subtítulo 2
		s:s:2 -- subtítulo 3
		s:s:X -- subtítulo X
language=en
	Set language, in this case for language for subtitle.



[Source](https://bernd.dev/2020/04/adding-subtitles/)



# Insertar capítulos en el video y preservar todas los metadatas que contenga.

Acá es importante saber qué metadata contiene el video, para ello:

	$  ffprobe -hide_banner -i video.mp4


   Así obtendremos información del fichero y sabremos que mantener.


   En este ejemplo de comando, se preservará la metadata de video 1, audio 1, subtítulos 1, se agregará los capítulos del fichero de entrada y se copiarán los codecs para el video final.

	$  ffmpeg -hide_banner -i video.mp4 -f ffmetadata -i metadataFile.txt -map 0:v -map 0:a -map 0:s -map_metadata 1 -map_chapters 1 -c copy outVideo.mp4


-map 0:v	- mantiene metadata de video

-map 0:a	- mantiene metadata de audio

-map 0:s	- mantiene metadata de subtitulo

-map_metadata	- usa el fichero de entrada "metadataFile.txt"

-c copy		- solo copia el codec


[Source](https://stackoverflow.com/questions/70280531/problems-adding-chapters-ffmpeg)


---

**`transformChapters.py`** es un script que transforma los capítulos dentro de un archivo con formato:


* Sin titulo para el grupo de capítulos.
	00:00:00 - texto

	00:00:00 texto


* Con titulo para el grupo de capítulos.
	Titulo Capítulos
	00:00:00 - texto

	Titulo Capítulos
	00:00:00 texto


Lo convierte, por ejemplo:


* Sin titulo para el grupo de capítulos, genera titulo por defecto:
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

* Con titulo para el grupo de capítulos.
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




Bueno, al final de todo se obtendrá un video con subtítulos, capítulos, audio y video, tomará tiempo tanto como la potencia del procesador lo permita.
