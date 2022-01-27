#Pgm4_vigenere.py

#Name: Nathan Tyson

#This is a program which implements the Vigenere cipher.
#Defintion of Vigenere cipher: https://www.geeksforgeeks.org/vigenere-cipher/
#Website that allows encoding message through Vigenere cipher:  https://www.dcode.fr/vigenere-cipher

#Specifications:
                #This program will create a window for a user to input a phrase and a keyword
                #the phrase will be encoded using the amount of letters in the key
                #as well as being encoded according to the Vigenere cipher, which is described in the links above.
                #The resulting encoded message will then be displayed in the window

#Design:
       #The code will take input from the user through Entry boxes
       #The code will then run the text through a loop that utilizes the Vigenere cipher encryption method,
       #The code will then display the resulting encoded message to the user

from graphics import *

def cipher():
    #create a window
    win_width = 600
    win_height = 400
    win = GraphWin("Vigenere Cipher", win_width, win_height)
    win.setBackground("grey")

    # create text instructions
    encode_text = "Enter text to be encoded:"
    inst = Text(Point(150, 100), encode_text)
    inst.draw(win)
    key_text = "Enter key:"
    inst2 = Text(Point(200, 200 ), key_text)
    inst2.draw(win)

    #create input boxes
    text_input = Entry(Point(400, 100), 20)
    text_input.setText("")
    text_input.draw(win)
    key_input = Entry(Point(400, 200), 10)
    key_input.setText("")
    key_input.draw(win)

    win.getMouse()

   #cipher
    text = text_input.getText()
    key= key_input.getText()

    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    text_int = [ord(i) for i in text]
    cipher_text = ''
    for i in range(len(text_int)):
        value = (text_int[i] + key_as_int[i % key_length]) % 26
        cipher_text += chr(value + 65)

    #show result of cipher
    result_position = Point(150, 300)
    show_result = Text(result_position, "The encoded message is: ")
    show_result.draw(win)
    cipher_result = Text(Point(400, 300), cipher_text)
    cipher_result.draw(win)
    win.getMouse()
    win.close()


def main():
    cipher()
main()