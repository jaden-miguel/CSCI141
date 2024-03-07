# Name: Jaden Miguel
# Date: 7 May 2019
# Purpose: Turtle shape lab #5


import turtle
jaden = turtle.Turtle()

def draw_square(t, side_length):
    """ Use the turtle t to draw a square with side_length.
        Precondition: t’s pen is down
        Postcondition: t’s position and orientation are the same as before
    """
    for x in range(4):
        t.forward(side_length)
        t.left(90)


#draw_square(jaden, 100)




def draw_rectangle(t, width, height):
    """ Draw a rectangle using turtle t with size width x height
        Precondition: t’s pen is down
        Postcondition: t’s position and  orientation are the same as before
    
    """
    for x in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
       
        

#draw_rectangle(jaden, 100, 50)



def draw_triangle(t, side_length):
    """ Draw an equilateral triangle using turtle t with side_length
        Precondition: t’s pen is down
        Postcondition: t’s position and orientation are the same as before
    """
    for x in range(3):
        t.forward(side_length)
        t.left(120)
        

#draw_triangle(jaden, 500)



def draw_polygon(t, side_length, num_sides):
    """ Draw a polygon with num_sides sides, each with length side_length
        using turtle t
        Precondition: t’s pen is down; num_sides > 2
        Postcondition: t’s position and orientation are the same as before
    """
    angle = 360 / num_sides
    
    for x in range(num_sides):
        t.forward(side_length)
        t.left(angle)
        
    
#draw_polygon(jaden, 100, 10)


def draw_snowflake(t, side_length, num_sides):
    """ Use t to draw a snowflake made of ngon-sided polygons. The snowflake
        contains 10 copies of a polygon with num_sides and side_length, each
        drawn at a 36-degree angle from the previous one.
        Postcondition: t’s position and orientation are the same as before
    """
    for j in range(10):
        draw_polygon(t, side_length, num_sides)
        t.right(36)

#draw_snowflake(jaden, 100, 5)



def teleport(t, x, y):
    """ Move the turtle to (x, y), ensuring that nothing is drawn along the
        way. Postcondition: the turtle’s orientation and pen up/down state is
        the same as before.
    """
    if t.isdown():
        t.penup()
        t.goto(x, y)
        t.pendown()
    else:
        t.penup()
        t.goto(x, y)
        
    
    

#teleport(jaden, 200, 150)



def main():
    turtle.tracer(0,0)
    draw_snowflake(jaden, 150, 6)
    teleport(jaden, -500, 0)
    for j in range(12):
        draw_triangle(jaden, 100)
        jaden.right(30)
    turtle.update()
    teleport(jaden, 500, 0)
    for i in range(12):
        draw_triangle(jaden, 100)
        jaden.right(30)
    turtle.update()





if __name__ == "__main__":
    main()
























