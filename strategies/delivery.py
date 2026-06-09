from abc import ABC, abstractmethod

class DeliveryStrategy(ABC):
    @abstractmethod
    def calculate_delivery_charge(self, distance):
        pass

class BikeDelivery(DeliveryStrategy):
    def calculate_delivery_charge(self, distance):
        return 20 + (distance * 0.5)  # Base charge + per km charge
    
    @property
    def get_delivery_type(self):
        return "Bike"
    
class CarDelivery(DeliveryStrategy):
    def calculate_delivery_charge(self, distance):
        return 50 + (distance * 1)  # Base charge + per km charge
    
    @property
    def get_delivery_type(self):
        return "Car"
