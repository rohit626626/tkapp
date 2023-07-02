from distutils.command.sdist import sdist
from tkinter import *
root=Tk()
root.geometry("444x333")

def myfun():
    print("This is my fun")

def newfun():
    print("This is new fun")
mainmenu=Menu(root)

m1=Menu(mainmenu, tearoff=0)
m1.add_command(label="New Project", command=myfun)
m1.add_command(label="Save", command=newfun)
m1.add_separator()
m1.add_command(label="Save As", command=newfun)
m1.add_command(label="Print", command=myfun)

root.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)

m2=Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut", command=myfun)
m2.add_command(label="Copy", command=newfun)
m2.add_command(label="Past", command=newfun)
m2.add_command(label="Find", command=myfun)

root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit", menu=m2)

root.mainloop()