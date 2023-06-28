#Generadores

#Funcion normal (return)
def FuncionPares(limite):
	num = 1
	miLista = []

	while num < limite:
		miLista.append(num*2)
		num += 1

	return miLista


print(FuncionPares(10))

#Generador
def generaPares(limite):
	num = 1

	while num < limite:
		yield num*2
		num += 1

devuelvePares = generaPares(10)

print(next(devuelvePares))

print("Más Código")

print(next(devuelvePares))

print("Más Código")

print(next(devuelvePares))

print("Más Código")

print(next(devuelvePares))