def calc():
    print("welcome to the digital calculator")
    print("we can +,-,*,/")


    num1 = float(input("enter your number 1 : "))
    operator = input("enter operator(+,-,*,/)")
    num2 = float(input("enter your number 2 : "))



    if (operator =="+"):
        print(num1 + num2)
    elif (operator =="-"):
        print(num1 - num2)
    elif (operator =="*"):
        print(num1 * num2)
    elif (operator =="/"):
        if(num2!= 0):
            print(num1 / num2)

        else:
            print("enter valid number ")


    else:
        print("enter valid operator +,-,*,/")
    
calc()