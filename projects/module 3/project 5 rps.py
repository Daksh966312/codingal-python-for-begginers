#create the rock paper sissors game using random.choice function
import random
choices = ("rock", "paper", "scissors")
print(type(choices))

player = input("rock paper or scissors (type quit to exit): ").lower()
quit = "quit"
if player == quit:
    print("had fun!")
    exit()
comp = random.choice(choices)
print(comp)

if player == comp:
    print("tie")
elif player == "rock" and comp == "siccors":
    print("player wins")
elif player == "paper" and comp == "rock":
    print("player wins")
elif player == "scissors" and comp == "paper":
    print("player wins")
else:
    print("computer wins")
