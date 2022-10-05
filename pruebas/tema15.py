'''for i in ["Pildoras","Informaticas",3]:
    print("Hola!", end= " ")
'''
miEmail = input("Tu dirección de email:")

email = False

for i in miEmail:
    if(i=="@"):
        email = True

if (email == True):
    print ("Email correcto")
else:
    print ("Email incorrecto")
