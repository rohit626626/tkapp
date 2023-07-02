from tkinter import *
root=Tk()
root.geometry("333x233")

def add():
    global i
    lbx.insert(ACTIVE, f"{i}")
    i+=1

i=0

lbx=Listbox(root)
lbx.pack()
lbx.insert(END, "First item of List")

Button(text="Add New Item", pady=10, command=add).pack()

root.mainloop()