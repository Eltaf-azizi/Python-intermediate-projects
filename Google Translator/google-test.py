from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Translator")
root.geometry("400x800")
root.config(bg='Red')



frame = Frame(root).pick(side=BOTTOM)


lab_txt = Label(root, text= "Sourse Text", font=("Time New Roman", 20, "Bold"), fg="Black")

lab_txt.place(x=100, y=100, height=20, width=300)



Sortxt = Text(frame, font=("Time New Roman", 20, "bold"), wrap=WORD)

Sortxt.place(x=10, y=130, height=200, width=480)


root.mainloop()