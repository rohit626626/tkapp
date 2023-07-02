from tkinter import *
root=Tk()

canvas_width=800
canvas_height=400

root.geometry(f"{canvas_width}x{canvas_height}")
can_widget=Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()

can_widget.create_line(50,0,800,400, fill="red")
can_widget.create_rectangle(10,50,700,300, fill="green")
can_widget.create_text(200, 200, text="Python Deshboard")
can_widget.create_oval(200,250,300,385)
root.mainloop()