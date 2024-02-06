import mysql.connector

class DBUTIL:
    def __init__(self,host,user,password,port,database):
        self.connection=mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            port=port,
            database=database
        )
        self.cursor=self.connection.cursor()

    def execute_query(self,query,values=None):
        try:
            self.cursor.execute(query,values)
            self.connection.commit()
        except Exception as e:
            print(f"Error executing query: {str(e)}")
            self.connection.rollback()

    def fetch_one(self,query,values=None):
        self.cursor.execute(query,values)
        return self.cursor.fetchone()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()