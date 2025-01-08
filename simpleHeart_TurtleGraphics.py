# Author: reDragonCoder 

import turtle

bob=turtle.Turtle()
bob.shape("turtle")
bob.screen.bgcolor('black')
bob.screen.title("Heart")
bob.color('red')
bob.shapesize(.5)

bob.penup()
bob.goto(-10.0,-202.0)
bob.left(53.8)
bob.pendown()
bob.forward(300)
bob.circle(100,200)

bob.penup()
bob.goto(-10.0,-202.0)
bob.setheading(180)
bob.right(53.8)
bob.pendown()
bob.forward(300)
bob.circle(-100,200)
bob.hideturtle()

turtle.done()