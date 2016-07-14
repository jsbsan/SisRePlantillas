# SisRePlantillas

**************************************** 
***                                  ***     
*** Sistema de Relleno de Plantillas ***
***                                  ***     
**************************************** 
''IDEA DEL PROGRAMA
Programa para la linea de comandos.

'leer el parametro 2º que es el nombre del archivo que tiene los datos del relleno: NOMBRE

'empezar a analizar el fichero:
'1 quitar todos los comentarios: "'", "/*" ,"//"
'2 crea otra copia y esta si es la que va a analizar
'3 ordenes:
'[origen] XXX -> indica en la siguiente linea la plantilla.svg que debe de leer

'[destino] -> indica donde va a guardar y con que nombre (por defecto nombre de plantilla + _NOMBRE.svg)

'#etiqueta#
'sustituye el texto "#etiqueta#" por el texto indicado a continuacion

'una vez ternimando la lectura del archivo, crea los .pdf y los une, dejando los .svg por si se quiere editar.

'nota:
'tambien es posible definir varios origen y destino, para trabajar con varias plantillas

