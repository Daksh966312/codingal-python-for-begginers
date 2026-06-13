number = int(input("enter a number- "))
temp = number
sum_digits = 0
count = 0

while temp > 0:
    digit = temp % 10
    sum_digits = sum_digits + digit
    count = count + 1
    temp = temp // 10

print("sum of digits- ", sum_digits)
print("number of digits- ", count)