## <Nathan Tyson>
## lab3.py

# Calculate the average of a group of numbers per assignment instructions
def average():
    """Compute and print average"""
    number = int(input("How many grades to average: "))
    total = 0.0
    for i in range(1, number + 1):
        print("Enter your grade on HW", i, ": ", end = "" )
        x = float(input())
        total = total + x
    print("The average of the numbers is: ", (total / number ))


def tip_jar():
    total = 0
    for i in range(5):
        tip = eval(input("How much money will you add? "))
        total = total + tip
    print("The total amount is: ", total)

def newton():
    x = int(input("Enter a number for X: "))
    improvements = eval(input("Amount of improvements: "))
    approx = x / 2
    for i in range(int(approx)):
        approx = (approx + (x / approx)) / 2
    print(approx)

def sequence():
    numofterms = eval(input("Enter a number: "))
    for i in range(1, numofterms + 1, 2):
        print(i, i, end=' ')

def pi():
    n = eval(input("Enter the number of terms: "))
    for i in range(2, n + 1, 2):
        numerator = i
    for x in range(1, n + 1, 2):
        denominator = x
    result = numerator / denominator
    for y in range(n):
        endproduct = result * result
    print(endproduct)








def main():
    #average()
    #tip_jar()
    #newton()
    #sequence()
    pi()

main()
