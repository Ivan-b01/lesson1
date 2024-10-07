from tkinter import*
root = Tk()
root.title('number pad')
root.geometry('250x300')
nums = [[9,8,7],[6,5,4],[3,2,1],['#', 0, '*']]
for i in range(4): 
    root.columnconfigure(i, weight=1, minsize=75)
    root.rowconfigure(i, weight=1, minsize=50)
for i in range(4): 
    for j in range(3): 
        frame = Frame(
            master=root,
            releif=SUNKEN,
            borderwidth=1
            bg="#456f2f"
        )    
        frame.grid(row=i, column=j, sticky='nsew')
        label = Label(master=frame, text=nums[i][j], bg='194f10', font=('Arial', 18))
        label.pack(expand=True, fill='both', padx=5, pady=5)
root.mainloop()