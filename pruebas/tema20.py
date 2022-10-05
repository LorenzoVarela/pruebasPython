'''
yield from
'''

def devuleveCiudades(*ciudades):
    for elemento in ciudades:
        #for subElemento in elemento:
            #yield subElemento
        yield from elemento


ciudadades_devueltas = devuleveCiudades("Madrid","Barcelona","Bilbao","Valencia")

print(next(ciudadades_devueltas))
print(next(ciudadades_devueltas))
