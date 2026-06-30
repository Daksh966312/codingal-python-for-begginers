try:
    num1, num2 = eval(input("enter 2 numbers, seperated by a comma: "))
    result = num1 / num2 
    print(result)
except ZeroDivisionError:
    print("please enter a non zero second number")
except SyntaxError:
    print("comma is missing please enter a comma")
except:
    print("wrong input provided")