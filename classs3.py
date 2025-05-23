class Employee:
   salary = 280
   increment = 20
   
   @property
   def salaryafterincrement(self):
      
      return self.salary + self.salary *(self.increment/100)
      
   @salaryafterincrement.setter
   def salaryafterincrement(self,salary):
      self.increment = ((salary/self.salary) -1)*100

e = Employee()
e.salaryafterincrement = 300
print(e.salaryafterincrement)
print(e.increment)

      
#salary increment thay and ketla taka thay ee batave