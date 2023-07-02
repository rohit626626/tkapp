from tkinter import *
root=Tk()
root.geometry("844x533")
root.title("Tk app")

# label option
lab1=Label(text="9Frame In Tkinter _ Python Tkinter GUI Tutorial In Hindi #8 - YouTube (360p)",bg="pink", fg="white", padx=100, pady=100, font="comicsence 12 bold", borderwidth=3, relief=SUNKEN)

# pack option
lab1.pack(side=BOTTOM, anchor="sw", fill=X, padx=100, pady=50)

root.mainloop()