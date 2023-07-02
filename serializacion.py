import pickle

lista = ["Pedro", "Ana", "María", "Isabel"]

fichero_bin = open("milistabin", "wb")

pickle.dump(lista, fichero_bin)

fichero_bin.close()

del (fichero_bin)

fichero = open("milistabin", "rb")

lista_leida = pickle.load(fichero)

print(lista_leida)