#Pgm10_hangman.py
#this program allows the user to play hangman

#Name: Nathan Tyson

#Specifications:
               #This progrm will allow the user to play hangman
               #it attains a list of words from a text file (word_list())
               #then chooses a random word from this list (secret_word())
               #then that word is split up into a list, and each character is turned into an underscore (split()
               #then it will ask the user to input a letter, if it is right, ind_guess will pass it to word_update()
               #which replaces the underscore with the entered character.
               #this will continue either until the user correctly fills all spaces, or 7 wrong guesses is accrued.


#Design:
        #This program is obviously meant to involve graphics, however after spending many hours pulling my hair out
        #in attempts at making such a thing happen, I have regretfully and disgracefully resigned from the task.
        #Therefore, this program will take place entirely in the console, run by print statements.
        #Each function has it's own purpose, which is then put together in the final function, play_game().
from graphics import*
from random import*

#hang man graphics
# def drawPiece(tries, win, win_width, win_height, win_hangmanpic):
#     hangman_yaxis = win_width / 2.2  # The body of the hangman will align with this axis
#     if tries == 1:
#         #Draw the post
#         line1 = Line(Point(win_width - win_width / 3, 100), Point(win_width - win_width / 3, 300))
#         line1.draw(win)
#         win_hangmanpic.append(line1)
#         line2 = Line(Point(win_width - win_width / 3, 300), Point(hangman_yaxis, 300))
#         line2.draw(win)
#         win_hangmanpic.append(line2)
#         line3 = Line(Point(hangman_yaxis, 300), Point(hangman_yaxis, 270))
#         line3.draw(win)
#         win_hangmanpic.append(line3)
#     elif tries == 2:
#         #Draw the head
#         circle4 = Circle(Point(hangman_yaxis, 254), 16)
#         circle4.draw(win)
#         win_hangmanpic.append(circle4)
#     elif tries == 3:
#         #Draw the torso
#         line5 = Line(Point(hangman_yaxis, 238), Point(hangman_yaxis, 180))
#         line5.draw(win)
#         win_hangmanpic.append(line5)
#     elif tries == 4:
#         #Draw the left arm
#         line6 = Line(Point(hangman_yaxis, 225), Point(hangman_yaxis - 20, 200))
#         line6.draw(win)
#         win_hangmanpic.append(line6)
#     elif tries == 5:
#         #Draw the right arm
#         line7 = Line(Point(hangman_yaxis, 225), Point(hangman_yaxis + 20, 200))
#         line7.draw(win)
#         win_hangmanpic.append(line7)
#     elif tries == 6:
#         # Strike 6: Draw the left leg
#         line8 = Line(Point(hangman_yaxis, 180), Point(hangman_yaxis - 15, 135))
#         line8.draw(win)
#         win_hangmanpic.append(line8)
#     elif tries == 7:
#         #Draw the right leg
#         line9 = Line(Point(hangman_yaxis, 180), Point(hangman_yaxis + 15, 135))
#         line9.draw(win)
#         win_hangmanpic.append(line9)
#
#         # GAME OVER: Draw a face on our hangman guy
#         # Draw his "X"-eyes
#         line10 = Line(Point(hangman_yaxis + 7, 260), Point(hangman_yaxis + 2, 255))
#         line10.draw(win)
#         win_hangmanpic.append(line10)
#         line11 = Line(Point(hangman_yaxis + 2, 260), Point(hangman_yaxis + 7, 255))
#         line11.draw(win)
#         win_hangmanpic.append(line11)
#         line12 = Line(Point(hangman_yaxis - 7, 260), Point(hangman_yaxis - 2, 255))
#         line12.draw(win)
#         win_hangmanpic.append(line12)
#         line13 = Line(Point(hangman_yaxis - 2, 260), Point(hangman_yaxis - 7, 255))
#         line13.draw(win)
#         win_hangmanpic.append(line13)
#
#         # Draw his mouth
#         line14 = Line(Point(hangman_yaxis - 7, 247), Point(hangman_yaxis + 7, 247))
#         line14.draw(win)
#         win_hangmanpic.append(line14)


def word_list():
    infile = open("wordlist.txt", "r")
    words = infile.read().split(" ")
    list = [words[0], words[1], words[2], words[3], words[4]]
    return list


def secret_word():
    list1 = word_list()
    random1 = randint(0, 4)
    if random1 == 0:
        return list1[0]
    elif random1 == 1:
        return list1[1]
    elif random1 == 2:
        return list1[2]
    elif random1 == 3:
        return list1[3]
    elif random1 == 4:
        return list1[4]


def split(word):
    word = [char for char in word]
    length = len(word)
    for i in range(length):
        word[i] = "_ "
    return word


def ind_guess(guess, word):
    word1 = list(word)
    for i in range(len(word1)):
        if guess == word1[i]:
            return True


def word_update(blanks, guess, word):
    word1 = list(word)
    correct = ind_guess(guess, word)
    while correct == True:
        for i in range(len(word1)):
            if guess == word1[i]:
                blanks[i] = guess

        return blanks


def correct_guess(blanks, word):
    string = ""
    blanks = string.join(blanks)
    blanks = blanks.replace(" ", "")
    if blanks == word:
        return True


def play_game():
    word = secret_word()
    blanks = split(word)

    tries = 0
    print("Welcome to my Hangman Game!")
    print(blanks)

    keep_going = True
    while keep_going:
        guess = input("Guess a letter: ")
        individual = ind_guess(guess, word)
        update = word_update(blanks, guess, word)
        correct = correct_guess(blanks, word)

        if correct == True:
            print("Congratulations, You Win!")
            keep_going = False
        elif individual == True:
            print(update)
        elif individual != True:
            tries += 1
            print("Try again")
            if tries > 7:
                print("Game Over, your word was: ", word)
                keep_going = False


def main():
    play_game()


main()