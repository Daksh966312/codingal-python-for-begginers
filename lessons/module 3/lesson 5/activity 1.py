import random 

# print(random.randint(1, 100))

# print(random.random())

#print(erandom.choice("daksh mirchandani"))

secret = random.randint(1,100)
playing = True
while playing:
    guess = int(input("guess the number: "))
    if guess == secret:
        print("you won")
        break
    else:
        print("try again")
    