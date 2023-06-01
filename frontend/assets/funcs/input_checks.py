'''

    This is used to store different input checking functions

'''

import re

def checkNoEmptyInputs(inputs):
    '''
    This function is used to check an array of inputs to make sure they are not empty or blank.
    :param inputs: array of inputs
    :return: False if any input is empty or blank, True otherwise
    '''

    for input in inputs:
        if input.text().strip() == "":
            return False

    return True

def checkNoSpaces(inputs):
    '''
    This function is used to check if there are any spaces in the values.
    :param inputs: array of inputs
    :return: False if there are spaces, True otherwise
    '''

    for input in inputs:
        text = input.text()
        if " " in text:
            return False

    return True

def checkMatchingPasswords(password1, password2):
    '''
    This is used to check if 2 password inputs match
    :param password1: str
    :param password2: str
    :return: False if they dont match, True otherwise
    '''

    if password1.text() == password2.text():
        return True
    else:
        return False

def checkValidEmail(emailText):
    '''
    This is used to check if the email is a valid one
    :param email: str
    :return: False if invalid, True otherwise
    '''

    regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    # Checking valid/invalid
    if re.match(regex, emailText):

        return True

    else:

        return False

def checkIfAccountExists(cursor, emailText):
    '''
    This is used to check if the account exists or not
    :param cursor: connection
    :param emailText: str
    :return: False if already exists, True otherwise
    '''

    query = "SELECT COUNT(*) FROM Users WHERE User_Email = ?"
    cursor.execute(query, (emailText))
    count = cursor.fetchone()[0] # This will check if there is an account already

    if count > 0:
        return False
    else:
        return True

def checkIfAccountExists_LOGIN(cursor, emailText, passwordText):
    '''
    This is used to check if the account exists or not (THIS IS FOR LOGIN)
    :param cursor: connection
    :param emailText: str
    :param passwordText: str
    :return: False if already exists, True otherwise
    '''

    query = "SELECT COUNT(*) FROM Users WHERE User_Email = ? AND User_Password = ?"
    cursor.execute(query, (emailText, passwordText))
    count = cursor.fetchone()[0] # This will check if there is an account already

    if count > 0:
        return False
    else:
        return True


