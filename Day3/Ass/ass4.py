def function1():
  num1 = int(input("Enter num1 = "))
  num2 = int(input("Enter num2 = "))
  num3 = int(input("Enter num3 = "))
    
    
  if (num1>num2) and (num1>num3):
     print(f"num1 is greater")
     max = num1
  elif (num2 > num3) and (num2 > num1):
     print(f"num2 is greater")
     max = num2
  else: 
     print(f"num3 is greater")
     max = num3
    
 # print("maximum number is = {max}")
function1()


