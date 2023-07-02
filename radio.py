from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("333x133")

def myfun():
    print(f"I have  {var.get()}")

var=StringVar()
var.set("Radio")
 

Label(root, text="Choice food").pack()

radio=Radiobutton(root, text="Dosa", variable=var, value="Dosa").pack(anchor="w")
radio=Radiobutton(root, text="Itly", variable=var, value="Itly").pack(anchor="w")
radio=Radiobutton(root, text="Somasa", variable=var, value="Somasa").pack(anchor="w")

Button(text="Order now", pady=10, command=myfun).pack()





root.mainloop()