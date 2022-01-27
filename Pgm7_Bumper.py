#Pgm7_Bumper.py

#Name: Nathan Tyson

#This program will simulate two bumper cars (represented as circles) that will move around in a graphic window,
# changing colors whenever they collide with eachother and the walls.

#Specifications:
                 #This program will simulate two bumper cars in a Graphic Window that will move around, and upon
                 #hitting eachother or the walls of the window, they will go in the opposite direction with a new
                 #velocity and color.
                 #This program will utilize 7 different functions that will be called in the last function to
                 #execute the graphics display.


#Design:
        #1st function: getRandom(moveAmount). This will return a random number that will decide the initial speed.
        #2nd function: didCollide(ball1, ball2). This will return a boolean value when the cars collide with eachother,
                    #True for if they collide, and False if they do not.
        #3rd function: hitVertical(ball, win). This will return a boolean value when the cars hit a vertical wall,
                    #True for if they did, and False if they do not.
        #4th function: hitHorizontal(ball, win). This will return a boolean value when the cars hit a horizontal wall,
                    #True for if they did, and False if they do not.
        #5th function: randomColor(circle). This will change the color of the bumper car to something random every
                    #time that they collide either with eachother or any of the walls.
        #6th function: collisionVelocities(listV, ball1, ball2, mass1, mass2). This will calculate the new velocities
                    #of the bumper cars whenever they collide with eachother or the walls of the window.
        #7th function: bumper_cars(). This will be the last function, which will create the actual window and the
                    #bumper cars themselves, and will call all of the other functions into action, creating the
                    #simulation.



from graphics import *
from random import randint
from time import sleep


def getRandom(moveAmount):  # returns a random number for moveAmount
    return randint(-moveAmount, moveAmount)


def didCollide(ball1, ball2):  # returns True or False upon bumper cars colliding
    ball1Point = ball1.getCenter()
    ball2Point = ball2.getCenter()
    ball1X = ball1Point.getX()
    ball1Y = ball1Point.getY()
    ball2X = ball2Point.getX()
    ball2Y = ball2Point.getY()
    ball1Radius = ball1.getRadius()
    ball2Radius = ball2.getRadius()
    distance = (((ball2X - ball1X) ** 2) + ((ball2Y - ball1Y) ** 2)) ** (1 / 2)
    radius = ball1Radius + ball2Radius
    if distance <= radius:
        answer = True
        randomColor(ball1)
        randomColor(ball2)
    else:
        answer = False
    return answer


def hitVertical(ball, win):  # returns True if car hits either side wall, False if not
    ballPoint = ball.getCenter()
    ballX = ballPoint.getX()
    radius = ball.getRadius()
    width = win.getWidth()
    if ballX <= radius or ballX >= width - radius:
        answer = True
        randomColor(ball)
    else:
        answer = False
    return answer


def hitHorizontal(ball, win):  # returns True if car hits top or bottom wall, False if not
    ballPoint = ball.getCenter()
    ballY = ballPoint.getY()
    radius = ball.getRadius()
    height = win.getHeight()
    if ballY <= radius or ballY >= height - radius:
        answer = True
        randomColor(ball)
    else:
        answer = False
    return answer


def randomColor(circle):  # returns a random color
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    circle.setFill(color_rgb(r, g, b))


def collisionVelocities(listV, ball1, ball2, mass1, mass2):  # returns list of new velocities when colliding
    # Velocities of bumper cars
    velocityCar1X = listV[0][0]
    velocityCar1Y = listV[0][1]
    velocityCar2X = listV[1][0]
    velocityCar2Y = listV[1][1]
    # location of bumper cars
    ball1Point = ball1.getCenter()
    ball2Point = ball2.getCenter()
    ball1X = ball1Point.getX()
    ball1Y = ball1Point.getY()
    ball2X = ball2Point.getX()
    ball2Y = ball2Point.getY()
    # difference equation
    deltaX = ball2X - ball1X
    deltaY = ball2Y - ball1Y
    # distance between bumper cars
    distance = ((deltaX ** 2) + (deltaY ** 2)) ** (1 / 2)
    unX = deltaX / distance
    unY = deltaY / distance
    utX = -unY
    utY = unX
    v1n = (unX * velocityCar1X) + (unY * velocityCar1Y)
    v2n = (unX * velocityCar2X) + (unY * velocityCar2Y)
    v1t = (utX * velocityCar1X) + (utY * velocityCar1Y)
    v2t = (utX * velocityCar2X) + (utY * velocityCar2Y)
    #velocities after collision
    v1Prime = v1t
    v2Prime = v2t
    #collisions
    v1nPrime = (v1n * (mass1 - mass2) + 2 * mass2 * v2n) / (mass1 + mass2)
    v2nPrime = (v2n * (mass2 - mass1) + 2 * mass1 * v1n) / (mass1 + mass2)
    v1nPrimeX = v1nPrime * unX
    v1nPrimeY = v1nPrime * unY
    v2nPrimeX = v2nPrime * unX
    v2nPrimeY = v2nPrime * unY
    v1tPrimeX = v1t * utX
    v1tPrimeY = v1t * utY
    v2tPrimeX = v2t * utX
    v2tPrimeY = v2t * utY
    v1X = v1nPrimeX + v1tPrimeX
    v1Y = v1nPrimeY + v1tPrimeY
    v2X = v2nPrimeX + v2tPrimeX
    v2Y = v2nPrimeY + v2tPrimeY
    return [[v1X, v1Y], [v2X, v2Y]]

def bumper_cars():  #function that creates window and bumper cars, as well as calling other functions into action.
    # create window
    win = GraphWin("Bumper Cars", 500, 500)
    width = win.getWidth()
    height = win.getHeight()
    # create bumper cars
    radius = 40
    car1 = Circle(Point(radius + 30, height / 2), radius)
    car2 = Circle(Point(width - (radius + 30), height / 2), radius)
    randomColor(car1)
    randomColor(car2)
    car1.setOutline("red")
    car2.setOutline("blue")
    car1.draw(win)
    car2.draw(win)
    # initial velocities
    v1X = getRandom(15)
    v1Y = getRandom(15)
    v2X = getRandom(15)
    v2Y = getRandom(15)
    velocityList = [[v1X, v1Y], [v2X, v2Y]]
    # mass of bumper cars
    car1mass = 1
    car2mass = 1
    # loop that moves the bumper cars
    for i in range(500):
        sleep(.04)
        if didCollide(car1, car2):
            velocityList = collisionVelocities(velocityList, car1, car2, car1mass, car2mass)
        if hitVertical(car1, win):
            velocityList[0][0] = -velocityList[0][0]
        if hitVertical(car2, win):
            velocityList[1][0] = -velocityList[1][0]
        if hitHorizontal(car1, win):
            velocityList[0][1] = -velocityList[0][1]
        if hitHorizontal(car2, win):
            velocityList[1][1] = -velocityList[1][1]

        car1.move(velocityList[0][0], velocityList[0][1])
        car2.move(velocityList[1][0], velocityList[1][1])

def main():
    bumper_cars()

main()