"""
Author: Myles Blackwell
Date: 1/27/2025
Purpose: Working with Lists and Tuples with Input Validation
"""

daysOfTheWeek = ("Monday","Tuesday","Wednesday","Thursday","Friday",'Saturday',"Sunday")


temperture = []
for i in daysOfTheWeek:
    valid = False
    while valid == False:
     value = -21
     try:
        print("Enter the temperature for", i,":", end=" ")
        value = int(input())
     except:
        print("Please enter an integer")
    else:
        if value > -20 and value < 120:
            print("here")
            valid = True
        else:
            valid = False
            print("Temerture has to be greater than -20 degrees and less than 120 degrees.")
