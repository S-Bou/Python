
class Empleado:
	def __init__(self, nombre, cargo, salario):
		self.nombre=nombre
		self.salario=salario
		self.cargo=cargo

	def __str__(self):
		return "{} que trabaja como {} tiene un salario de {} €".format(self.nombre, self.cargo, self.salario)


listaEmpleador = [

Empleado("Juan", "Director", 6700),
Empleado("Ana", "Presidente", 7500),
Empleado("Antonio", "Administrativo", 2100),
Empleado("Sara", "Secretaria", 2150),
Empleado("Mario", "Botones", 1800)

]

def calculo_comision(empleado):
	if(empleado.salario<=3000):
		empleado.salario=empleado.salario*1.03

	return empleado

listaEmpleadosComision=map(calculo_comision, listaEmpleador)

for empleado in listaEmpleadosComision:
	print(empleado)


