'''

    This is used to store some functions that is used for displaying data from the database

'''

from backend.database.accessing_db import connectToDB
from backend.database._queries import *

def display_all_users(self):
    '''
    This is used to display all the current users to the console
    :param self: self
    :return:
    '''

    connection = connectToDB(self)
    cursor = connection.cursor()

    try:

        cursor.execute(get_all_users)
        entries = cursor.fetchall()
        connection.commit()

        print("All Current Users:")
        for entry in entries:
            print(entry)

    except Exception as e:
        print("Error retrieving indexes. Might be that there are no indexes.")

def display_all_anime(self):
    '''
    This is used to display all the different anime to the console
    :param self: self
    :return:
    '''

    connection = connectToDB(self)
    cursor = connection.cursor()

    try:

        cursor.execute(get_all_anime)
        entries = cursor.fetchall()
        connection.commit()

        print("All Anime:")
        for entry in entries:
            print(entry)

    except Exception as e:
        print("Error retrieving indexes. Might be that there are no indexes.")


