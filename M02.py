'''
Author: Myles Blackwell
Date: 1-27-2025
Purpose: Credit Card Payment Calculator
'''

#prompt of balance on the card
print("What is the balance on your card")
cardBalance = float(input())

#promt for intrest rate
print("What is the annual interest rate? Enter a whole number")
interestRate = int(input()) * 0.01

#promt for months
print("How many months do you want to pay off the balance?")
months = int(input())

monthlyPayment = (
    (cardBalance * (interestRate/12))
    /(1-(1+(interestRate/12))**-months))

#total amount is equal to monthly pay amout for x amounts
totalAmount = monthlyPayment * months

#total amount of interest paid
totalInterest = totalAmount - cardBalance

print("Your Monthly Payment:\t$",round(monthlyPayment,2))
print("Your Total Amount Paid:\t$",round(totalAmount,2))
print("Your Total Interest Paid:\t$",round(totalInterest,2))
