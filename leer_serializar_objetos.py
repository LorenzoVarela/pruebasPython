import pickle
from Modulos.modulo_vehiculo import *


fichero = open("losCoches","rb")

misCoches = pickle.load(fichero)

fichero.close()

for c in misCoches:
    print(c.estado())


del(fichero)
