from tkinter import *
import speedtest



def speedcheck():
    sp =speedtest.Speedtest()
    sp.get_server()
    down = str(round(sp.download()/(10**7), 3)) + " Mbps"
    up = str(round(sp.upload()/(10**7), 3)) + " Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)



sp = Tk()

sp.title(" Internet Speed Tester")
sp.geometry("700x700")
sp.config(bg="Blue")

lab = Label(sp, text = "Internet Speed Tester", font=("Time new Roman", 30, "bold"),bg="Blue",fg="White")
lab.place(x=100, y=40, height=49, width=480)


lab = Label(sp, text = "Downloading Speed", font=("Time new Roman", 30, "bold"))
lab.place(x=100, y=130, height=49, width= 480)


lab_down = Label(sp, text = "00", font=("Time new Roman", 30, "bold"))
lab_down.place(x=100, y=200, height=49, width=480)


lab = Label(sp, text = "Upload Speed", font=("Time new Roman", 30, "bold"))
lab.place(x=100, y=290, height=49, width=480)


lab_up = Label(sp, text = "00", font=("Time new Roman", 30, "bold"))
lab_up.place(x=100, y=370, height=49, width=480)


button = Button(sp, text="Check Speed", font=("Time New Roman", 30, "bold"),relief=RAISED, bg="Red", command=speedcheck)
button.place(x=100, y= 370, height=49, width=480)





sp.mainloop()
