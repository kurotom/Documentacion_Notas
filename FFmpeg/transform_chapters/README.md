# Script ffmetadata

**`transformChapters.py`** es un script que transforma los capítulos una lista en un documento de texto en un documento en formato para incorporar capítulos al video.


## Formato de capítulos

En el documento de texto, los capítulos pueden estar en dos formas.

1) Sin título para el grupo de capítulos.

```
00:00:00 - texto 1
```

```
00:00:00 texto 2
```

2) Con título para el grupo de capítulos.

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



