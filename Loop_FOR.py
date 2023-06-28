#Loop_FOR

for i in ["primavera", "verano", "otoño", "invierno"]:
	print(i, end=" ")
print()
for i in range(5, 50, 3):
	print(f"Valor de la variable {i}")

valido = False

email = input("Introduce tu email: ")

for i in range(len(email)):
	if email[i]=="@":
		valido = True

if valido:
	print("Email correcto")

else:
	print("Email incorrecto")