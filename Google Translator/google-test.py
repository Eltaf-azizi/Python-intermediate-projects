from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Translator")
root.geometry("400x800")
root.config(bg='Red')



frame = Frame(root).pick(side=BOTTOM)


lab_txt = Label(root, text= "Sourse Text", font=("Time New Roman", 20, "Bold"), fg="Black"bg="Red")

lab_txt.place(x=100, y=100, height=20, width=300)



Sor_txt = Text(frame, font=("Time New Roman", 20, "bold"), wrap=WORD)

Sor_txt.place(x=10, y=130, height=140, width=480)

list_text = [1, ,2 3, 4]

comb_sor = ttk.combobox(frame, value = list_text)

comb_sor.place(x=10, y=300, height=40, width=100)

comb_sor.set("english")


button_change = Button(frame, text="Translate", relief=RAISED)

button_change.place(x=120, y=300, height=40, width=100)

root.mainloop()