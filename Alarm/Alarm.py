from tkinter import *
from datetime import datetime
from playsound import playsound
from tkinter import messagebox
import time, datetime
from playsound import playsound
from threading import *
import termcolor2
import os
from win10toast import ToastNotifier

os.system("cls")
# =================================================== Main

window = Tk()
window.title("Alarm")
window.geometry("550x350")
window.resizable(False, False)
window.configure(bg="#FFFFFF")
window.iconname("Icon.ico")
window.iconbitmap("Icon.ico")
# D8D8D8
canvas = Canvas(window,
                bg="#FFFFFF",
                height=500,
                width=550,
                bd=0,
                highlightthickness=0,
                relief="ridge")
canvas.place(x=0, y=0)

toaster = ToastNotifier()
# =================================================== Function


def putfile(filename, filedata):
    myfile = open(filename, "a")
    return myfile.write(filedata)
    myfile.close()


def Threading():
    t1 = Thread(target=button_Set)
    t1.start()


def playS():
    toaster.show_toast("Alarm Alert!",f"Times Up",icon_path=None,duration=10,threaded=True)
    y = 0
    putfile("Timer.txt", str(time.localtime()))
    putfile("Timer.txt", "\n====================\n")
    for x in range(1,11):
        playsound("Alarm06.wav")
        y += 1
        if y == 10:
            
            window.destroy()


def button_Set():
    try:
        while True:
            time.sleep(1)
            set_alarm_time = f"{Hour.get()}:{Minute.get()}:{Second.get()}"
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            set_alarm_time1 = termcolor2.colored("Set Alarm: ", 'red')
            current_time1 = termcolor2.colored("Current Time: ", 'red')
            putfile(
                "Timer.txt",
                f"{set_alarm_time1}{set_alarm_time}  |  {current_time1}{current_time}\n"
            )
            if current_time == set_alarm_time:
                playS()

    except:
        raise TclError("Something Went Wrong")
        messagebox.showerror("Error", "Something Went Wrong")


def clean_Entry():
    Hour.set("")
    Minute.set("")
    Second.set("")


# =================================================== Entry

Hour = StringVar()
Minute = StringVar()
Second = StringVar()

Entry0 = Entry(bd=0, bg="#D8D8D8", highlightthickness=0, textvariable=Hour)
Entry0.place(x=85, y=116, width=112, height=28)

Entry1 = Entry(bd=0, bg="#D8D8D8", highlightthickness=0, textvariable=Minute)
Entry1.place(x=225, y=116, width=112, height=28)

Entry2 = Entry(bd=0, bg="#D8D8D8", highlightthickness=0, textvariable=Second)
Entry2.place(x=365, y=116, width=112, height=28)

# =================================================== Design

Alarm = PhotoImage(file=f"Main.png")
Alarm_img = canvas.create_image(290, 40, image=Alarm)

Ding = PhotoImage(file=f"Ding.png")
Ding_img = canvas.create_image(50, 130, image=Ding)

Main = PhotoImage(file=f"Main2.png")
Main_img = canvas.create_image(280, 300, image=Main)

Entry = PhotoImage(file=f"Entry.png")
Entry_img0 = canvas.create_image(140, 130, image=Entry)
Entry_img1 = canvas.create_image(280, 130, image=Entry)
Entry_img2 = canvas.create_image(420, 130, image=Entry)

# =================================================== Button

Button_0 = PhotoImage(file=f"Button.png")
Button0 = Button(image=Button_0,
                 borderwidth=0,
                 highlightthickness=0,
                 command=Threading,
                 relief="flat")
Button0.place(x=237, y=173, width=85, height=38)

Button_1 = PhotoImage(file=f"Clean.png")
Button1 = Button(image=Button_1,
                 borderwidth=0,
                 highlightthickness=0,
                 command=clean_Entry,
                 relief="flat")
Button1.place(x=486, y=108, width=45, height=42)

# =================================================== Label

canvas.create_text(140,
                   100,
                   text="Hour",
                   fill="#716F75",
                   font=("None", int(12.0)))

canvas.create_text(280,
                   100,
                   text="Minute",
                   fill="#716F75",
                   font=("None", int(12.0)))

canvas.create_text(420,
                   100,
                   text="Second",
                   fill="#716F75",
                   font=("None", int(12.0)))

canvas.create_text(140,
                   160,
                   text="01-24",
                   fill="#716F75",
                   font=("None", int(8.0)))

canvas.create_text(280,
                   160,
                   text="00-60",
                   fill="#716F75",
                   font=("None", int(8.0)))

canvas.create_text(420,
                   160,
                   text="00-60",
                   fill="#716F75",
                   font=("None", int(8.0)))

window.mainloop()