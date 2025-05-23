class programmer:
   company = "microsoft"
   def __init__(self , name, salary , pin):
     self.name = name
     self.salary = salary
     self.pin = pin
     
     
k = programmer("krishn" , 129996 , 395006)
k1 = programmer("divya" , 129996 , 395006)
k2 = programmer("hingu" , 129996 , 395006)



print(k.name , k.pin , k.salary , k.company)
print(k1.name , k1.pin , k1.salary , k1.company)
print(k2.name , k2.pin , k2.salary , k2.company)