a= int(input("enter your number : "))

for i in range (2,a):
    if(a%i)==0:
        print("your number is not prime")
        break


    else:
        print("number is prime")
    break
