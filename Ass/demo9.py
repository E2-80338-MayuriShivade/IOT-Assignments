#global variable
num1=11
def function1():
   global num1
   num2=22
   num1=66
   print(f"value of num2 = {num2}")

function1()
print(f"value of num1 = {num1}")
num2=33
num1=44
