"""
Author: Myles Blackwell
Date: 2/5/2-25
Purpose: M03 Lecture Lab Activity
"""

clubs = {}


start = True

print("Welcome to the Student Club Manager!")
while start:
    print( #Menu
        """
1. Add a Club
2. Add a Student to a Club
3. Remove a Student from a Club
4. View All Clubs and Members
5. List Students in a  Club
6. Check if a Student is in Any Club
7. Exit
"""
    )

    menuInput = int(input("Enter your Choice: "))
    
    if menuInput == 1: #Menu Item 1 - Add club
        duplicate = True
        while duplicate: #If it is already a duplicate
            clubName = str(input("Enter the club name: ")) #get input

            for club in clubs:  #check if there is duplicate
                if club == clubName:
                    duplicate = True
                    print("Club already exist")
                    break
                else:
                    duplicate = False
                
            if len(clubs) == 0:
                duplicate = False
        
        clubs[clubName] = set() #creates and empty set
        print(f'Club "{clubName}" added.')

            
    elif menuInput == 2: #Menu Item 2 - Add Student to a club
        try:
            #get inputs
            club = input("Enter the Club: ") 
            student = input("Enter student name: ")
            for stud in clubs[club]: #If the student is already in that club
                if stud == student:
                    print(f"Student is already in {club}")
            clubs[club].add(student)
            print(f'{student} has been added to {club}')
        except KeyError: #if the club is not found as a key
            print(f'The "{club} is not found"')

    elif menuInput == 3: #Menu Item 3 - Remove a student fom a club
        try: #if the club or student was not found
            club = input("Enter the club: ") #club input
            student = input("Enter a student name: ") #student input
            clubs[club].remove(student) #attempts remove based on the input
            print(f'{student} has been removed from the {club}') #submission message
        except KeyError:
            print(f"The student or club was not found") #error message

    elif menuInput == 4: #Menu Item 4 - Prints the club and the students that belong to that club
        print("Club Memberships:") 
        for club in clubs: 
            if len(clubs[club]) == 0: #If the club is empty
                print(f"{club}: (no members)")
            else:
                print(f"{club}:",end=' ') #adds it each student to club line
                for student in clubs[club]:
                    print(student,end=', ')
                print("\n", end='')

    elif menuInput == 5: #Menu Item 5 - Prints all the students in a certain club
        try: #if club is not found 
            club = input("Enter the club: ") #club input
            if len(clubs[club]) == 0: #if club is empty
                print(f"{club}: (no members)")
            else:
                print(f"{club}:",end=' ') #add the club then all the students in the same line
                for student in clubs[club]:
                    print(student,end=', ')
        except KeyError:
            print("Club was not found")

    elif menuInput == 6: # Menu Item 6 - Takes the student name and goes through each club then print if found in that club
        name = input("Enter the student:") #student name input
        studentFound = False #if student is found in a club or not
        for club in clubs:
            for student in clubs[club]:
                if(student == name): #if found in that club print
                    print(f"{name} is in {club}")
                    studentFound = True #shows found
        if studentFound == False: #if was not found then it prints not found message
            print(f"{name} was not found in any club")

    elif menuInput == 7: #Menu Item 7 - Ends the similation
        start = False #turns the while loop false
        print("Exiting... Goodbye!")  

    else: #input validation
        print("Please choose from 1-7")      


        
