#ContinuePass

nombre = "Pildoras informaticas"
contador = 0
for i in nombre:

	if i == " ":
		continue
	contador += 1
	
print(f"Sin espacios = {contador}")
print(f"Con espacios = {len(nombre)}")

class MiClase:
	pass #Para implementar más tarde

email = input("Introduce tu email, por favor: ")

for i in email:
	if i == "@":
		arroba = True
		break

else:
	arroba = False

print(arroba)