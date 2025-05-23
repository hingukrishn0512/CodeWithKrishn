n = int(input("enter number"))

for i in range (1,n+1):
    print(" "*(n-i),end="")
    print("*"*(4*i-i),end="")
    print("")
   