class employ:      
   
    def __init__(self):
        print("hello everyone")
        a=1
      
class programmer(employ):      
   
    def __init__(self):
        print("hello ")
        b=2
      
class manager(programmer):      
   
    def __init__(self):
        super().__init__()
        print("hello gm")
        c=3

        
#o = employ()
#t =  programmer()
k = manager()