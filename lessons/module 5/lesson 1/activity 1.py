class Student:

    attend_school = True
    def __init__(self, name, grade): 
        # creating an attribute for the object
        self.name = name 
        self.grade = grade 
# s1 is an object 
s1 = Student("Daksh", 9)
print(s1.name)

s2 = Student("Nilay",9)
print(s2.name)

print(s1.grade)
print(s2.grade) 