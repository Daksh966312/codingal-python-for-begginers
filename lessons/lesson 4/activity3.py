#1) Ask the user to enter marks for 4 subjects: math, english, science, and hindi. Store each mark in its own variable.

print("Enter Marks Obtained in all Subjects: ")
math = int(input("maths :"))
english = int(input("english :"))
science = int(input("science :"))
hindi = int(input("hindi :"))



#2) Add all 4 subject marks and store the total in `sum`.
sum = math+english+science+hindi
print("sum of math,english,science and hindi = ",sum)

#3) Print the total marks stored in `sum`.

#4) Calculate the percentage:
#- Divide `sum` by 400 (total maximum marks for 4 subjects, assuming each is out of 100)
#- Multiply the result by 100
#Store the final value in `perc`.
perc = (sum/400)*100

print(end="Percentage Mark = ")
print(perc)
#5) Print the percentage stored in `perc`.