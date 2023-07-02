from tkinter import *
root=Tk()

def fun(event):
    print(f"Your mouse position is {event.x}, {event.y}")
root.geometry("444x333")

widget=Button(root, text="click")
widget.pack()

widget.bind('<Button-1>', fun)
widget.bind('<Double-1>', quit)


root.mainloop()