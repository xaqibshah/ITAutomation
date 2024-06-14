def greeting (name):
    print ("Hello, " + name + "!")



#greeting("Saqib")
#greeting("Ali")


def greetingDept (name, department):
    print ("Welcome, " + name + "!")
    print ("You are part of " + department)

#greetingDept("Saqib", "Computer Science")
#greetingDept("Ali", "Electrical Engineering")


def sumnum (num1, num2):
    print (int(num1) + int(num2))


num1  = sumnum(5, 10)

print(num1)



def sumnum2 (num1, num2):
    return num1 + num2


a = sumnum2(5, 10)
b = sumnum2(20, 30)
c = a + b
#print("The sum of the two sums is: ", c)
