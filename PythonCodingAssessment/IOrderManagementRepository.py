from abc import ABC, abstractmethod
from datetime import datetime

from DBUTIL import DBUTIL




class IOrderManagementRepository(ABC):
    @abstractmethod
    def create_order(self, order, products ):
        pass

    @abstractmethod
    def cancel_order(self, user_id, order_id):
        pass

    @abstractmethod
    def create_product(self, admin_user ,product):
        pass

    @abstractmethod
    def create_user(self, user):
        pass

    @abstractmethod
    def get_all_products(self):
        pass

    @abstractmethod
    def get_orderby_user(self):
        pass


class OrderProcessor(IOrderManagementRepository):
    def __init__(self,db_util):
        self.db_util = db_util

    def get_all_users(self):
        query="select * from users"
        return self.db_util.fetch_all(query)

    def get_all_orders(self):
        query="select * from orders"
        return self.db_util.fetch_all(query)

    def generate_order_id(self):
        return len(self.get_all_orders())+1

    def generate_user_id(self):
        return len(self.get_all_users())+1

    def create_user_in_db(self,user):
        query = "insert into users (user_id,user_name,password,role) values {%s,%s,%s,%s}"
        values = (user["user_id"],user["user_name"],user["password"],user["role"])
        self.db_util.execute_query(query,values)

    def get_user_by_id(self,user_id):
        query="select * from users where user_id= %s"
        values={user_id}
        return self.db_util.fetch_one(query , values)

    def get_order_by_id(self,order_id):
        query="select * from users where order_id= %s"
        values={order_id}
        return self.db_util.execute_query(query,values)

    def create_orderdetail_in_db(self,order_id,product_id,quantity):
        query="insert into order_details (order_id,product_id,quantity) values {%s,%s,%s}"
        values={order_id,product_id,quantity}
        self.db_util.execute_query(query,values)

    def create_order_in_db(self,order):
        query="insert into orders {order_id,user_id,order_date,totalamt values {%s,%s,%s,%s}"
        values = {order["order_id"],order["user"]["user_id"],order["order_date"],order["totalamt"]}
        self.db_util.execute_query(query,values)

        for product in order["products"]:
            self.create_orderdetail_in_db(order["order_id"],product["product_id"],product["quantity"])

    def get_current_datetime(self):
        return datetime.now()

    def create_order(self,user,products):
        user_exist=self.get_user_by_id(user["user_id"])

        if user_exist is None:
            self.create_user(user)

        order_id = self.generate_order_id()

        tot_amt = sum(product["price"]*product["qtyinstock"] for product in products)

        order_date = self.get_current_datetime()

        order={
            "order_id" : order_id,
            "user" : user,
            "order_date" : order_date,
            "total_amount" : tot_amt,
            "products" : products
        }

        self.create_order_in_db(order)

        for product in products:
            product_id = product["product_id"]
            quantity = product["qtyinstock"]
            self.create_order_detail_in_db(order_id,product_id,quantity)

        self.create_order_in_db(order)

    def create_user(self,user):
        user_id=self.generate_user_id()
        user["user_id"]=user_id
        self.create_user_in_db(user)


    def cancel_order(self, user_id, order_id):
        user_exist = self.get_user_by_id(user_id)
        order_exist = self.get_order_by_id(order_id)
        if user_exist is None or order_exist is None:
            print("User or order not found")
        else:
            query="delete * from products where product_id = {%s}"
            values={order_id}
            self.db_util.execute_query(query,values)


def main():
    db_util = DBUTIL("localhost", user="root", password="12345678", port=3306, database="ordermanagement")
    order_processor = OrderProcessor(db_util)

    while True:
        print("Menu")
        print("1. Create user")
        print("2. create product")
        print("3. cancel order")
        print("4. getAllProducts")
        print("5. getorderbyuser")
        print("6. exit")
        option = input("Enter your choice: ")

        if option == "1":
            username = input("username: ")
            password = input("password: ")
            role = input("role (Admin or User): ")
            user = {"username": username, "password": password, "role": role}
            OrderProcessor.create_user(user)
            print("User created successfully.")

        elif option == "2":
            product={
                "product_name" : input("product name:"),
                "description" : input("Description: "),
                "price": float(input("price: ")),
                "qtyinstock" : input("Quantity in stock :"),
                "type" : input("product type(Electronic/clothing)")
            }

            OrderProcessor.create_product(product)
            print("Product created successfully.")

        elif option == "3":

            user_id = int(input("User ID: "))
            order_id = int(input("Order ID: "))
            OrderProcessor.cancel_order(user_id,order_id)
            print("Order cancelled successfully.")

        elif option == "4":

            products = OrderProcessor.get_all_products()
            print("Products:")
            for product in products:
                print(product)

        elif option == "5":

            user_id = int(input("User ID: "))
            orders = OrderProcessor.get_order_by_user(user_id)
            for order in orders:
                print(order)

        elif option == "6":
            print("I QUIT")
            break

        else:
            print("valid option")

if __name__ == "__main__":
    main()



