# PART 1: Create a dictionary of student records
student_data = {
    "id1": {"name": "Sara", "class": "V", "subject": "english, math, science"},
    "id2": {"name": "David", "class": "V", "subject": "english, math, science"},
    "id3": {"name": "Sara", "class": "V", "subject": "english, math, science"},
    "id4": {"name": "Surya", "class": "V", "subject": "english, coding, math"},
} 

print(student_data)

print(student_data.get("id6", "not there"))

student_data["id5"] = {"name": "Daksh", "class": "IX", "subject": "maths"}

print(student_data)

student_data["id5"]["subject"] = "sst"

print(student_data)

seen_names = []
cleaned_records = {

}

for id,details in student_data.items():
    if details['name'] not in seen_names:
        seen_names.append(details['name'])
        cleaned_records[id] = details

print(cleaned_records)
