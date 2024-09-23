import random

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

deck = []
for suit in suits:
    for rank in ranks:
        deck.append(rank + " of " + suit)

# random number from 0 - 1 not including 1
# rand_0to1 = random.random()
# print(rand_0to1)

# random integer from 10 - 100 including 100
# rand_int = random.randint(10, 100)
# print(rand_int)

# picking a random card
# rand_choice = random.choice(deck)
# print(rand_choice)

# random sample of k size of a given collection
# rand_sample = random.sample(deck, k = 5)
# print(rand_sample)

# shuffles our list of cards
# random.shuffle(deck)
# print(deck)