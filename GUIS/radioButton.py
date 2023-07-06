from tkinter import *

root = Tk()

varOpcion = IntVar()

def Imprimir():
	#print(varOpcion.get())
	if varOpcion.get()==1:
		etiqueta.config(text="Has elegido masculino")
	else:
		etiqueta.config(text="Has elegido femenino")

Label(root, text="Género:").pack()

Radiobutton(root, text="Masculino", variable=varOpcion, value=1, command=Imprimir).pack()
Radiobutton(root, text="Femenino", variable=varOpcion, value=2, command=Imprimir).pack()

etiqueta = Label(root)
etiqueta.pack()

root.mainloop()