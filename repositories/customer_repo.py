
class CustomerRepository:
    def __init__(self, database):
        self.database = database

    def create(self, customer):
        conn = self.database.connect()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO customers (name, phone, customer_type) VALUES (?, ?, ?)
        """, (customer.name, customer.phone, customer.customer_type))
        conn.commit()
        self.database.close()

    def get_all(self):
        conn = self.database.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, phone, customer_type FROM customers")
        customers = cursor.fetchall()
        self.database.close()
        return customers

    def get_by_id(self, customer_id):
        conn = self.database.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, phone, customer_type FROM customers WHERE id = ?", (customer_id,))
        customer = cursor.fetchone()
        self.database.close()
        return customer
    
    def delete(self, customer_id):
        conn = self.database.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM customers WHERE id = ?", (customer_id,))
        conn.commit()
        self.database.close()

    def update(self, customer_id, name=None, phone=None, customer_type=None):
        conn = self.database.connect()
        cursor = conn.cursor()
        if name:
            cursor.execute("UPDATE customers SET name = ? WHERE id = ?", (name, customer_id))
        if phone:
            cursor.execute("UPDATE customers SET phone = ? WHERE id = ?", (phone, customer_id))
        if customer_type:
            cursor.execute("UPDATE customers SET customer_type = ? WHERE id = ?", (customer_type, customer_id))
        conn.commit()
        self.database.close()