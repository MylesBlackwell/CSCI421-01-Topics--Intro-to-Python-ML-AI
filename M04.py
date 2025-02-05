"""
Author: Myles Blackwell
Date: 2-5-2025
Purpose: Movie Recommendation System
"""

#add movie function
def addMovie(movie,genre):
    try: #if genre is not found
        if movie in movies[genre]: #if alrady in the genre
            raise ValueError("movie already exit")
        else: #adds movie to dict
             movies[genre].add(movie)
             print(f'Movie "{movie}" added to genre "{genre}')
    except KeyError as e: 
        raise e
    
#def removeMovie():

#def viewAllMovies():

#def searchMovie():

#def randomMovie()

#key is genere #value is a set containging movies
movies = { 
"horror": set([]),
"Action": set(["Creed","Gladiator", "Without Remorse"]),
"Drama" : set(["Just Mercy", "Forest Gump"]),
"Romance": set([]),
"Comedy" : set(["Friday"])
}

start = True
print("Welcome to movie Recomendation System")
while start:
    print(
"""
1. Add a movie
2. Remove a movie
3. View All Movies
4. Search Movies by Genre
5. Suggest a Random Movide
6. Exit
"""
        )
    choice = int(input("Enter your choice: "))

    if choice == 1: #Item 1 - Add movie
        try:
            movie = input("Enter the movide name") #user inputs
            genre = input("Enter the movie Sci-Fi")

            addMovie(movie,genre) #adds movie
        except ValueError: #if key already exist
            print("The movie is already in that genre:")
        except KeyError:   #if genere already exist
            print("This genre was not found")
    