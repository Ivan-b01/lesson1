from tkinter import *
from datetime import date
window = Tk()
window.title('Getting started with widgets')
window.geometry('400x300')
lbl = Label(text = 'hey there!', fg = 'white', bg = '#54f6f0', height=1, width=300)
name_lbl = Label(text='fullname', bg='#454f6f')
name_entry = Entry()
def display(): 
    name = name_entry.get()
    global message
    message = "welcome to the application! \nToday's date is: "
    greet = 'hello '+name+"\n"
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())
text_box = Text(height=3)
btn = Button(text='Begin', command=display, height=1, bg='green', fg ='white')
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
window.mainloop()