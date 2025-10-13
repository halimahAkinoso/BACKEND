class pet():
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

        # function to display class information
    def display_info(self):
            print (f"Name:{self.name} species:{self.species} age:{self.age}")
    def celebrate_birthday(self):
         if self.age == self.age +1:
              print ("Happy birthday!", self.name)
dog =pet("Buddy", "Dog", 5)
cat = pet("Whiskers", "Cat", 3)         
# print(dog)
# print(cat)
dog.display_info()