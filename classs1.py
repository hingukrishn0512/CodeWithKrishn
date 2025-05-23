class vector2D:
    def __init__(self , i , j):
        self.i = i
        self.j = j
    def show(self):
        print(f"the vector {self.i}i + {self.j}j ")


class vector3d(vector2D):
    def __init__(self, i, j , k):
        super().__init__(i, j)
        self.k = k
    def shoW(self):
        print(f"the vector {self.i}i + {self.j}j + {self.k}k")

o = vector2D(1 ,2)
o.show()
d = vector3d(1, 2, 10)
d.shoW()

