#Diccionarios

miDiccionario = {"Alemania":"Berlín", "Francia":"Paris", "Reino unido":"Londres", "España":"Madrid"}

otroDiccionario = {12:"Berlín", "Francia":14, "Reino unido":"Londres", "España":"Madrid"}

miTupla = ("España", "Francia", "Reino Unido", "Alemania")

tercerDiccionario = {miTupla[0]:"Madrid", miTupla[1]:"Paris",miTupla[2]:"Londres",miTupla[3]:"Berlin",}

print(miDiccionario["Francia"])

miDiccionario["Italia"]="Lisboa"

print(miDiccionario)

miDiccionario["Italia"]="Roma"

print(miDiccionario)

del miDiccionario["Reino unido"]

print(miDiccionario)

print(miDiccionario.keys())
print(miDiccionario.values())
print(len(miDiccionario))