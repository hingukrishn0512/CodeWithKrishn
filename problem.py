a1= int(input("enter your marks you got in english"))
a2= int(input("enter your marks you got in maths"))
a3= int(input("enter your marks you got in science"))

b= (100*(a1+ a2 + a3 ))  /300 

                                            #percentage khadva mate
if(b>=40 and  a1>33 and a2>33 and a3>33 ):
    print("you passed the exam ",b)

else:
    print("sorry better luck next time",b)

print("thanks for visiting") 