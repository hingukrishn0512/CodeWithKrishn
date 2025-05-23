marks = {

  "krishn": 100,
  "jitendra": 99,
}
      
print(marks, type(marks))    #dictonary can be used
                                # to store the data like marks 
                                #of the students

print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"krishn": 99 } )
print(marks.pop("jitendra"))
print(marks.get("krishn"))
print(marks) #makes update pan thay sake ama anu bracket alg lagavu pade
                 #dictonaries are mutable we can upate and the 
                 #original will be change or we can say that update
print(marks.__contains__("krishn"))
#contain valu khali true or false ma answer apse