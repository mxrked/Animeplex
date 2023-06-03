'''

    This is the User Hub Window

'''

from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtGui import QCursor

from frontend.assets.variables.arrays import *
from frontend.assets.classes.connection import db_connection

from backend.database.creating_data import create_anime_data
from backend.database.accessing_db import closeConnectionToDB
from backend.database.displaying_data import *


import sys, pyodbc



class UserHubWindow(QMainWindow):


    def __init__(self):
        super(UserHubWindow, self).__init__()

        uic.loadUi("frontend/ui/UserHubWindow.ui", self)


        # Define widgets
        # EX: self.testWidget = self.findChild(QLineEdit, "startWindow_TestLE")
        self.logoutBtn = self.findChild(QPushButton, "UserHubWindow_LogoutBtn")
        self.emailLabel = self.findChild(QLabel, "UserHubWindow_EmailLabel")
        self.viewAnimeBtn = self.findChild(QPushButton, "UserHubWindow_ViewAllAnimeBtn")
        self.watchedAnimeBtn = self.findChild(QPushButton, "UserHubWindow_ViewWatchedAnimeBtn")
        self.favoriteAnimeBtn = self.findChild(QPushButton, "UserHubWindow_ViewFavoritedAnimeBtn")

        # Define functions
        # EX: def doSomething():
        #       print("Test")

        def logout():
            '''
            This is used to logout the user
            :return:
            '''

            from frontend.windows import StartWindow

            current_user_based_on_ID.clear()

            closeConnectionToDB(self)

            startWindow = StartWindow.StartWindow()

            startWindow.move(self.pos())
            startWindow.show()

            self.hide()

        def openViewAnimeWindow():
            '''
            This is used to open the ViewAnimeWindow
            :return:
            '''


            from frontend.windows import ViewAnimeWindow

            connection = db_connection

            create_anime_data(self, connection)

            ViewAnimeWindow.UIWindow.emailLabel.setText(self.emailLabel.text()) # Setting the email label text

            ViewAnimeWindow.UIWindow.move(self.pos())
            ViewAnimeWindow.UIWindow.show()

            display_all_anime(self)

            self.hide()

        def openWatchedAnimeWindow():
            '''
            This is used to open the WatchedWindow
            :return:
            '''

            from frontend.windows import WatchedWindow

            WatchedWindow.UIWindow.move(self.pos())
            WatchedWindow.UIWindow.show()

            self.hide()

        def openFavoritedAnimeWindow():
            '''
            This is used to open the FavoritedWindow
            :return:
            '''

            from frontend.windows import FavoritedWindow

            FavoritedWindow.UIWindow.move(self.pos())
            FavoritedWindow.UIWindow.show()

            self.hide()

        def exitApp():
            '''
            This is used to close the app
            :return:
            '''
            closeConnectionToDB(self)
            sys.exit()



        # Apply functions to/style widgets
        self.logoutBtn.clicked.connect(logout)
        self.viewAnimeBtn.clicked.connect(openViewAnimeWindow)
        self.watchedAnimeBtn.clicked.connect(openWatchedAnimeWindow)
        self.favoriteAnimeBtn.clicked.connect(openFavoritedAnimeWindow)

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

        current_user_based_on_ID.clear()

        closeConnectionToDB(self)

        startWindow = StartWindow.StartWindow()

        startWindow.move(self.pos())
        startWindow.show()

        self.hide()




# initializing app
app = QApplication(sys.argv)
UIWindow = UserHubWindow()
app.exec_()
