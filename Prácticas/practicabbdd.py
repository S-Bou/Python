from tkinter import *
from tkinter import messagebox
import sqlite3


# ------------------------- FUNCIONES --------------------------------------
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

def limpiarCampos():
	miNombre.set("")
	miId.set("")
	miApellido.set("")
	miPass.set("")
	miDireccion.set("")
	textoComnetario.delete(1.0, END)

def crear():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()

	datos=miNombre.get(), miPass.get(), miApellido.get(), miDireccion.get(), textoComnetario.get("1.0", END)


	"""miCursor.execute("INSERT INTO DatosUsuarios VALUES(NULL, '" + miNombre.get() +
		"','" + miPass.get() +
		"','" + miApellido.get()+
		"','" + miDireccion.get() +
		"','" + textoComnetario.get("1.0", END) + "')")"""

	miCursor.execute("INSERT INTO DatosUsuarios VALUES(NULL,?,?,?,?,?)", (datos))

	miConexion.commit()

	messagebox.showinfo("BBDD", "Registro insertado con éxito")

def leer():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()

	miCursor.execute("SELECT * FROM DatosUsuarios WHERE ID=" + miId.get())
	
	elUsuario=miCursor.fetchall()

	for usuario in elUsuario:
		miId.set(usuario[0])
		miNombre.set(usuario[1])
		miPass.set(usuario[2])
		miApellido.set(usuario[3])
		miDireccion.set(usuario[4])
		textoComnetario.insert(1.0, usuario[5])

	miConexion.commit()

def actualizar():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()

	miCursor.execute("UPDATE DatosUsuarios SET nombre_usuario='" + miNombre.get() +
		"', password='" + miPass.get() + 
		"', apellido='" + miApellido.get() + 
		"', direccion='" + miDireccion.get() + 
		"', comentarios='" + textoComnetario.get("1.0", END) + 
		"' WHERE ID=" + miId.get())

	miConexion.commit()
	messagebox.showinfo("BBDD", "Registro actualizado con éxito")

def eliminar():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()

	miCursor.execute("DELETE FROM DatosUsuarios WHERE ID=" + miId.get())

	miConexion.commit()
	messagebox.showinfo("BBDD", "Registro borrado con éxito")

# ---------------------------- MAINWINDOW -------------------------------------------------

root = Tk()
root.title("Gestión BBDD")
barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

root.eval('tk::PlaceWindow . center')

bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=salirAplicacion)

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos", command=limpiarCampos)

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crea", command=crear)
crudMenu.add_command(label="Lee", command=leer)
crudMenu.add_command(label="Actualizar", command=actualizar)
crudMenu.add_command(label="Borrar", command=eliminar)

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

miId=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPass=StringVar()
miDireccion=StringVar()

cuadroID=Entry(miFrame, textvariable=miId)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="right")

cuadroPass=Entry(miFrame, textvariable=miPass)
cuadroPass.grid(row=2, column=1, padx=10, pady=10)
cuadroPass.config(show="?")

cuadroApellido=Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame, textvariable=miDireccion)
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

botonCrear=Button(miFrame2, text="Create", command=crear)
botonCrear.grid(row=0, column=0, padx=10, pady=10, sticky="e")

botonLeer=Button(miFrame2, text=" Read ", command=leer)
botonLeer.grid(row=0, column=1, padx=10, pady=10, sticky="e")

botonActualizar=Button(miFrame2, text="Update", command=actualizar)
botonActualizar.grid(row=0, column=2, padx=10, pady=10, sticky="e")

botonBorrar=Button(miFrame2, text="Delete", command=eliminar)
botonBorrar.grid(row=0, column=3, padx=10, pady=10, sticky="e")

root.mainloop()