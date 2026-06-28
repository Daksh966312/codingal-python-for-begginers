# Write a program to check alphabet “A” is present in the given string or not. And 
#  terminate the loop after finding the alphabet “A.”

sentence = input("enter a string: ")
for i in sentence:
    if i == "A":
        print("found it!")
        break
else:
    print("not found :(")
         
    