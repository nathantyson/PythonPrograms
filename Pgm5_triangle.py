# triangle.py
# Author: Zelle (pp. 103-04)
# Modified by Pharr to eliminate coordinates

#Name: Nathan Tyson

#Warning to Doctor Crosby: I am very sorry about the state of this program, even after asking for you to explain
                          # the concept of parameters and referencing functions I still seem to not understand it.
                          # I thought that I understood in class, but everything that I try doesn't work.
                          # I sincerely apologize for making you take the time to explain it, and then still not
                          # grasping the concept.

#Specifications:
                #This is a program that utilizes differing functions in order to create a triangle in a graphic
                #window, and then upon clicking, display the area and perimeter of that triangle.

#Design:
        #function make_triangle will set the parameters for a polygon
        #function Triangle will make the graphic window, add the polygon, and then display the area and perimeter.
        #function distance will be the formula for distance between two points on the polygon
        #function perimeter will use the distance formula to calculate the perimeter of the polygon.
        #function area will use the perimeter to calculate the area of the triangle.

from graphics import *
from math import *


def make_Triangle(p1, p2, p3):

    # Use Polygon object to draw the triangle
    triangle = Polygon(p1, p2, p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    return triangle

def Triangle(triangle, area_result, perimeter):
    win_width = 400
    win_height = 400
    
    win = GraphWin("Draw a Triangle", win_width, win_height)
    message = Text(Point(win_width/2, win_height-10), '')

    triangle.draw(win)
    win_width = 400
    win_height = 400

    win.getMouse()


    instDisplay = Point(win_width / 2, win_height - 30)
    display_results = Text(instDisplay, "Perimeter = " + str(perimeter) + ", Area = " + str(area_result))
    display_results.draw(win)


    # Wait for another click to exit
    message.setText("Click anywhere to quit")
    win.getMouse()
    win.close()

def distance(p1, p2):
    p1 = [200, 100]
    p2 = [300, 300]
    p3 = [100, 300]

    distance = sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
    return distance

def perimeter(triangle):
    p1 = [200, 100]
    p2 = [300, 300]
    p3 = [100, 300]
    firstX = p1[0]
    firstY = p1[1]
    secondX = p2[0]
    secondY = p2[1]
    thirdX = p3[0]
    thirdY = p3[1]

    first_lineX = secondX - firstX
    first_lineY = secondY - firstY
    second_lineX = thirdX - secondX
    second_lineY = thirdY - secondY
    third_lineX = firstX - thirdX
    third_lineY = firstY - thirdY

    # calculate line length, then perimeter
    first_line_length = (first_lineX ** 2) + (first_lineY ** 2)
    first_line_length_result = sqrt(first_line_length)

    second_line_length = (second_lineX ** 2) + (second_lineY ** 2)
    second_line_length_result = sqrt(second_line_length)

    third_line_length = (third_lineX ** 2) + (third_lineY ** 2)
    third_line_length_result = sqrt(third_line_length)

    perimeter = first_line_length_result + second_line_length_result + third_line_length_result
    return perimeter

def area(triangle):
    p1 = [200, 100]
    p2 = [300, 300]
    p3 = [100, 300]
    firstX = p1[0]
    firstY = p1[1]
    secondX = p2[0]
    secondY = p2[1]
    thirdX = p3[0]
    thirdY = p3[1]

    first_lineX = secondX - firstX
    first_lineY = secondY - firstY
    second_lineX = thirdX - secondX
    second_lineY = thirdY - secondY
    third_lineX = firstX - thirdX
    third_lineY = firstY - thirdY

    # calculate line length, then perimeter
    first_line_length = (first_lineX ** 2) + (first_lineY ** 2)
    first_line_length_result = sqrt(first_line_length)

    second_line_length = (second_lineX ** 2) + (second_lineY ** 2)
    second_line_length_result = sqrt(second_line_length)

    third_line_length = (third_lineX ** 2) + (third_lineY ** 2)
    third_line_length_result = sqrt(third_line_length)

    perimeter = first_line_length_result + second_line_length_result + third_line_length_result

    s = perimeter / 2
    area1 = (s - first_line_length_result)
    area2 = (s - second_line_length_result)
    area3 = (s - third_line_length_result)
    area = s * (area1 * area2 * area3)
    area_result = sqrt(area)
    return area_result





def main():
    p1 = Point(200, 100)
    p2 = Point(300, 300)
    p3 = Point(100, 300)
    perimeter = 647.213595
    area_result = 20000.0
    triangle = make_Triangle(p1, p2, p3)
    Triangle(triangle, area_result, perimeter)
    distance(p1, p2)



main()
