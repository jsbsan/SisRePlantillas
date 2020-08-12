#!/usr/bin/env python
# -*- coding: utf-8
 
import os,sys
#Variable para la ruta al directorio
path = '.'
 
#Lista vacia para incluir los ficheros
lstFiles = []
 
#Lista con todos los ficheros del directorio:
lstDir = os.walk(path)   #os.walk()Lista directorios y ficheros
 
 
#Crea una lista de los ficheros jpg que existen en el directorio y los incluye a la lista.
 
for root, dirs, files in lstDir:
    for fichero in files:
        (nombreFichero, extension) = os.path.splitext(fichero)
        if(extension == ".png"):
            lstFiles.append(nombreFichero+extension)
            #print (nombreFichero+extension)
             
print(lstFiles)            
print ('LISTADO FINALIZADO')
print "longitud de la lista = ", len(lstFiles)
nombrepdf=lstFiles[1]
nombrepdf=nombrepdf[0:7]

for i in lstFiles:
        comando="convert "+i+" "+i[0:12]+".pdf"	
        salida=os.system(comando)
#convierto en un unico pdf, todos los pdf generados
salida=os.system("pdftk *.pdf cat output "+ nombrepdf+".pdf")    

#borrado de pdf auxiliares...
for i in lstFiles:
        comando=i[0:12]+".pdf"	
        salida=os.remove(comando)

print ("Convertido todos los .png a un unico .pdf: "+ nombrepdf+".pdf")


