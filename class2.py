   
class calculator:
    
    
    def __init__(self , n):
        self.n = n
  
    def square(self):
        print(f"the square of the number is {self.n*self.n}")
    
    
    @staticmethod
    def hello():
        print("hello there !!")

a = calculator(32)
a.hello()
a.square()


