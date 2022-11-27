
# FFmpeg

Hace unos días, se me presentó un problema, y al investigar el asunto, me encontré con las siguientes soluciones.

El software usado es:

	* yt-dlp
	* ffmpeg

En un sistema operativo, Fedora.




# Unir audio y video convirtiendo el codec.

```
$  ffmpeg -i video.mp4 -i audio.wav -c:v copy -c:a aac output.mp4
```

Asumiendo que el video no tiene ningun audio y el codec del audio se traducirá a otro codec.



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


---

# La maravillosa herramienta, yt-dlp 


# Descargar los subtitulos.

```
$  yt-dlp --write-subs --sub-langs en --skip-download url_Video
```
	
Escribe los subtitulos automáticamente sin descargar el video. Se puede obtener los subtitulos en varios formatos disponibles listados por `--list-subs` y utilizando `--sub-format [formato]`.

```
$  yt-dlp --write-auto-subs --sub-langs en --skip-download url_Video
```

---


# Convertir los subtitulos con formato vtt a srt

```
$  ffmpeg -i subtitle.en.vtt subtitle.srt
```

Este es opcional porque ffmpeg permite los subtitulos vtt.



# Insertar subtitulos en el video.

```
$  ffmpeg -hide_banner -i video.mp4 -i subtitulo.vtt -c copy -c:s mov_text -metadata:s:s:0 language=eng out.mp4
```


-c:v o -codec copy<br>
&nbsp;&nbsp; Set the video codec. This is an alias for -code<br>

-c:s mov_text<br>
&nbsp;&nbsp; Set the subtitle codec. This is an alias for -codec:s.<br>

-metadata<br>
&nbsp;&nbsp; Set a metadata key/value pair.<br>
&emsp;&emsp; s:s:0 -- subtitlulo 1<br>
&emsp;&emsp; s:s:1 -- subtitlulo 2<br>
&emsp;&emsp; s:s:2 -- subtitlulo 3<br>
&emsp;&emsp; s:s:X -- subtitlulo X<br>

language=en<br>
&nbsp;&nbsp; Set language, in this case for language for subtitle.<br>
	


[Source](https://bernd.dev/2020/04/adding-subtitles/)



# Insertar capítulos en el video y preserver todas las metadatas que contenga.

Acá es importante saber qué metadata contiene el video, para ello:

```
$  ffprobe -hide_banner -i video.mp4
```


Asi obtendremos informacion del fichero y sabremos que mantener.

En este ejemplo de comando, se preservará la metadata de video 1, audio 1, subtitulos 1, se agregará los capitulos del fichero de entrada y se copiarán los codecs para el video final.

```    
$  ffmpeg -i video.mp4 -f ffmetadata -i metadataFile.txt -map 0:v -map 0:a -map 0:s -map_metadata 1 -map_chapters 1 -c copy outVideo.mp4
```

-map 0:v	- mantiene metadata de video<br>
-map 0:a	- mantiene metadata de audio<br>
-map 0:s	- mantiene metadata de subtitulo<br>
-map_metadata	- usa el fichero de entrada "metadataFile.txt"<br>
-c copy		- solo copia el codec<br>


[Source](https://stackoverflow.com/questions/70280531/problems-adding-chapters-ffmpeg)


---

**`transformChapters.py`** es un script que transforma los capitulos dentro de un archivo con formato:


* Sin titulo para el grupo de capítulos.<br>
	00:00:00 - texto<br>

	00:00:00 texto<br>


* Con titulo para el grupo de capítulos.<br>
	Titulo Capitulos<br>
	00:00:00 - texto<br>

	Titulo Capitulos<br>
	00:00:00 texto<br>


Lo convierte, por ejemplo:


* Sin título para el grupo de capítulos, genera titulo por defecto:
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

* Con título para el grupo de capítulos.
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




Bueno, al final de todo se obtendrá un video con subtitulos, capitulos, audio y video, tomará tiempo tanto como la potencia del procesador lo permita.


