import tkinter
from tkinter import*

from PIL import ImageTk,Image


def Learn_shapes():
    #jan.destroy()
    t1 = tkinter .Tk()
    t1.geometry('1200x800')
    t1.title("LEARN DIFFERENT SHAPES")
    i1 = ImageTk.PhotoImage(tkinter.Image.open("shapes2.png"))

    label1 = tkinter .Label(image=i1)
    label1.pack()
    tkinter .Checkbutton(t1, text='I have completed the learning part successfully', font="comicsansms 14") \
        .pack()
    button_quit = tkinter .Button(
        t1, text='EXIT', font="comicsansms 14", command=t1.quit)
    button_quit.pack()
    t1.mainloop()
