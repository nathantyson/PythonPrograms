#Pgm2_mean.py
#program to calculate RMS Average and Harmonic Mean from user input

#Nathan Tyson

#Specifications: <Code will allow user to specify amount of values to be entered, followed by allowing
#                the user to input each individual value of their choice.
#                <One function will calculate both the RMS Average, and another function will calculate
#                the Harmonic Mean of these values,
#                which will then output the results to the user.
#                <The formula for the RMS Average is the square root of the arithmetic mean of the squares
#                of the numbers given by the user.
#                <The formula for the Harmonic Mean is the amount of numbers given by the user, divided by
#                the sum of 1 over every number leading up to the given number, excluding zero.

#Design: <This program will ask the user to enter a number of values.
#        <The program will then ask the user to enter an amount of numbers equal to the original value entered.
#        <Then the program will calculate the RMS Average
#        <The program will then present this values to the user.
#        <The program will then do the same for the Harmonic Mean.

from math import *

def rms_average():
    num_of_values = eval(input("Enter a number of values for an RMS Average calculation: "))
    total = 0
    for i in range(num_of_values):
        ind_values = eval(input("Enter a number: "))
        total = (ind_values**2 + total)
    arithmetic_mean = total / num_of_values
    print("The RMS Average of the numbers is: ", sqrt(arithmetic_mean))


def harmonic_mean():
    num_of_values = eval(input("Enter a number of values for a Harmonic Mean Calculation: "))
    total = 0
    for i in range(num_of_values):
        ind_values = eval(input("Enter a number: "))
        total = (1 / ind_values + total)
    mean = num_of_values / total
    print("The Harmonic Mean of the numbers is: ", mean)


def main():
    rms_average()
    harmonic_mean()

main()