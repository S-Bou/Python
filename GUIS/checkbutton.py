from tkinter import *

root=Tk()
root.title("Ejemplo")
root.geometry("250x650")

playa=IntVar()
montana=IntVar()
turismorural=IntVar()

def opcionesViaje():
	opcionEscogida=""

	if playa.get()==1:
		opcionEscogida+=" playa"
	if playa.get()==2:
		opcionEscogida+=" montana"
	if playa.get()==3:
		opcionEscogida+=" turismorural"

	textoFinal.config(text=opcionEscogida)

foto=PhotoImage(file="SkullICO.png")
Label(root, image=foto).pack()

frame=Frame(root)
frame.pack()

Label(frame, text="Elige destino", width=50).pack()

Checkbutton(root, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(root, text="Montaña", variable=playa, onvalue=2, offvalue=0, command=opcionesViaje).pack()
Checkbutton(root, text="Turismo rural", variable=playa, onvalue=3, offvalue=0, command=opcionesViaje).pack()

textoFinal=Label(frame)
textoFinal.pack()

root.mainloop()
