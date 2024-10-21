from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
root = Tk()
root.title('Denomination Counter')
root.configure(bg='light blue')
root.geometry('650x400')
upload = Image.open("cashtally.png")
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='light blue')
label.place(x=180, y=20)
label1 = Label(root,
               text="Hey User! Welcome to Denomination Counter Application.", bg='light blue')
label1.place(relx=0.5, y=340, anchor=CENTER)
def msg(): 
    Msgbox = messagebox.showinfo(
       "Alert", 'Do you want to calcu;ate the denomitation count?' 
    )
if MsgBox == 'ok': 
    topwin()
