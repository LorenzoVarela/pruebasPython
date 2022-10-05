'''for i in range(5,50,3):
    print(f"Valoe de la variable {i}")
    '''

valido = False
email="lorenzo.varela@gmail.com"

for i in range(len(email)):
    if email[i]=="@":
        valido = True

if valido:
    print("Correcto")
else:
    print("Incorrectos")