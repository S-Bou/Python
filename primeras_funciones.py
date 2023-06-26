
miLista = ["María", "Pepe", True, 666, 3.1415, "Marta", "Antonio"]

miLista.append("Almudena")

miLista.insert(2, "Sandra")

miLista.extend(["Manolo", "Miguel"])

print(miLista[:])

print(miLista.index("Pepe"))

print("Pepe" in miLista)

print(miLista[3:6])

miLista.remove(666)