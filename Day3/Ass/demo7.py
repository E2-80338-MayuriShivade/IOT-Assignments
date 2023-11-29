#simple function

def function1():
    print("Inside function1 body")

#function with 1 parameter
def function2(param):
    function1()
    print(f"value of param = {param}")
    print(f"type of param = {type(param)}")

function2(22)
function2(True)
function2('pune')

#function with 2 parameter

def function3(param1,param2):
     return param1 + param2

result = function3(11,33)
print(f"result from function = {result}")


result = function3(11.22,33.05)
print(f"result from function = {result}")


result = function3('sunbeam ','pune')
print(f"result from function = {result}")
