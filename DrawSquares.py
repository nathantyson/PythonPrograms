"""
Lab 4 - Graphics
Name:
"""

from graphics import *
from math import *

def squares():
    """Draw squares

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """

    #Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    #number of times user can add a new square
    numClicks = 5

    #create a space to instruct user
    instPt = Point(width/2, height-10)
    instructions = Text(instPt,"Click to add a new square")
    instructions.draw(win)

    #builds a square
    shape = Rectangle(Point(0,0), Point(20,20))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    #allows the user to click multiple times to add a new
    #square
    for i in range(numClicks):
        p = win.getMouse()
        c = shape.getCenter() #center of square

        #move amount is distance from center of square to the
        #point where the user clicked
        dx = p.getX()
        dy = p.getY()
        dx1 = dx - 10
        dy1 = dy - 10
        dx2 = dx + 10
        dy2 = dy + 10



        shape2 = Rectangle(Point(dx1, dy1), Point(dx2, dy2))
        shape2.setOutline("red")
        shape2.setFill("red")
        shape2.draw(win)

    win.getMouse()
    win.close()

def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    numClicks = 2

    instPt = Point(width / 2, height - 10)
    instructions = Text(instPt, "Click two points to create a rectangle")
    instructions.draw(win)

    for i in range(1, numClicks):
        p = win.getMouse()

        c = win.getMouse()




        shape2 = Rectangle(p, c)
        shape2.setOutline("red")
        shape2.setFill("red")
        shape2.draw(win)
    #calculate area and perimeter
    width1 = c.getX()
    width2 = p.getX()
    width_result = width1 - width2
    length1 = c.getY()
    length2 = p.getY()
    length_result = length1 - length2
    area = (length_result) * (width_result)
    perimeter = 2 * (length_result + width_result)

    #display width and perimeter
    instPt2 = Point(width / 2, height - 30)
    instructions2 = Text(instPt2, "Area = " + str(area) + "Perimeter = " + str(perimeter))
    instructions2.draw(win)
    win.getMouse()
    win.close()

    print("Hello, rectangle")

def circle():
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    numClicks = 2

    instPt = Point(width / 2, height - 10)
    instructions = Text(instPt, "Click two points to create a circle")
    instructions.draw(win)

    for i in range(1, numClicks):
        center = win.getMouse()
        centerX = center.getX()
        centerY = center.getY()

        radiuspoint = win.getMouse()
        radiusX = radiuspoint.getX()
        radiusY = radiuspoint.getY()
        radius = (radiusX - centerX) **2 + (radiusY - centerY) **2
        radiusfinal = sqrt(radius)

        shape2 = Circle(Point(centerX, centerY), radiusfinal)
        shape2.setOutline("red")
        shape2.setFill("red")
        shape2.draw(win)

    #calculate area of circle
    area = 3.1415 * radiusfinal
    finalarea = area ** 2

    # display area
    instPt2 = Point(width / 2, height - 30)
    instructions2 = Text(instPt2, "Area = " + str(finalarea))
    instructions2.draw(win)
    win.getMouse()
    win.close()


def pi2():
    n = int(input("Enter an amount of terms to be summed: "))
    total = 0
    sign = 1
    for i in range(n):
        denominator = 2 * (i) + 1
        total = total + sign * ((4)/(denominator))
        sign = sign * (-1)
    print("The sum of these values is: ", total)


def main():
    #squares()
    rectangle()
    circle()
    pi2()

main()
