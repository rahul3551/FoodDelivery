from models.order import Order
from utils.validators import Validator


class OrderService:
    def __init__(self, order_repo, customer_service, restaurant_service):
        self.order_repo = order_repo
        self.customer_service = customer_service
        self.restaurant_service = restaurant_service

    def create_order(self, customer_id, restaurant_id, amount, distance, discount_strategy, delivery_charge_strategy):
        customer = self.customer_service.get_customer_by_id(customer_id)
        restaurant = self.restaurant_service.get_restaurant_by_id(restaurant_id)

        if not customer:
            raise Exception("Customer not found")
        if not restaurant:
            raise Exception("Restaurant not found")
        
        if not Validator.validate_order_amount(amount):
            raise Exception("Invalid order amount")
        
        discount = discount_strategy.apply_discount(amount)
        delivery_charge = delivery_charge_strategy.calculate_delivery_charge(distance)
        final_amount = amount - discount + delivery_charge

        # derive delivery type from the strategy (property `get_delivery_type`)
        try:
            delivery_type = delivery_charge_strategy.get_delivery_type
        except Exception:
            delivery_type = None

        order = Order(customer_id, restaurant_id, amount, discount, delivery_charge, final_amount, delivery_type=delivery_type)
        self.order_repo.create(order)

        return order
    
    def get_all_orders(self):
        return self.order_repo.get_all()


