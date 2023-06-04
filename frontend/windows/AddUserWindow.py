'''

    This is the Add User Window

'''

from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtGui import QCursor

from frontend.assets.classes.connection import db_connection
from frontend.assets.funcs.input_checks import *

from backend.database._queries import *
from backend.database.accessing_db import closeConnectionToDB
from backend.database.displaying_data import *


import sys, pyodbc



class AddUserWindow(QMainWindow):


    def __init__(self):
        super(AddUserWindow, self).__init__()

        uic.loadUi("frontend/ui/AddUserWindow.ui", self)


        # Define widgets
        # EX: self.testWidget = self.findChild(QLineEdit, "startWindow_TestLE")
        self.goBackBtn = self.findChild(QPushButton, "AddUserWindow_BackBtn")
        self.emailLE = self.findChild(QLineEdit, "AddUserWindow_EmailLineEdit")
        self.passwordLE = self.findChild(QLineEdit, "AddUserWindow_PasswordLineEdit")
        self.reEnterPasswordLE = self.findChild(QLineEdit, "AddUserWindow_ConfirmPasswordLineEdit")
        self.clearBtn = self.findChild(QPushButton, "AddUserWindow_ClearBtn")
        self.createBtn = self.findChild(QPushButton, "AddUserWindow_CreateBtn")
        self.invalidEmail = self.findChild(QLabel, "AddUserWindow_InvalidEmailLabel")
        self.passwordsDontMatch = self.findChild(QLabel, "AddUserWindow_PasswordsDontMatchLabel")
        self.spacesDetected = self.findChild(QLabel, "AddUserWindow_SpacesDetectedLabel")
        self.emptyInputs = self.findChild(QLabel, "AddUserWindow_EmptyInputsLabel")
        self.accountAlreadyExists = self.findChild(QLabel, "AddUserWindow_AccountAlreadyExistsLabel")
        self.success = self.findChild(QLabel, "AddUserWindow_SuccessLabel")

        # Define functions
        # EX: def doSomething():
        #       print("Test")

        def goBack():
            '''
            This is used to go back to the Start Window
            :return:
            '''

            from frontend.windows import StartWindow

            clearInputs()
            hideLabels()

            closeConnectionToDB(self)

            startWindow = StartWindow.StartWindow()

            startWindow.move(self.pos())
            startWindow.show()

            self.hide()

        def clearInputs():
            self.emailLE.setText(None)
            self.passwordLE.setText(None)
            self.reEnterPasswordLE.setText(None)

        def hideLabels():
            '''
            This is used to hide the labels
            :return:
            '''
            self.invalidEmail.setFixedHeight(0)
            self.passwordsDontMatch.setFixedHeight(0)
            self.spacesDetected.setFixedHeight(0)
            self.emptyInputs.setFixedHeight(0)
            self.accountAlreadyExists.setFixedHeight(0)
            self.success.setFixedHeight(0)

        def addUser():
            '''
            This is used to add a new user
            :return:
            '''

            connection = db_connection
            cursor = connection.cursor()

            emailText = self.emailLE.text()
            passwordText = self.passwordLE.text()

            watched_array = ""
            favorites_array = ""

            # Validation checks
            inputs = [self.emailLE, self.passwordLE, self.reEnterPasswordLE]
            noEmptys = checkNoEmptyInputs(inputs)
            noSpaces = checkNoSpaces(inputs)
            validEmail = checkValidEmail(emailText)
            passwordsMatch = checkMatchingPasswords(self.passwordLE, self.reEnterPasswordLE)
            accountNotInUse = checkIfAccountExists(cursor, emailText)

            if noEmptys:

                if noSpaces:

                    if validEmail:

                        if passwordsMatch:

                            if accountNotInUse:

                                # BINGO!!!

                                try:

                                    query = f"INSERT INTO Users (User_Email, User_Password, User_Watched_Array, User_Favorites_Array) VALUES (?, ?, ?, ?)"
                                    print(query)

                                    cursor.execute(query, (emailText, passwordText, watched_array, favorites_array))
                                    connection.commit()

                                    clearInputs()
                                    hideLabels()
                                    self.success.setFixedHeight(50)

                                except Exception as e:
                                    print("Error inserting data: " + str(e))


                            else:

                                hideLabels()
                                self.accountAlreadyExists.setFixedHeight(50)

                        else:

                            hideLabels()
                            self.passwordsDontMatch.setFixedHeight(50)

                    else:

                        hideLabels()
                        self.invalidEmail.setFixedHeight(50)

                else:

                    hideLabels()
                    self.spacesDetected.setFixedHeight(50)

            else:

                hideLabels()
                self.emptyInputs.setFixedHeight(50)

        def exitApp():
            '''
            This is used to close the app
            :return:
            '''
            closeConnectionToDB(self)
            sys.exit()



        # Apply functions to/style widgets
        self.goBackBtn.clicked.connect(goBack)
        self.clearBtn.clicked.connect(clearInputs)
        self.createBtn.clicked.connect(addUser)

        # Displaying result of program detection


        # Show the app
        self.show()



    def closeEvent(self, event):
        '''
        This is used to close the window on the red X
        :param event:
        :return:
        '''

        from frontend.windows import StartWindow

        closeConnectionToDB(self)

        startWindow = StartWindow.StartWindow()

        startWindow.move(self.pos())
        startWindow.show()

        self.hide()


# initializing app
app = QApplication(sys.argv)
UIWindow = AddUserWindow()
app.exec_()
