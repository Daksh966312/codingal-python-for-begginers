marks = 71
# if marks >= 91 and marks <=100:
#     print("A+")

if marks in range(91, 101):
    print("A+")

elif marks in range(81, 91):
    print("A")

elif marks in range(71, 81):
    print("B")

elif marks in range(61, 71):
    print("C")

elif marks in range(1, 61):
    print("fail")