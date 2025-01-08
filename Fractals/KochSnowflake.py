# Author: reDragonCoder

# The Koch snowflake is a IFS fractal that can be represented by a Lindenmayer system
# NOTE: IFS=iterated function system fractals

# Koch snowflake l-system representation
#   axiom = “F- -F- -F”
#   rules = {“F”:”F+F- -FF+F””}
#   iterations = 4
#   angle = 6 

# Library
from turtle import *

# Functions
def koch_flake(length, order):
    if(order==0):
        forward(length)
        return
    koch_flake(length/3, order-1)
    left(60)
    koch_flake(length/3, order-1)
    right(120)
    koch_flake(length/3, order-1)
    left(60)
    koch_flake(length/3, order-1)

def draw_flake():
    speed(0)
    up()
    backward(200/2.0)
    down()
    col=["red", "green", "blue", "yellow"]
    for i in range(3):
        begin_fill()
        color(col[i])
        koch_flake(300.0, 4)
        if i<2:
            left(-120)
        end_fill()
    mainloop()

# Execution
draw_flake()