class Family_members:
    def __init__(self, eye_colour, personality_traits):
        self.eye_colour = eye_colour
        self.personality_traits = personality_traits 

    def show_traits(self):
        print(self.eye_colour)
        print(self.personality_traits)

###############################################################################################################################################################################################################################################################################################################################################

class Kid(Family_members):
    def __init__(self, name, age, eye_colours, personality):
        self.name = name
        self.age = age
        super().__init__(eye_colours, personality)
    def show_traits(self):
        print(self.name)
        print(self.age)
        super().show_traits()
    def favourite_hobby(self, hobby):
        print(self.name, "loves", hobby)

###############################################################################################################################################################################################################################################################################################################################################

child = Kid("Abhishek", 100, "Brown", "optimism")

print("is kid a subclass of familymembers?", issubclass(Kid, Family_members))

child.show_traits()
child.favourite_hobby("singing")