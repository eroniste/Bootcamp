import psycopg2

DB_NAME = "your_databse"
DB_USER = "your_username"
DB_PASSWORD = "your_password"
DB_HOST = "localhost"
DB_PORT = "5432"

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
