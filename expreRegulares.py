import re

lista_nombres = [
'Ana Gómez',
'María Martín',
'Sandra López',
'Santiago Martín',
'Sandra Fernandez'
]

for elemento in lista_nombres:
	if re.findall('^Sandra', elemento):
		print(elemento)

nombre1 = "Sandra López"
nombre2 = "Antonio Gómez"
nombre3 = "sandra López"

if re.match("Sandra", nombre3, re.IGNORECASE):
	print("Match: Sí hemos encontrado el nombre")
else:
	print("Match: No lo hemos encontrado")

if re.search("López", nombre1):
	print("Search: Sí hemos encontrado el nombre")
else:
	print("Search: No lo hemos encontrado")