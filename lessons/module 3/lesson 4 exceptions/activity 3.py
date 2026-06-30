valid = False

while not valid:  # using nested while loop
    try:
        n = int(input("Enter the number 3: "))
        if n != 3:
            continue
        valid = True
    except ValueError:
        print("Invalid. Please enter a valid number.")