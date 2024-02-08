import unittest
import datetime

from Entity.lease import Lease
from Entity.vehicle import Vehicle
from dao.ICarLeaseRepositoryImpl import ICarLeaseRepositoryImpl
from Exception.exceptions import LeaseNotFoundException


class TestCar(unittest.TestCase):
    def test_car_creation(self):
        car_data = Vehicle(1,'Toyota','Corolla',2019,50,'available',5,2)
        self.assertEqual(car_data.vehicle_id,1)
        self.assertEqual(car_data.make,'Toyota')
        self.assertEqual(car_data.model,'Corolla')
        self.assertEqual(car_data.year,2019)
        self.assertEqual(car_data.daily_rate,50)
        self.assertEqual(car_data.status,'available')
        self.assertEqual(car_data.passenger_capacity,5)
        self.assertEqual(car_data.engine_capacity,2)

    def test_lease_creation(self):
        lease_data = Lease(1,1,1,'2024-2-5','2024-2-10','monthly')
        self.assertEqual(lease_data.lease_id,1)
        self.assertEqual(lease_data.vehicle_id, 1)
        self.assertEqual(lease_data.customer_id, 1)
        self.assertEqual(lease_data.start_date, '2024-2-5')
        self.assertEqual(lease_data.end_date, '2024-2-10')
        self.assertEqual(lease_data.category, 'monthly')

