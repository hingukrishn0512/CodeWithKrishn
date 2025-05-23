def fibonaaci(n):
    a = 0
    b = 1
    print("welcome in the series ")
    for i in range(n):
        print(a , end=" ")
        a,b = b,a+b
        
num = int(input("enter the number : "))
  
if num <= 0:
    print("Please enter a positive number.")
else:
    fibonaaci(num)