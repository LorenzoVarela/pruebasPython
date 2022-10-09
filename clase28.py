class Coche():
    def __init__(self):
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__rueda = 4
        self.__enmarcha=False

    def arrancar(self, arrancamos):
        
        self.__enmarcha=arrancamos

        if(self.__enmarcha):
            chequeo=self.__chequeo_interno()

        if(self.__enmarcha and chequeo):
            return "El coche está en marcha"
        elif(self.__enmarcha and chequeo==False):
            return "Algun error en el chequeo"
        else:
            return "El coche está parado"
    
    def estado(self):
        print ("El coche tiene ", self.__rueda, " ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ",
        self.__largoChasis)
    
    def __chequeo_interno(self):
        print("realizando chequeo interno")
        self.gasolina="ok"
        self.aceinte="ko"
        self.puertas="cerradas"

        if (self.gasolina=="ok" and self.aceinte=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False

    
        
miCoche=Coche()

print(miCoche.arrancar(True))

miCoche.estado()

print("------------------------ instanciamos otro coche ------------------------")

miCoche2=Coche()
miCoche2.estado()
