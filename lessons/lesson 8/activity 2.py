# 1) Ask the user to enter the numerator and store it in `numn`.
numn = float(input("enter the numerator- "))
# print(type(numn))
# 2) Ask the user to enter the denominator and store it in `numd`.
numd = float(input("enter the denominator- "))
# 3) Check if `numn` is divisible by `numd`:
if numn % numd == 0:
    print("they are divisible")
else:
    print("the are not divisible")
# - Find the remainder when `numn` is divided by `numd`.

# - If the remainder is 0, it means perfectly divisible.

# 4) If divisible, print that `numn` is divisible by `numd`.

# 5) Otherwise, print that `numn` is not divisible by `numd`.