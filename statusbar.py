from tkinter import *
root=Tk()
root.geometry("333x133")

def upload():
    statusvar.set("Please wait...")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("Ready")

statusvar=StringVar()
statusvar.set("Ready to process")

sbar=Label(root, textvariable=statusvar, relief=SUNKEN, anchor="w")
sbar.pack(side=BOTTOM, fill=X)

Button(root, text="Upload", command=upload).pack()
root.mainloop()