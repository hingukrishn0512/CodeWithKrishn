
current = (input("enter the value of the current : "))
voltage = (input("enter the value of the voltage : "))
resistance = (input("enter the value of resistance :  "))

# v =ir

if current == "":
    print(float(int(voltage)/int(resistance)))
elif voltage == "":
    print(float(int(current)*int(resistance)))
elif resistance == "":
    print(float(int(voltage)/int(current)))
else:
    print("sitaram")