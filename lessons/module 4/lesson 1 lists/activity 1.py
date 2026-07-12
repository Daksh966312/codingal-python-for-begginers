 # 1) Create an empty list named `empty_list`.
empty_list = []
print(empty_list)
print(len(empty_list))
# (This list currently has no elements.)

# 2) Print a blank line using `print()`.

# 3) Create a list of numbers and store it in `numbers`.
numbers = [1, 2, 3, 4, 5] 
print(numbers)
print(len(numbers))
numbers.append(23)
print(numbers)
print(len(numbers))
# (The list contains: 1, 2, 3, 4, 5.)

# 4) Print the list `numbers`.

# 5) Create a new list `triples` using the `*` operator:
triples = [1, 2, 3]*3
print(triples)
# a) Start with the list [1, 2, 3].

# b) Multiply it by 3 to repeat the elements three times.

# c) Store the result in `triples`.

# 6) Print the list `triples`.

# 7) Create a list `aList` with values [100, 200, 300, 400, 500].
alist = [100, 200, 300, 400, 500]

# 8) Reverse the list using slicing:

# a) Use `aList[::-1]` to reverse the order of elements.
# alist = alist[::-1]
alist.reverse()
print(alist)
# b) Store the reversed list back into `aList`.

# 9) Print the reversed list `aList` and add a newline at the end.