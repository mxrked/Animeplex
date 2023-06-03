'''

    This is used to store some queries that might be used

'''

#from backend.database.accessing_db import connectToDB
from frontend.assets.classes.connection import db_connection

import pyodbc


# Inserters
def insert_new_anime(self, animeName, animeWatched, animeFavorited):
    '''
    This is used to insert/create a anime entry for the Anime table
    :param self: self
    :param animeName: str
    :param animeWatched: boolean
    :param animeFavorited: boolean
    :return:
    '''

    # connection = connectToDB(self)

    connection = db_connection
    cursor = connection.cursor()

    # Preventing duplicate data
    check_current_anime = "SELECT COUNT(*) FROM Anime WHERE Anime_Name = ?"
    cursor.execute(check_current_anime, (animeName))
    check_count = cursor.fetchone()[0]

    if check_count > 0:
        print(f"Anime with name '{animeName}' already exists.")
        return

    # Inserting the new anime (IF THERE ISNT A DUPLICATE)
    insert_anime = "INSERT INTO Anime (Anime_Name, Anime_Watched, Anime_Favorited) VALUES (?, ?, ?)"
    cursor.execute(insert_anime, (animeName, animeWatched, animeFavorited))

    print(cursor)

    connection.commit()

    # cursor.close()
    # connection.close()


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