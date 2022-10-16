from io import open


archivo_texto = open("miArchivo.txt","w")

frase="Estupendo día para hacer estas cosas \n el sabado"

archivo_texto.write(frase)

archivo_texto.close()

archivo_texto2 = open("miArchivo.txt","r")
texto = archivo_texto2.read()
archivo_texto2.close()
print(texto)

archivo_texto2 = open("miArchivo.txt","r")
leneas_texto = archivo_texto2.readlines()
archivo_texto2.close()
print(leneas_texto[0])

archivo_texto2 = open("miArchivo.txt","a")
archivo_texto2.write("\n Linea nueva")
archivo_texto2.close()
