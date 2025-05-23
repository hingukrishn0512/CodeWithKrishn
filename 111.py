class twodvector:
    def __init__(self,i,j):
        self.i = i
        self.j = j
        
    def show(self):
        print(f"{self.i}i + {self.j}j ")
class threeDvector(twodvector):
    def __init__(self, i, j,k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"{self.i}i + {self.j}j + {self.k}")


a = twodvector(1,2)
a.show()
b = threeDvector(1,2,3)
b.show()
