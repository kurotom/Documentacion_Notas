# yt-dlp

**yt-dlp**, fork de *youtube-dl*, descarga elementos media y librerías para varios sitios.


# Ayuda

```
$ yt-dlp --help
```



# Listar formatos

```
$ yt-dlp --list-formats url_Video
```


# Descargar video

```
$ yt-dlp --format [numeroFomatoVideo] url_Video
```


# Descargar audio

```
$ yt-dlp --format [numeroFomatoAudio] url_Video
```



# Listar subtítulos disponibles

```
$ yt-dlp --list-subs url_Video
```

# Listar formato subtítulos disponibles

```
$ yt-dlp --sub-format [formato] url_Video
```


# Descargar los subtítulos.

```
$  yt-dlp --write-subs --sub-langs en --skip-download url_Video
```
	
Escribe los subtítulos automáticamente sin descargar el video.

```
$  yt-dlp --write-auto-subs --sub-langs en --skip-download url_Video
```
