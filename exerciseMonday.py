movies = ["Captain America 4", "Deadpool", "Conclave", "Longlegs", "Deadpool", "Deadpool"]


# What index is Deadpool at? What about Longlegs?


print(movies[1])

# new_movie = input("Do you want to add a new movie?")
# movies.append(new_movie)

# Looping through a list
num = 1
for movie in movies:
    print(str(num) + ". " + movie)
    num = num + 1

# List Methods
movies.sort() # how would they be sorted?
print(movies)

last_movie = movies.pop() # removes the last element
print(last_movie)


movies.remove("Deadpool") # removes first occurence
print(movies)

movies.insert(0, "Fantastic Mr Fox")
print(movies)

print(len(movies))
print(movies[len(movies) - 1]) # How to print last element in a list 


numbers = [1, 2, 2, 4, 2, 5, 6, 1]
for num in numbers:
    if num == 2:
        numbers.remove(num)

print(numbers)


name = "noah marestaing"
for letter in name:
    print(letter)
    if letter == "a":
        name.replace("a", "")

print(name)


groceries = ["cheez its", "nerds gummy clusters", "doritos", "cocoa puffs", "pepsi", "dr. pepper", "mountain dew"]

# for their project make them ask user for a name and then print out their name without vowels




