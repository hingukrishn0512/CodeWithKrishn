class calculator:
    def __init__(self , n):
        self.n = n

    def square(self):
        print(f"the square of the number is {self.n*self.n}")
    
a = calculator(67)
a.square()