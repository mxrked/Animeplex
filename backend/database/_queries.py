'''

    This is used to store some queries that might be used

'''

from backend.database.accessing_db import connectToDB


import pyodbc


# Inserters
# def insert_new_user(self, userEmail, userPassword, userWatched, userFavorited):
#     '''
#     This is used to create/insert a new user
#     :param self: self
#     :param userEmail: str
#     :param userPassword: str
#     :param userWatched: array
#     :param userFavorited: array
#     :return:
#     '''
#
#     connection = connectToDB(self)
#     cursor = connection.cursor()
#
#     # Keeping the ID incremented correctly
#     cursor.execute("SELECT MAX(ID) FROM Users")
#     max_id = cursor.fetchone()[0]
#     new_id = max_id + 1 if max_id else 1
#
#     # Inserting the new user
#     insert_new_user = "INSERT INTO Users (ID, User_Email, User_Password, User_Watched_Array, User_Favorited_Array) VALUES (?, ?, ?, ?, ?)"
#     cursor.execute(insert_new_user, (new_id, userEmail, userPassword, userWatched, userFavorited))
#     connection.commit()
#
#     cursor.close()
#     connection.close()

# Removers
def remove_user(self, userEmail, userPassword):
    '''
    This is used to remove a user
    :param self: self
    :param userEmail: str
    :param userPassword: str
    :return:
    '''

    connection = connectToDB(self)
    cursor = connection.cursor()

    # Removing the user
    removing_user = "DELETE FROM Users WHERE User_Email = ? AND User_Password = ?"
    cursor.execute(removing_user, (userEmail, userPassword))
    connection.commit()

    cursor.close()
    connection.close()


# Getters
get_all_users = "SELECT * FROM Users"
get_all_emails = "SELECT User_Email FROM Users"
get_all_passwords = "SELECT User_Password FROM Users"
get_all_anime = "SELECT * FROM Anime"
get_all_anime_names = "SELECT Anime_Name FROM Anime"
get_all_anime_watched = "SELECT * FROM Anime WHERE Anime_Watched = 1"
get_all_anime_not_watched = "SELECT * FROM Anime WHERE Anime_Watched = 0"
get_all_anime_favorited = "SELECT * FROM Anime WHERE Anime_Favorited = 1"
get_all_anime_not_favorited = "SELECT * FROM Anime WHERE Anime_Favorited = 0"

def get_specific_user_array(userID, arrayName):
    '''
    This is used to return a specific user array
    :param userID: int
    :param arrayName: str
    :return: specific_array
    '''

    # Making sure the userID parameter is a int
    if not isinstance(userID, int):

        raise ValueError("userID must be an integer.")

    if isinstance(userID, int):

        validUserIDType = True


    # Making sure the arrayName parameter is a str
    if not isinstance(arrayName, str):

        raise ValueError("arrayName must be an str.")

    if isinstance(arrayName, str):

        validArrayNameType = True



    # Getting the array after valid type checks
    if validUserIDType and validArrayNameType:

        specific_array = "SELECT " + arrayName + " FROM Users WHERE ID = " + userID

        return  specific_array

