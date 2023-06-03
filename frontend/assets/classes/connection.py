'''

    This is used to create a connection class to access the connection method

'''

# from backend.database.accessing_db import connectToDB

import pyodbc

class Connection:
    def __init__(self):
        self.connect = None

    def connectToDB(self):
        '''
        This is used to connect to the database
        :return: connect
        '''

        try:
            if self.connect is not None:
                return self.connect

            connectionString = 'Driver={ODBC Driver 17 for SQL Server};Server=localhost;Database=Animeplex;Trusted_Connection=yes;'
            self.connect = pyodbc.connect(connectionString)

            if self.connect:
                print("Connected to the database.")
                return self.connect

        except pyodbc.Error as e:
            print("Failed to connect to the database.")

# Create an instance of Connection class
make_connection = Connection()
db_connection = make_connection.connectToDB()