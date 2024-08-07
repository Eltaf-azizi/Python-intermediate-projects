from tkinter import *

clock = Tk()

clock.title('     **** Digital Clock ****')
clock.geometry('1000x500')
clock.config(bg='yellow')

lab_hr = Label(clock, text="00", font=('Time New Roman', 70,"bold"),
               bg='red',fg='white')

lab_hr.place(x=40, y=40,height=100, width=140)



clock.mainloop()