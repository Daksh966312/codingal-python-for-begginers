r = ("r", "a", "c", "e", "c", "a", "r")
start = 0
end = len(r) - 1

palindrome = True

while start < end:
    if r[start] != r[end]:
        palindrome = False
        break

    start += 1
    end -= 1

if palindrome:
    print("This is a palindrome")
else:
    print("NOT a palindrome")