"""
Author: Myles Blackwell
Date: 2/5/2-25
Purpose: M03 Lecture Lab Activity
"""

clubs = {}


start = True

while start:
    print( #Menu
        """
Welcome to the Student Club Manager!
1. Add a Club
2. Add a Student to a Club
3. Remove a Student froma Club
4. View All Clubs and Members
5. List Students in a  Club
6. Check if a Student is in Any Club
"""
    )

    menuInput = input("Enter your Choice: ")
    
    if menuInput == 1: #Menu Item 1 - Add club
        notDuplicate = False
        while not notDuplicate: #If it is already in the club dic
            clubName = input("Enter the club naem: ") #get input
            for club in clubs:
                if club == clubName:
                    notDuplicate = True
        clubs[clubName] = {}
        print(f'Club "{clubName}" added.')
    elif menuInput == 2: #Menu Item 2 - Add Student to a club
        try:
            club = input("Enter the Club: ")
        except: KeyError
            print(f'The "{club} is not found"')


        
        



    start = False