# Author: reDragonCoder

# IFS fractal

# L-system defines this curve as 
#   axiom = “F”
#   rules = {“F”:”+F- -F+”}
#   iterations = 10
#   angle = 45

# Library
from turtle import *

# Functions
def levy_c_curve(length, order):
    if(order==0):
        forward(length)
        return
    right(45)
    levy_c_curve(length, order-1)
    left(90)
    levy_c_curve(length, order-1)
    right(45)

def draw_levy_c():
    speed(0)
    up()
    backward(300/2.0)
    down()
    for i in range(2):
        levy_c_curve(8, 10)
        right(180)
    mainloop()

# Execution
draw_levy_c()