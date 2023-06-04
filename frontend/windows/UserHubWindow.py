'''

    This is the User Hub Window

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtGui import QCursor

from frontend.assets.variables.arrays import *
from frontend.assets.classes.connection import db_connection
from frontend.assets.funcs.return_funcs import *

from backend.database._queries import *
from backend.database.creating_data import create_anime_data
from backend.database.accessing_db import closeConnectionToDB
from backend.database.displaying_data import *


import sys, pyodbc, functools, ast



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

            resetCheckboxes()
            resetItems()

            startWindow = StartWindow.StartWindow()

            startWindow.move(self.pos())
            startWindow.show()

            self.hide()

        def resetCheckboxes():
            '''
            This is used to reset the checkboxes
            :return:
            '''

            from frontend.windows import ViewAnimeWindow

            for widget in ViewAnimeWindow.UIWindow.animeFrameLayout.children():
                if isinstance(widget, QCheckBox):
                    widget.blockSignals(True)
                    widget.setChecked(False)
                    widget.blockSignals(False)


            # for checkbox in favorited_cbs:
            #     checkbox.blockSignals(True)
            #     checkbox.setChecked(False)
            #     checkbox.blockSignals(False)

        def resetItems():
            '''
            This is used to reset the anime items
            :return:
            '''

            from frontend.windows import ViewAnimeWindow

            layout = ViewAnimeWindow.UIWindow.animeFrameLayout  # Replace with your specific layout variable

            # Remove all widgets from the layout
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.setParent(None)
                    widget.deleteLater()
                else:
                    spacer = item.spacerItem()
                    if spacer:
                        layout.removeItem(spacer)
                    else:
                        layout.removeItem(item)

        def markAsWatched(state, animeName):
            '''
            This is used to mark the anime item as watched
            :param state:
            :return:
            '''

            if state == Qt.Checked:

                widget = app.sender()
                print(widget.property("watched_cb") + " marked as Watched.")

                update_anime_watched(self, animeName, 1)

                # FIX (<class 'pyodbc.ProgrammingError'>, ProgrammingError('42000', '[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]Column, parameter, or variable #1: Cannot find data type Demon Slayer. (2715) (SQLExecDirectW)'), <traceback object at 0x0000022B55886480>)
                checked_watched.append(animeName)

                converted_checked_watched = ', '.join(checked_watched)

                update_user_watched_array(self, current_user_based_on_ID[0], converted_checked_watched)


            else:

                widget = app.sender()
                print(widget.property("watched_cb") + " marked as Not Watched.")

                update_anime_watched(self, animeName, 0)

                checked_watched.append(animeName)
                checked_watched.remove(animeName)

                if len(checked_watched) <= 0:

                    update_user_watched_array(self, current_user_based_on_ID[0], "NULL")

                else:

                    update_user_watched_array(self, current_user_based_on_ID[0], checked_watched)



            # Printing all checked
            for checked in checked_watched:
                print(checked)

        # def markAsFavorited(state, animeName):
        #     '''
        #     This is used to mark the anime item as favorited
        #     :param state:
        #     :return:
        #     '''
        #
        #     if state == Qt.Checked:
        #
        #         widget = app.sender()
        #         print(widget.property("favorited_cb") + " marked as Favorited.")
        #
        #         update_anime_favorited(self, animeName, 1)
        #         checked_favorited.append(animeName)
        #
        #     else:
        #
        #         widget = app.sender()
        #         print(widget.property("favorited_cb") + " marked as Not Favorited.")
        #
        #         update_anime_favorited(self, animeName, 0)
        #         checked_favorited.remove(animeName)
        #
        #     # Printing all checked
        #     for checked in checked_favorited:
        #         print(checked)

        def openViewAnimeWindow():
            '''
            This is used to open the ViewAnimeWindow
            :return:
            '''

            from frontend.windows import ViewAnimeWindow

            connection = db_connection

            create_anime_data(self, connection)
            get_anime_names = returnAnimeNames(connection.cursor())
            get_user_watched = returnUserWatchedArray(connection.cursor(), current_user_based_on_ID[0]) # Gets all the checked item names

            print("User Watched: " + str(get_user_watched))
            # print(convert_user_watched_to_array)

            # Converting the return value into array
            converted_user_watched = returnConvertedToArray(get_user_watched)


            ViewAnimeWindow.UIWindow.emailLabel.setText(self.emailLabel.text()) # Setting the email label text

            # Adding the content to the frame
            for anime_name in get_anime_names:

                anime_item = QWidget()
                anime_item_layout = QHBoxLayout()
                anime_item_checkbox_layout = QHBoxLayout()

                anime_item.setLayout(anime_item_layout)

                label = QLabel(anime_name)
                empty_label_1 = QLabel()
                empty_label_2 = QLabel()
                watched_cb = QCheckBox("Watched:")
                favorite_cb = QCheckBox("Favorite:")

                label.setProperty("anime_name", anime_name)
                watched_cb.setProperty("watched_cb", anime_name)
                favorite_cb.setProperty("favorited_cb", anime_name)

                watched_cbs.append(watched_cb)
                favorited_cbs.append(favorite_cb)

                if len(get_user_watched) > 0:

                    for name in converted_user_watched:

                        if label.text() == name:
                            watched_cb.blockSignals(True)
                            watched_cb.setChecked(True)
                            watched_cb.blockSignals(False)

                            break

                # Making text be on left side and not the right
                watched_cb.setLayoutDirection(Qt.RightToLeft)
                favorite_cb.setLayoutDirection(Qt.RightToLeft)

                watched_cb.stateChanged.connect(lambda state, name=anime_name: markAsWatched(state, name))
                #favorite_cb.stateChanged.connect(lambda state, name=anime_name: markAsFavorited(state, name))

                anime_item_layout.addWidget(label)
                anime_item_layout.addStretch(1)  # Aligns the checkboxes to the right

                anime_item_checkbox_layout.addWidget(watched_cb)
                anime_item_checkbox_layout.addWidget(empty_label_1)
                anime_item_checkbox_layout.addWidget(empty_label_2)
                anime_item_checkbox_layout.addWidget(favorite_cb)
                anime_item_checkbox_layout.addSpacing(10)

                anime_item_layout.addLayout(anime_item_checkbox_layout)

                ViewAnimeWindow.UIWindow.animeFrameLayout.addWidget(anime_item)

                # ViewAnimeWindow.UIWindow.animeFrameLayout.addWidget(label)
                # ViewAnimeWindow.UIWindow.animeFrameLayout.addWidget(watched_cb)


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
