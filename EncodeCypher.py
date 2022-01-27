#lab 7

from math import *

def print_formatting():
    value = float(input("Enter a floating point value: "))
    print("The dollar value of this float is ${0:0.2f}".format(value))
    print("The exponential value of this float is {0:8.6e}".format(value))
    print("A field 9 digits wide with this float is {0:0.9f}".format(value))
    print("A field 9 digits wide starting with zeroes is {:09.6f}".format(value))

def encode():
    msg = input("Enter the Message: ")
    key = int(input("Enter the key: "))
    msg = msg.replace(' ', '')
    msg = msg.replace('', ' ').split()

    ciphertext = ''
    for i in range(len(msg)):
        value = ((ord(msg[i]) - 97 + key) % 26)
        ch = chr(value + 97)
        ciphertext += ch
    print(ciphertext)

def sphere_area(radius):
    area = 4 * pi * radius ** 2
    return area
def sphere_volume(radius):
    volume = (4 / 3) * pi * radius ** 3
    return volume

def sum_n(n):
    acc = 0
    for i in range(1,n+1):
        acc += i
    return acc

def sum_n_cubes(n):
    acc = 0
    for i in range(1,n+1):
        acc+= i **3
    return acc

def main():
    #print_formatting()
    #encode()
    print(sphere_area(5))
    print(sphere_volume(5))
    print(sum_n(5))
    print(sum_n_cubes(5))

main()