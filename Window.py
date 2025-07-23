# Import Tkinter
from tkinter import *

from datetime import date

#Configure the window
root = Tk()

root.title("My tkinter app")

root.geometry('400x300')

lbl = Label(text = "Hey there!! ", fg = 'cyan', bg = "blue",height = 1,width = 300)

Name_lbl = Label(text = "Full Name", bg = 'red',fg = 'blue')

Name_entry = Entry()

def display():
    
    name = Name_entry.get()
    
    global message
    
    message = "Welcome to the application! \n Today's date is:"
    
    greet = "Hello ",name "\n"
    
    text_box.insert(END,greet)
    
    text_box.insert(END,message)
    
    text_box.insert(END.date.today)
    
text_box = Text(height = 4)

btn = Button(text = "Begin", command = display, height = 1,bg = 'cyan' fg = 'white')

lbl.pack()

Name_lbl.pack()

btn.pack()

text_box.pack()

root.mainloop()

