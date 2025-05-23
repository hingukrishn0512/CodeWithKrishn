import random
n = random.randint(1,100)

a = 1
guesses = 0
while (a != n):
   
    guesses +=1
    a = int(input("Guess the number : "))
    if (a>n):
      print("choose the lower number")
    else:
      print("choose the greater number")

print(f"you have guessed the Real number {a} congratulations")




   