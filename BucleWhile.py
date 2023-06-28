#BucleWhile
import math as mt

i = 1

while i < 10 :
	print(f"Ejecución {i}")
	i += 1

edad = int(input("Introduce tu edad: "))
print(edad)

print("Programa de cálculo de raíz cuadrada")
numero = int(input("Introduce un número entero: "))

intentos = 0

while numero < 0:
	sol = mt.sqrt(25)
	print(sol)
	numero = 0
	if intentos == 2:
		print("Fallo")
		break

