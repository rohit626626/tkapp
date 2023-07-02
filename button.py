from tkinter import *
root=Tk()
root.geometry("444x333")

def hello():
    print ("This is b1 burton data")

def msg():
    print ("This is b2 burton message")

f1=Frame(root, bg="blue", borderwidth=5, relief=SUNKEN)
f1.pack(side=LEFT, anchor="nw")

b1=Button(f1, bg="green", text="Print data", command=hello)
b1.pack(side=LEFT)

b2=Button(f1, bg="green", text="Message", command=msg)
b2.pack(side=LEFT, padx=10)

b3=Button(f1, bg="green", text="Submit")
b3.pack(side=LEFT)

root.mainloop()