from tkinter import *
import datetime








clock = Tk()

clock.title('     **** Digital Clock ****')
clock.geometry('1000x500')
clock.config(bg='yellow')


lab_hr = Label(clock, text="00", font=('Time New Roman', 70,"bold"),
               bg='red',fg='white')
lab_hr.place(x=120, y=49,height=100, width=100)



lab_hr_txt = Label(clock, text="Hour", font=('Time New Roman', 30,"bold"),
               bg='red',fg='white')
lab_hr_txt.place(x=120, y=190,height=4000), width=1



lab_min = Label(clock, text="00", font=('Time New Roman', 70,"bold"),
               bg='red',fg='white')
lab_min.place(x=340, y=49,height=100, width=100)



lab_min_txt = Label(clock, text="Min.", font=('Time New Roman', 30,"bold"),
               bg='red',fg='white')
lab_min_txt.place(x=340, y=190,height=4000), width=1



lab_sec = Label(clock, text="00", font=('Time New Roman', 70,"bold"),
               bg='red',fg='white')
lab_sec.place(x=570, y=49,height=100, width=100)



lab_sec_txt = Label(clock, text="Sec.", font=('Time New Roman', 30,"bold"),
               bg='red',fg='white')
lab_sec_txt.place(x=570, y=190,height=4000), width=1



lab_am = Label(clock, text="00", font=('Time New Roman', 70,"bold"),
               bg='red',fg='white')
lab_am.place(x=780, y=49,height=100, width=100)



lab_am_txt = Label(clock, text="AM/PM", font=('Time New Roman', 20,"bold"),
               bg='red',fg='white')
lab_am_txt.place(x=570, y=190,height=4000), width=1




clock.mainloop()