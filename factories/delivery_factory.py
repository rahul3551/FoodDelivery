from strategies.delivery import BikeDelivery, CarDelivery


class DeliveryFactory:
    @staticmethod
    def create(delivery_type):
        if delivery_type.lower() == "car":
            return CarDelivery()
        return BikeDelivery()