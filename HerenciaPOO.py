
class Vehiculos():

	def __init__(self, marca, modelo):
		self.marca = marca
		self.modelo = modelo
		self.enmarcha = False
		self.acelera = False
		self.frena = False

	def Arrancar(self):
		self.enmacha = True

	def Acelerar(self):
		self.acelera = True

	def Frenar(self):
		self.frena = True

	def Estado(self):
		print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",
			self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

class Moto(Vehiculos):
	pass

miMoto = Moto("Yamaha", "XVS")
miMoto.Estado()
