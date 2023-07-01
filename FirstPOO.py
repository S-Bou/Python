
class Coche():

	def __init__(self):
		self.__largoChasis = 250
		self.__anchoChasis = 120
		self.__ruedas = 4  #Encapsulado
		self.__enmarcha = False

	#PROPIEDADES ---------------------------------------------------------------------------


	#ATRIBUTOS -------------------------------------------------------------------------------
	def arranca(self, arrancamos):
		self.__enmarcha = arrancamos

		if(self.__enmarcha):
			chequeo = self.__chequeo_interno()

		if(self.__enmarcha and chequeo):
			return "El coche está en marcha."
		elif(self.__enmarcha and chequeo == False):
			return "Algo ha ido mal en el chequeo, no se puede arrancar."
		else:
			return "El coche está parado."
	
	def estado(self):
		print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ",
		self.__anchoChasis, " uy un largo de ", self.__largoChasis)

	def __chequeo_interno(self):
		print("Realizando chequeo interno")
		self.gasolina = "ok"
		self.aceite = "ok"
		self.puertas = "cerradas"

		if(self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
			return True
		else:
			return False

print("-------------- A continuación creamos el primer objeto  ----------------")
miCoche1 = Coche()
print(miCoche1.arranca(True))
miCoche1.estado()

print("-------------- A continuación creamos el segundo objeto ----------------")
miCoche2 = Coche()
print(miCoche2.arranca(False))
miCoche2.estado()

