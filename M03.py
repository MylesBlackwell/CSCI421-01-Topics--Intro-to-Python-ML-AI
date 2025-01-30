"""
Author: Myles Blackwell
Date: 1/27/2025
Purpose: Working with Lists and Tuples with Input Validation
"""

daysOfTheWeek = ("Monday","Tuesday","Wednesday","Thursday","Friday",'Saturday',"Sunday")


temperature = {}
for i in daysOfTheWeek:
    valid = False
    while not valid:
        try:
            value = int(input(f"Enter the temperature for {i}: "))
            print("value is:" , value)
            if -20 < value < 120:
                temperature[i] = value
                valid = True
            else:
                print("Temerture has to be greater than -20 degrees and less than 120 degrees.")

        except:
            print("Please enter an integer")

menuStart = True

while menuStart:
    validMenuStart = False
    while not validMenuStart:
        valueMenuStart = input("\n\n\n Main Menu:\n would you like to change a temperature? y/n:")
        if valueMenuStart == "y":
            validMenuStart = True
            for day,temp in temperature.items():
                print(day,":\t",temp)
                
        elif valueMenuStart == "n":
            validMenuStart = True
            menuStart = False
        else:
            print("Please enter only 'y' or 'n'")