
from datetime import datetime


class Order:
    def __init__(self, customer_id, restaurant_id, amount, discount=0, delivery_charge=0, final_amount=None, delivery_type=None):
        self.customer_id = customer_id
        self.restaurant_id = restaurant_id
        self.amount = amount
        self.discount = discount
        self.delivery_charge = delivery_charge
        self.delivery_type = delivery_type
        self.created_at = datetime.now()
        self.final_amount = final_amount

    def __str__(self):
        return f"Order for Customer ID: {self.customer_id}, Restaurant ID: {self.restaurant_id}, Amount: {self.amount}, Final Amount: {self.final_amount}, Created At: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"