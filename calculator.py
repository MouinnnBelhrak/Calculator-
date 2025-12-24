import tkinter as tk

def press(num):

    entry_var.set(entry_var.get() + str(num))


def erase():

    entry_var.set(entry_var.get()[:-1])

  
def clear() :

    entry_var.set("0")

def equal():

    try:

        entry_var.set(str(eval(entry_var.get())))

    except :

        entry_var.set("Error")

  
win=tk.Tk()

win.text="Calculator"

entry_var=tk.StringVar()
entry= tk.Entry(win , textvariable=entry_var , justify="right" , font=("Arial" , 16))\
.grid(row = 0 , column=0 , columnspan=5)


Buttons = [

    ('7' , 1 , 0) , ('8' , 1 , 1) , ('9' , 1 , 2) , ('+' , 1 , 3) , ('<--' , 1 , 4) ,

    ('4' , 2 , 0) , ('5' , 2 , 1) , ('6' , 2 , 2) , ('-' , 2 , 3) ,

    ('1' , 3 , 0) , ('2' , 3 , 1) , ('3' , 3 , 2) , ('/' , 3 , 3) ,

    ('0' , 4 , 0) , ('c' , 4 , 1) , ('=' , 4 , 2) , ('*' , 4 , 3) ,

]


for (text , r , c) in Buttons :

    if text=="=" :

        action=equal

    elif text=='c':

        action=clear

    elif text=="<--":

        action=erase

    else :

        action = lambda t=text: press(t)

    tk.Button(win , text=text , width= 5 , height=2 , command= action)\
    .grid(row= r , column= c)

  
  
win.mainloop()