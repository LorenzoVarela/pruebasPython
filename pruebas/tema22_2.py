# Excepciones

def divide():
    try:
        op1=(float(input("Introduce el primer núemro: " )))
        op2=(float(input("Introdiuce el segundo níumer: ")))

        print("la división es " + str(op1/op2))
    except ValueError:
        print("El valor introducido es erroneo")
    except ZeroDivisionError:
        print("No se puede dividir por 0")
    except:
        print("A ocurrio un error")
    finally:
        print("Cálculo finalizado")

divide()
