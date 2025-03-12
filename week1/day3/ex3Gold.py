class MenuManager:
    def __init__(self):
        self.menu = [
            {'name': 'Soup', 'price': 10, 'spice': 'B', 'gluten': False},
            {'name': 'Hamburger', 'price': 15, 'spice': 'A', 'gluten': True},
            {'name': 'Salad', 'price': 18, 'spice': 'A', 'gluten': False},
            {'name': 'French Fries', 'price': 5, 'spice': 'C', 'gluten': False},
            {'name': 'Beef bourguignon', 'price': 25, 'spice': 'B', 'gluten': True}
        ]
    
    def add_item(self, name, price, spice, gluten):
        new_dish = {'name': name, 'price': price, 'spice': spice, 'gluten': gluten}
        self.menu.append(new_dish)
        print(f"Dish '{name}' added successfully!")
    
    def update_item(self, name, price, spice, gluten):
        for dish in self.menu:
            if dish['name'] == name:
                dish['price'] = price
                dish['spice'] = spice
                dish['gluten'] = gluten
                print(f"Dish '{name}' updated successfully!")
                return
        print(f"Dish '{name}' not found in the menu.")
    
    def remove_item(self, name):
        for dish in self.menu:
            if dish['name'] == name:
                self.menu.remove(dish)
                print(f"Dish '{name}' removed successfully!")
                print("Updated menu:")
                print(self.menu)
                return
        print(f"Dish '{name}' not found in the menu.")

if __name__ == "__main__":
    manager = MenuManager()
    manager.add_item("Pizza", 20, "A", True)
    manager.update_item("Hamburger", 18, "B", False)
    manager.remove_item("Salad")
    manager.update_item("Pasta", 22, "C", True)
    manager.remove_item("Spaghetti")
