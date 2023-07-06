#from tkinter import *
import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.title("Ejemplo")
root.geometry("650x350")

def infoAdicional():
	messagebox.showinfo("Procesador de Juan", "Procesador de textos versión 2018")

def avisoLicencia():
	messagebox.showwarning("Licencia", "Producto bajo licencia GNU")

def salirAplicacion():
	#valor = messagebox.askquestion("Salir", "¿Desea salir de la aplicación?") #devuelve: yes/no
	valor = messagebox.askokcancel("Salir", "¿Desea salir de la aplicación?") #Devuelve True/False
	#if valor=="yes":
	if valor:
		root.destroy()

def cerrarDocumento():
	valor = messagebox.askretrycancel("Reintentar", "No es posible cerrar. Documento bloqueado.")
	if not valor:
		root.destroy()


barraMenu=tk.Menu(root)
root.config(menu=barraMenu)

archivoMenu=tk.Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)
archivoMenu.add_command(label="Salir", command=salirAplicacion)

archivoEdicion=tk.Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas=tk.Menu(barraMenu, tearoff=0)

archivoAyuda=tk.Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de ...", command=infoAdicional)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edición", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

root.mainloop()
