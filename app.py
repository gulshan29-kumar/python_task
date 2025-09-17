age=(input("enter the numerical value: "))
if not age.isdigit:
    print("its not a valid integer")
else:    
   if age>65:
      print("you are a senior")
   elif age>18:
    print("you are a adult")   
   else :
    print("You are a minor")    