'''

    This is used to store functions that return something

'''

from backend.database._queries import get_all_anime_names

def returnUserID(cursor, emailText, passwordText):
    '''
    This is used to return the primary key
    :param cursor: connection
    :param emailText: str
    :param passwordText: str
    :return: ID
    '''

    query = f"SELECT ID FROM Users WHERE User_Email = ? AND User_Password = ?"
    cursor.execute(query, (emailText, passwordText))

    row = cursor.fetchone()

    if row:

        id = row.ID
        print("The user ID: " + str(id))
        return id

    else:
        print("Could not get the ID")

def returnUserEmail(cursor, emailText, passwordText):
    '''
        This is used to return the email
        :param cursor: connection
        :param emailText: str
        :param passwordText: str
        :return: email
        '''

    query = f"SELECT ID FROM Users WHERE User_Email = ? AND User_Password = ?"
    cursor.execute(query, (emailText, passwordText))

    row = cursor.fetchone()

    if row:

        id = row.ID

        # Getting the email
        email_query = f"SELECT User_Email FROM Users WHERE ID = ?"
        cursor.execute(email_query, id)
        email_row = cursor.fetchone()

        if email_row:

            email = email_row.User_Email
            print("User's Email: " + email)

            return email

        else:

            print("Email not found for the primary key.")



    else:
        print("Could not get the ID")

def returnAnimeNames(cursor):
    '''
    This is used to return the anime names
    :param cursor: connections
    :return: anime_names
    '''

    cursor.execute(get_all_anime_names)
    rows = cursor.fetchall()

    anime_names = [row.Anime_Name for row in rows]

    return anime_names

def returnUserWatchedArray(cursor, userID):
    '''
        This is used to return the email
        :param cursor: connection
        :param userID: int
        :return: watched_array
        '''

    query = "SELECT User_Watched_Array FROM Users WHERE ID = ?"

    # Bind the ID value to the query parameters
    cursor.execute(query, userID)

    # Fetch the result
    result = cursor.fetchone()

    # Check if a result was found
    if result:
        user_watched_array = result[0]
        print(user_watched_array)

        return user_watched_array

    else:
        print(f"No entry found with ID {userID}")

def returnConvertedToArray(values):
    '''
    This is used to return a converted array
    :param values: str
    :return: converted_to_array
    '''

    if len(values) > 0:
        converted_to_array = values.split(", ")

        return converted_to_array