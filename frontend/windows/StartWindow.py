'''

    This is the Start Window

'''

from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtGui import QCursor

from frontend.assets.qrcs.StartWindow import top_bg
from frontend.assets.funcs.display_success_error_label import display_success_error_label
from frontend.assets.variables.arrays import active_connections

from backend.database.accessing_db import closeConnectionToDB
from backend.database.displaying_data import *


import sys, pyodbc, atexit



class StartWindow(QMainWindow):


    def __init__(self):
        super(StartWindow, self).__init__()

        uic.loadUi("frontend/ui/StartWindow.ui", self)


        # Define widgets
        # EX: self.testWidget = self.findChild(QLineEdit, "startWindow_TestLE")
        self.createBtn = self.findChild(QPushButton, "StartWindow_CreateBtn")
        self.loginBtn = self.findChild(QPushButton, "StartWindow_LoginBtn")
        self.exitBtn = self.findChild(QPushButton, "StartWindow_ExitBtn")
        self.infoBtn = self.findChild(QPushButton, "StartWindow_InfoBtn")
        self.bothDetectedLabel = self.findChild(QLabel, "startWindow_BothDetectedLabel")
        self.bothNotDetectedLabel = self.findChild(QLabel, "startWindow_BothNotFoundLabel")
        self.sSMSNotDetectedLabel = self.findChild(QLabel, "startWindow_SSMSNotFoundLabel")
        self.oDBCNotDetectedLabel = self.findChild(QLabel, "startWindow_ODBCNotFoundLabel")
        self.onlySSMSDriversFoundLabel = self.findChild(QLabel, "startWindow_OnlySSMSDriversFoundLabel")
        self.failedToConnectLabel = self.findChild(QLabel, "startWindow_FailedDBConnectLabel")

        self.bothDetectedLabel.hide()
        self.bothNotDetectedLabel.hide()
        self.sSMSNotDetectedLabel.hide()
        self.oDBCNotDetectedLabel.hide()
        self.onlySSMSDriversFoundLabel.hide()
        self.failedToConnectLabel.hide()

        # Define functions
        # EX: def doSomething():
        #       print("Test")

        def openAddUserWindow():
            '''
            This is used to open the AddUserWindow
            :return:
            '''

            from frontend.windows import AddUserWindow

            AddUserWindow.UIWindow.move(self.pos())
            AddUserWindow.UIWindow.show()

            self.hide()

        def openLoginWindow():
            '''
            This is used to open the AddUserWindow
            :return:
            '''

            from frontend.windows import LoginWindow

            LoginWindow.UIWindow.move(self.pos())
            LoginWindow.UIWindow.show()

            self.hide()

        def exitApp():
            '''
            This is used to close the app
            :return:
            '''

            atexit.register(cleanup_connections) # Making the function run ALWAYS when exiting

            #closeConnectionToDB(self)
            sys.exit()



        # Apply functions to/style widgets
        self.createBtn.clicked.connect(openAddUserWindow)
        self.loginBtn.clicked.connect(openLoginWindow)
        self.exitBtn.clicked.connect(exitApp)

        # Displaying result of program detection
        display_success_error_label(self)

        # Show the app
        self.show()


    def closeEvent(self, event):
        '''
        This is used to close the window on the red X
        :param event:
        :return:
        '''

        atexit.register(cleanup_connections)
        # closeConnectionToDB(self)
        sys.exit()


def cleanup_connections():
    '''
    This is used to close all connections
    :return:
    '''

    for connection in active_connections:
        connection.close()


# initializing app

def main():
    app = QApplication(sys.argv)
    UIWindow = StartWindow()
    UIWindow.show()
    app.exec_()
