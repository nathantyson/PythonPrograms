#Pgm3_traffic.py
#Name - Nathan Tyson

#Specifications:
#          This is a program that will calculate an average number of vehicles that travel down
#          a specific amount of roads individually and the average of such,
#          as well as the average and total of all the roads.
#          The amount of roads will be provided by the user.
#          It will also calculate and output the number of days that each road has had a counter installed.

#Design:
#      First, the user will input the number of roads
#      Then a loop will determine how many cars have travelled down each road, and the average of each.
#      Then another loop will determine the total amount and average of all the roads
#      This information will then be outputted to the user.


def traffic():
    num_of_roads = eval(input("Enter the amount of roads surveyed: "))
    total = 0
    indtotal = 0
    for i in range(num_of_roads):
        days = eval(input("Enter the amount of days surveyed on road " + str(i + 1) + ": "))
        for n in range(days):
            cars = eval(input("Enter the amount of cars on day " + str(n + 1) + ": "))
            indtotal = indtotal + cars
        print("The individual total amount of cars is: ",indtotal,"The individual average of cars is: ",(indtotal/days))
        total = total + indtotal
    print("The total amount of cars is: ", total, ", The total average of cars is: ", (total/num_of_roads))





def main():
    traffic()

main()