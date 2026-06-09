
from utils.validators import Validator
from repositories.customer_repo import CustomerRepository
from models.customer import Customer, PremiumCustomer

class CustomerService:
    def __init__(self, customer_repo):
        self.customer_repo = customer_repo

    def create_customer(self, name, phone, customer_type):
        if not Validator.validate_phone_number(phone):
            raise ValueError("Invalid phone number. Must be a 10-digit number.")
        if customer_type == "premium":
            customer = PremiumCustomer(name, phone)
        else:
            customer = Customer(name, phone)
        self.customer_repo.create(customer)
        return customer

    def get_all_customers(self):
        return self.customer_repo.get_all()

    def get_customer_by_id(self, customer_id):
        return self.customer_repo.get_by_id(customer_id)

    def delete_customer(self, customer_id):
        self.customer_repo.delete(customer_id)

    def update_customer(self, customer_id, name=None, phone=None, customer_type=None):
        if phone and not Validator.validate_phone_number(phone):
            raise ValueError("Invalid phone number. Must be a 10-digit number.")
        self.customer_repo.update(customer_id, name, phone, customer_type)