#set: 


def function1():
    s1={10,20,30,40,50}   #can not allow duplicate values and declare inside "{}" bractes
    s2={40,30,20,10}
    print(f"type of s1={type(s1)}")
    print(f"value of s1={s1}")
    print(f"s2={s2}")

    print(f"intersection of s1 and s2={s1.intersection(s2)}")
    print(f"union of s1 and s2={s1.union(s2)}")
function1()
