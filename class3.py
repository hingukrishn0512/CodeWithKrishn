
from random import randint
class train:
    def __init_subclass__(self , trainNo):
        self.trainNo = trainNo     # self ma agar hu name badli nakhu to pan output ma change nai ave
        pass
    def booking (self ,trainNo,fro,to ):
        print(f"ticket is booked in train no  : {trainNo} from {fro} to {to}")
     
    def status (self , trainNo):
        print(f"train No {trainNo} is running succesfully")
   
    def fare (self , trainNo , fro , to):
        print(f"ticket fare in trainNo {trainNo} is fro {fro} to {to} is {randint(222,555)}")

t = train()
t.booking(1222,"rampur" , "udaipur")
t.status(1222)
t.fare(1222,"rampur" , "udaipur")

