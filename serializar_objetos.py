import pickle
from Modulos.modulo_vehiculo import *


coche1=Vehiculos("Mazda","MX")
coche2=Vehiculos("Seat","Leon")
coche3=Vehiculos("Renault","Megane")

coches = [coche1, coche2, coche3]

fichero=open("losCoches","wb")
pickle.dump(coches, fichero)
fichero.close()

del(fichero)