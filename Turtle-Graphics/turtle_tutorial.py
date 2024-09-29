# Author: reDragonCoder 

import turtle

my_turtle = turtle.Turtle() #creating a turtle
my_turtle.shape("classic") #specify shape of turtle
my_turtle.screen.bgcolor("white") #specify window background color
my_turtle.screen.title("Tutorial") #set title
my_turtle.color('red') #specify turtle color
my_turtle.shapesize(2) #specify turtle size

#get coordinate of screen
def buttonclick(x,y):
    print("You clicked at this coordinate({0},{1})".format(x,y))
turtle.onscreenclick(buttonclick,1) #onscreen function to send coordinate
turtle.listen() # listen to incoming connections
turtle.speed(10) #set the speed
turtle.done()