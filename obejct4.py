class employ:          #class banavu
    name = "Krishn"
    language = "python"  #class attribute
   
    def __init__(self):
        print("hello brother")   #call karva ni jarrur nathi jate thay      

  

    def getinfo(self):
        print(f"the name is {self.name} and the \nthe language is {self.language}")
    
    @staticmethod
    def greet():    #ane self ni jaruur nathi kemke staic method vapru che
        print("hello good morning")

divya = employ()  #class ma name nakhi e anu object banavu
divya.name="krishn" #object  attribute
divya.language = "java"

divya.getinfo()    #self mukvu jarruri che function ma
divya.greet()