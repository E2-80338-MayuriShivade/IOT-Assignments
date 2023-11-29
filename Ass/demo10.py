#defalut argument,named parameter

def function1(a=3,b=4,c=1):
    print(f"p1 = {a} , p2 = {b} , p3 = {c}")


function1(11,22,33)
function1(11,22)     #value pass by user has highest priority
function1(11)
function1()

#named parameter(python only)
function1(b=66)
function1(a=55)
