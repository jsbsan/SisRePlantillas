# SisRePlantillas

**************************************** 
 # Sistema de Relleno de Plantillas 
**************************************** 
IDEA DEL PROGRAMA

Programa para la linea de comandos.

leer el parametro 2º que es el nombre del archivo que tiene los datos del relleno: NOMBRE

empezar a analizar el fichero:

1 quitar todos los comentarios: "'", "/*" ,"//","*"

2 crea otra copia y esta si es la que va a analizar

3 ordenes:
# [origen] XXX 
-> indica en la siguiente columnas la plantilla.svg (XXX) que debe de leer


# [destino] YYY(&nombre) 
-> indica donde va a guardar y con que nombre (por defecto nombre de plantilla + _NOMBRE.svg)

# #etiqueta#  dato


'sustituye el texto "#etiqueta#" por el dato indicado en la siguiente columnas

Para añadir imagen a la plantilla:
[imagen] nombre

[x] numero

[y] numero

[fw]  numero

[fh]  numero

x: indica la coordenada x donde se inserta la imagen (esquina inferior izq)

y: indica la coordenada y donde se inserta la imagen  (esquina inferior izq)

fw: indica ancho de la imagen que tendra en la plantilla

fh: indica alto de la imagen que tendra en la plantilla 


Si no hay indicaciones de fw y fh, se establece anchos segun el nombre del archivo de iamgen.

Si termina en "V.png"
    w = 350
    h = 467



Si termina en "H.png" 
    w = 420
    H= 315






'una vez ternimando la lectura del archivo, se añaden los datos y se crean  los .svg (por si se quiere editar) y las imagenes .png de dichos archivos .svg.

'nota:
'tambien es posible definir varios origen y destino, para trabajar con varias plantillas en el mismo archivo de datos

