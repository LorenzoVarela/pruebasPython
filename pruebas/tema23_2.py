from cmath import sqrt


import math

def raizCuadrada(numero):
    if numero<0:
        raise ValueError("El numero no pude ser negativo")
    else:
        return sqrt(numero)


op1=(int(input("Introduce un número: ")))
try:
    print(raizCuadrada(op1))
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)

print("CAlculado")