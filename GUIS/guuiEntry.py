from tkinter import *

raiz = Tk()
raiz.title("Primera ventana")

miFrame = Frame(raiz, width=1200, height=600, pady=15, padx=15)
miFrame.pack()

cuadroNombre = Entry(miFrame)
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

nombreLabel = Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=0, column=0, sticky="w", pady=4, padx=4)

passLabel = Label(miFrame, text="Password: ")
passLabel.grid(row=1, column=0, sticky="w", pady=4, padx=4)

apellidoLabel = Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=2, column=0, sticky="w", pady=4, padx=4)

direccionLabel = Label(miFrame, text="Dirección de envío: ")
direccionLabel.grid(row=3, column=0, sticky="w", pady=4, padx=4)

raiz.mainloop()
