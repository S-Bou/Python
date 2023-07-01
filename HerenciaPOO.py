
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
			self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n")

class Furgoneta(Vehiculos):

	def Carga(self, cargar):
		self.cargado = cargar
		if(self.cargado):
			return "La furgoneta está cargada"
		else:
			return "La furgoneta no está cargada"

class Moto(Vehiculos):
	hcaballito = ""

	def Caballito(self):
		self.hcaballito = "Haciendo caballito"

	def Estado(self):
		print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",
			self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena,
			"\n", self.hcaballito)

class VElectrico():

	def __init__(self):
		self.autonomia = 100

	def CargarEnergia(self):
		self.cargando = True

class BicicletaElectrica(Vehiculos, VElectrico):
	pass

miBici = BicicletaElectrica("Orbea", "HBO")
miBici.Estado()

miMoto = Moto("Yamaha", "XVS")
miMoto.Caballito()
miMoto.Estado()

miFurgoneta = Furgoneta("Mercedes", "Vito")
miFurgoneta.Arrancar()
miFurgoneta.Estado()
print(miFurgoneta.Carga(True))
