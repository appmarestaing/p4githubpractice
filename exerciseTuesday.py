# Create a function that asks for someones birth year and then prints out how old they will be in 2025.
import random



# Math stuff
a = 100
b = 200 
c = 9 * a
d = b / 2
print(c)
print(a ** 2)

# Does anyone know how we could convert this back into an integer?
print(d)


# Input and Output
num1 = input("what number do you want?")
print(num1 * 2)

# to convert to int
num1 = int(num1)

# to convert to float
num1 = float(num1)

# to convert to string
num1 = str(num1)


# Creating a variable
# What are these called where it's like a word in quotes?
first_name = "noah"
last_name = "marestaing"

# How would we make it so that they are spaced out?
full_name = first_name + last_name
print(full_name)

# How would we ask the user instead of just always printing out the same name?

# How could we make that into a function?




user_num = input("Give a number")
user_num = int(user_num)

if user_num % 2 == 0:
    print("this number is even")
else:
    print("this number is odd")



age = 20
is_citizen = True

if age >= 18 and is_citizen == True:
    print("You can vote")
else:
    print("sorry you can't vote")



    


num = random.randint(0, 100)

while True:
    guess = int(input("guess a number"))
    if guess < num:
        print("the number you want is greater than that")
    elif guess > num:
        print("the number you want is less than that")
    else:
        print("congrats you found it")
        break


