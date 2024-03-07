# Author: Scott Wehrwein
# Date: 5/3/2019
# A program to test the functions written for lab 5.
# See the lab 5 handout for what the output of this
# program should look like if all the functions are
# workig correctly. Go to the bottom of this file
# and uncomment each function call, beginning with
# test_draw_square, to test each function.

import turtle
import turtleshape as ts


def test_draw_square(t, x, y):
    """ Draws a pattern of squares of different sizes, starting at (x,y) """
    # tests draw_sqare
    t.up()
    t.goto(x, y) # move here without drawing
    t.down()
    for i in range(8): # draw some squares of increasing size
        ts.draw_square(t, 10*i)
        t.up()
        t.left(45)
        t.forward(5)
        t.right(45)
        t.down()

    turtle.update()
    
    
def test_draw_rectangle(t, x, y):
    """ Draws a pattern of rectangles of different sizes, starting at (x,y) """
    t.up()
    t.goto(x, y) # move here without drawing
    t.down()
    t.color("orange")
    t.left(120)
    for i in range(3, 13):
        ts.draw_rectangle(t, i*8, 50/i)
        t.left(36)
    turtle.update()
    
def test_draw_triangle(t, x, y):
    """ Draws a pattern of triangles of different sizes, starting at (x,y) """
    # tests draw_sqare
    t.up()
    t.goto(x, y) # move here without drawing
    t.color("purple")
    t.down()
    for i in range(4): # draw some triangles of increasing size
        ts.draw_triangle(t, (i % 2 + 1) * 20)

        t.left(90)

    turtle.update()


def test_draw_polygon(t, x, y):
    """ Draws a pattern of polygons of different sizes, starting at (x,y) """
    t.up()
    t.goto(x, y) # move here without drawing
    t.setheading(0)
    t.down()
    for sides in range(3, 18):
        ts.draw_polygon(t, 40, sides)
    turtle.update()

def test_draw_snowflake(t, x, y):
    """ Draws three different snowflake pattens with turtle t
        starting at (x,y).
    """
    t.up()
    t.goto(x, y) # move here without drawing
    t.down()
    t.color("teal")
    ts.draw_snowflake(t, 20, 3) # triangle side length 10
    
    t.up()
    t.goto(x+100, y+50)
    t.down()
    t.color("green")
    ts.draw_snowflake(t, 30, 5) # pentagons, side length 15
    
    t.up()
    t.goto(x-50, y+100)
    t.down()
    t.color("blue")
    ts.draw_snowflake(t, 1, 200) # 200-gons, side length 1

    turtle.update()
    
def test_teleport(t, x, y):
    """ Use teleport to draw a grid of dots of different colors.
        Also draw vertical red lines through the grid to test
        that turtle pen state is restored after teleport. Bottom
        left corner of the pattern is at (x,y).
    """
    # test that the turtle goes to the right place
    turtle.colormode(255)
    for i in range(0, 100, 10):
        for j in range(0, 50, 10):
            ts.teleport(t, x+i, y+j)
            t.color(0, 150+i, 150+j)
            t.dot(3)

    # test that the pen state is maintained correctly
    ts.teleport(t, x, y)
    t.color("red")
    t.setheading(90)
    for i in range(0, 100, 10):
        if i % 20 == 0:
            t.up() # should not draw even-numbered vertical lines
            ts.teleport(t, x + i, y)
            t.forward(40) 
        else:
            t.down() # should draw odd-numbered vertical lines
            ts.teleport(t, x + i, y)
            t.forward(40) 
        
    turtle.update()

if __name__ == "__main__":
    
    t = turtle.Turtle()
    t.speed(0)
    # comment these lines out for debugging purposes: it may be
    # helpful to see where the turtle is and watch it draw
    turtle.tracer(0, 0)
    t.hideturtle()

    # make sure the window size is consistent
    screen = t.getscreen() # gets the object representing the window
    screen.setup(500, 500) # sets the window's size

    # draw a dot to verify that everything's set up correctly:
    t.color("green")
    t.dot(5)
    t.color("black")
    
    # Uncomment each of the following tests to make sure that
    # the corresponding function works correctly. The output
    # should match the drawing in the lab handout. Do not modify
    # these lines, except to uncomment them.
    
    test_draw_square(t, -200, -200)
    
    test_draw_rectangle(t, -200, 0)
    
    test_draw_triangle(t, -100, 100)
    
    test_teleport(t, -200, 150)
    
    test_draw_polygon(t, 100, 0)
    
    test_draw_snowflake(t, 50, -200)
