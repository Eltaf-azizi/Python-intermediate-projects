from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES


def change(text="type", src= "English", dest="Spanish"): 
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text, src = src1, dest = dest1)
    return trans1.text

    return trans1


def data():
    s = comb_sor.get()
    d = comb_dest.get()
    msg = Sor_txt.get(1.0, END)
    textget = change(text = msg, src=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, textget)




root = Tk()
root.title("Translator")
root.geometry("400x800")
root.config(bg='Red')



frame = Frame(root).pick(side=BOTTOM)


lab_txt = Label(root, text= "Sourse Text",
                 font=("Time New Roman", 20, "Bold"),
                   fg="Black"bg="Red"
                )

lab_txt.place(x=100, y=100, height=20, width=300)


Sor_txt = Text(frame, font=("Time New Roman", 20, "bold"), wrap=WORD)
Sor_txt.place(x=10, y=130, height=140, width=480)


list_text = list(LANGUAGES.value())


comb_sor = ttk.combobox(frame, value = list_text)
comb_sor.place(x=10, y=300, height=40, width=100)
comb_sor.set("english")


button_change = Button(frame, text="Translate", relief=RAISED, command=data)
button_change.place(x=170, y=300, height=40, width=140)


comb_dest = ttk.combobox(frame, value = list_text)
comb_dest.place(x=230, y=300, height=40, width=140)
comb_dest.set("english")


lab_txt = Label(root, text= "Dest Text", font=("Time New Roman", 20, "Bold"), fg="Black"bg="Red")
lab_txt.place(x=100, y=370, height=20, width=300)


dest_txt = Text(frame, font=("Time New Roman", 20, "bold"), wrap=WORD)
dest_txt.place(x=10, y=400, height=140, width=480)





root.mainloop()