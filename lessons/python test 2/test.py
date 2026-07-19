def add(a,b):
    return (a+b) 

def subtract(a,b):
    return (a-b) 

def multiply(a,b):
    return (a*b)  

def divide(a,b):
    try:
        return (a/b)
    except ZeroDivisionError:
        print("cannot be divided by 0")
        exit()
try:
    a = float(input("Enter a num:"))
    b = float(input("enter any num:")) 
except ValueError:
    print("please enter a valid numerical input ")
    exit()
        


op = input("enter an operation: +,-,*,/: ")
if op == "+":
    print(add(a,b)) 
elif op == "-":
    print(subtract(a,b))
elif op == "*":
    print(multiply(a,b))
elif op == "/":
    print(divide(a,b))
