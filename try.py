try:
    a  = int(input("enter the number : "))
    b  = int(input("enter the number : "))
    result = a/b

except ValueError:
    print("enter valid number")

except ZeroDivisionError:
    print("sarkhu nakh oyyy gandu")

except IndexError:
    print("te nakhu avu kaai avej nai ")

finally:
   print("this is forever") 