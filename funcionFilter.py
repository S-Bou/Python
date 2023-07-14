def numero_par(num):
	if num % 2 == 0:
		return True

numeros = [17, 24, 7, 39, 8, 51, 92]

#print(list(filter(numero_par, numeros)))

# Filter + lambda
print(list(filter(lambda numero_par: numero_par%2==0, numeros)))

class Empleado:
	def __init__(self, nombre, cargo, salario):
		self.nombre=nombre
		self.salario=salario
		self.cargo=cargo

	def __str__(self):
		return "{} que trabaja como {} tiene un salario de {} €".format(self.nombre, self.cargo, self.salario)


listaEmpleador = [

Empleado("Juan", "Director", 750000),
Empleado("Ana", "Presidente", 850000),
Empleado("Antonio", "Administrativo", 25000),
Empleado("Sara", "Secretaria", 27000),
Empleado("Mario", "Botones", 21000)

]

salarios_altos = filter(lambda empleado:empleado.salario>50000, listaEmpleador)

for empleado_salario in salarios_altos:
	print(empleado_salario)


