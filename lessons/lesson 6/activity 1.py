# ACTIVITY 1 - AND-OR SEPARATOR

# 1) Store values in `a`, `b`, and `c`.
a = 30
b = 0
c = -200
# 2) Check an AND condition using `a and b and c`:
#all integers except zero evaluate to true
if a and b and c:
    print("all evaluate to true")
else:
    print("at least one of a, b, c is false")
# - This becomes True only if all three values are treated as True.

# - If the condition is True, print the “all true” message.

# - Otherwise, print the “at least one false” message.

# 3) Re-assign (change) new values to `a`, `b`, and `c` for the next checks.
e = 0
f = 0
g = 0
# 4) Check an OR condition: `a > 0 or b > 0`
if e > 0 or f > 0:
    print("either is greater than 0")
else:
    print("no number greater than 0")
# - If at least one of them is greater than 0, print the “either is greater than 0” message.

# - Otherwise, print the “no number is greater than 0” message.

# 5) Check another OR condition: `b > 0 or c > 0`
if f > 0 or g > 0:
    print("either is greater than 0")
else:
    print("no number greater than 0")
# - If at least one of them is greater than 0, print the “either is greater than 0” message.

# - Otherwise, print the “no number is greater than 0” message.