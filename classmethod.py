class employee:
    a=1

    @classmethod  # ana lidhe class attribute dekhado
    def show(cls):
        print(f"the class attribute is {cls.a}")
    
    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name (self , value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


e = employee()
e.a=45
e.name = "hingukrishn divyalakhani"

print(e.name)