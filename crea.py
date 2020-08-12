#!/usr/bin/env python
# -*- coding: utf-8 -*-


#crear un directorio conel nombre del parametro pasado y dentro de ese nuevo directorio
#crea un archivo con el mismo nombre
import sys
import os


print "Número de parámetros: ", len(sys.argv)
print "Lista de argumentos: ", sys.argv
valor=len(sys.argv)
if valor>1:
     print "Valores: ";valor
     os.mkdir(sys.argv[1])
     f = open ( os.getcwd() + "/" + sys.argv[1] + "/"+ sys.argv[1],'w')
     f.close()
