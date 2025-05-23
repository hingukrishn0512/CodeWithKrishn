a = int(input("please enter your number :"))
b = int(input("please enter your number :"))
print(f"the value of  the power is {a**b}")

if(b==0):
    raise IndexError("hey you are powering the 0 its unvalid ") #custom error
 

else:
  print(f"the answer is  {a**b}")

