class employee():
    company = "microsoft"
    name = "krishn"
    salary = 12344444
    def show (self):
        print(f"the name of a employee is{self.name} and salary is {self.salary} and company {self.company}")


class programmer(employee):   #inheritance kemke upar wala function thi ama 
    company = "tcs"           #ferfar karu che
    name = "divya"
    salary = 1234444
    def showlanguage (self):
        print(f"the name of a employee is{self.name} and salary is {self.salary} and company {self.company}")

a = employee
b = programmer

print(a.company ,a.name , a.salary)
print(b.company ,b.name , b.salary)