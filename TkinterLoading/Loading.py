from tkinter import *
from tkinter.ttk import Progressbar

root= Tk()

width_of_window = 427
height_of_window = 250
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_1 = (screen_width / 2) - (width_of_window / 2)
y_1 = (screen_height / 2) - (height_of_window / 2)
root.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_1, y_1))
root.overrideredirect(True)

progress = Progressbar(root,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=500,mode="determinate")

def main_Window():
    root1 = Tk()
    root1.geometry("427x250")
    l1 = Label(root,text="Add Text Here",fg="dark grey",bg = None)
    l = ("Calibi (Body)",24,"bold")
    l1.config(font=l)
    l1.place(x=80,y=100)
    root1.mainloop()

def bar():
    l4 = Label(root,text = "Loading...",fg = "white",bg = "#249794")
    lst4=  ("Calibi (Body)",18)
    l4.config(font= lst4)
    l4.place(x=0,y=200)

    import time
    r = 0
    for i in range(100):
        progress["value"]=r
        root.update_idletasks()
        time.sleep(0.01)
        r = r+1
    root.destroy()
    main_Window()

progress.place(x=-10,y=235)

Frame(root,width=427,height = 241,bg = "#249794").place(x=0,y=0)
b1=Button(root,width=10,height=1,text="Get Started",command=bar,border=0,fg="#249794")
b1.place(x=170,y=200)


# l1 = Label1(root,)

root.mainloop()
