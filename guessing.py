import random

a = input("Enter a letter: ")
b = 'computer'

random_choice = random.choice(b)


print("Random letter from 'computer':", random_choice)

try:
    if a == b:
        print("Excellent")
    elif a != b:
        print("Try again")
    else:
        print("Chalte re")

except IndexError:
    print("Thik se daala nahi bhai 😅")

finally:
   raise  NameError("Tere se nahi hoga, chutiya banaya 😂")
