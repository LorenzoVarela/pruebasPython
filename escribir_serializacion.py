import pickle

lista_nombre = ["Pedro","Ana","María", "Isabel"]

fichero_binario = open("lista_nombres","wb")

pickle.dump(lista_nombre, fichero_binario)

fichero_binario.close()

del(fichero_binario)