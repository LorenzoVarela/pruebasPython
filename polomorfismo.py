class Coche():
    def deplazamiento(self):
        print("ME desplazo empleand 4 ruedas")

class Moto():
    def deplazamiento(self):
        print("ME desplazo empleand 2 ruedas")

class Camion():
    def deplazamiento(self):
        print("ME desplazo empleand 6 ruedas")


def desplamientoVehiculo(vehiculo):
    vehiculo.deplazamiento()

vehiculo=Coche()
desplamientoVehiculo(vehiculo)