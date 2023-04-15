#digital date & time project
#started on 05-03-22 & ended on 05-03-22
from tkinter import *
import time

def Dclock():
    curr_time=time.strftime("Time:%H:%M:%S\nDate:%y-%m-%d")
    clock.config(text=curr_time)
    clock.after(100,Dclock)
window=Tk()
window.title("DIGI CLOCk")
message = Label(window,font=("arial",40,"italic"),text="tapaswi",fg="white",bg="black")
message.grid(row=0,column=0)
clock=Label(window,font=("times",40,"bold"),fg="black",bg="white")
clock.grid(row=1,column=0)
Dclock()
mainloop()