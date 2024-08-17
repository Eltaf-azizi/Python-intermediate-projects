from tkinter import *
import os

st = Tk()
st.title("ShutDown App")
st.geometry("700x700")
st.config(bg="Blue")

rButton = Button(st, Text="Restart", font=("Time New Roman", 30,"Bold"), relief=RAISED, cursor="plus")
rButton.place(x=200, y=20, height=40, width=100)

st.mainloop()
