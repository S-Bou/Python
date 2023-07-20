from tkinter import *
from tkinter import messagebox
import random
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

	messagebox.showinfo("BBDD", "Registro insertado con éxito")

def leer():
	numero = random.randrange(0, 99)
	miId.set(str(numero))

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

# ---------------------- CAMPOS --------------------------------

miFrame = Frame(root)
miFrame.pack()

miId=StringVar()


cuadroID=Entry(miFrame, textvariable=miId)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

# ------------------------ LABELS -----------------------------------

idLabel=Label(miFrame, text="ID:")
idLabel.grid(row=0, column=0, padx=10, pady=10, sticky="e")

# --------------------- BOTONES ----------------------------------------

miFrame2=Frame(root)
miFrame2.pack()

botonCrear=Button(miFrame, text="Número", command=leer)
botonCrear.grid(row=0, column=0, padx=10, pady=10, sticky="e")


root.mainloop()