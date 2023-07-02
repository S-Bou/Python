from io import *

archivo_texto = open("mifile.txt", "w")

frase = "Estupendo día de noche \nsiendo Sábado"

archivo_texto.write(frase)

archivo_texto.close()

archivo_texto = open("mifile.txt", "r")

text = archivo_texto.read()

archivo_texto.close()

print(text)
