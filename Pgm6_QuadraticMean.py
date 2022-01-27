#Pgm6_QuadraticMean.py
#This is a program that reads a text file and calculates the quadratic mean from numbers in the file, line by line.

#Name: Nathan Tyson

#Specifications:
                #This program will include 5 functions, in which the end goal is calculating and outputting
                  #the Quadratic Mean of a list of numbers taken from a text file.
                #The program will read a line of the text file. I am using the first line of the file,
                  #however that can be modified to reading the other lines by changing the .readline() in to_numbers()
                #The program will turn that list of strings into a list of floats,
                  #square those floats, take the sum of those squares,
                  #divide the sum by the amount of values in the list,
                  #square root that number, and then output the result.
                #The text file used is "squares.txt"


#Design:
        #The first function (to_numbers) will turn the list of strings from the text file into floats,
          #then will return that list of floats.
        #The second function (make_squares) will square the floats in the list, then returns those squares.
        #The third function (sum_list) will add together all of the squares in the list, and return the sum.
        #The fourth function(compute_mean) will divide the sum by the amount of values in the original list,
          #then take the square root of that number, and return the result.
        #The fifth function (quadratic_mean) will call all of the previous functions into action,
          #which will result in printing out both the original list of numbers (strings), as well as
          #the Quadratic Mean of those numbers.


from math import*

def to_numbers(string):
    #This function turns the list of strings from the text file into floats, then returns that list of floats
    infile = open("squares.txt", "r")
    string = infile.readline(7)
    list_of_strings = string.split(",")
    list = [float(list_of_strings[0]), float(list_of_strings[1]), float(list_of_strings[2]), float(list_of_strings[3])]
    return list

def make_squares(list):
    #This function squares the floats in the list, then returns those squares
    numbers = to_numbers("")
    zero = (numbers[0]) ** 2
    one = (numbers[1]) ** 2
    two = (numbers[2]) ** 2
    three = (numbers[3]) ** 2
    squares = [zero, one, two, three]
    return squares

def sum_list(list):
    #This function adds together all of the squares in the list, and returns the sum
    numbers = make_squares(list)
    zero = numbers[0]
    one = numbers[1]
    two = numbers[2]
    three = numbers[3]
    sum = zero + one + two + three
    return sum

def compute_mean(sum, n):
    #This function divides the sum by the amount of values in the original list,
    #takes the square root of that number, and then returns the result
    sum = sum_list(list)
    mean = sum / n
    mean_result = sqrt(mean)
    return mean_result

def quadratic_mean(list, squares, sum, mean_result):
    #This function puts all of the functions into action, printing out the original list of numbers from the text file,
    #And then finally printing out the quadratic mean f those numbers.
    infile = open("squares.txt", "r")
    data = infile.readline()
    print("The original numbers are:", data)
    n = len(to_numbers(""))
    list = to_numbers("")
    squares = make_squares(list)
    sum = sum_list(list)
    mean_result = compute_mean(sum, n)
    print("The Quadratic Mean of these numbers is:", mean_result)




def main():
    quadratic_mean(to_numbers(''), make_squares(list), sum_list(list), sum_list(list))

main()