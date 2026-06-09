
from utils.constants import customer_types_list, customer_types_dict

class Customer:
    total_customers = 0

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        Customer.total_customers += 1
        
    @property
    def customer_type(self):
        return customer_types_dict["regular"]
    
    @classmethod
    def get_total_customers(cls):
        return cls.total_customers
    
    def __str__(self):
        return f"Customer: {self.name}, Phone: {self.phone}, Type: {self.customer_type}"
    
class PremiumCustomer(Customer):
    @property
    def customer_type(self):
        return customer_types_dict["premium"]
    
