from Util.DBUtil import DBUtil
from dao.ICarLeaseRepository import ICarLeaseRepository
import datetime


class ICarLeaseRepositoryImpl(ICarLeaseRepository):
    def __init__(self):
        super().__init__()
        self.con = DBUtil.dbconnection()

    def add_customer(self, customer):
        customer_id = customer.customer_id
        firstname = customer.first_name
        lastname = customer.last_name
        email = customer.email
        phone_number = customer.phone_number
        query = "INSERT INTO customer VALUES (%s, %s, %s, %s, %s)"
        cursor = self.con.cursor()
        cursor.execute(query, (customer_id, firstname, lastname, email, phone_number))
        self.con.commit()
        print("Customer added successfully.")
        cursor.close()

    def list_customers(self):
        cursor = self.con.cursor()
        cursor.execute("select * from customer")
        customers = cursor.fetchall()
        cursor.close()
        return customers

    def find_customer_by_id(self, customer_id):
        cursor = self.con.cursor()
        query = "select * from customer where customer_id=%s"
        cursor.execute(query, (customer_id,))
        return cursor.fetchone()

    def generate_customer_id(self):
        cursor = self.con.cursor()
        query = "select customer_id from customer"
        cursor.execute(query)
        ids = cursor.fetchall()
        ids_list = [t[0] for t in ids]
        i = 1
        res_id=0
        while True:
            if i in ids_list:
                i=i+1
                continue
            else:
                res_id = i
                break
        return res_id

    def add_car(self, car):
        car_id = car.vehicle_id
        make = car.make
        model = car.model
        year = car.year
        daily_rate = car.daily_rate
        status = car.status
        passenger_capacity = car.passenger_capacity
        engine_capacity = car.engine_capacity
        query = "insert into vehicle values (%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor = self.con.cursor()
        cursor.execute(query, (car_id, make, model, year, daily_rate, status, passenger_capacity, engine_capacity))
        self.con.commit()
        print("Car Added Successfully")
        cursor.close()

    def generate_car_id(self):
        cursor = self.con.cursor()
        query = "select vehicle_id from vehicle"
        cursor.execute(query)
        ids = cursor.fetchall()
        ids_list = [t[0] for t in ids]
        i = 1
        res_id = 0
        while True:
            if i in ids_list:
                i=i+1
                continue
            else:
                res_id = i
                break
        return res_id

    def find_car_by_id(self, car_id):
        cursor = self.con.cursor()
        query = "select * from vehicle where vehicle_id=%s"
        cursor.execute(query, (car_id,))
        return cursor.fetchone()

    def list_available_cars(self):
        cursor = self.con.cursor()
        query = "select * from vehicle where status='available'"
        cursor.execute(query)
        return cursor.fetchall()

    def list_rented_cars(self):
        cursor = self.con.cursor()
        query = "select * from vehicle where LOWER(status)='notAvailable'"
        cursor.execute(query)
        return cursor.fetchall()

    def generate_lease_id(self):
        cursor = self.con.cursor()
        query = "select lease_id from lease"
        cursor.execute(query)
        ids = cursor.fetchall()
        ids_list = [t[0] for t in ids]
        i = 1
        res_id = 0
        while True:
            if i in ids_list:
                i = i+1
                continue
            else:
                res_id = i
                break
        return res_id

    def create_lease(self, customer_id, car_id, start_date, end_date):
        lease_id = self.generate_lease_id()
        type_lease = input("Enter the type of lease: ")
        query = "insert into lease values (%s,%s,%s,%s,%s,%s)"
        cursor = self.con.cursor()
        cursor.execute(query, (lease_id, customer_id, car_id, start_date, end_date, type_lease))
        self.con.commit()
        print("lease added successfully")
        cursor.close()

    def find_lease_by_id(self, lease_id):
        cursor = self.con.cursor()
        query = "select * from customer where lease_id=%s"
        cursor.execute(query, (lease_id,))
        return cursor.fetchone()

    def remove_car(self, car_id):
        query = "delete from vehicle where vehicle_id=(%s)"
        cursor = self.con.cursor()
        cursor.execute(query, (car_id,))
        self.con.commit()

    def remove_customer(self, customer_id):
        query = "delete from customer where customer_id=(%s)"
        cursor = self.con.cursor()
        cursor.execute(query, (customer_id,))
        self.con.commit()

    def list_active_leases(self):
        query = ("select l.lease_id,l.startdate,l.enddate,type,v.status from lease l join vehicle v "
                 "on l.vehicle_id=v.vehicle_id")
        cursor = self.con.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def list_lease_history(self):
        query = "select * from lease"
        cursor = self.con.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def record_payment(self, lease, amount):
        payment_id = 2
        lease_id = lease.lease_id
        payment_date = datetime.date
        query = "insert into payment values (%s,%s,%s,%s)"
        cursor = self.con.cursor()
        cursor.execute(query,(payment_id,lease_id,payment_date,amount))

    def calculate_payment(self):
        query = "select sum(amount) from payment"
        cursor = self.con.cursor()
        cursor.execute(query)
        return cursor.fetchone()

    def payment_history(self,customer_id):
        query = """
                SELECT p.payment_id,l.customer_id,p.lease_id,p.paymentdate,p.amount
                FROM payment p
                JOIN lease l ON p.lease_id = l.lease_id 
                WHERE l.customer_id = %s
            """
        cursor = self.con.cursor()
        cursor.execute(query, (customer_id,))
        return cursor.fetchall()





































