ages = {
    "Abishek" : 33,
    "Daksh" : 13,
    "gojo" : 28,
    "praveen" : 13
}
target_age = 13
count = 0

for key in ages:
    print(ages[key])
    if ages[key] == target_age:
        count += 1
print("the number of people who are",target_age, "years are: ", count)

