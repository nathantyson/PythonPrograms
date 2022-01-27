# Lab5.py
# Name: Nathan Tyson

from graphics import *
from math import *

def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target
    outer_circle = Circle(Point(250, 250), 250)
    outer_circle.setOutline("black")
    outer_circle.setFill("white")
    outer_circle.draw(win)
    #second circle
    second_circle = Circle(Point(250, 250), 200)
    second_circle.setOutline("black")
    second_circle.setFill("black")
    second_circle.draw(win)
    #third circle
    third_circle = Circle(Point(250,250), 150)
    third_circle.setOutline("blue")
    third_circle.setFill("blue")
    third_circle.draw(win)
    #fourth circle
    fourth_circle = Circle(Point(250,250), 100)
    fourth_circle.setOutline("red")
    fourth_circle.setFill("red")
    fourth_circle.draw(win)
    #inner circle
    inner_circle = Circle(Point(250,250), 50)
    inner_circle.setOutline("yellow")
    inner_circle.setFill("yellow")
    inner_circle.draw(win)
    # Wait for another click to exit
    win.getMouse()
    win.close()

def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    # Add code here to accept the mouse clicks, draw the triangle.
    num_clicks = 3

    first = win.getMouse()
    second = win.getMouse()
    third = win.getMouse()

    triangle_shape = Polygon(first, second, third)
    triangle_shape.setOutline("black")
    triangle_shape.setFill("black")
    triangle_shape.draw(win)
    #get x and y points and then determine remainder
    firstX = first.getX()
    firstY = first.getY()
    secondX = second.getX()
    secondY = second.getY()
    thirdX = third.getX()
    thirdY = third.getY()

    first_lineX = secondX - firstX
    first_lineY = secondY - firstY
    second_lineX = thirdX - secondX
    second_lineY = thirdY - secondY
    third_lineX = firstX - thirdX
    third_lineY = firstY - thirdY

    #calculate line length, then perimeter
    first_line_length = (first_lineX ** 2) + (first_lineY ** 2)
    first_line_length_result = sqrt(first_line_length)

    second_line_length = (second_lineX ** 2) + (second_lineY ** 2)
    second_line_length_result = sqrt(second_line_length)

    third_line_length = (third_lineX ** 2) + (third_lineY ** 2)
    third_line_length_result = sqrt(third_line_length)

    perimeter = first_line_length_result + second_line_length_result + third_line_length_result

    #calculate area
    s = perimeter / 2
    area1 = (s - first_line_length_result)
    area2 = (s - second_line_length_result)
    area3 = (s - third_line_length_result)
    area = s * (area1 * area2 * area3)
    area_result = sqrt(area)

    # and display its perimeter and area in the graphics window.
    instDisplay = Point(win_width / 2, win_height - 30)
    display_results = Text(instDisplay, "Perimeter = " + str(perimeter) + ", Area = " +str(area_result))
    display_results.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()

def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    #create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    #create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width/2, win_height-20), msg)
    inst.draw(win)

    #create circle in window's center
    shape = Circle(Point(win_width/2, win_height/2 - 30), 50)
    shape.draw(win)

    #red_texPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width/2 - 50, win_height/2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")
    red_input = Entry(Point(win_width - 175, win_height / 2 + 40), 5)
    red_input.setText("")
    red_input.draw(win)

    #green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0,30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    green_input = Entry(Point(win_width - 175, win_height - 128), 5)
    green_input.setText("")
    green_input.draw(win)

    #blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0,60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")
    blue_input = Entry(Point(win_width - 175, win_height - 97), 5)
    blue_input.setText("")
    blue_input.draw(win)

    #display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    for i in range(5):
        win.getMouse()
        c = shape.clone()

        r = int(red_input.getText())
        g = int(green_input.getText())
        b = int(green_input.getText())

        color = color_rgb(r, g, b)
        c.setFill(color)
        c.draw(win)





    #close window
    win.getMouse()
    win.close()
    
    
def main():
    #target()
    #triangle()
    color_shape()

main()





