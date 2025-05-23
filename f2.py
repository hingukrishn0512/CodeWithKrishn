a = 2
b= 3
c = 4

def greatestnumber(a , b , c):

    if (a>b and a>c):
        return a
    
    elif(c>b and c>a):
        return c
    
    elif(b>a and b>c):
        return b
    
print(greatestnumber(a , b , c))
    
