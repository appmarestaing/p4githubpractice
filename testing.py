import random
import time



def generate_wheel():
    spaces = []
    for i in range(18):
        spaces.append("red")
    for i in range(18):
        spaces.append("black")
    for i in range(2):
        spaces.append("green")
    return spaces


def spin(spaces):
    landed = random.choice(spaces)
    return landed


def play_game():
    money = 1000
    
    

    spaces = generate_wheel()

    while True:
        print("you have $" + str(money))
        bet = int(input("how much do you want to bet?"))
        color = input("what do you want to bet on?")
        print("the wheel is spinning. Good luck!")
        spot = spin(spaces)
        time.sleep(2)
        print("it landed on " + spot)

        if spot == color:
            money = money + bet
            print("congratulations, you won! you now have $" + str(money))
        else:
            money = money - bet
            print("sorry, you lost! you now have $" + str(money))

        play_again = input("do you want to play again?")
        if play_again == "no":
            break


play_game()


