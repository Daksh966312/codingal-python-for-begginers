# 1) Ask the user to enter a number and store it in `num`.
num = int(input("enter number- "))
# 2) Set `sum` to 0.
sum = 0
# (This will store the total of the cubes of each digit.)

# 3) Copy `num` into `temp`.
temp = num
# (We will change `temp` while checking digits, but we must keep `num` unchanged.)

# 4) Repeat while `temp` is greater than 0:
while temp > 0:
    digit = temp % 10 
    sum = sum + digit ** 3
    temp = temp // 10
# a) Find the last digit of `temp` and store it in `digit`.
if sum == num:
    print("armstrong number")
else:
    print("not an armstrong number")
# b) Add (digit × digit × digit) to `sum`.

# c) Remove the last digit from `temp` so you can move to the next digit.

# 5) After the loop, compare `num` and `sum`:

# - If they are the same, print: `num` is an Armstrong number.

# - Otherwise, print: `num` is not an Armstrong number.

