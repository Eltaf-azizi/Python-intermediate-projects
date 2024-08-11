from tkinter import *
import speedtest

sp = Tk()

sp.title(" Internet Speed Tester")
sp.geometry("700x700")
sp.config(bg="Blue")

lab = Label(sp, text = "Internet Speed Tester", font=("Time new Roman", 30, "bold"),bg="Blue",fg="Red")
lab.place(x=100, y=40)


sp.mainloop()
