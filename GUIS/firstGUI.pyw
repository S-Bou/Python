from tkinter import *

raiz = Tk()

raiz.title("Primera ventana")

#raiz.resizable(True, False)

raiz.iconbitmap("SkullICO.ico")

#raiz.geometry("650x350")

raiz.config(bg="blue")

raiz.config(bd="25")

raiz.config(relief="groove")

raiz.config(cursor="hand2")

miFrame = Frame()

miFrame.pack()

miFrame.config(bg="red")

miFrame.config(width="650", height="350")

miFrame.config(bd="35")

miFrame.config(relief="sunken")

miFrame.config(cursor="pirate")

varLabel = Label(miFrame, Text="Hola M")

raiz.mainloop()