from tkinter import *
from PIL import ImageTk, Image
root=Tk()

root.geometry("400x300")
#simple photo
# photo=PhotoImage(file="img1.png")

#jpg images
image=Image.open("photo.jpg")
photo=ImageTk.PhotoImage(image)

lab1=Label(image=photo)
lab1.pack()

root.mainloop()