# Cut video


Formato `[start]` y `00:00:000`

```
$ ffmpeg -ss [start] -i videoIN.mp4 -t [duration] -c copy videoOut.mp4
```



```
ffmpeg -ss [start] -i videoIN.mp4 -to [end] -c copy -copyts videoOut.mp4
```


* Formato del tiempo `00:01:23.000` o `83` (segundos).
* `-t` o `-to` tiempo de finalizar.
* `-c copy`, copia primer video, audio, subtitulo.


[https://trac.ffmpeg.org/wiki/Seeking](https://trac.ffmpeg.org/wiki/Seeking)


En caso de tener que re-codificar video y audio:

```
$ ffmpeg -ss [start] -i in.mp4 -t [duration] -c:v libx264 -c:a aac -strict experimental -b:a 128k out.mp4
```


[Fuente](https://superuser.com/questions/377343/cut-part-from-video-file-from-start-position-to-end-position-with-ffmpeg)
