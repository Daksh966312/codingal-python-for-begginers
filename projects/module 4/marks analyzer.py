marks_list = [40, 32, 28.5, 31, 40]
print(marks_list)
sample_list = [40, 40, 40, 40, 40]*3
print(sample_list)
print("length of marks ", len(marks_list))

print(marks_list[0])
print(marks_list[-1])

print("first three", marks_list[0:3])
print(marks_list[::-1])

sum = 0
for marks in marks_list:
     sum = sum + marks
print(sum)

avg = sum / len(marks_list)
print(avg)

marks_list.sort(reverse = True)
print(marks_list)

def check():
     for marks in marks_list:
          (marks_list[0], marks_list[-1])
          if (marks_list[0]) == (marks_list[-1]):
               print("they are equal")
          else:
               print("NO")
check()