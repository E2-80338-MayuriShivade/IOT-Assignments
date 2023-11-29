#dictionary


def function1():
    person=["abc","pune",20,"8669501037"]
    print(f"person info={person}")

function1()

#key value pair

def function2():
    person={
          "name":"abc",
	  "address":"pune",
	  "age":20,
	  "mobile":"86657415"
    }
    print(f"person info={person}")
    print(f"type of person={type(person)}")
    
    print(f"Name of person={person['name']}")
    print(f"address of person={person['address']}")
    print(f"age of person={person['age']}")
    print(f"mobile of person={person['mobile']}")

function2()
