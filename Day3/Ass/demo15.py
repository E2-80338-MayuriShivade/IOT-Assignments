#list of list

def function1():
    l1=[[1,2,3],[50,60,70],[100,200,300]]
    print(l1)

    for l in l1:
      print(l)

    for l in l1:
       for ele in l:
         print(ele)
function1()


def function2():
   l1=[(1,2,3),(5,6,7),(40,30,10)]
   print(l1)

   for t in l1:
     print(t) 

function2()

def function3():
    l1=[
       ("abc",11),
       ("pqr",22),
       ("xyz",33)
    ]

    for t in l1:
       print(t)

  # for (name,age)
function3()

def function4():
   student={
         "name":"abc",
	"mark": [89,70,89,67]
   }
   print(student)
   print(f"Name={student['name']}")
   print(f"marks=")

   for m in student['mark']:
       print(m)
function4()  
