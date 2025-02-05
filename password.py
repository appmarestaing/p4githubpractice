import requests
import random
import string


passwordLength = 12 # have students make it so it asks the user how long they want the password to be


# function that generates a single random character
def random_character():
    choices = string.ascii_letters + string.digits + string.punctuation 
    return random.choice(choices)

# function that generates a password made up of a bunch of random characters
def generate_strong_password():
    password = ""
    for i in range(passwordLength):
        password = password + random_character()
    print(password)

generate_strong_password()

# function that fetches and returns a random word from the herokuapp api
def fetch_word():
    url = "https://random-word-api.herokuapp.com/word?length=6"

    response = requests.get(url)

    if response.status_code == 200:
        word = response.json()[0]  # The API returns a list with one word
    else:
        print("Failed to fetch the word.")

    return word

# function that replaces vowels or letters with symbols 
def replaceLetters(word):
    word = word[0].upper() + word[1:]
    if "a" in word:
        word = word.replace("a", "@")
    elif "e" in word:
        word = word.replace("e", "3") # have them do the replacements for a and i
    elif "i" in word:
        word = word.replace("i", "1")
    elif "o" in word:
        word = word.replace("o", "0")
    return word
    
# function that generates a password made of two random words
def generate_less_strong_password():
    word1 = fetch_word()
    word2 = fetch_word()
    word1 = replaceLetters(word1)
    word2 = replaceLetters(word2)
    password = word1 + word2
    print(password)

generate_less_strong_password()