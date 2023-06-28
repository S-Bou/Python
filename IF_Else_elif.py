print("Verificación de acceso")

edad_usuario = int(input("Introduce tu edad, por favor"))

if edad_usuario < 18:
	print("No puedes pasar")
elif edad_usuario > 100:
	print("Edad incorrecta")
else:
	print("Pudes pasar")

if 0 < edad < 100:
	pass

print("El programa ha finalizado")