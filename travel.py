from tkinter import *
root=Tk()
root.geometry("444x333")

def getvals():
    print("Form submit")

    print(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentmodevalue.get(), foodservicevalue.get()}")

    with open("records.txt","a") as f:
        f.write(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentmodevalue.get(), foodservicevalue.get()}\n")


Label(text=" Welcome to Travels",bg="pink", fg="white", font="comicsence 12 bold").grid(row=0, column=3)
name=Label(root,text="Name")
phone=Label(root,text="Phone")
gender=Label(root,text="Gender")
emergency=Label(root,text="Emergency Number")
paymentmode=Label(root,text="Payment Mode")

name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmode.grid(row=5, column=2)

namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emergencyvalue=StringVar()
paymentmodevalue=StringVar()
foodservicevalue=IntVar()

nameentry=Entry(root, textvariable=namevalue)
phoneentry=Entry(root, textvariable=phonevalue)
genderentry=Entry(root, textvariable=gendervalue)
emergencyentry=Entry(root, textvariable=emergencyvalue)
paymentmodeentry=Entry(root, textvariable=paymentmodevalue)

nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmodeentry.grid(row=5, column=3)

foodservice=Checkbutton(text="Tick a food", variable=foodservicevalue)
foodservice.grid(row=6, column=3)

Button(text="Submit", command=getvals).grid(row=7, column=3)

root.mainloop()