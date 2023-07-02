from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("444x333")

def myfun():
    print("This is my fun")
    tmsg.showinfo("Show", "This is info")


def newfun():
    print("This is new fun")
    tmsg.showerror("Error", "This is error")

def my():
    print("This is wearning")
    tmsg.showwarning("Wearning", "This is warning")

mainmenu=Menu(root)

m1=Menu(mainmenu, tearoff=0)
m1.add_command(label="Showinfo", command=myfun)
m1.add_command(label="Error", command=newfun)
m1.add_command(label="Wearning", command=my)

root.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)


root.mainloop()