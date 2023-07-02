from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("333x133")

def myfun():
    print(f"I have  {mymoney.get()} money")

Label(root, text="Money").pack()

mymoney=Scale(root, from_=0, to=150, orient=HORIZONTAL, tickinterval=50)
mymoney.pack()

Button(root, text="Get Rupes", pady=10, command=myfun).pack()





root.mainloop()