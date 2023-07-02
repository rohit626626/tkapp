from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("333x133")

scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

text=Text(root, yscrollcommand=scrollbar.set)
text.pack(fill=BOTH)
scrollbar.config(command=text.yview)

root.mainloop()