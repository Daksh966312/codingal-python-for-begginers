class String:
    def __init__(self):
        self.str1 = ""

    def get_string(self):
        self.str1 = input("enter a string: ")

    def display_string(self, mode=""):
        if mode == 'l':
            print(self.str1.lower())

        elif mode == 'u':
            print(self.str1.upper())
        
        else:
            print(self.str1)

    def reverse(self):
         print("reversed string " , self.str1[::-1])

s = String()

s.get_string()
s.display_string("u")
s.reverse()