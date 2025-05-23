#a= "*"
#star = 1
#i= 1
#for i in range (0,3):
 #   star = a*1
  #   print(star)


n = int(input("enter number"))

for i in range (1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-i),end="")
    print("")