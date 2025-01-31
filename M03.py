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
            dayNum = 1
            for day,temp in temperature.items():
                print(dayNum,":\t",day,":",temp)
                dayNum += 1

            validTempChange = False
            while not validTempChange:
                try:
                    tempPick = int(input("Enter the day of the week you want to update\t:"))
                    if 0 < tempPick < 8:
                        validTempChange = True
                    else:
                        print("Please chose one the numbers 1-7")

                except ValueError:
                    print("Please put in one of the numbers")
            
            validNewTemp = False
            while not validNewTemp:
                try:
                    newTemp = int(input("Enter the new temperature:\t"))
                    if -20 < newTemp < 120:
                        temperature[i] = newTemp
                        validNewTemp = True
                    else:
                        print("Temerture has to be greater than -20 degrees and less than 120 degrees.")
                except:
                    print("Please enter an integer")
                
        elif valueMenuStart == "n":
            validMenuStart = True
            menuStart = False
        else:
            print("Please enter only 'y' or 'n'")

highsLows = ['Monday',temperature['Monday'],'Tuesday',temperature['Tuesday']]
for day,temp in temperature.items():
    if temp > highsLows[1]:
        highsLows[0] = day
        highsLows[1] = temp
    
    if temp < highsLows[3]:
        highsLows[2] = day
        highsLows[3] = temp


print(f"Hottest day: {highsLows[0]} ({highsLows[1]}°F) Collest day: {(highsLows[2])} ({highsLows[3]}°)")