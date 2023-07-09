from tkinter import *
from tkinter import messagebox
import sqlite3


# ------------------------- FUUNCIONES --------------------------------------
def conexionBBDD():
	miConexion = sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()
	try:
		miCursor.execute(''' 
			CREATE TABLE DatosUsuarios (
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				nombre_usuario VARCHAR(50),
				password VARCHAR(50),
				apellido VARCHAR(10),
				direccion VARCHAR(50),
				comentarios VARCHAR(100))
			''')
		messagebox.showinfo("BBDD", "BBDD creada con éxito")
	except:
		messagebox.showwarning("¡Atención!", "La base de datos ya existe.")

def salirAplicacion():
	valor = messagebox.askquestion("Salir", "¿Desea salir de la aplicación?")
	if(valor=="yes"):
		root.destroy()


root = Tk()
root.title("Gestión BBDD")
barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

root.eval('tk::PlaceWindow . center')

bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=salirAplicacion)

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos")

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crea")
crudMenu.add_command(label="Lee")
crudMenu.add_command(label="Actualizar")
crudMenu.add_command(label="Borrar")

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de ...")

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

# ---------------------- CAMPOS --------------------------------

miFrame = Frame(root)
miFrame.pack()

cuadroID=Entry(miFrame)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="right")

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=2, column=1, padx=10, pady=10)
cuadroPass.config(show="?")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

textoComnetario=Text(miFrame, width=16, height=5)
textoComnetario.grid(row=5, column=1, padx=10, pady=10)
scrollVert=Scrollbar(miFrame, command=textoComnetario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")

textoComnetario.config(yscrollcommand=scrollVert.set)

# ------------------------ LABELS -----------------------------------

idLabel=Label(miFrame, text="ID:")
idLabel.grid(row=0, column=0, padx=10, pady=10, sticky="e")

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=1, column=0, padx=10, pady=10, sticky="e")

passLabel=Label(miFrame, text="Password:")
passLabel.grid(row=2, column=0, padx=10, pady=10, sticky="e")

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=3, column=0, padx=10, pady=10, sticky="e")

direccionLabel=Label(miFrame, text="Dirección:")
direccionLabel.grid(row=4, column=0, padx=10, pady=10, sticky="e")

comentariosLabel=Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=5, column=0, padx=10, pady=10, sticky="e")

# --------------------- BOTONES ----------------------------------------

miFrame2=Frame(root)
miFrame2.pack()

botonCrear=Button(miFrame2, text="Create")
botonCrear.grid(row=0, column=0, padx=10, pady=10, sticky="e")

botonLeer=Button(miFrame2, text=" Read ")
botonLeer.grid(row=0, column=1, padx=10, pady=10, sticky="e")

botonActualizar=Button(miFrame2, text="Update")
botonActualizar.grid(row=0, column=2, padx=10, pady=10, sticky="e")

botonBorrar=Button(miFrame2, text="Delete")
botonBorrar.grid(row=0, column=3, padx=10, pady=10, sticky="e")

root.mainloop()