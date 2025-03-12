import random

class MyList:
    def __init__(self, letters):
        self.letters = letters

    def get_reversed_list(self):
        return self.letters[::-1]

    def get_sorted_list(self):
        return sorted(self.letters)

    def generate_random_list(self):
        return [random.randint(0, 100) for _ in range(len(self.letters))]

my_list = MyList(['a', 'b', 'c', 'd', 'e'])

print("Reversed List:", my_list.get_reversed_list())
print("Sorted List:", my_list.get_sorted_list())
print("Random List:", my_list.generate_random_list())
