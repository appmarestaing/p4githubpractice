movies = ["One Piece", "Purple Hearts", "Soul", "Pulp Fiction"]

# printing first item in list at index 0
print(movies[0])

# looping through our list 
num = 1
for movie in movies:
    print(str(num) + ". " + movie)
    num = num + 1

# list methods

# sorts our movies alphabetically
movies.sort()
print(movies)

# adds item to end of list
movies.append("Wall-E")
print(movies)

# removes item from end of list
movies.pop()
print(movies)

# removes specific item 
movies.remove("One Piece")
print(movies)

# adds item at a specific index
movies.insert(1, "Fantastic Mr Fox")
print(movies)

# replacing specific items in our list
movies[0:2] = ["Oppenheimer"]
print(movies)


# looping through a string
name = "noah marestaing"
for letter in name:
    print(letter)