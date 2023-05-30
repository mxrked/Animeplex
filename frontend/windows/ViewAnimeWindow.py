'''

    This is the View Anime Window

'''

from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtGui import QCursor

from backend.database.accessing_db import closeConnectionToDB
from backend.database.displaying_data import *


import sys, pyodbc



class ViewAnimeWindow(QMainWindow):


    def __init__(self):
        super(ViewAnimeWindow, self).__init__()

        uic.loadUi("frontend/ui/ViewAnimeWindow.ui", self)


        # Define widgets
        # EX: self.testWidget = self.findChild(QLineEdit, "startWindow_TestLE")

        # Define functions
        # EX: def doSomething():
        #       print("Test")

        def exitApp():
            '''
            This is used to close the app
            :return:
            '''
            closeConnectionToDB(self)
            sys.exit()



        # Apply functions to/style widgets


        # Displaying result of program detection


        # Show the app
        self.show()



    def closeEvent(self, event):
        '''
        This is used to close the window on the red X
        :param event:
        :return:
        '''

        closeConnectionToDB(self)
        sys.exit()


# initializing app
app = QApplication(sys.argv)
UIWindow = ViewAnimeWindow()
app.exec_()
