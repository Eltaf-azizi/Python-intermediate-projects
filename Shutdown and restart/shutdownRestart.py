from tkinter import *
import os

def restart(): 
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("Shutdown /r /t 20")
def logout():
    os.system("shutdown -1")
def shutdown():
    os.system("shutdown /s /t 1")

st = Tk()
st.title("ShutDown App")
st.geometry("700x700")
st.config(bg="Blue")

r_Button = Button(st, text="Restart", font=("Time New Roman", 20,"bold"),
                   relief=RAISED, cursor="plus")
r_Button.place(x=230, y=100, height=40, width=200, command=restart)

rt_Button = Button(st, text="Restart Time", font=("Time New Roman", 20,"bold"),
                    relief=RAISED, cursor="plus")
rt_Button.place(x=230, y=200, height=40, width=200, command=restart_time)

lg_Button = Button(st, text="Log-Out", font=("Time New Roman", 20,"bold"),
                    relief=RAISED, cursor="plus", command=logout)
lg_Button.place(x=230, y=300, height=40, width=200)

st_Button = Button(st, text="ShutDown", font=("Time New Roman", 20,"bold")
                   , relief=RAISED, cursor="plus", command=shutdown)
st_Button.place(x=230, y=400, height=40, width=200)


st.mainloop()
