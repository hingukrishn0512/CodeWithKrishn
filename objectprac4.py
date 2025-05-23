class calculator:
    def __init__(self , n):
        self.n = n

    def square(self):
        print(f"the square of the number is {self.n**0.5}")
    
a = calculator(49)
a.square()     