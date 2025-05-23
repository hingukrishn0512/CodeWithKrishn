class Employee:
    company = "Microsoft"
    name = "Krishn"
    salary = 12344444
    
    def show(self):
        print(f"The name of the employee is {self.name}, salary is {self.salary}, and company is {self.company}")


class Programmer(Employee):  
    company = "TCS"           
    name = "Divya"
    salary = 1234444
    language = "Python"
    
    def show_language(self):
        print(f"The name of the employee is {self.name}, salary is {self.salary}, company is {self.company}, and language is {self.language}")


class Child(Programmer, Employee):   
    company = "ITC"
    
    def lang(self):
        print(f"The name of the language is {self.language} and the company is {self.company}")
    

# Create objects of the classes
a = Employee()
b = Programmer()
c = Child()

# Calling the methods
a.show()         # Calls the show method from Employee class
b.show()         # Calls the show method from Programmer class (inherited from Employee)
b.show_language() # Calls the show_language method from Programmer class
c.lang()         # Calls the lang method from Child class
