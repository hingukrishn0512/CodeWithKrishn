class number:
    def __init__(self , n):
        self.n = n
        
    def __add__(self , num):  #operator overloading
        return self.n + num.n
    def __mul__(self , num):  #operator overloading
        return self.n * num.n
    
    def __sub__(self , num):  #operator overloading
        return self.n - num.n
n = number(13)
m = number(12)

print(m+n)
print(m*n)
print(m-n)
