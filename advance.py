from  functools import reduce

# lamda function 
square = lambda x:x*x
print(square(4))

#join function
l1 = ["krishn", "hingu"]
final = "-".join(l1)
print(final)

#format function
a = "{0} krishn is good {1}".format("hingu" ,"boy" )
print(a)  #andar vayu jay and also indexing pn chale

#map function

l2 = [1,3,6,9]
square1 = lambda x:x*x

sqare = map(square1,l2)
print(list(sqare))

# filter function
def even(l2):
   if (l2%2 ==0):
    return True
   return False # filter karine je jotu hoy ee ape
onlyeven = filter(even,l2) #pela function then argument
print(list(onlyeven))
    
# reduce function
def sum(a,b):
  return a+b
print(reduce(sum , l2))  #sum karse pela jemke 1+2+3 to pela 1+2 then +3