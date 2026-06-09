

from app import App
from database.database import SQLiteDatabase
from repositories.customer_repo import CustomerRepository
from repositories.restaurant_repo import RestaurantRepository
from repositories.order_repo import OrderRepository
from services.customer_service import CustomerService
from services.restaurant_service import RestaurantService
from services.order_service import OrderService
from controllers.customer_controller import CustomerController
from controllers.restaurant_controller import RestaurantController
from controllers.order_controller import OrderController
from cli.cli import CLI


def main():
    database = SQLiteDatabase("food_delivery.db")

    customer_repo = CustomerRepository(database)
    restaurant_repo = RestaurantRepository(database)
    order_repo = OrderRepository(database)

    customer_service = CustomerService(customer_repo)
    restaurant_service = RestaurantService(restaurant_repo)
    order_service = OrderService(order_repo, customer_service, restaurant_service)

    customer_controller = CustomerController(customer_service)
    restaurant_controller = RestaurantController(restaurant_service)
    order_controller = OrderController(order_service, customer_controller, restaurant_controller)

    cli = CLI(customer_controller, restaurant_controller, order_controller)
    app = App(cli)
    app.run()

if __name__ == "__main__":
    main()