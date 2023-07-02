from tkinter import *

raiz = Tk()
raiz.title("Calculadora")
miFrame = Frame(raiz, padx=10, pady=10, background="black")

miFrame.pack()
WidthB = 6
HeightB = 2
operacion = ""
resultado = 0
#----------------------------- PANTALLA --------------------------------
numeroPantalla = StringVar()
pantalla = Entry(miFrame, textvariable=numeroPantalla, font=("Comic Sans MS", 12))
pantalla.grid(row=0, column=0, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")

#---------------------------- Pulsaciones teclado ---------------------------
def numeroPulsado(numero):
	global operacion 
	
	if(operacion != ""):
		numeroPantalla.set(numero)
		operacion = ""
	else:
		numeroPantalla.set(numeroPantalla.get() + numero)

#---------------------------- Función SUMA ----------------------------------------
def suma(num):
	global operacion
	global resultado

	operacion = "suma"
	resultado += int(num)
	numeroPantalla.set(resultado)

#---------------------------- Funcion EL_RESULTADO -------------------------------
def ElResultado():
	global resultado
	numeroPantalla.set(resultado+int(numeroPantalla.get()))
	resultado = 0

#---------------------------- Fila de BOTONES 1 -----------------------------
boton7 = Button(miFrame, text="7", width=WidthB, height=HeightB, command=lambda:numeroPulsado("7"))
boton7.grid(row=1, column=0)
boton8 = Button(miFrame, text="8", width=WidthB, height=HeightB, command=lambda:numeroPulsado("8"))
boton8.grid(row=1, column=1)
boton9 = Button(miFrame, text="9", width=WidthB, height=HeightB, command=lambda:numeroPulsado("9"))
boton9.grid(row=1, column=2)
botonDivi = Button(miFrame, text="/", width=WidthB, height=HeightB, command=lambda:numeroPulsado("/"))
botonDivi.grid(row=1, column=3)

#---------------------------- Fila de BOTONES 2 -----------------------------
boton4 = Button(miFrame, text="4", width=WidthB, height=HeightB, command=lambda:numeroPulsado("4"))
boton4.grid(row=2, column=0)
boton5 = Button(miFrame, text="5", width=WidthB, height=HeightB, command=lambda:numeroPulsado("5"))
boton5.grid(row=2, column=1)
boton6 = Button(miFrame, text="6", width=WidthB, height=HeightB, command=lambda:numeroPulsado("6"))
boton6.grid(row=2, column=2)
botonMult = Button(miFrame, text="x", width=WidthB, height=HeightB, command=lambda:numeroPulsado("x"))
botonMult.grid(row=2, column=3)

#---------------------------- Fila de BOTONES 3 -----------------------------
boton1 = Button(miFrame, text="1", width=WidthB, height=HeightB, command=lambda:numeroPulsado("1"))
boton1.grid(row=3, column=0)
boton2 = Button(miFrame, text="2", width=WidthB, height=HeightB, command=lambda:numeroPulsado("2"))
boton2.grid(row=3, column=1)
boton3 = Button(miFrame, text="3", width=WidthB, height=HeightB, command=lambda:numeroPulsado("3"))
boton3.grid(row=3, column=2)
botonRest = Button(miFrame, text="-", width=WidthB, height=HeightB, command=lambda:numeroPulsado("-"))
botonRest.grid(row=3, column=3)

#---------------------------- Fila de BOTONES 4 -----------------------------
botonComa = Button(miFrame, text=",", width=WidthB, height=HeightB, command=lambda:numeroPulsado(","))
botonComa.grid(row=4, column=0)
boton0 = Button(miFrame, text="0", width=WidthB, height=HeightB, command=lambda:numeroPulsado("0"))
boton0.grid(row=4, column=1)
botonIgual = Button(miFrame, text="=", width=WidthB, height=HeightB, command=lambda:ElResultado())
botonIgual.grid(row=4, column=2)
botonSuma = Button(miFrame, text="+", width=WidthB, height=HeightB, command=lambda:suma(numeroPantalla.get()))
botonSuma.grid(row=4, column=3)





raiz.mainloop()
