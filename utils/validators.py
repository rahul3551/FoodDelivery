from .constants import customer_types_list


class Validator:
    @staticmethod
    def validate_phone_number(phone_number):
        if not phone_number.isdigit() or len(phone_number) != 10:
            # raise ValueError("Phone number must be a 10-digit number.")
            return False
        return True
    
    @staticmethod
    def validate_customer_type(customer_type):
        if customer_type not in customer_types_list:
            # raise ValueError(f"Customer type must be one of {valid_types}.")
            return False
        return True
    
    @staticmethod
    def validate_order_amount(amount):
        if amount < 0:
            # raise ValueError("Order amount cannot be negative.")
            return False
        return True