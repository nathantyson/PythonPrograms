# CSCI-220 Lab 12 - Classes and While Loops

# Student 1: Nathan
# Student 2: Jacques
from random import *
# Activity 1 - Built-in List Functions

class FindAndRemoveFirst():

    def __init__(self, list):
        self.instance = list


    def do_it1(self, value_a):
        instance = self.instance
        for i in range(len(instance)):
            if instance[i] == value_a:
                instance[i] = "Jacques"
        return instance

    def do_it2(self, value_a):
        instance = self.instance

        i = instance.index(value_a)
        instance[i]="Nathan"

        return instance

    def print_list(self):
        instance = self.instance
        print(instance)




    # Add methods (__init_, do_it1, do_it2, print_list) here

# Activity 2 - List Search with While

class LinearSearch():
    def __init__(self):
        self.infile = open("DataSorted.txt", "r")

    def Find(self, search_value):
        infile = self.infile
        listt = infile.read()


        test_text = listt.index(search_value)
        if test_text == None:
            return False
        else:
            return True

# Activity 3 - Good Input
class GoodInput():
    def __init__(self):
            '''reee'''
    def get_input(self):
        inputt = int(input("Give a good input. Within 1-10. Thanks. "))
        if 1 < inputt < 10:
            print("Good input. ")
            return inputt
        else:
            print("You suck lul")
            self.get_input()
# Activity 4 - Counting Digits
class Digits():
    def get_num_digits(self,number):
        string = str(number)
        list = [char for char in string]
        x = 0
        for char in string:
            x += 1
        return x


def num_digits():
    digits = []
    num = 1
    while num > 0:
        num = int(input("Enter a number: "))
        if num <= 0:
            break
        number = Digits()
        print(number.get_num_digits(num))


# Activity 5 - Hi-Lo Game
class HiLoGame():
    def __init__(self):
        self.the_number = randint(1, 100)

    def play(self,dumber):
        number = self.the_number
        if dumber == number:
            return False
        elif dumber > number:
            print("Dumber is too high")
            return True
        elif dumber < number:
            print("Dumber is too low")
            return True
        else:
            print("Something funky happened")
    def give_answer(self):
        return self.the_number

def game():
    game = HiLoGame()

    tester = True
    reps = 0
    while tester and reps <= 7:
        dum = int(input("Guess a number from 1 to 100: "))
        tester = game.play(dum)
        reps+=1
    print("Game Over")
    if reps > 7:
        print("You Lost")
        print("The correct number was ", game.give_answer())
    else:
        print("You Win in", reps, " of guesses!")

# Main function to test it all

def main():
    '''reeeeee'''
    # Test the first activity
    #
    # a1_a = FindAndRemoveFirst([10,20,30,40,50])
    # a1_a.do_it1(20)
    # a1_a.print_list()
    #
    #
    # a1_b = FindAndRemoveFirst([10, 20, 30, 40, 50])
    # a1_b.do_it2(50)
    # a1_b.print_list()
    #
    # # Add code here to test the other activities
    #
    # file_boy = LinearSearch()
    # print(file_boy.Find("15"))
    #
    # inputingthings = GoodInput()
    # print(inputingthings.get_input())

    num_digits()

    #game()
# Execute the functions in the file

if __name__ == '__main__':
    main()
