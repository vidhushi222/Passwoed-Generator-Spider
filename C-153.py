# -*- coding: utf-8 -*-
"""
Created on Sat May  7 14:00:51 2022

@author: vidhushi bhatt
"""

from tkinter import *
import random


root=Tk()

root.title("3D Arrays")
root.geometry("400x400")
root.configure(bg="salmon")

label=Label(root)
Array_3D=[[['2','5','1','9','7','0'],["Head","Tail"],["V","M","P","A","B","F","D","N"]]]

print(Array_3D[0][2][3])


def new_password():
    random1=random.randint(0, 5)
    random2=random.randint(0,1)
    random3=random.randint(0,7)
    letter1=str(Array_3D[0][0][random1])
    letter2=Array_3D[0][1][random2]
    letter3=Array_3D[0][2][random3]
    label["text"]=letter1+""+letter2+""+letter3
    
btn=Button(root,text="GENERATE NEW PASSWORD",command=new_password)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
label.place(relx=0.5,rely=0.6,anchor=CENTER)
root.mainloop()