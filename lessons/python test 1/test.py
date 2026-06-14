secret = 27
# players_number = int(input("enter a number between 1 and 100:"))
i = 1
lives = 5
while i <= 5:
    players_number = int(input("enter a number between 1 and 100:"))
    if players_number == secret:
        print("you win")
        break 
    # elif players_number in range(1, 30):
    #     print("🔥 hot")
    # elif players_number in range(31, 60):
    #     print(" 🌡️ warm")
    # elif players_number in range(61, 80):
    #     print(" 🥶 cold")
    # elif players_number in range(90, 100)
    if players_number > secret:
        print("lower number")

    elif players_number < secret:
        print("higher number")

    lives = lives - 1
    print("remaining live - ", "❤️  " * lives)
    i = i + 1

print("the secret number was- ", secret)