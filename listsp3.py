movies = ["The Thing", "Animal House", "Rush Hour", "Rush Hour 2"]


print(movies[0])

# printing out list of movies
num = 1
for movie in movies:
    print(str(num) + ". " + movie)
    num = num + 1

# Different List Methods
movies.sort() # sorts list in order or alphabetically
print(movies)

movies.append("Fantastic 4") # append adds item to end
print(movies)

movies.pop() # pop removes item from end of list
movies.pop()
print(movies)

# remove removes first instance of an item
movies.remove("Animal House")
print(movies)

# insert inserts item at specific index
movies.insert(2, "Deadpool")
print(movies)

print(len(movies))

# print last item in our list
print(movies[len(movies) - 1])


# removing number from a list
numbers = [1, 2, 2, 9, 2, 2, 12, 9]

while 2 in numbers:
    numbers.remove(2)

print(numbers)

name = "noah marestaing"
for letter in name:
    print(letter)