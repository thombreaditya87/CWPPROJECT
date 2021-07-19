import tkinter
from tkinter import*

from PIL import ImageTk,Image



def Learn_colours():
    #jan.destroy()
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