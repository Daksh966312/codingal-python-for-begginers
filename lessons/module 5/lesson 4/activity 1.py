class Useraccount:
    def __init__(self):
        self.username = "mangoes"
        self.__password = "mango"
    def show_password(self):
        print(self.__password)
acc = Useraccount()
print(acc.username)
# print(acc.__password)
acc.show_password()