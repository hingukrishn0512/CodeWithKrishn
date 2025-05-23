class Animals:
    def __init__(self, tiger, lion):    
        self.tiger = tiger
        self.lion = lion

class Pets(Animals):
    def __init__(self, tiger, lion, cats):
        super().__init__(tiger, lion)
        self.cats = cats

class Dogs(Pets):
    def __init__(self, tiger, lion, cats, pavelian):
        super().__init__(tiger, lion, cats)
        self.pavelian = pavelian

    def display(self):
        print("Tiger:", self.tiger)
        print("Lion:", self.lion)
        print("Cat:", self.cats)
        print("Dog:", self.pavelian)

# 🔹 Creating object
my_dog = Dogs("Bengal Tiger", "Asiatic Lion", "Persian Cat", "German Shepherd")

# 🔹 Calling the function
my_dog.display()
