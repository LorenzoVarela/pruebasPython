class Vehiculos():

    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.enmarcha=True
    
    def acelera(self):
        self.acelera=True

    def frenar(self):
        self.frena=True
    
    def estado(self):
        print ("Marca: ", self.marca,"\nModelo: ", self.modelo,"\nenmarcha: ", self.enmarcha,
              "\nacelera: ",self.acelera, "\nfrena: ", self.frena)

class Moto(Vehiculos):
    hcaballito="No hace caballito"

    def caballito(self):
        self.hcaballito="Haciendo caballito"
    
    def estado(self):
        print ("Marca: ", self.marca,"\nModelo: ", self.modelo,"\nenmarcha: ", self.enmarcha,
              "\nacelera: ",self.acelera, "\nfrena: ", self.frena, "\n ", self.hcaballito)

class Furgoneta(Vehiculos):
    def carga(self, cargar):
        self.cargado=cargar
        if (self.cargado):
            return "La furgoneta  está cargada"
        else:
            return "La furgoneta NO está cargada"


class quad(Moto):
    pass


class VElectrico():
    def __init__(self):
        self.autonomia=100

    def cargarEnergia(self):
        self.cargando=True
    

class EBicicleta(VElectrico, Vehiculos):
    pass

