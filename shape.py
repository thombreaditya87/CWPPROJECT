# import tkinter module
import tkinter
import turtle
import tkinter.messagebox

from tkinter import*
from tkinter.ttk import*

# creating main tkinter window/toplevel
#master = Tk()
window = tkinter.Tk()
# create a GUI window
#root = tkinter.Tk()

#root.title("COLORGAME")

canvas = tkinter.Canvas(master = window, width = 800, height = 800)
canvas.grid(padx=2, pady=2, row=0, column=0, rowspan=10, columnspan=10) # , sticky='nsew')
#draw = turtle.Turtle()
draw = turtle.RawTurtle(canvas)

draw.speed(1000000)
draw.hideturtle()
draw.pensize(3)
draw.color("red")


# this wil create a label widget
l1 = Label(window, text="Shape:")
l2 = Label(window, text="Color:")

# grid method to arrange labels in respective
# rows and columns as specified
l1.grid(row=0, column=0, sticky=W, pady=2)
l2.grid(row=1, column=0, sticky=W, pady=2)

# entry widgets, used to take entry from user
e1 = Entry(window)
e2 = Entry(window)

# this will arrange entry widgets
e1.grid(row=0, column=1, pady=2)
e2.grid(row=1, column=1, pady=2)

def Jan (a, x, y, size):
    draw.pu()
    draw.goto(x, y)
    draw.pd()
    for i in range (0, 4):
        draw.forward(size)
        draw.right(90)

x =-40
y = -40
size = 140
for i in range (0, 10):
    for j in range (0, 10):
        Jan (draw, x, y, size)


# infinite loop which can be terminated by keyboard
# or mouse interrupt
window.mainloop()
mainloop()