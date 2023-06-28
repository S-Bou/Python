#Tuplas

mitupla = ("Juan", 12, 1, 666)

otraTupla = "Juan", 12, 1, 666, 666

milista = list(mitupla)

mitupla2 = tuple(milista)

print(mitupla2)

print("Juan" in mitupla)

print(otraTupla.count(666))

print(len(mitupla))

mituplaunitaria = ("Pepe",)

print(len(mituplaunitaria))

varuno, vardos, vartres, varcuatro = mitupla

print(varuno, vardos, vartres, varcuatro)