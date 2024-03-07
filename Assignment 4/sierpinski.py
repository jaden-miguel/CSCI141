# Author: Jaden Miguel
# Date: 5/12/19
# Description: Sierpinski Triangle program, will follow A4 outline 

import turtle
from random import randrange, choice
from math import sqrt


def turtle_setup(canv_width, canv_height):
    """ Set up the canvas and a turtle for coloring pixels. Return a turtle
        object in hidden state with its pen up. The canvas has size canv_width
        by canv_height, with a coordinate system where (0,0) is in the bottom
        left corner, and automatic re-drawing of the canvas is disabled so that
        turtle.update() must be called to update the drawing.
    """
    # create a turtle to color pixels with
    t = turtle.Turtle()
   
    # set the screen size, coordinate system, and color mode:
    
    screen = t.getscreen()
    screen.setup(canv_width, canv_height)
    screen.setworldcoordinates(0, 0, canv_width, canv_height)
    turtle.colormode(255) # specify how colors are set: we'll use 0-255
    
    t.up() # lift the pen
    t.hideturtle() # hide the turtle triangle
    screen.tracer(0, 0) # turn off redrawing after each movement
    
    return t


def getRandomPt(dimension1, dimension2):
    """ This function requires two dimensions to be passed, 
        will calculate and return a tuple value of x and y
    """  
    x = randrange(0, dimension1)
    y = randrange(0, dimension2)
    return (x, y)


def midpoint(P1x, P1y, P2x, P2y):
    """ This function will require four values to be passed to it,
        and will calculate the midpoint between the x and y values.
        Returns a tuple of x & y
    """ 
    mid_x = (P1x + P2x) / 2
    mid_y = (P1y + P2y) / 2
    return mid_x, mid_y


def distance(P1x, P1y, P2x, P2y):
    """ This function requires four values to be passed to it.
        Uses pythagorean theorem to calculate the distance between the two.
        Returns the int value, which is the distance
    """
    a = P2x - P1x
    b = P2y - P1y
    c = sqrt(a**2 + b**2)
    return c


def getRandCorner(dimension1, dimension2):
    """ This function takes two parameters in which will determine
        a random corner from each of the three provided.
        Returns an x,y coordinate that is a random corner.
    """
    corners = []
    corner1 = (dimension1 / 2, dimension2)
    corners.append(corner1)
    
    corner2 = (0, 0)
    corners.append(corner2)
    
    corner3 = (dimension1, 0)
    corners.append(corner3)
    
    #return a random corner in the list
    return choice(corners)

    
def chooseColor(m, dimension1, dimension2):
    """ This function takes three parameters, midpoint and the two dimensions
    The red color scales from 255 to 0 based on distance from corner 1, the green scales 
    with distance from corner 2, and blue scales with distance from corner 3.
    Returns a rgb value as a tuple in form (red, green, blue)
    """
    
    #if else are in to set limiting values (no negatives or higher than 255)
    red = 255 - (distance(m[0], m[1], dimension1/2, dimension2))
    red = int(red)
    if red < 0:
        red = 0
    elif red > 255:
        red = 255 
    
    green = 255 - (distance(m[0], m[1], 0, 0))
    green = int(green)
    if green < 0:
        green = 0
    elif green > 255:
        green = 255
    
    
    blue = 255 - (distance(m[0], m[1], dimension1, 0))
    blue = int(blue)
    if blue < 0:
        blue = 0
    elif blue > 255:
        blue = 255
    
    return(red, green, blue)

    

if __name__ == "__main__":
    # Write your main program here.
    
    # Start by prompting the user for dimensions, then
    # calling the turtle_setup function.
    dimension1 = int(input("Canvas width? "))
    dimension2 = int(input("Canvas height? "))
    
    t = turtle_setup(dimension1, dimension2)
    

    # Chaos game - pseudocode from the assignment handout:
    
    # Let p be a random point in the window
    
    p = getRandomPt(dimension1, dimension2)
    
        
    # loop 10000 times:
    
    for x in range(10000):
        if x > 10:
            
        # corner1 = (dimension1 / 2, dimension2)
        # corner2 = (0, 0)
        # corner3 = (dimension1, 0)
    
    #     c = a random corner of the triangle
            c = getRandCorner(dimension1, dimension2)
    
    
    #     m = the midpoint between p and c
            m = midpoint(p[0], p[1], c[0], c[1])
        
    
    #     choose a color for m
            mColor = chooseColor(m, dimension1, dimension2)
        
    #     color the pixel at m
            t.color(mColor)
            t.goto(m)
            t.dot(1, mColor)
        
    
            p=m
    
    turtle.update()    
    
    
   
    
    
    
    
    
    
    
    
    