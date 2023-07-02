from tkinter import *
root=Tk()
root.geometry("333x133")
root.title("Tk Program")
root.wm_iconbitmap("img.ico")
root.configure(background="red")

width=root.winfo_screenwidth()
height=root.winfo_screenheight()

print(f"{width}x{height}")
Button(text="Close", command=root.destroy).pack()

root.mainloop()