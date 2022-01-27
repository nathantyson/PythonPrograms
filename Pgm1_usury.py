#<program that receives input from user in order to calculate amount of interest over time>
#Nathan Tyson

#Specifications:
#     First, this program must ask the user to input an initial loan amount.
#     Then ask the user to input the time period allowed to repay the loan.
#     Then ask the user to input the interest rate of the loan.
#  The program will then calculate and return to the user:
#  the monthly payment
#  the amount paid over the life of the loan
#  the total interest paid

#Design: (all variable names will be displayed in parentheses)
#     Create function that allows the user to input an integer for the initial loan amount (principal)
#     ^as well as asking to input an integer for the time period allowed to repay the loan (months)
#     ^as well as asking to input a float for the interest rate (interest)
#   The first formula will divide the interest by 1200, which will turn into the interest rate (rate)
#   The second formula will be: principal * rate * (1 + rate)^months
#                   Divided by: (1 + rate)^months -1
#   This will be the monthly payment.
#   The third formula will be: months * monthly payment
#   This will be the total amount paid.
#   The fourth formula will be: total amount paid - principal
#   This will be the total interest paid


#     The program will then display:
#                      Monthly Payment: (number)
#                      Amount Paid over the life of the loan: (number)
#                      Total Interest Paid: (number)

#establish variables
interest = eval(input("Enter your interest as a decimal number: "))
principal = eval(input("Enter your initial loan payment: "))
months = eval(input("Enter your time allowed to repay the loan: "))

# Function for user to input interest, principal, and time
# this will return the monthly payment, total amount paid, and the total interest paid
def calculate_loan ():
    interest_rate = interest / 1200
    monthly_payment_top = principal * interest_rate * (1 + interest_rate) ** months
    monthly_payment_bottom = (1 + interest_rate) ** months - 1
    monthly_payment_total = monthly_payment_top / monthly_payment_bottom
    print("Monthly Payment =", monthly_payment_total)
    total_amount_paid = months * monthly_payment_total
    print("Total Amount Paid = ", total_amount_paid)
    total_interest_paid = total_amount_paid - principal
    print("Total Interest Paid =", total_interest_paid)


calculate_loan()







