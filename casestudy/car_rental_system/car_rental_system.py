from Entity.customer import Customer
from Entity.vehicle import Vehicle
from dao.ICarLeaseRepositoryImpl import ICarLeaseRepositoryImpl
from Exception.exceptions import CarNotFoundException
from Exception.exceptions import CustomerNotFoundException


class Car_Rental_System(ICarLeaseRepositoryImpl):
    def __init__(self):
        super().__init__()


    def main(self):
        while True:
            print("--------------")
            print("1. Add new customers: ")
            print("2. Retrieve customer Details: ")
            print("3. Add new Car: ")
            print("4. Retrieve car information: ")
            print("5. Add new Lease: ")
            print("6. List Available cars: ")
            print("7. Retrieve payment history for customer: ")
            print("8. Total revenue from payments")
            print("9. Break")
            print("----------------")
            choice = int(input("Enter your choice: "))
            match choice:
                case 1:
                    customer_id = self.generate_customer_id()
                    firstname = input("Enter First name: ")
                    lastname = input("Enter last name: ")
                    email = input("Enter email:")
                    phone_number = input("Enter phone number:")
                    customer = Customer(customer_id, firstname, lastname, email, phone_number)
                    self.add_customer(customer)
                    print("The customer id of customer is:", customer_id)

                case 2:
                    customer_id = int(input("Enter the id of customer: "))
                    customer_details = self.find_customer_by_id(customer_id)
                    if customer_details:
                        print("Customer id: ", customer_details[0])
                        print("First name: ", customer_details[1])
                        print("Last name: ", customer_details[2])
                        print("Mail: ",customer_details[3])
                        print("Phone number: ",customer_details[4])

                    else:
                        raise CustomerNotFoundException("Customer is not found")

                case 3:
                    vehicle_id = self.generate_car_id()
                    make = input("Enter manufacturer of car: ")
                    model = input("Enter model of car: ")
                    year = int(input("Enter year:"))
                    daily_rate = int(input("Enter daily rate:"))
                    status = input("Enter status: ")
                    passenger_capacity = int(input("Enter passenger capacity: "))
                    engine_capacity = int(input("Enter engine capacity: "))
                    car_obj = Vehicle(vehicle_id, make, model, year, daily_rate, status, passenger_capacity,
                                      engine_capacity)
                    self.add_car(car_obj)

                case 4:
                    car_id = int(input("Enter the id of car: "))
                    car_details = self.find_car_by_id(car_id)
                    if car_details:
                        print(car_details)
                    else:
                        raise CarNotFoundException("Car is not found")

                case 5:
                    customer_id = int(input("Enter the id of customer: "))
                    car_id = int(input("Enter the id of car: "))
                    start_date = input("Enter the date of start: ")
                    end_date = input("Enter the date of end: ")
                    self.create_lease(customer_id, car_id, start_date, end_date)

                case 6:
                    active_cars = self.list_available_cars()
                    for i in active_cars:
                        print(i)

                case 7:
                    customer_id = int(input("Enter the id of customer: "))
                    res = self.payment_history(customer_id)
                    print(res)

                case 8:
                    total_amount = self.calculate_payment()
                    print(" The total amount is :", total_amount[0])

                case 9:
                    break


car = Car_Rental_System()
car.main()
