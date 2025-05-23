class demo:
 a= 4
o= demo()
print(o.a) #print class attribute because instance attribute is not present

o.a = 0
print(o.a)#print instance attribute because its present
 

print(demo.a) # print class attribute 

#class attribute doesnt change 
#first we just print class then intance attribute classs doesnt change