import pickle

class Persona():
	def __init__(self, nombre, genero, edad):
			self.nombre = nombre
			self.genero = genero
			self.edad = edad
			print(f"Se ha creado una persona con el nombre: {self.nombre}")

	def __str__(self):
		return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas:
	personas = []

	def __init__(self):
		listaDePersonas = open("ext_file", "ab+")
		listaDePersonas.seek(0)						#Situar el cursor al inicio del fichero

		try:
			self.personas = pickle.load(listaDePersonas)
			print(f"Se han cargado los datos de {len(self.personas)} personas.")
		except:
			print("El fichero está vacío.")
		finally:
			listaDePersonas.close()
			del(listaDePersonas)

	def setPersona(self, p):
		self.personas.append(p)
		self.SavePeopleInFile()

	def getPersonas(self):
		for p in self.personas:
			print(p) 

	def SavePeopleInFile(self):
		listaDePersonas = open("ext_file", "wb")
		pickle.dump(self.personas, listaDePersonas)
		listaDePersonas.close()
		del(listaDePersonas)

	def ReadInfoExternFile(self):
		print("Data readed: ")
		for p in self.personas:
			print(p)


miLista = ListaPersonas()
persona = Persona("Ana", "Femenino", 19)
miLista.setPersona(persona)
miLista.ReadInfoExternFile()

