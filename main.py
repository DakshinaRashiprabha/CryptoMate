from cgitb import reset
from tkinter import *
from tkinter import messagebox
import base64
import os

from pyexpat.errors import messages


def encrypt():
    password=code1.get()

    if password=="1226":
        screen1=Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#663333")

        message=text1.get(1.0,END)
        encode_message=message.encode("ascii")
        base64_bytes=base64.b64encode(encode_message)
        encrypt=base64_bytes.decode("ascii")

        Label(screen1,text="ENCRYPT",font="arial",fg="white",bg="#663333").place(x=10,y=0)
        text3=Text(screen1,font="Rpbote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text3.place(x=10,y=40,width=380,height=150)

        text3.insert(END,encrypt)

    elif password =="":
        messagebox.showerror("encryption","Input Password")

    elif password != "1226" :
        messagebox.showerror("encryption","Invalid Password")



def decrypt():
    password = code2.get()

    if password == "1226":
        screen2 = Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#FF9900")

        message = text2.get(1.0, END)
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decrypt = base64_bytes.decode("ascii")

        Label(screen2, text="DECRYPT", font="arial", fg="white", bg="#FF9900").place(x=10, y=0)
        text3 = Text(screen2, font="Rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text3.place(x=10, y=40, width=380, height=150)

        text3.insert(END, decrypt)

    elif password == "":
        messagebox.showerror("encryption", "Input Password")

    elif password != "1226":
        messagebox.showerror("encryption", "Invalid Password")


def first_screen():

    global screen
    global code1
    global code2
    global text1
    global text2

    screen = Tk()
    screen.geometry("600x600")

    #image
    image_icon = PhotoImage(file = "image01.png")
    screen.iconphoto(False,image_icon)

    screen.title("CryptoMate")

    def reset():
        code1.set("")
        code2.set("")
        text1.delete(1.0,END)
        text2.delete(1.0, END)

    #Encryption
    Label(text="Enter Text for Encryption :",fg="black",font=("calbri",13)).place(x=10,y=10)
    text1 = Text(font="Robote 20",bg="#e5e8e8",relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=10,y=40,width=580,height=80)

    Label(text="Enter Secret Key :", fg="black", font=("calbri", 13)).place(x=10, y=120)

    code1 = StringVar()
    Entry(textvariable=code1,width=19,bd=0,font=("arial,25"),show="*").place(x=10,y=145)

    Button(text="ENCRYPT", height="2", width=23, bg="#663333", fg="white", bd=0,command=encrypt).place(x=200, y=175)

    #decryption
    Label(text="Enter Text for Decryption :", fg="black", font=("calbri", 13)).place(x=10, y=270)
    text2 = Text(font="Robote 20", bg="#e5e8e8", relief=GROOVE, wrap=WORD, bd=0)
    text2.place(x=10, y=300, width=580, height=80)

    Label(text="Enter Secret Key :", fg="black", font=("calbri", 13)).place(x=10, y=380)

    code2 = StringVar()
    Entry(textvariable=code2,width=19,bd=0,font=("arial,25"),show="*").place(x=10,y=405)

    Button(text="DECRYPT",height="2",width= 23,bg="#FF9900",fg="white",bd=0,command=decrypt).place(x=200,y=435)

    #Restart
    Button(text="RESET",height="2",width=82,bg="#FF0000",fg="white",bd=0,command=reset).place(x=10,y=480)
    screen.mainloop()

first_screen()
