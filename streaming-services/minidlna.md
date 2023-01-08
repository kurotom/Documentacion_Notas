# miniDLNA

[https://sourceforge.net/projects/minidlna/](https://sourceforge.net/projects/minidlna/)


MiniDLNA es un software de servidor con el objetivo de ser totalmente compatible con los clientes [DLNA](http://en.wikipedia.org/wiki/Digital_Living_Network_Alliance)/[UPnP](http://en.wikipedia.org/wiki/Universal_Plug_and_Play). El daemon MiniDNLA sirve archivos multimedia (música, imágenes y video) a clientes en una red. Los clientes de ejemplo incluyen aplicaciones como totem y xbmc, y dispositivos como reproductores multimedia portátiles, teléfonos inteligentes y televisores.

MiniDLNA es una alternativa simple y liviana a MediaTomb, pero tiene menos funciones. No tiene una interfaz web para la administración y debe configurarse editando un archivo de texto.


1. Instalar repositorio RPM Fusion

[Descargar e instalar Repositorio RPM Fusion](https://rpmfusion.org/Configuration)


2. Instalar `minidlna`

```
$ sudo dnf install minidlna
```


3. Configurar `/etc/minidlna.conf`

```
port=8200
user=[USUARIO]

media_dir=V,/directorio/to/movies/

friendly_name=Name Service

db_dir=/directorio/to/minidlna/db

log_dir=/directorio/to/minidlna/log

log_level=general,artwork,database,inotify,scanner,metadata,http,ssdp,tivo=warn

album_art_names=Cover.jpg/cover.jpg/AlbumArtSmall.jpg/albumartsmall.jpg/AlbumArt.jpg/albumart.jpg/Album.jpg/album.jpg/Folder.jpg/folder.jpg/Thumb.jpg/thumb.jpg

inotify=no
enable_tivo=no
tivo_discovery=bonjour
strict_dlna=no
notify_interval=900
serial=12345678
model_number=1
```


4. Configurar minidlna.service

```
$ sudo vim /usr/lib/systemd/system/minidlna.service
```

```
[Unit]
Description=MiniDLNA is a DLNA/UPnP-AV server software
After=network-online.target syslog.target local-fs.target
Wants=network-online.target

[Service]
User=[USUARIO]
Group=[USUARIO]
Type=simple
ExecStart=/usr/sbin/minidlnad -S

[Install]
WantedBy=multi-user.target
```


5. Permisos

Asegurarse que el usuario que utilizará el servicio tenga los permisos necesarios para acceder al directorio de medios y para crear directorios log y db (cache).


6. Puertos

Abrir puertos:

* TCP `8200`

* UDP `1900`



7. Iniciar, detener, estado del servicio

```
$ sudo systemctl start minidlna.service 

$ sudo systemctl stop minidlna.service 

$ sudo systemctl status minidlna.service 
```


Habilitar el servicio

```
$ sudo systemctl enable minidlna.service 
```



[miniDLNA](https://help.ubuntu.com/community/MiniDLNA)
[Resolucion permisos](https://forums.gentoo.org/viewtopic-t-1124365-start-0.html)


