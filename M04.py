"""
Author: Myles Blackwell
Date: 2-5-2025
Purpose: Movie Recommendation System
"""
import random
import json

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
    
def removeMovie(movie, genre):
    try: #if genre is not found
        if movie in movies[genre]: #if alrady in the genre
            raise ValueError("movie already exit")
        else: #adds movie to dict
             movies[genre].remove(movie)
             print(f'Movie "{movie}" has been to genre "{genre}')
    except KeyError as e: 
        raise e

def viewAllMovies():
    for genre in movies:
            print(f"\n{genre}: ", end="")
            movieList = movies[genre]
            for movie in movieList:
                print(movie, end=", ")

def searchMovie(genre):
    try:
        print(f"\n{genre}: ", end = "")
        for movie in movies[genre]:
            print(movies, end=", ")
    except KeyError as e:
        raise e

def randomMovie():
    genre = random.choice(list(movies.keys()))
    movie = random.choice(list(movies[genre]))
    return movie

moviesFile = 'movies.txt' #file for saved movies

global movies #key is genere #value is a set containging movies
with open(moviesFile, 'r') as file:
    movies = json.load(file)

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
            movie = input("Enter the movie name") #user inputs
            genre = input("Enter the movie Sci-Fi")

            addMovie(movie,genre) #adds movie
        except ValueError: #if key already exist
            print("The movie is already in that genre:")
        except KeyError:   #if genere already exist
            print("This genre was not found")
    
    elif choice == 2: #Item 2 - Remove Movie
        try:
            movie = input("Enter the movie name") #user inputs
            genre = input("Enter the movie Sci-Fi")

            removeMovie(movie,genre)
        except KeyError:   #if genere already exist
            print("This genre or movie was not found")
    
    elif choice == 3: #Item 3 - View All Movie
        print("Movies in the collection:")

        viewAllMovies()

    elif choice == 4: #Item 4 - Search Movies by Genere
        print("Search movies by genre:")
        try:
            genre = input("Enter Genre: ")

            searchMovie(genre)
        except KeyError: 
            print("This genre was not found")
    
    elif choice == 5: #Item 5 - Suggest a Random Moive 6
        movie = randomMovie()
        print(f'How about watching "{movie}"?')
    
    elif choice == 6 : #Item 6 - Ending
        moviesConverted = {genre: list(movie) for genre, movie in movies.items()} #converts the sets into list because set is not compatable to JSON

        with open(moviesFile, 'w') as file:
            json.dump(moviesConverted, file)
        
        print("Saving movies and exiting... Goodbye!")
        start = False
    
    else:
        print("Please enter a choice 1-6")