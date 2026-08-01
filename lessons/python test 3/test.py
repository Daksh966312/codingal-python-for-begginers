grades_book = {
    "alice" : 85,
    "bob" : 92,
    "charlie" : 78,
    "Diana" : 95,
    "Ethan" : 64
}

total_score = 0
for score in grades_book.values():
    total_score += score

class_avg = total_score / len(grades_book)
print("class avg: ", class_avg)

top_scorer = max(grades_book, key=grades_book.get) 
bottom_scorrer = min(grades_book, key=grades_book.get)

print("topper", top_scorer)
print("lowest scoring student: ", bottom_scorrer)

search_name = input("enter a student name to look up their grade: ")

student_grade = grades_book.get(search_name, "student not found")

print(student_grade)