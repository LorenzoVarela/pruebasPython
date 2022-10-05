'''
Excepciones
'''

def evaluaEdad(edad):
    if edad<0:
        raise TypeError("La edad no puede ser menor que cero")

    if edad<20:
        return "Eres muy joven"
    elif edad<40:
        return "Eres joven" 
    elif edad<60:
        return "Eres maduro"
    elif edad<100:
        return "Cuidate ..."

print(evaluaEdad(50))