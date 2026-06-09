
class OrderRepository:
    def __init__(self, database):
        self.database = database

    def create(self, order):
        conn = self.database.connect()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO orders (customer_id, restaurant_id, amount, discount, delivery_charge, final_amount, delivery_type, created_at) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            order.customer_id,
            order.restaurant_id,
            order.amount,
            order.discount,
            order.delivery_charge,
            order.final_amount,
            order.delivery_type,
            order.created_at.strftime('%Y-%m-%d %H:%M:%S')
        ))
        conn.commit()
        self.database.close()

    def get_all(self):
        conn = self.database.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, customer_id, restaurant_id, amount, discount, delivery_charge, final_amount, delivery_type, created_at FROM orders")
        orders = cursor.fetchall()
        self.database.close()
        return orders
    
    def get_by_id(self, order_id):
        conn = self.database.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, customer_id, restaurant_id, amount, discount, delivery_charge, final_amount, delivery_type, created_at FROM orders WHERE id = ?", (order_id,))
        order = cursor.fetchone()
        self.database.close()
        return order
    
    def delete(self, order_id):
        conn = self.database.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM orders WHERE id = ?", (order_id,))
        conn.commit()
        self.database.close()   

    def update(self, order_id, customer_id=None, restaurant_id=None, amount=None, discount=None, delivery_charge=None, final_amount=None):
        conn = self.database.connect()
        cursor = conn.cursor()
        if customer_id:
            cursor.execute("UPDATE orders SET customer_id = ? WHERE id = ?", (customer_id, order_id))
        if restaurant_id:
            cursor.execute("UPDATE orders SET restaurant_id = ? WHERE id = ?", (restaurant_id, order_id))
        if amount:
            cursor.execute("UPDATE orders SET amount = ? WHERE id = ?", (amount, order_id))
        if discount:
            cursor.execute("UPDATE orders SET discount = ? WHERE id = ?", (discount, order_id))
        if delivery_charge:
            cursor.execute("UPDATE orders SET delivery_charge = ? WHERE id = ?", (delivery_charge, order_id))
        if final_amount:
            cursor.execute("UPDATE orders SET final_amount = ? WHERE id = ?", (final_amount, order_id))
        conn.commit()
        self.database.close()