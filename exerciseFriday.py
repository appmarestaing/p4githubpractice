import random



num = 20
if num % 2 == 0:
    print(str(num) + " is an even number")
else:
    print(str(num) + " is not an even number")


age = 20
is_registered = False
is_citizen = True

if age > 18 and is_registered and is_citizen:
    print("you can vote")
else:
    print("sorry")


# program that has user guess a random number
random_num = random.randint(0, 100)
# update so it tells the user how many guesses it took them to gues

while True:
    guess = int(input("guess a number \n"))
    if guess > random_num:
        print("guess lower")
    elif guess < random_num:
        print("guess higher")
    else:
        print("congratulations")
        break

