
from models.restaurant import Restaurant


class RestaurantService:
    def __init__(self, restaurant_repo):
        self.restaurant_repo = restaurant_repo

    def create_restaurant(self, name, city):
        restaurant = Restaurant(name, city)
        self.restaurant_repo.create(restaurant)

    def get_all_restaurants(self):
        return self.restaurant_repo.get_all()
    
    def get_restaurant_by_id(self, restaurant_id):
        return self.restaurant_repo.get_by_id(restaurant_id)
    
    def delete_restaurant(self, restaurant_id):
        self.restaurant_repo.delete(restaurant_id)

    def update_restaurant(self, restaurant_id, name=None, city=None):
        self.restaurant_repo.update(restaurant_id, name, city)