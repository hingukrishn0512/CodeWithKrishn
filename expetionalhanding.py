a = input("Hey, please enter your number: ")

if not a.isdigit():
    print("Enter a valid number")
else:
    print("You are good to go")

print()

# same loguc in try and except method 

try:
    b= int(input("hey , please enter the number : "))
    print(b)
except Exception as e:
    print(e)