import sys
import random
import string

from turtle import update
password = []
characters_left = -1


def update_characters_left(number_of_characters):
    global characters_left
    #ToDo: validation
    if number_of_characters < 0 or number_of_characters > characters_left:
        print("Number incorrect. Choose a number between 0 and", characters_left)
        sys.exit(0)
    else:
        characters_left -= number_of_characters
        print("Characters left", characters_left)


password_length = int(input("How many characters should the password be?: "))

if password_length < 5:
    print("Password has to be at least 5 characters long. Try again")
    sys.exit(0)
else:
    characters_left = password_length

lowercase_letters = int(
    input("How many lowercase letters should be in the password?: "))
update_characters_left(lowercase_letters)
uppercase_letters = int(
    input("How many uppercase letters should be in the pasword?: "))
update_characters_left(uppercase_letters)
special_characters = int(
    input("How many special characters should be in the pasword?: "))
update_characters_left(special_characters)
digits = int(
    input("How many digits should be in the pasword?: "))
update_characters_left(digits)
if characters_left > 0:
    print("Not all characters used. Adding",
          characters_left, "lowercase letters to the password")
    lowercase_letters += characters_left
print()
print("Password length:", password_length)
print("lowercase letters:", lowercase_letters)
print("uppercase letters:", uppercase_letters)
print("special characters:", special_characters)
print("digits:", digits)

for _ in range(password_length):
    if lowercase_letters > 0:
        password.append(random.choice(string.ascii_lowercase))
        lowercase_letters -= 1
    if uppercase_letters > 0:
        password.append(random.choice(string.ascii_uppercase))
        uppercase_letters -= 1
    if special_characters > 0:
        password.append(random.choice(string.punctuation))
        special_characters -= 1
    if digits > 0:
        password.append(random.choice(string.digits))
        digits -= 1

random.shuffle(password)
print("wygenerowane hasło:", "".join(password))
