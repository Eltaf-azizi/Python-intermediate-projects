from tkinter import *
import datetime



def date_time() :
    time = datetime.datetime.now()
    hr = time.strftime('%I')
    mi = time.strftime('%M')
    sec = time.strftime('%S')
    am = time.strftime("%p")
    date = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%y")
    day = time.strftime("%a")





    lab_hr.config(text=hr)
    lab_min.config(text=mi)
    lab_sec.config(text=sec)
    lab_am.config(text=am)
    lab_date.config(text=date)
    lab_mo.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)

    lab_hr.after(200,date_time)




clock = Tk()

clock.title('     **** Digital Clock ****')
clock.geometry('1000x500')
clock.config(bg='#1C1C1C')


# ****** Time

lab_hr = Label(clock, text="00", font=('Time New Roman', 70,"bold"),
               bg='#1C1C1C',fg='white')
lab_hr.place(x=120, y=49,height=100, width=100)



lab_hr_txt = Label(clock, text="Hour", font=('Time New Roman', 30,"bold"),
               bg='#1C1C1C',fg='white')
lab_hr_txt.place(x=120, y=190,height=40, width=100)



lab_min = Label(clock, text="00", font=('Time New Roman', 70,"bold"),
               bg='#1C1C1C',fg='white')
lab_min.place(x=340, y=49,height=100, width=100)



lab_min_txt = Label(clock, text="Min.", font=('Time New Roman', 30,"bold"),
               bg='#1C1C1C',fg='white')
lab_min_txt.place(x=340, y=190,height=40, width=100)



lab_sec = Label(clock, text="00", font=('Time New Roman', 70,"bold"),
               bg='#1C1C1C',fg='white')
lab_sec.place(x=570, y=49,height=100, width=100)



lab_sec_txt = Label(clock, text="Min.", font=('Time New Roman', 30,"bold"),
               bg='#1C1C1C',fg='white')
lab_sec_txt.place(x=340, y=190,height=40, width=100)


lab_am = Label(clock, text="00", font=('Time New Roman', 47,"bold"),
               bg='#1C1C1C',fg='white')
lab_am.place(x=780, y=49,height=100, width=100)



lab_am_txt = Label(clock, text="Sec.", font=('Time New Roman', 30,"bold"),
               bg='#1C1C1C',fg='white')
lab_am_txt.place(x=570, y=190,height=40,width=100)



# ******** Date
lab_date = Label(clock, text="00", font=('Time New Roman', 70,"bold"),
               bg='#1C1C1C',fg='white')
lab_date.place(x=120, y=270,height=100, width=100)



lab_date_txt = Label(clock, text="Date", font=('Time New Roman', 30,"bold"),
               bg='#1C1C1C',fg='white')
lab_date_txt.place(x=120, y=410,height=40, width=100)



lab_mo = Label(clock, text="00", font=('Time New Roman', 70,"bold"),
               bg='#1C1C1C',fg='white')
lab_mo.place(x=570, y=270,height=100, width=100)



lab_mo_txt = Label(clock, text="Month", font=('Time New Roman', 30,"bold"),
               bg='#1C1C1C',fg='white')
lab_mo_txt.place(x=570, y=410,height=40, width=114)



lab_year = Label(clock, text="00", font=('Time New Roman', 70,"bold"),
               bg='#1C1C1C',fg='white')
lab_year.place(x=340, y=270,height=100, width=100)



lab_year_txt = Label(clock, text="Year", font=('Time New Roman', 30,"bold"),
               bg='#1C1C1C',fg='white')
lab_year_txt.place(x=340, y=410,height=40, width=100)



lab_day = Label(clock, text="00", font=('Time New Roman', 45,"bold"),
               bg='#1C1C1C',fg='white')
lab_day.place(x=780, y=270,height=100, width=104)



lab_day_txt = Label(clock, text="Day", font=('Time New Roman', 30,"bold"),
               bg='#1C1C1C',fg='white')
lab_day_txt.place(x=780, y=410,height=40,width=100)



date_time()

clock.mainloop()