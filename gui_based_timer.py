# -*- coding: utf-8 -*-
"""GUI based timer.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NKcBLERc4oaOnSKDXJivBrY-JlqQtTrZ
"""

from tkinter import*
from playsound import playsound
import random
import time

root=tk()
root.title("timer")
root.geometry("400x600")
root.config(bg="#000")
root.resizable(false,false)

heading=label(root,test="timer",font="arial 30 bold",bg="#000",fg="white")
heading.pack( pady=10)
#clock
label(root,font+("aerial",15,"bold"),text="current time:",bg="#000",fg="white").place(x=65,y=70)
def clock():
    clock_time=time.strftime("%H:%M:%S %p")
    current_time.config(text=clock_time)
    current_time.after(1000,clock)

current_time=label(root,font=("arial",15,"bold"),text="",fg="#000",bg="#fff")
current_time.place(x=190,y=70)
clock()

#timer
hrs=stringvar()
entry(root,textvariable=hrs,width=2,font="arial 50",bg="#000",fg="white",bd=0).place(x=30,y=155)
hrs.set("00")

mins=stringvar()
entry(root,textvariable=mins,width=2,font="arial 50",bg="#000",fg="white",bd=0).place(x=150,y=155)
mins.set("00")

sec=stringvar()
entry(root,textvariable=sec,width=2,font="arial 50",bg="#000",fg="white",bd=0).place(x=270,y=155)
sec.set("00")

label(root,text="hour",font="arial 12",bg="#000",fg="white").place(x=105,y=200)
label(root,text="mins",font="arial 12",bg="#000",fg="white").place(x=225,y=200)
label(root,text="secs",font="arial 12",bg="#000",fg="white").place(x=345,y=200)

def timer():
    times=int(hrs.get())*3600+int(mins.get())*60+int(secs.get())
    while times> -1:
        minute,second=(times//60,times%60)
        hour=0
        if minute>60:
            hour,minute=(minute//60,minute%60)

            sec.set(second)
            min.set(minute)
            hrs.set(hour)

            root.update()
            time.sleep(1)

if(times==0):
          playsound("alarm.mp3")
          sec.set("00")
          min.set("00")
          hrs.set("00")
          times-=1

def brush():
    hrs.set("00")
    mins.set("02")
    secs.set("00")


def face():
    hrs.set("00")
    mins.set("15")
    secs.set("00")

def eggs():
    hrs.set("00")
    mins.set("10")
    secs.set("00")

button=button(root,text="start",bg="#ea3548",fg="white",width=20,font="arial 10 bold",bd=0,command=timer)
button.pack(padx=5,pady=40,side=BOTTOM)

image1=photoimage(file="brush.png")
button1=button(root,image=image1,bg="#000",bd=0,command=brush)
button1.place(x=7,y=300)

image2=photoimage(file="face.png")
button2=button(root,image=image2,bg="#000",bd=0,command=face)
button2.place(x=137,y=300)

image3=photoimage(file="eggs.png")
button3=button(root,image=image3,bg="#000",bd=0,command=eggs)
button3.place(x=267,y=300)

root.mainloop()