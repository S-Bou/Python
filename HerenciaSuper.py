
class Persona():
	def __init__(self, nombre, edad, residencia):
		self.nombre = nombre
		self.edad = edad
		self.residencia = residencia

	def Descripcion(self):
		print(f"Nombre: {self.nombre} \nEdad: {self.edad} \nResidencia: {self.residencia}")

class Empleado(Persona):
	def __init__(self, salario, antigüedad, nombre_E, edad_E, residencia_E):

		super().__init__(nombre_E, edad_E, residencia_E)

		self.salario = salario
		self.antigüedad = antigüedad

	def Descripcion(self):
		super().Descripcion()
		print(f"Salario: {self.salario} \nAntigüedad: {self.antigüedad}") 


primerEmpleado = Empleado(1500, 15, "Manuel", 55, "México")
primerEmpleado.Descripcion()

print(isinstance(primerEmpleado, Empleado))
