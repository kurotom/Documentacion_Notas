#!/bin/bash
#
#	23-04-2020
#
path_pelicula='/home/ocio/peliculas/listas/'

case "$1" in
	*\ *)
		SIN_ESPACIOS=$(echo $1 | tr " " "_")
		mv "$1" "$SIN_ESPACIOS"
	;;
	*)
		SIN_ESPACIOS=$1
	;;
esac
#
FILE_MP4=$(find $SIN_ESPACIOS -regextype posix-egrep -regex '.*(mp4|mkv|avi)$')
FILE_SRT=$(find $SIN_ESPACIOS -regextype posix-egrep -regex '.*(srt|sub)$')
#
echo -e "\nPelicula a trabajar $1"
echo -e "Archivos: $FILE_MP4 $FILE_SRT"
echo -e "\n"
#							    #
#############################################################
#							    #
init="//////////////////////////////////////////////////"
end="\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"
#
case "$FILE_MP4" in
	*\ *)
		echo "con espacios"
		echo "$FILE_MP4"
		PELICULA=$(echo $FILE_MP4 | tr " " "_")
		mv "$FILE_MP4" "$PELICULA"
	;;
	*)
		echo "sin espacios"
		echo "$FILE_MP4"
		PELICULA=$FILE_MP4
	;;
esac
case "$FILE_SRT" in
	*\ * )
		echo "con espacios"
		echo $FILE_SRT
		OUT=$(echo $FILE_SRT.srt | tr " " "_")
		mv "$FILE_SRT" "$OUT"
	;;
	*)
		echo "sin espacios"
		echo $FILE_SRT
		OUT=$FILE_SRT
	;;
esac

