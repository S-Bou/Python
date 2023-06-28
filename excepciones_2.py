import math 

def divide():
	try:
		op1 = float(input("Introduce el primer número: "))

		op2 = float(input("Introduce el segundo número: "))

		print("La división es: " + str(op1/op2))
	except ValueError:
		print("El valor introducido es erroneo")
	except ZeroDivisionError:
		print("No se puede dividir entre cero")
	finally:
		print("Cálculo finalizado")

#divide()

def evaluaEdad(edad):
	if edad < 0:
		raise TypeError("No se permiten edades negativas")

	if edad < 20:
		return "Eres muy joven"
	elif edad < 40:
		return "Eres joven"
	elif edad < 65:
		"Eres maduro"
	elif edad < 100:
		return "cuidate"

print(evaluaEdad(18))

def calculaRaiz(num1):
	if num1 < 0:
		raise ValueError("El número no puede ser negativo")
	else:
		return math.sqrt(num1)

op1 = int(input("Introduce un número: "))

try:
	print(calculaRaiz(op1))
except ValueError as ErrorDeNumeroNegativo:
	print(ErrorDeNumeroNegativo)

print("Sigue el código")