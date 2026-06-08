#  STUDENT CAN TAKE EXAM UNDER TWO CONDITIONS:

# Take the required input for attendance
attendance = float(input("enter percentage- "))
# - Student should have attendance >= 75%
if attendance >= 75:
    print("allowed")

else:
    print("not allowed")
    mc = input("do you have a medical certificate- ")
    if mc == "yes":
        print("allowed")
    elif mc == "no":
        print("not allowed")
    else:
        print("please reply yes or no")
# - Check if attendance matches above criteria - Then Print "Allowed"

# - If attendance is low, Student should have a medical certificate

# - Take input for medical certificate

# - Check if student replied Yes or No

# - If Yes, Print "Allowed"

# - Else No, Print "Not Allowed"