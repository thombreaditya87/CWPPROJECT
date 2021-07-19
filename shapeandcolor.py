import tkinter
import turtle
import tkinter.messagebox
import random
#import reference

from tkinter import *
from PIL import Image, ImageTk
#from reference import *



def Learn_shapes():
    t1 = Tk()
    t1.geometry('1200x800')
    t1.title("LEARN DIFFERENT SHAPES")
    i1 = ImageTk.PhotoImage(Image.open("shapes2.png"))
    label1 = Label(image=i1)
    label1.pack()
    Checkbutton(t1, text='I have completed the learning part successfully', font="comicsansms 14")\
        .pack()
    button_quit = Button(
        t1, text='EXIT', font="comicsansms 14", command=t1.quit)
    button_quit.pack()
    t1.mainloop()


def Learn_colours():
    t2 = Tk()
    t2.geometry('1200x800')
    t2.title("LEARN DIFFERENT COLOURS")
    i1 = ImageTk.PhotoImage(Image.open("colors1.png"))
    label1 = Label(image=i1)
    label1.pack()
    Checkbutton(t2, text='I have completed the learning part successfully', font="comicsansms 14")\
        .pack()
    button_quit = Button(
        t2, text='EXIT', font="comicsansms 14", command=t2.quit)
    button_quit.pack()
    t2.mainloop()

root.mainloop()