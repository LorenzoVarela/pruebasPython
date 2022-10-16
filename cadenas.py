nombreUsuario=input("Introduce tu nombre: ")
edad=input("Introduce tu edad")

while(edad.isdigit()==Fales):
    print("Introduce un valor correcto")
    edad=input("Introduce tu edad")

print("tu nombre es: ", nombreUsuario.upper())
pritn("Tu edad es: ", edad)