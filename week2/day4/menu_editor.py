import psycopg2

DB_NAME = "your_databse"
DB_USER = "your_username"
DB_PASSWORD = "your_password"
DB_HOST = "localhost"
DB_PORT = "5432"
# I have issues with Pgadmin 4 regarding the password so i couldn't retrieve the details for the above
def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
    )

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        """Saves the item to the database."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s) RETURNING item_id;
        """, (self.name, self.price))
        conn.commit()
        cursor.close()
        conn.close()

    def delete(self):
        """Deletes the item from the database."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM Menu_Items WHERE item_name = %s;
        """, (self.name,))
        conn.commit()
        cursor.close()
        conn.close()

    def update(self, new_name, new_price):
        """Updates the item's name and price."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Menu_Items SET item_name = %s, item_price = %s WHERE item_name = %s;
        """, (new_name, new_price, self.name))
        conn.commit()
        cursor.close()
        conn.close()
        self.name = new_name
        self.price = new_price

class MenuManager:
    @classmethod
    def get_by_name(cls, name):
        """Returns an item by name or None if not found."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT item_id, item_name, item_price FROM Menu_Items WHERE item_name = %s;
        """, (name,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        if result:
            return MenuItem(result[1], result[2])
        return None

    @classmethod
    def all_items(cls):
        """Returns all items from the Menu_Items table."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT item_name, item_price FROM Menu_Items;
        """
        )
        items = cursor.fetchall()
        cursor.close()
        conn.close()
        return [MenuItem(name, price) for name, price in items]

# Example usage
item = MenuItem('Burger', 35)
item.save()
item.delete()
item.update('Veggie Burger', 37)
item2 = MenuManager.get_by_name('Beef Stew')
items = MenuManager.all_items()

# Print all items
for i in items:
    print(f"{i.name}: {i.price}")

def show_user_menu():
    while True:
        print("\nMenu Options:")
        print("(V) View an Item")
        print("(A) Add an Item")
        print("(D) Delete an Item")
        print("(U) Update an Item")
        print("(S) Show the Menu")
        print("(E) Exit")
        
        choice = input("Choose an option: ").strip().upper()
        
        if choice == "V":
            name = input("Enter the item name: ")
            item = MenuManager.get_by_name(name)
            if item:
                print(f"{item.name}: {item.price}")
            else:
                print("Item not found.")
        elif choice == "A":
            add_item_to_menu()
        elif choice == "D":
            remove_item_from_menu()
        elif choice == "U":
            update_item_from_menu()
        elif choice == "S":
            show_restaurant_menu()
        elif choice == "E":
            show_restaurant_menu()
            print("Exiting program.")
            break
        else:
            print("Invalid option, please try again.")

def add_item_to_menu():
    name = input("Enter item name: ")
    price = int(input("Enter item price: "))
    item = MenuItem(name, price)
    item.save()
    print("Item was added successfully.")

def remove_item_from_menu():
    name = input("Enter item name to remove: ")
    item = MenuManager.get_by_name(name)
    if item:
        item.delete()
        print("Item was deleted successfully.")
    else:
        print("Error: Item not found.")

def update_item_from_menu():
    old_name = input("Enter the current item name: ")
    old_item = MenuManager.get_by_name(old_name)
    if old_item:
        new_name = input("Enter new item name: ")
        new_price = int(input("Enter new item price: "))
        old_item.update(new_name, new_price)
        print("Item was updated successfully.")
    else:
        print("Error: Item not found.")

def show_restaurant_menu():
    items = MenuManager.all_items()
    print("\nRestaurant Menu:")
    for item in items:
        print(f"{item.name}: {item.price}")

# Example usage
if __name__ == "__main__":
    show_user_menu()

