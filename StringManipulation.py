# Lab6.py
# Name 1: Sammi Ramsden
# Name 2: Nathan Tyson

from graphics import *

def string_processing():
    """
    Do interesting things with strings
    """
    string = input("Enter a string")

    # First character
    print("First character:", string[0])

    # Last character
    print("Last character:", string[-1])

    # Characters 2-5
    print("Characters 2-5:", string[2:6])

    # First and last concatenated
    print("First and last:", string[0] + string[-1])

    # First 3 characters repeated 10 times
    print("First 3 * 10:", string[0:3] * 10)

    # Numbers of characters
    print("Length:", len(string))

def process_list():

    pt = Point(5,10)
    values = [5, 'hi', 2.5, "there", pt, "7.2"]
    x = values[1] + values[3]
    print(x)
    x = float(values[0]) + float(values[2])
    print(x)
    x = values[1] * 5
    print(x)
    x = [values[2], values[3], values[4]]
    print(x)
    x = [values[2], values[3], values[0]]
    print(x)
    x = [values[2], values[0], float(values[5])]
    print(x)
    x = len(values)
    print(x)

def name_reverse():
    name = input("Enter name in first last order").split(' ')

    print(name[1], ', ', name[0], sep = '')

def initial():
    name_amt = eval(input("Enter an amount of names"))
    for i in range(1, name_amt + 1):
        print("What is the first name of student", i, ":", sep = ' ')
        first = input()
        print("Enter the last name of", first)
        last = input()

        initials = ''.join([first[0], last[0]])

        print("The initials of", first, "are: ", initials, sep=' ')

def names():
    names = input("Enter comma separated list of names")
    x = names.split(",")

    for i in range(len(x)):
        name = x[i]
        y = name.split(" ")
        first = y[0]
        last = y[1]


        print(first[0], last[0], sep = '', end = '')

# def thirds():
#     sentences = eval(input("How many sentences will be input?"))
#
#     for i in range(1, sentences + 1):
#         print("Enter a sentence")
#         sentence = input()
#
#         letter = 2
#         letter_var = 3
#
#         for n in range(len(sentence)):
#             print(sentence[letter:letter_var])
#             letter_var = letter_var + 3



def word_average():
    sentence_amt = eval(input("Enter an amount of sentences to be processed: "))

    for i in range(sentence_amt):
        sentence = input("Enter a sentence: ").split(' ')
        wrd_amount = len(sentence)
        sentence2 = ''.join(sentence)
        average = len(sentence2) / wrd_amount
        print(average)

def pig_latin():
    sentence = input("Enter a sentence:").split(' ')

    for i in range(len(sentence)):
        sentence[i] = sentence[i] + (sentence[i]) [0]
        sentence[i] = (sentence[i])[1:] + str('ay')
    print(" ".join(sentence))

def main():
    #string_processing()
    process_list()
    #name_reverse()
    #initial()
    #names()
    #thirds()
    #word_average()
    #pig_latin()

main()
