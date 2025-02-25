#Creating Variables
a = 100 
b = 9
c = 10 * a
d = b / 3
e = b ** 2

# Converts to an integer
d = int(d)

# Converts to a float (decimal number)
d = float(d)

# Converts to a string
d = str(d)

print(c)
print(d)
print(e)

# We have to convert e to a string in order to print it in a sentence like this
print("there are " + str(e) + " students in this class")

# Function that takes a first name and last name and prints them
def name_printer():
    first_name = input("first name?")
    last_name = input("last name?")
    print(first_name + " " + last_name)

# Calling(using) this function twice
name_printer()
name_printer()
