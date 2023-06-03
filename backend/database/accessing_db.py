'''

    This is used to store functions for connecting/disconnecting from the database

'''

import pyodbc

connect = None # This is used to pass the close function on the connection if there isnt one

# def connectToDB(self):
#     '''
#     This is used to connect to the database
#     :return: connect
#     '''
#
#     # This is used to pass the close function on the connection if there isnt one
#     global connect
#
#     try:
#
#         # This is used to pass the close function on the connection if there isnt one
#         if connect is not None:
#             return connect
#
#         connectionString = 'Driver={ODBC Driver 17 for SQL Server};Server=localhost;Database=Animeplex;Trusted_Connection=yes;'
#         connect = pyodbc.connect(connectionString)
#
#         if connect:
#             print("Connected to the database.")
#             return connect
#
#     except pyodbc.Error as e:
#
#         print("Failed to/Not connect to the database.")
#
#         # Displaying failed connection error
#         self.failedToConnectLabel.setFixedWidth(650)
#         self.failedToConnectLabel.setFixedHeight(50)
#
#         # Disabling buttons
#         self.createBtn.setEnabled(False)
#         self.createBtn.setStyleSheet(
#             "QPushButton { background-color: rgba(18, 18, 18, 0.3); border-image: none; border: none; color: rgba(0,0,0,0.4); }")
#         self.loginBtn.setEnabled(False)
#         self.loginBtn.setStyleSheet(
#             "QPushButton { background-color: rgba(18, 18, 18, 0.3); border-image: none; border: none; color: rgba(0,0,0,0.4); }")


def closeConnectionToDB(self):
    '''
    This is used to close the connect to the database
    :return:
    '''

    # This is used to pass the close function on the connection if there isnt one
    global connect

    try:

        # This is used to pass the close function on the connection if there isnt one
        if connect is not None:
            connect.close()

            connect = None

            print("Connection closed.")

    except pyodbc.Error as e:
        pass

