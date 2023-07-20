import doctest
import re

class Areas:
	'''Esta clase calcula las áreas de diferentes figuras geométricas'''
	def areaCuadrado(lado):
		'''Calcula el área de un cuadrado elevando al cuadrado el lado pasado por parámetro'''
		return "El área del cuadrado 3s: " + str(lado*lado)

	def areaTriangulo(base, altura):
		'''
		Calcula el área de un triangulo utilizando los parámetros base y altura

		>>> Areas.areaTriangulo(3, 6)
		'El área del triangulo es: 9.0'

		>>> Areas.areaTriangulo(4, 5)
		'El área del triangulo es: 10.0'

		>>> Areas.areaTriangulo(3, 9)
		'El área del triangulo es: 13.5'
		

		'''
		return "El área del triangulo es: " +str((base*altura)/2)

	def compruebaMail(mailUsuario):
		'''
		La función compruebaMail evalúa un mail recibido en busca de la @.
		Si tiene una @ es correcto, si tiene más de una @ es incorrecto, 
		si la @ está al final es incorrecto.

		>>> Areas.compruebaMail('juan@cursos.es')
		True

		>>> Areas.compruebaMail('juancursos.es@')
		False

		>>> Areas.compruebaMail('juancursos.es')
		False

		>>> Areas.compruebaMail('juan@cursos@.es')
		False

		'''
		arroba = mailUsuario.count('@')

		if(arroba!=1 or mailUsuario.rfind('@')==(len(mailUsuario)-1) or mailUsuario.find('@')==0):
			return False
		else:
			return True


doctest.testmod()