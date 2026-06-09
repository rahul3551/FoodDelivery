
class RestaurantController:
    def __init__(self, restaurant_service):
        self.restaurant_service = restaurant_service

    def add_restaurant(self):
        name = input("Enter restaurant name: ")
        city = input("Enter restaurant city: ")
        restaurant = self.restaurant_service.create_restaurant(name, city)
        print("Restaurant added successfully")
        print(restaurant)

    def view_restaurants(self):
        restaurants = self.restaurant_service.get_all_restaurants()

        if not restaurants:
            print("No restaurants found")
            return

        for restaurant in restaurants:
            print(f"ID: {restaurant[0]}, Name: {restaurant[1]}, City: {restaurant[2]}")