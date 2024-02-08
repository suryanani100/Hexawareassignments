from mysql import connector
import mysql


class DBUtil:
    @staticmethod
    def dbconnection():
        con = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="root",
            password="nanideepu",
            database="car_rental_system"
        )
        return con

