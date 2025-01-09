# Author: reDragonCoder

# IFS fractal

# L-system for dragon curve
#   axiom = “FX”
#   rules =  {“X”:”X+YF+”, “Y”:”-FX-Y”)
#   iterations = 8
#   angle = 90

# Library
from turtle import *

# Functions
def dragon_fractal(iterations, axiom, var1, replace1, var2, replace2, length, angle):
    old=axiom
    for i in range(iterations):
        new=''
        for char in old:
            if(char==var1):
                new+=replace1
            elif(char==var2):
                new+=replace2
            else:
                new+=char
        old=new
    for char in old:
        if(char=="F"):
            forward(length)
        elif(char=='+'):
            right(angle)
        elif(char=='-'):
            left(angle)

def draw_fractal(fractal_name):
    speed(0)
    bgcolor('black')
    pencolor('red')
    if(fractal_name=="dragon"):
        up()
        backward(200/2.0)
        left(90)
        down()
        dragon_fractal(10, 'FX', 'X', "X+YF+", "Y", "-FX-Y", 8, 90)

# Execution
draw_fractal("dragon")
mainloop()
