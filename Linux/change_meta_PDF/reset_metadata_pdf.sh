#!/bin/bash
# kurotom

args=$(echo $* | wc -w)

if [ $args == 0 ]; then
	echo -e "\nUso: \n$0 fichero_original fichero_final\n"
else
	if [[ $args > 0 && $args < 3 ]]; then

		original=$(echo $1)
		final=$(echo $2)

		if [[ $original == *.pdf && $final == *pdf ]]; then

			filemarks="pdfmarks"

			marcas="""
				[ /Title (Title Document)\n
			    /Author (Name author)\n
			    /Subject ()\n
			    /Keywords ()\n
			    /ModDate (D:YYYYMMDDHHmmSS)\n
			    /CreationDate (D:YYYYMMDDHHmmSS)\n
			    /Creator (Name creator)\n
			    /Producer ()\n
			    /DOCINFO pdfmark\n
			"""
		
			echo -e $marcas > $filemarks

			linkFile1=$(readlink -f $1)

			if [[ -f $linkFile1 ]]; then

				gs -dSAFER -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile=$final $original $filemarks
				rm $filemarks

			else

				echo "Ficheros no existe/n."

			fi


			echo -e "\a\nFinalizado.\n"

		else
			echo -e "Argumento 1 debe ser un fichero PDF\nArgumento 2 debe tener una extensión PDF."
		fi


	else
		echo -e "\nUso: \n$0 fichero_original.pdf nombre_fichero_final.pdf\n"
	fi

fi


# kurotom
