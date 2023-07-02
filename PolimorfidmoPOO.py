
class Coche():

	def Desplazamiento(self):
		print("Me desplazo con 4 ruedas")

class Moto():

	def Desplazamiento(self):
		print("Me desplazo con 2 ruedas")

class Camion():

	def Desplazamiento(self):
		print("Me desplazo con 6 ruedas")

miVehiculo = Moto()
miVehiculo.Desplazamiento()

miVehiculo2 = Coche()
miVehiculo2.Desplazamiento() 

miVehiculo3 = Camion()
miVehiculo3.Desplazamiento() 

def DesplazamientoVehiculo(vehiculo):
	vehiculo.Desplazamiento()

miVehiculo4 = Camion()
DesplazamientoVehiculo(miVehiculo4)
