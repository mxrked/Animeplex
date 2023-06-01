'''

    This is used to store functions that return something

'''

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