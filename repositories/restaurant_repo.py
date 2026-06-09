
class RestaurantRepository:
    def __init__(self, database):
        self.database = database

    def create(self, restaurant):
        conn = self.database.connect()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO restaurants (name, city) VALUES (?, ?)
        """, (restaurant.name, restaurant.city))
        conn.commit()
        self.database.close()

    def get_all(self):
        conn = self.database.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, city FROM restaurants")
        restaurants = cursor.fetchall()
        self.database.close()
        return restaurants

    def get_by_id(self, restaurant_id):
        conn = self.database.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, city FROM restaurants WHERE id = ?", (restaurant_id,))
        restaurant = cursor.fetchone()
        self.database.close()
        return restaurant
    
    def delete(self, restaurant_id):
        conn = self.database.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM restaurants WHERE id = ?", (restaurant_id,))
        conn.commit()
        self.database.close()

    def update(self, restaurant_id, name=None, city=None):
        conn = self.database.connect()
        cursor = conn.cursor()
        if name:
            cursor.execute("UPDATE restaurants SET name = ? WHERE id = ?", (name, restaurant_id))
        if city:
            cursor.execute("UPDATE restaurants SET city = ? WHERE id = ?", (city, restaurant_id))
        conn.commit()
        self.database.close()