from tkinter import *
import math
import numpy as np
from tkinter import messagebox

file=open("Contacts.txt","a")

root = Tk()
root.title("CONTACT BOOK")
root.geometry("650x550")
root.configure(bg="cyan")

label_name=Label(root,text="NAME:",width=10,bg="cyan")
label_name.place(x=50,y=100)

e_name = Entry(root, borderwidth=2, width=50)
e_name.place(x=150,y=100)

label_number=Label(root,text="NUMBER:",width=10,bg="cyan")
label_number.place(x=50,y=150)

e_number = Entry(root, borderwidth=2, width=50)
e_number.place(x=150,y=150)

label_email=Label(root,text="E-MAIL:",width=10,bg="cyan")
label_email.place(x=50,y=200)

e_email = Entry(root, borderwidth=2, width=50)
e_email.place(x=150,y=200)



def submit():
    name=e_name.get()
    number=e_number.get()
    email=e_email.get()
    file.writelines("NAME:"+name+" "+"\n")
    file.writelines("NUMBER:"+number+"\n")
    file.writelines("EMAIL:"+email+"\n")
    file.writelines("\n")

    messagebox.askokcancel("message","SUBMITTED!")

    e_name.delete(0,END)
    e_number.delete(0, END)
    e_email.delete(0, END)


submit_button=Button(root,text="SUBMIT",command=submit)
submit_button.place(x=250,y=250)


root.mainloop()