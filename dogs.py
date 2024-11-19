class Dog:
    def __init__(self, name, age, weight, breed):
        self.name = name
        self.age = age
        self.weight = weight
        self.breed = breed

    def print_dog(self):
      print(f"{self.name} is a {self.breed}. It is {self.age} years old. It weighs {self.weight}kg ")

    def human_years(self):
       print(f"{self.name} is {self.age*7} years old in human years")

class Huntingdog(Dog):
    def __init__(self, name, age, weight, breed, handler):
         Dog.__init__(self, name, age, weight, breed,)
         self.handler =handler
    def hunting(self):
        print(f"{self.name} is a hunting dog. It helps {self.handler} to hunt bush meat.")



bax = Dog('Bax', 12, 30, 'kangal')
tiger = Huntingdog("Tiger", 2, 45, "Husky", "Rachel")

# if isinstance(tiger,Huntingdog):
#     print(f"{tiger.name} can hunt anything")
# else:
#     print(f"Do not risk it. This dog cannot hunt")



# bax.print_dog()
# bax.human_years()
# tiger = Huntingdog('Tiger', 5, 45, 'Belgian Melanoir', 'Manny')
# tiger.print_dog()
# tiger.human_years()
# tiger.hunting()
# print(f"{tiger.name} is way bigger than {bax.name}. Because {bax.breed}s are a larger breed than {tiger.breed}s ")