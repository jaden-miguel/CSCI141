# Name: Jaden Miguel
# Date: 30 April 2019
# Purpose: Third part of Lab 4, turtledraw.py, draw 4 figures

import turtle

wn = turtle.Screen
jaden = turtle.Turtle()

turtle.tracer(0,0)
jaden.speed(9)

#move turtle to starting position
jaden.penup()
jaden.goto(-200,-200)
jaden.pendown()
    
    
    
    
for i in range(4):

    for m in range(1, 61):

        jaden.color("red")

        #draw square
        for x in range(4):
            jaden.forward(100)
            jaden.left(90)
        
        jaden.left(6)
    
    
        turtle.update()
    
    jaden.penup()
    jaden.forward(400)
    jaden.pendown()
    jaden.left(90)