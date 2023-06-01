'''

    This is the Login Window

'''

from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtGui import QCursor

from frontend.assets.funcs.input_checks import *
from frontend.assets.funcs.return_funcs import *
from frontend.assets.variables.arrays import *

from backend.database.accessing_db import closeConnectionToDB
from backend.database.displaying_data import *


import sys, pyodbc



class LoginWindow(QMainWindow):


    def __init__(self):
        super(LoginWindow, self).__init__()

        uic.loadUi("frontend/ui/LoginWindow.ui", self)


        # Define widgets
        # EX: self.testWidget = self.findChild(QLineEdit, "startWindow_TestLE")
        self.backBtn = self.findChild(QPushButton, "LoginWindow_BackBtn")
        self.emailLE = self.findChild(QLineEdit, "LoginWindow_EmailLineEdit")
        self.passwordLE = self.findChild(QLineEdit, "LoginWindow_PasswordLineEdit")
        self.clearBtn = self.findChild(QPushButton, "LoginWindow_ClearBtn")
        self.loginBtn = self.findChild(QPushButton, "LoginWindow_LoginBtn")
        self.accountNotExist = self.findChild(QLabel, "LoginWindow_AccountDoesNotExistLabel")
        self.emptyInputs = self.findChild(QLabel, "LoginWindow_EmptyInputsLabel")
        self.spacesDetected = self.findChild(QLabel, "LoginWindow_SpacesDetectedLabel")

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

        def hideLabels():
            '''
            This is used to hide the labels
            :return:
            '''
            self.accountNotExist.setFixedHeight(0)
            self.spacesDetected.setFixedHeight(0)
            self.emptyInputs.setFixedHeight(0)

        def openUserHub():
            '''
            This is used to open the UserHubWindow
            :return:
            '''

            from frontend.windows import UserHubWindow

            UserHubWindow.UIWindow.move(self.pos())
            UserHubWindow.UIWindow.show()

            self.hide()

        def loginUser():
            '''
            This is used to login the user
            :return:
            '''

            connection = connectToDB(self)
            cursor = connection.cursor()

            emailText = self.emailLE.text()
            passwordText = self.passwordLE.text()

            # Validation checks
            inputs = [self.emailLE, self.passwordLE]
            noEmptys = checkNoEmptyInputs(inputs)
            noSpaces = checkNoSpaces(inputs)
            accountExists = checkIfAccountExists_LOGIN(cursor, emailText, passwordText)
            getID = returnUserID(cursor, emailText, passwordText)

            if noEmptys:

                if noSpaces:

                    if not accountExists:

                        from frontend.windows.UserHubWindow import UIWindow

                        # BINGO!!

                        print("Account exists!!")

                        print(getID)

                        # Adding the id of the current user to the current_user_based_on_ID array
                        current_user_based_on_ID.clear()
                        current_user_based_on_ID.append(getID)

                        hideLabels()
                        clearInputs()

                        userEmail = returnUserEmail(cursor, emailText, passwordText)
                        userID = returnUserID(cursor, emailText, passwordText)

                        UIWindow.emailLabel.setText("User: " + str(userEmail) + " - ID(" + str(userID) + ")")

                        openUserHub() # Opens the UserHubWindow

                    else:

                        hideLabels()
                        self.accountNotExist.setFixedHeight(50)

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
        self.backBtn.clicked.connect(goBack)
        self.clearBtn.clicked.connect(clearInputs)
        self.loginBtn.clicked.connect(loginUser)

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
UIWindow = LoginWindow()
app.exec_()
