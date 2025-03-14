import random
from Dog import Dog

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *dogs):
        dog_names = ", ".join([dog.name for dog in dogs])
        print(f"{self.name}, {dog_names} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            print(random.choice(tricks))
        else:
            print(f"{self.name} is not trained yet!")


dog1 = PetDog("Buddy", 4, 50)
dog2 = PetDog("Max", 3, 40)
dog3 = PetDog("Rocky", 5, 60)


dog1.train()
dog1.do_a_trick()


dog1.play(dog2, dog3)
