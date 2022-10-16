from io import *

archivo_texto = open("miArchivo.txt","r")

texto = archivo_texto.read()

print(len(texto))

archivo_texto.close()