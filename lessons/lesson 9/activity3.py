print("1. fruits")
print("2. junk foods")

food_choice = int(input("enter 1 for fruits and enter 2 for junk food- "))

if food_choice == 2:
    print("1.pizza,\n 2.burger,\n 3.ice cream,\n 4.waffles,")
    junk_choice = int(input("pick a nuber to order- "))
    if junk_choice == 1:
        print("pizza is ordered")
    elif junk_choice == 2:
        print("burger is ordered")
    elif junk_choice == 3:
        print("ice cream")
    else:
        print("waffles is on its way")



elif food_choice == 1:
    print("1.mangoes,\n 2.apples")
    fruit_choice = int(input("pick a nuber to order- "))
    if fruit_choice == 1:
        print("mangoes is ordered")
    elif fruit_choice == 2:
        print("apples is ordered")

