from tkinter import *

root = Tk()

miFrame = Frame(root, width=500, height=500)

miFrame.pack()

miImage = PhotoImage(file="SkullICO.png")

#Label(miFrame, text="Hola mundo", fg="red", font=("Comic Sans MS", 18)).place(x=200, y=200)

Label(miFrame, image=miImage).place(x=10, y=10)

root.mainloop()