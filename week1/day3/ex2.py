class Dog :
    def __init__(self, name, height):
        self.name = name
        self.height = height
    def bark(self):
        print(f"T{self.name} goes woof!")
    def jump(self):
        print(f"{self.name} jumps {self.height} cm high")
davids_dog= Dog("Rex", 50)
davids_dog.bark()
davids_dog.jump()
