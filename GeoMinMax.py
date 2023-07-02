from tkinter import *
root=Tk()

# width x height
root.geometry("400x300")

# width,height
root.minsize(250,200)

# width,height
root.maxsize(600,500)

# labels
lab1=Label(text="This is python app")
lab1.pack()


root.mainloop()