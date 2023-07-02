from tkinter import *
from PIL import ImageTk, Image
root=Tk()
root.geometry("1000x1000")

def every_100(text):
    final_text=""
    for i in range(0, len(text)):
        final_text+=text[i]
        if i%100==2 and i!=0:
            final_text+="\n"

texts=[]
photos=[]

for i in range(0,3):
    with open(f"{i+1}.txt") as f:
        text=f.read()
        texts.append(text)

    image=Image.open(f"{i+1}.png")
    image=image.resize((225,225), Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))

f0=Frame(root, width=800, height=70)
Label(f0, text="Today News", font="lucida 33 bold").pack()
f0.pack()

f1=Frame(root, width=900, height=200)
Label(f1, text=texts[0], padx=22, pady=22).pack(side="left")
Label(f1, image=photos[0], anchor="e").pack()
f1.pack(anchor="w")

f2=Frame(root, width=900, height=200)
Label(f2, text=texts[1], padx=22, pady=22).pack(side="left")
Label(f2, image=photos[1], anchor="e").pack()
f2.pack(anchor="w")

f3=Frame(root, width=900, height=200)
Label(f3, text=texts[2], padx=22, pady=22).pack(side="left")
Label(f3, image=photos[2], anchor="e").pack()
f3.pack(anchor="w")


root.mainloop()