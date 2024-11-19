import dogs , cat, time

class Hostel:
    def __init__(self,name):
        self.name = name 
        self.kennel = {}
    def __str__(self):
        return f"Welcome to {self.name}. "


    def check_in(self, dog):
        if isinstance(dog,dogs.Dog):
            self.kennel[dog.name] = dog
            print(f"{dog.name} has been checked into {self.name}")
        else:
            print(f"Sorrym only dogs are allowed in {self.name}. ")


def testcode():
    bax = dogs.Dog('Bax', 3, 23, 'Boxer')
    warrior = dogs.Huntingdog('Warrior', 3, 45, 'German Shepherd', 'Rachel')
    joey = cat.Cat('Joey', 1, 23)

    dogHaven = Hostel('Dog Haven')

    dogHaven.check_in(bax)
    time.sleep(1)
    dogHaven.check_in(warrior)
    time.sleep(1)
    dogHaven.check_in(joey)

testcode()
