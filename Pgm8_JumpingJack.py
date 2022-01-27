#Pgm8_JumpingJack.py
#This is a program that uses graphics to show a stick figure doing jumping jacks, using buttons to pause and quit
#the animation.

#Specifications:
                #This program will simulate a person doing jumping jacks by creating a graphic window and drawing
                #a stick figure in two frames, which will then animate between the two frames by using
                #.sleep from the time module.
                #Originally this program was meant to be started using a button, paused with a button, and exited
                #with a button, however I can not (for the life of me) get it to work correctly.
                #I am hoping to figure this out in the coming days and make a revised edition of the code.

#Design:
        #There will (eventually, when i get it to work) be a function is_clicked() that gets a mouse click within
        #the three buttons and utilizes that information to control the stick figure.
        #The function buttons() creates the three buttons and puts them into the graphic window.
        #Finally, the function jumping_jack() creates the actual simulation of a person performing jumping jacks.


from graphics import*
from time import*
win = GraphWin("Jumping Jack", 500, 500)
def is_clicked(point, rectangle):
    ll = rectangle.getP1()
    ur = rectangle.getP2()

    return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()

def buttons():
    start_button = Rectangle(Point(10, 400), Point(100, 450)).draw(win)
    start = Text(Point(50, 470), "Start").draw(win)
    pause_button = Rectangle(Point(210, 400), Point(295, 450)).draw(win)
    pause = Text(Point(250, 470), "Pause").draw(win)
    quit_button = Rectangle(Point(400, 400), Point(490, 450)).draw(win)
    quit = Text(Point(450, 470), "Quit").draw(win)
    return start_button, pause_button, quit_button


def jumping_jack():

    stick_1 = Polygon(Point(250, 20), Point(210, 100), Point(290, 100), Point(250, 20), Point(250, 100),
                      Point(250, 120), Point(150, 120), Point(350, 120), Point(250, 120),
                      Point(250, 240), Point(200, 340), Point(250, 240), Point(300, 340), Point(250, 240))

    stick_2 = Polygon(Point(250, 20), Point(210, 100), Point(290, 100), Point(250, 20), Point(250, 100),
                      Point(250, 120), Point(150, 80), Point(250, 120), Point(350, 80), Point(250, 120),
                      Point(250, 240), Point(240, 340), Point(250, 240), Point(260, 340), Point(250, 240))

    while True:

            stick_1.draw(win)
            sleep(1.5)
            stick_1.undraw()
            stick_2.draw(win)
            sleep(1.5)
            stick_2.undraw()
    win.getMouse()
    win.close()




def main():
    jumping_jack()

main()