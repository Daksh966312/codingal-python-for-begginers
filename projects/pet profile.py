class Pets:
    def __init__(self, name, animal, age):
        self.name = name
        self.animal = animal 
        self.age = age

    #a function defined inside the class is called method 
    
    def display_profile(self):
        print("pet profile")
        print("name:", self.name)
        print("animal:", self.animal)
        print("age:", self.age)

pet1 = Pets("buddy", "dog", 3)
pet1.display_profile()

pet2 = Pets("Koko", "crcodile", 8)
pet2.display_profile()