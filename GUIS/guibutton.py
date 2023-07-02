from tkinter import *

raiz = Tk()
raiz.title("Primera ventana")

miFrame = Frame(raiz, width=1200, height=600, pady=15, padx=15)
miFrame.pack()

minombre = StringVar()

cuadroNombre = Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=0, column=1, pady=4, padx=4)
cuadroNombre.config(fg="blue", justify="center")

cuadroPass = Entry(miFrame)
cuadroPass.grid(row=1, column=1, pady=4, padx=4)
cuadroPass.config(fg="blue", justify="center", show="*")

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=2, column=1, pady=4, padx=4)
cuadroApellido.config(fg="blue", justify="center")

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, pady=4, padx=4)
cuadroDireccion.config(fg="blue", justify="center")

textComments = Text(miFrame, width=15, height=5)
textComments.grid(row=4, column=1, pady=4, padx=4)

scrollVert = Scrollbar(miFrame, command=textComments.yview)
scrollVert.grid(row=4, column=2, sticky="nsew", pady=4)

textComments.config(yscrollcommand=scrollVert.set)

nombreLabel = Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=0, column=0, sticky="w", pady=4, padx=4)

passLabel = Label(miFrame, text="Password: ")
passLabel.grid(row=1, column=0, sticky="w", pady=4, padx=4)

apellidoLabel = Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=2, column=0, sticky="w", pady=4, padx=4)

direccionLabel = Label(miFrame, text="Dirección: ")
direccionLabel.grid(row=3, column=0, sticky="w", pady=4, padx=4)

labelcomments = Label(miFrame, text="Comentarios: ")
labelcomments.grid(row=4, column=0, sticky="w", pady=4, padx=4)

def codigoBoton():
	minombre.set("Juan")

botonEnvio = Button(raiz, text="Enviar", command=codigoBoton)
#botonEnvio.grid(row=5, column=0, pady=4, padx=4)
botonEnvio.pack(anchor="center", pady=4, padx=4)

#botonLimpiar = Button(miFrame, text="Limpiar", command=codigoBoton)
#botonLimpiar.grid(row=5, column=1, pady=4, padx=4)

raiz.mainloop()