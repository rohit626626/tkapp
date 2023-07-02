from tkinter import *
root=Tk()
root.geometry("444x333")

def getvals():
    print(userval.get())
    print(passval.get())

user=Label(root, text="Username")
password=Label(root, text="Password")
user.grid()
password.grid(row=1)

userval=StringVar()
passval=StringVar()

userentry=Entry(root, textvariable=userval)
passentry=Entry(root, textvariable=passval)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

Button(text="Submit", command=getvals).grid()

root.mainloop()