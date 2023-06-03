'''

    This is used to create the Anime table data

'''

from frontend.assets.classes.connection import db_connection

# from backend.database.accessing_db import connectToDB
from backend.database._queries import insert_new_anime

def create_anime_data(self, animeNames, connection):
    '''
    This is used to create anime table data
    :return:
    '''

    cursor = connection.cursor()

    watched = False
    favorited = False

    # Checking if there isnt any watched or favorited anime before creation
    check_watched_and_favorited = "SELECT COUNT(*) FROM Anime WHERE Anime_Watched = 1 OR Anime_Favorited = 1"
    cursor.execute(check_watched_and_favorited)
    check_result = cursor.fetchone()
    check_count = check_result[0] if check_result else 0

    if check_count > 0:

        print("Data creation prevented. There are items that are listed as watched or favorited.")

    else:

        # Adding the data

        for animeName in animeNames:

            try:

                insert_new_anime(self, animeName, watched, favorited)

            except Exception as e:
                print("Error retrieving indexes. Might be that there are no indexes.")


