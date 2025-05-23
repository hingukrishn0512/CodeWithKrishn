#f= open("file.txt")
#line= f.readline()
#while(line != ""):
#    print(line)
    
#f.close()

#with open("file.txt") as f:
#    print(f.read())               #ama close karva ni jarrur nathi

with open("file.txt") as f:
    content = f.read()
    if("hingu" in content):
        print("hingu word is present ")

    else:
        print("absent")


    