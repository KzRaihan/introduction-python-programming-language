""" 
 WAP to ask to the user to enter names their 3 favorite moves and store them in list
"""
# First way
mov1 = input("Enter 1st movie name: ")
mov2 = input("Enter 2nd movie name: ")
mov3 = input("Enter 3th movie name: ")

list = [mov1, mov2, mov3]

print("\nYour favorite movies are: ", list)
print("Type: ", type(list))

# 2nd way with method append
movie = [] # Declare list

mov1 = input("Enter 1st movie name: ")
mov2 = input("Enter 2nd movie name: ")
mov3 = input("Enter 3th movie name: ")

movie.append(mov1)
movie.append(mov2)
movie.append(mov3)

print("\nFavorite 3 movies name: ", movie)
print("Type: ", type(movie))

# 3Th way for one variable
F_movie = [] # declare list
mov = input("Enter first movie name: ")
F_movie.append(mov)

mov = input("Enter Second movie name: ")
F_movie.append(mov)

mov = input("Enter Third movie name: ")
F_movie.append(mov)

print("\nMovies name: ", F_movie)
print("Type: ", type(F_movie))