name=${PELICULA%YIFY*}
codificacion=$(file -i $OUT | awk 'BEGIN {FS=" "}/charset/{print $3}')
codec=${codificacion##*=}


CODEC=$(echo $codec | tr [:lower:] [:upper:])
CODEC_FINAL="UTF-8"
#							    #
#############################################################
#############################################################
#							    #
#
#SUB="Style: Default,Arial,16,&Hffffff,&Hffffff,&H0,&H0,0,0,0,0,100,100,0,0,1,1,0,2,10,10,10,0"
#ASS="Style: Default,Arial,22,&Hffffff,&Hffffff,&H0,&H0,1,0,0,0,100,100,0,0,1,1,0,2,10,10,10,0"
#
RE=reporte.log
#
echo $init
echo "Comprobando Codificacion Subtitulos"
#
if [ $codificacion == "charset=unknown-8bit" ]; then
	echo -e "\n"
	echo "*************************************"
	echo
	echo "Distinta Codificacion"
	echo -e "\t$codificacion"
	echo
	echo "*************************************"
	echo -e "\n"
	#
	# Cambia la codificacion a UTF-8
      	iconv -f ISO-8859-1 -t UTF-8 $OUT -o $OUT.srt
#	rm -rvf $FILE_SRT
	#
	#   Crea fichero subtitulo formato SSA/ASS
	ffmpeg -hide_banner -i $OUT.srt sub.ass
	#
	#   Cambia el tamaño letra y negrita
	sed -e 's/Arial,16/Arial,22/' sub.ass > sub1.ass
	sed -e 's/\&H0,0/\&H0,1/' sub1.ass > sub_final.ass
	#
	rm -rf $RE
	#   Inserta subtitulos forzado
	FFREPORT=file=$RE:level=0:level=8:level=16:level=24 ffmpeg -hide_banner -i "$PELICULA" -map_chapters -1 -vf "ass=sub_final.ass" $name".mp4"
#	echo "FFREPORT=file=$RE:level=0:level=8:level=16:level=24 ffmpeg -hide_banner -i $PELICULA -vf ass=sub.ass $name.mp4"
#	ffmpeg -hide_baner -i $PELICULA -vf "ass=sub.ass" $name".mp4"
#	echo "ffmpeg -hide_banner -i $PELICULA -vf ass=sub.ass $name.mp4"
	#
	#   Elimina fichero SSA/ASS
	rm -rvf sub.ass sub1.ass sub_final.ass
	mv "$SIN_ESPACIOS" $path_pelicula
	#
#		echo -e "\n\n\nPelicula, "$SIN_ESPACIOS", ha finalizado\n" >> $RE
#		cat $RE | mailx -s "Finalizó" -S "from=ffmpeg-terminó <NO_RESPONDER>" informe@sinpega.lol
#	rm -rf $RE
#
elif [ $codificacion != $CODEC_FINAL ]; then
	echo -e "\n"
	echo "*************************************"
	echo
        echo "Es distinto" $codificacion
	echo
	echo "*************************************"
	echo -e "\n"
       	iconv -f $CODEC -t UTF-8 $OUT -o $OUT.srt
#	rm -rvf $FILE_SRT
	#   Crea fichero subtitulo formato SSA/ASS
	ffmpeg -hide_banner -i $OUT.srt sub.ass
	#   Cambia el tamaño de fuente dejando el tipo de esta
	sed -e 's/Arial,16/Arial,22/' sub.ass > sub1.ass
	sed -e 's/\&H0,0/\&H0,1/' sub1.ass > sub_final.ass
	#
	rm -rf $RE
	#   Inserta subtitulos forzado
	FFREPORT=file=$RE:level=0:level=8:level=16:level=24 ffmpeg -hide_banner -i "$PELICULA" -map_chapters -1 -vf "ass=sub_final.ass" $name".mp4"
#	echo "FFREPORT=file=$RE:level=0:level=8:level=16:level=24 ffmpeg -hide_banner -i $PELICULA -vf ass=sub.ass $name.mp4"
#	ffmpeg -hide_baner -i $PELICULA -vf "ass=sub.ass" $name".mp4"
#	echo "ffmpeg -hide_banner -i $PELICULA -vf ass=sub.ass $name.mp4"
	#
	#   Elimina fichero SSA/ASS
	rm -rvf sub.ass sub1.ass sub_final.ass
	mv "$SIN_ESPACIOS" $path_pelicula
	#
	#	echo -e "\n\n\nPelicula, "$SIN_ESPACIOS", ha finalizado\n" >> $RE
	#	cat $RE | mailx -s "Finalizó" -S "from=ffmpeg-terminó <NO_RESPONDER>" informe@sinpega.lol
#	rm -rf $RE
	#
else
	echo -e "\n"
	echo "*************************************"
	echo
	echo "Codificacion" $codificacion
	echo
	echo "*************************************"
	echo -e "\n"
	#   Crea fichero subtitulo formato SSA/ASS
	ffmpeg -hide_banner -i $OUT sub.ass
	#   Cambia el tamaño de fuente dejando el tipo de esta
	sed -e 's/Arial,16/Arial,22/' sub.ass > sub1.ass
	sed -e 's/\&H0,0/\&H0,1/' sub1.ass > sub_final.ass
	#
	rm -rf $RE
	#   Inserta subtitulos forzado
	FFREPORT=file=$RE:level=0:level=8:level=16:level=24 ffmpeg -hide_banner -i "$PELICULA" -map_chapters -1 -vf "ass=sub_final.ass" $name".mp4"
#	echo "FFREPORT=file=$RE:level=0:level=8:level=16:level=24 ffmpeg -hide_banner -i $PELICULA -vf ass=sub.ass $name.mp4"
#	ffmpeg -hide_baner -i $PELICULA -vf "ass=sub.ass" $name".mp4"
#	echo "ffmpeg -hide_banner -i $PELICULA -vf ass=sub.ass $name.mp4"
	#
	#   Elimina fichero SSA/ASS
	rm -rvf sub.ass sub1.ass sub_final.ass
	mv "$SIN_ESPACIOS" $path_pelicula
	#
	#	echo -e "\n\n\nPelicula, "$SIN_ESPACIOS", ha finalizado\n" >> $RE
	#	cat $RE | mailx -s "Finalizó" -S "from=ffmpeg-terminó <NO_RESPONDER>" informe@sinpega.lol
	#
#	rm -rf $RE
fi
echo $end
#
