#yieldFrom

def devuelveCiudades(*ciudades):
	for elemento in ciudades:
		#for subElemento in elemento:
			#yield subElemento
		yield from elemento

ciudadesDevueltas = devuelveCiudades("Madrid", "Bilbao", "Barcelona", "Valencia")

print(next(ciudadesDevueltas))

print(next(ciudadesDevueltas))