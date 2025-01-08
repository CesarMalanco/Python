# Author: reDragonCoder

# Library
import turtle
from turtle import *

# Functions
def tree(length, angle):
    if(length<9):
        return
    else:
        pencolor('green')
        forward(length)
        right(angle)
        tree(0.8*length, angle)
        left(2*angle)
        tree(0.8*length, angle)
        right(angle)
        backward(length)
        pencolor('brown')

def draw_fractal():
    wn=turtle.Screen()
    wn.bgcolor("black")
    wn.title("Tree Fractal")
    speed(0)
    up()
    left(90)
    backward(200.0)
    down()
    tree(100, 30)
    mainloop()

# Execution
draw_fractal()
mainloop()
