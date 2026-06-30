try:
    n = int(input("enter a no. "))
    print("entered number: ", n)
except ValueError as ex:
    print("an exception has occured\nplease enter a number")
    print(ex) 