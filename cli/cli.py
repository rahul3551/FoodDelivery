from models.customer import Customer


class CLI:
    def __init__(self, customer_controller, restaurant_controller, order_controller):
        self.customer_controller = customer_controller
        self.restaurant_controller = restaurant_controller
        self.order_controller = order_controller

    def menu(self):
        while True:
            print("\nFood Delivery SOLID OOP Project")
            print("1. Add Customer")
            print("2. View Customers")
            print("3. Add Restaurant")
            print("4. View Restaurants")
            print("5. Create Order")
            print("6. View Orders")
            print("7. Show Customer Object Count")
            print("8. Show Total Customers (DB)")
            print("9. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.customer_controller.add_customer()
            elif choice == "2":
                self.customer_controller.view_customers()
            elif choice == "3":
                self.restaurant_controller.add_restaurant()
            elif choice == "4":
                self.restaurant_controller.view_restaurants()
            elif choice == "5":
                self.order_controller.create_order()
            elif choice == "6":
                self.order_controller.view_orders()
            elif choice == "7":
                print(f"Customer objects created in this run: {Customer.get_total_customers()}")
            elif choice == "8":
                self.customer_controller.total_customers_db()
            elif choice == "9":
                print("Thank you")
                break
            else:
                print("Invalid choice")