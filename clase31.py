class Persona():
    def __init__(self, nombre, edad, residencia):
        self.nombre = nombre
        self.edad = edad
        self.residencia = residencia

    def descripcion(self):
        print("Nombre: ", self.nombre, " Edad: ", self.edad, " Residencia: ", self.residencia)

class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        super().__init__(nombre_empleado,edad_empleado,residencia_empleado)
        self.salario = salario
        self.antiguedad = antiguedad
    def descripcion(self):
        super().descripcion()
        print("\nSalario: ", self.salario," Antigüedad: ", self.antiguedad)



empleados=Empleado(1500, 15, "Manuel", 55, "Colombia")
empleados.descripcion()

print(isinstance(empleados, Empleado))
print(isinstance(empleados, Persona))