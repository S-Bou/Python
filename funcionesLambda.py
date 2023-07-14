
def area_triangulo(base, altura):

	return (base*altura)/2

print(area_triangulo(5, 7))

triangulo1=area_triangulo(5, 7)
triangulo2=area_triangulo(9, 6)

print(triangulo1)
print(triangulo2)

# Función lambda o anónima
area_triangulo_lambda=lambda base, altura:(base*altura)/2

print(f"Lambda: {area_triangulo_lambda(5, 7)}")

al_cubo=lambda numero:pow(numero, 3)

al_cubo_2=lambda numero:numero**3

print(al_cubo_2(13))

destacar_valor=lambda comision:"¡{}! €".format(comision)

comision_ana=15585

print(destacar_valor(comision_ana))
