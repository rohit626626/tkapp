from tkinter import *
root=Tk()
root.geometry("844x533")
f1=Frame(root, bg="blue", borderwidth=5, relief=SUNKEN)
f1.pack(side=LEFT, fill="y")

f2=Frame(root, bg="red", borderwidth=5, relief=SUNKEN)
f2.pack(side=TOP, fill="x")

l1=Label(f1, text="Project tkinter")
l1.pack(pady=142)
l2=Label(f2, text="Welcome to tk Project", bg="pink", fg="white",  pady=15, font="comicsence 12 bold")
l2.pack()

root.mainloop()