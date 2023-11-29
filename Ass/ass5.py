#grade of students

def function1():
  sub1=int(input("Enter sub1 marks = "))
  sub2=int(input("Enter sub2 marks = "))
  sub3=int(input("Enter sub3 marks = "))

  avg=(sub1 + sub2 +sub3 )/3

  if (avg<=100) and (avg >=90):
     print("Grade A")
  elif (avg<=89) and (avg>=80):
     print("Grade B")
  elif (avg<=79) and (avg>=70):
     print("Grade D")
  elif (avg<=69) and (avg>=60):
     print("Grade C")
  else:
     print("Fail")
function1()  
