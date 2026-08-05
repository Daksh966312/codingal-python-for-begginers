import string 
import random

length = int(input("enter password: "))

characters = string.ascii_letters + string.digits

password = ""

for i in range(length):
    password += random.choice(characters)

password_list = list(password)
random.shuffle(password_list)
passwrd = "".join(password_list)

print(password)