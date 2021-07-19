import tkinter as tk

from tkinter import *
from PIL import Image, ImageTk

#from final01 import start


#from shapeandcolor import Learn_shapes,Learn_colours

def onclik1():

   import color


def onclik2():

    import shape


'''def onclick3():
    from shapeandcolor import Learn_shapes
def onclick4():
    from shapeandcolor import Learn_colours'''


def Learn_shapes():
    jan = Tk()
    jan.geometry('800x90')
    jan.title("LEARN DIFFERENT SHAPES")
    i1 = ImageTk.PhotoImage(Image.open("shapes2.png"))

    label1 = Label(image=i1)
    label1.pack()
    Checkbutton(jan, text='I have completed the learning part successfully', font="comicsansms 14") \
        .pack()
    button_quit = Button(
        jan, text='EXIT', font="comicsansms 14", command=jan.quit)
    button_quit.pack()
    jan.mainloop()


def Learn_colours():
    jan = Tk()
    jan.geometry('800x80')
    jan.title("LEARN DIFFERENT COLOURS")
    i1 = ImageTk.PhotoImage(Image.open("colors1.png"))
    label1 = Label(image=i1)
    label1.pack()
    Checkbutton(jan, text='I have completed the learning part successfully', font="comicsansms 14") \
        .pack()
    button_quit = Button(
        jan, text='EXIT', font="comicsansms 14", command=jan.quit)
    button_quit.pack()
    jan.mainloop()


#root.mainloop()


# def onclick3():


jan = tk.Tk()
jan.title('shape and color game')
jan.geometry("800x400")
# first step creat element
f2 = tk.Frame(jan, borderwidth=2)
#b1 = tk.Button(f2,text=" COLOR TEST ")
b1 = tk.Button(f2, text="  COLOR TEST  ", command=onclik1)
b1.grid(row=6, column=0)

b2 = tk.Button(f2, text=" SHAPE TEST ", command=onclik2)
# b2 = tk.Button(f2, text="  SHAPE TEST  ",
# font="comicsansms 10 bold", command=onclik1)
b2.grid(row=6, column=3)

b3 = tk.Button(f2, text="LearnShapes", command=Learn_shapes)
b3.grid(row=6, column=2)

b4 = tk.Button(f2, text="LearnColours", command=Learn_colours)
b4.grid(row=6, column=4)


#b4 = tk.Button(f2, text="  COLOR TEST  ", command=onclik1)
#b4.grid(row=6, column=0)


#btn1 = tk.Button(jan, text = "COLOR TEST",command =onclik1)
#btn2 = tk.Button(jan, text = "SHAPE TEST",command =onclik2)
#btn3 = tk.Button(jan, text = "SHAPE TEST",command =onclik2)
f2.pack()


# second step put element on main window
# btn1.pack()
# btn2.pack()

jan.mainloop()
