from tkinter import *
from tkinter import filedialog

root=Tk()
root.title("Ejemplo")
root.geometry("650x350")

def abreFichero():
	file = filedialog.askopenfilename(title="Abrir", initialdir="C:/Users/bouyo/Downloads", 
		filetypes=(("Ficheros de Excel", "*.xlsx"), ("Ficheros de texto", "*.txt"), ("Todos los ficheros", "*.*")))
	print(file)

Button(root, text="Abrir fichero", command=abreFichero).pack()

root.mainloop()
