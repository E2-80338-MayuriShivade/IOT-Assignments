#list:

def function1():
   l1=[11,22,44,33]   #if we write value inside "[]" it will be considered as list data type
   print(f"list l1={l1}")
   print(f"type of l1 = {type(l1)}")
   print(f"l1[0]={l1[0]}")
   print(f"l1[2]={l1[2]}")

function1()   


#def function2():

def function3():
    l1=[11,22,33,44]
    print(f"length of l1 = {len(l1)}")
    l1.append(100)
    l1.insert(2,200)
    l1.remove(33)
    l1.pop()   #remove last element from list

    print(f"list l1={l1}")

function3()    
