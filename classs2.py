class Animals:
    def __init__(self, dogs, cats, lions):
        self.dogs = dogs
        self.cats = cats
        self.lions = lions

    def show(self):
        print(f"The animals are {self.dogs}, {self.cats}, and {self.lions}")

class Pets(Animals):
    def __init__(self, dogs, cats, lions, tigers):
        super().__init__(dogs, cats, lions)
        self.tigers = tigers

    def show(self):
        # Override the show method to include tigers
        print(f"The animals are {self.dogs}, {self.cats}, {self.lions}, and {self.tigers}")

class Dogs(Pets):  # Class name should start with a capital letter as per convention
    def __init__(self, dogs, cats, lions, tigers):
        super().__init__(dogs, cats, lions, tigers)

    @staticmethod
    def bark():
        print("Bow bow!!")

# Creating an instance of the Animals class
a = Animals("Golden Retriever", "Persian", "Lion")
a.show()  # Correct way to call the show method

# Creating an instance of the Dogs class
o = Dogs("Golden Retriever", "Persian", "Lion", "Bengal Tiger")
o.show()  # Calling show method from the Pets class
o.bark()  # Calling static method bark
