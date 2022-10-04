# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SMSNtMDXU.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QCommandLinkButton, QFrame,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)
import icon_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1196, 809)
        MainWindow.setMinimumSize(QSize(1086, 687))
        icon = QIcon()
        icon.addFile(u"assets/imgs/logo2.jpg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.000000000000000)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, 0, 0)
        self.frame_2 = QFrame(self.tab)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:2, fx:0.499682, fy:0.5, stop:0.0568182 rgba(15, 19, 46, 255), stop:0.863636 rgba(255, 255, 255, 255));")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_2 = QTabWidget(self.frame_2)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.login = QWidget()
        self.login.setObjectName(u"login")
        self.frame_6 = QFrame(self.login)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(440, 60, 401, 541))
        self.frame_6.setStyleSheet(u"border-radius: 30px;\n"
"background-color: rgb(150, 125, 23);\n"
"")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_12 = QLabel(self.frame_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(90, 30, 211, 31))
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 26pt \"Poppins Black\";")
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_13 = QLabel(self.frame_6)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(80, 100, 261, 31))
        self.label_13.setStyleSheet(u"font: 900 12pt \"Poppins Black\";\n"
"color: rgb(255, 255, 255);")
        self.label_13.setAlignment(Qt.AlignCenter)
        self.login_username_2 = QLineEdit(self.frame_6)
        self.login_username_2.setObjectName(u"login_username_2")
        self.login_username_2.setGeometry(QRect(50, 220, 311, 41))
        self.login_username_2.setStyleSheet(u"background-color: rgb(208, 255, 232);\n"
"border-radius: 15px;\n"
"font: 14pt \"Rockwell\";")
        self.login_username_2.setAlignment(Qt.AlignCenter)
        self.login_password_2 = QLineEdit(self.frame_6)
        self.login_password_2.setObjectName(u"login_password_2")
        self.login_password_2.setGeometry(QRect(50, 310, 311, 41))
        self.login_password_2.setStyleSheet(u"background-color: rgb(208, 255, 232);\n"
"border-radius: 15px;\n"
"font: 14pt \"Rockwell\";")
        self.login_password_2.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.login_password_2.setEchoMode(QLineEdit.Password)
        self.login_password_2.setAlignment(Qt.AlignCenter)
        self.label_14 = QLabel(self.frame_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(70, 190, 111, 16))
        self.label_14.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.label_14.setAlignment(Qt.AlignCenter)
        self.label_15 = QLabel(self.frame_6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(60, 290, 111, 16))
        self.label_15.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.label_15.setAlignment(Qt.AlignCenter)
        self.bt_createAccount = QCommandLinkButton(self.frame_6)
        self.bt_createAccount.setObjectName(u"bt_createAccount")
        self.bt_createAccount.setGeometry(QRect(30, 450, 331, 41))
        self.bt_createAccount.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_createAccount.setStyleSheet(u"QPushButton{\n"
"	border-style: inset;\n"
"	border-top-right-radius: 20px;\n"
"	border-bottom-left-radius: 8px;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 900 12pt \"Poppins Black\";\n"
"}\n"
"QPushButton:pressed{\n"
"	background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffcd83, stop: 0.7 #fd8e43, stop: 1.0 #ff9826);\n"
"	border-bottom-right-radius: 30px;\n"
"	color: #dfe6ed;\n"
"}\n"
"\n"
"")
        self.bt_login = QPushButton(self.frame_6)
        self.bt_login.setObjectName(u"bt_login")
        self.bt_login.setGeometry(QRect(130, 370, 151, 60))
        self.bt_login.setMinimumSize(QSize(151, 60))
        self.bt_login.setMaximumSize(QSize(151, 60))
        self.bt_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_login.setStyleSheet(u"QPushButton{\n"
"	border-style: inset;\n"
"	border-top-right-radius: 20px;\n"
"	border-bottom-left-radius: 8px;\n"
"	color: rgb(40, 40, 40);\n"
"	background-color: rgb(0, 255, 0);\n"
"	font: 900 14pt \"Poppins Black\";\n"
"}\n"
"QPushButton:pressed{\n"
"	background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffcd83, stop: 0.7 #fd8e43, stop: 1.0 #ff9826);\n"
"	border-bottom-right-radius: 30px;\n"
"	color: #dfe6ed;\n"
"}\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/assets/buttons/layers.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_login.setIcon(icon1)
        self.bt_login.setIconSize(QSize(30, 30))
        self.frame_12 = QFrame(self.login)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(870, 80, 41, 41))
        self.frame_12.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.frame_13 = QFrame(self.login)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(940, 330, 41, 41))
        self.frame_13.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.label_16 = QLabel(self.login)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(0, 180, 451, 361))
        self.label_16.setStyleSheet(u"background-color: transparent;")
        self.label_16.setPixmap(QPixmap(u"assets/imgs/myLogo.jpg"))
        self.label_16.setScaledContents(True)
        self.tabWidget_2.addTab(self.login, "")
        self.frame_12.raise_()
        self.frame_13.raise_()
        self.label_16.raise_()
        self.frame_6.raise_()
        self.signup = QWidget()
        self.signup.setObjectName(u"signup")
        self.verticalLayout_11 = QVBoxLayout(self.signup)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.signup)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.frame_15 = QFrame(self.frame_9)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(450, 10, 401, 541))
        self.frame_15.setStyleSheet(u"border-radius: 30px;\n"
"background-color: rgb(150, 125, 23);")
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.label_17 = QLabel(self.frame_15)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(90, 20, 231, 31))
        self.label_17.setStyleSheet(u"font: 900 12pt \"Poppins Black\";\n"
"color: rgb(255, 255, 255);")
        self.label_17.setAlignment(Qt.AlignCenter)
        self.signup_username_2 = QLineEdit(self.frame_15)
        self.signup_username_2.setObjectName(u"signup_username_2")
        self.signup_username_2.setGeometry(QRect(50, 190, 311, 41))
        self.signup_username_2.setStyleSheet(u"background-color: rgb(208, 255, 232);\n"
"border-radius: 15px;\n"
"font: 14pt \"Rockwell\";")
        self.signup_username_2.setAlignment(Qt.AlignCenter)
        self.signup_password_2 = QLineEdit(self.frame_15)
        self.signup_password_2.setObjectName(u"signup_password_2")
        self.signup_password_2.setGeometry(QRect(50, 280, 311, 41))
        self.signup_password_2.setStyleSheet(u"background-color: rgb(208, 255, 232);\n"
"border-radius: 15px;\n"
"font: 14pt \"Rockwell\";")
        self.signup_password_2.setInputMethodHints(Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.signup_password_2.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.signup_password_2.setAlignment(Qt.AlignCenter)
        self.label_18 = QLabel(self.frame_15)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(50, 160, 111, 16))
        self.label_18.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.label_18.setAlignment(Qt.AlignCenter)
        self.label_19 = QLabel(self.frame_15)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(50, 250, 111, 16))
        self.label_19.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.label_19.setAlignment(Qt.AlignCenter)
        self.bt_back_2 = QCommandLinkButton(self.frame_15)
        self.bt_back_2.setObjectName(u"bt_back_2")
        self.bt_back_2.setGeometry(QRect(50, 490, 301, 41))
        self.bt_back_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_back_2.setStyleSheet(u"QPushButton{\n"
"	border-style: inset;\n"
"	border-top-right-radius: 20px;\n"
"	border-bottom-left-radius: 8px;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 900 12pt \"Poppins Black\";\n"
"}\n"
"QPushButton:pressed{\n"
"	background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffcd83, stop: 0.7 #fd8e43, stop: 1.0 #ff9826);\n"
"	border-bottom-right-radius: 30px;\n"
"	color: #dfe6ed;\n"
"}\n"
"\n"
"")
        self.bt_signup = QPushButton(self.frame_15)
        self.bt_signup.setObjectName(u"bt_signup")
        self.bt_signup.setGeometry(QRect(130, 430, 141, 51))
        self.bt_signup.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_signup.setStyleSheet(u"QPushButton{\n"
"	border-style: inset;\n"
"	border-top-right-radius: 20px;\n"
"	border-bottom-left-radius: 8px;\n"
"	color: rgb(40, 40, 40);\n"
"	background-color: rgb(0, 255, 0);\n"
"	font: 900 14pt \"Poppins Black\";\n"
"}\n"
"QPushButton:pressed{\n"
"	background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffcd83, stop: 0.7 #fd8e43, stop: 1.0 #ff9826);\n"
"	border-bottom-right-radius: 30px;\n"
"	color: #dfe6ed;\n"
"}\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/assets/buttons/log-in.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_signup.setIcon(icon2)
        self.bt_signup.setIconSize(QSize(30, 30))
        self.label_20 = QLabel(self.frame_15)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(50, 70, 111, 16))
        self.label_20.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.label_20.setAlignment(Qt.AlignCenter)
        self.signup_fullname_2 = QLineEdit(self.frame_15)
        self.signup_fullname_2.setObjectName(u"signup_fullname_2")
        self.signup_fullname_2.setGeometry(QRect(50, 100, 311, 41))
        self.signup_fullname_2.setStyleSheet(u"background-color: rgb(208, 255, 232);\n"
"border-radius: 15px;\n"
"font: 14pt \"Rockwell\";")
        self.signup_fullname_2.setAlignment(Qt.AlignCenter)
        self.label_21 = QLabel(self.frame_15)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(50, 340, 181, 16))
        self.label_21.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.label_21.setAlignment(Qt.AlignCenter)
        self.signup_comfirmpassword_2 = QLineEdit(self.frame_15)
        self.signup_comfirmpassword_2.setObjectName(u"signup_comfirmpassword_2")
        self.signup_comfirmpassword_2.setGeometry(QRect(50, 370, 311, 41))
        self.signup_comfirmpassword_2.setStyleSheet(u"background-color: rgb(208, 255, 232);\n"
"border-radius: 15px;\n"
"font: 14pt \"Rockwell\";")
        self.signup_comfirmpassword_2.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.signup_comfirmpassword_2.setEchoMode(QLineEdit.Password)
        self.signup_comfirmpassword_2.setAlignment(Qt.AlignCenter)
        self.label_22 = QLabel(self.frame_9)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(-30, 120, 501, 361))
        self.label_22.setStyleSheet(u"background-color: transparent;")
        self.label_22.setPixmap(QPixmap(u"assets/imgs/myLogo.jpg"))
        self.label_22.setScaledContents(True)
        self.label_22.raise_()
        self.frame_15.raise_()

        self.verticalLayout_11.addWidget(self.frame_9)

        self.tabWidget_2.addTab(self.signup, "")

        self.verticalLayout_6.addWidget(self.tabWidget_2)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.verticalLayout_3 = QVBoxLayout(self.tab_1)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.tab_1)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:2, fx:0.499682, fy:0.5, stop:0.0568182 rgba(15, 19, 46, 255), stop:0.863636 rgba(255, 255, 255, 255));")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(250, 0, 0, 100)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"background-color: transparent;\n"
"padding-right:250px;")
        self.label_5.setPixmap(QPixmap(u"assets/imgs/myLogo.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_5, 0, Qt.AlignHCenter)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(700, 300))
        self.frame_7.setStyleSheet(u"\n"
"\n"
"\n"
"background-color: transparent;\n"
"\n"
"")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 0, 0, 0)
        self.bt = QPushButton(self.frame_7)
        self.bt.setObjectName(u"bt")
        self.bt.setMinimumSize(QSize(200, 120))
        self.bt.setMaximumSize(QSize(500, 120))
        self.bt.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 97, 0);\n"
"}\n"
"QPushButton{\n"
"	border-style: inset;\n"
"	border-top-right-radius: 20px;\n"
"	border-bottom-left-radius: 8px;\n"
"	background-color: rgb(0, 255, 0);\n"
"	font: 800 19pt \"Poppins ExtraBold\";\n"
"	color: rgb(12, 12, 12);\n"
"}\n"
"QPushButton:pressed{\n"
"	background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffcd83, stop: 0.7 #fd8e43, stop: 1.0 #ff9826);\n"
"	border-bottom-right-radius: 30px;\n"
"	color: #dfe6ed;\n"
"}\n"
"\n"
"\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"assets/icons/ic_grid.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt.setIcon(icon3)
        self.bt.setIconSize(QSize(28, 28))

        self.horizontalLayout.addWidget(self.bt)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.bt_1 = QPushButton(self.frame_7)
        self.bt_1.setObjectName(u"bt_1")
        self.bt_1.setMinimumSize(QSize(200, 120))
        self.bt_1.setMaximumSize(QSize(500, 120))
        self.bt_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_1.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(121, 79, 0);\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-style: inset;\n"
"	border-top-right-radius: 20px;\n"
"	border-bottom-left-radius: 8px;\n"
"		background-color: rgb(185, 123, 0);\n"
"font: 800 16pt \"Poppins ExtraBold\";\n"
"	color: rgb(24, 24, 24);\n"
"}\n"
"QPushButton:pressed{\n"
"	background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffcd83, stop: 0.7 #fd8e43, stop: 1.0 #ff9826);\n"
"	border-bottom-right-radius: 30px;\n"
"	color: #dfe6ed;\n"
"}\n"
"\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"assets/icons/ic_grid_active.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_1.setIcon(icon4)
        self.bt_1.setIconSize(QSize(28, 28))

        self.horizontalLayout.addWidget(self.bt_1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.bt_2 = QPushButton(self.frame_7)
        self.bt_2.setObjectName(u"bt_2")
        self.bt_2.setMinimumSize(QSize(200, 120))
        self.bt_2.setMaximumSize(QSize(500, 120))
        self.bt_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_2.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(129, 129, 195);\n"
"}\n"
"QPushButton{\n"
"	border-style: inset;\n"
"	border-top-right-radius: 20px;\n"
"	border-bottom-left-radius: 8px;\n"
"	background-color: rgb(68, 68, 102);\n"
"font: 800 16pt \"Poppins ExtraBold\";\n"
"	color: rgb(13, 13, 13);\n"
"}\n"
"QPushButton:pressed{\n"
"	background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffcd83, stop: 0.7 #fd8e43, stop: 1.0 #ff9826);\n"
"	border-bottom-right-radius: 30px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.bt_2.setIcon(icon3)
        self.bt_2.setIconSize(QSize(28, 28))

        self.horizontalLayout.addWidget(self.bt_2)


        self.verticalLayout_4.addWidget(self.frame_7)


        self.verticalLayout_3.addWidget(self.frame)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_77 = QVBoxLayout(self.tab_2)
        self.verticalLayout_77.setSpacing(0)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.verticalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.frame_143 = QFrame(self.tab_2)
        self.frame_143.setObjectName(u"frame_143")
        self.frame_143.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:2, fx:0.499682, fy:0.5, stop:0.0568182 rgba(15, 19, 46, 255), stop:0.863636 rgba(255, 255, 255, 255));")
        self.frame_143.setFrameShape(QFrame.NoFrame)
        self.frame_143.setFrameShadow(QFrame.Raised)
        self.verticalLayout_78 = QVBoxLayout(self.frame_143)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.verticalLayout_78.setContentsMargins(130, 0, 130, 100)
        self.label_4 = QLabel(self.frame_143)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background-color: transparent;")
        self.label_4.setPixmap(QPixmap(u"assets/imgs/myLogo.jpg"))
        self.label_4.setScaledContents(True)

        self.verticalLayout_78.addWidget(self.label_4)

        self.frame_144 = QFrame(self.frame_143)
        self.frame_144.setObjectName(u"frame_144")
        self.frame_144.setMinimumSize(QSize(120, 120))
        self.frame_144.setMaximumSize(QSize(650, 300))
        self.frame_144.setStyleSheet(u"background-color: transparent;")
        self.frame_144.setFrameShape(QFrame.NoFrame)
        self.frame_144.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_144)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, -1, -1)
        self.frame_145 = QFrame(self.frame_144)
        self.frame_145.setObjectName(u"frame_145")
        self.frame_145.setStyleSheet(u"background-color: transparent;")
        self.frame_145.setFrameShape(QFrame.NoFrame)
        self.frame_145.setFrameShadow(QFrame.Raised)
        self.verticalLayout_80 = QVBoxLayout(self.frame_145)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.bt_3 = QPushButton(self.frame_145)
        self.bt_3.setObjectName(u"bt_3")
        self.bt_3.setMinimumSize(QSize(200, 120))
        self.bt_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_3.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(153, 129, 74);\n"
"}\n"
"QPushButton{\n"
"	border-style: inset;\n"
"	border-top-right-radius: 60px;\n"
"	border-bottom-left-radius: 8px;\n"
"	color: rgb(40, 40, 40);\n"
"	background-color: rgb(195, 165, 94);\n"
"	font: 900 14pt \"Poppins Black\";\n"
"}\n"
"QPushButton:pressed{\n"
"	background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffcd83, stop: 0.7 #fd8e43, stop: 1.0 #ff9826);\n"
"	border-bottom-right-radius: 30px;\n"
"	color: #dfe6ed;\n"
"}\n"
"\n"
"")
        icon5 = QIcon()
        icon5.addFile(u"assets/imgs/student.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_3.setIcon(icon5)
        self.bt_3.setIconSize(QSize(50, 50))

        self.verticalLayout_80.addWidget(self.bt_3)


        self.horizontalLayout_32.addWidget(self.frame_145)

        self.horizontalSpacer_3 = QSpacerItem(120, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_3)

        self.frame_147 = QFrame(self.frame_144)
        self.frame_147.setObjectName(u"frame_147")
        self.frame_147.setMinimumSize(QSize(300, 0))
        self.frame_147.setMaximumSize(QSize(150, 16777215))
        self.frame_147.setStyleSheet(u"background-color: transparent;")
        self.frame_147.setFrameShape(QFrame.StyledPanel)
        self.frame_147.setFrameShadow(QFrame.Raised)
        self.verticalLayout_81 = QVBoxLayout(self.frame_147)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.bt_4 = QPushButton(self.frame_147)
        self.bt_4.setObjectName(u"bt_4")
        self.bt_4.setMinimumSize(QSize(200, 120))
        self.bt_4.setMaximumSize(QSize(300, 120))
        self.bt_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_4.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(9, 35, 118);\n"
"}\n"
"QPushButton{\n"
"	border-style: inset;\n"
"	border-top-right-radius: 60px;\n"
"	border-bottom-left-radius: 8px;\n"
"	color: rgb(40, 40, 40);\n"
"	background-color: rgb(0, 85, 255);\n"
"	font: 900 14pt \"Poppins Black\";\n"
"}\n"
"QPushButton:pressed{\n"
"	background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffcd83, stop: 0.7 #fd8e43, stop: 1.0 #ff9826);\n"
"	border-bottom-right-radius: 30px;\n"
"	color: #dfe6ed;\n"
"}\n"
"\n"
"")
        icon6 = QIcon()
        icon6.addFile(u"assets/icons/ic_people-lg.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_4.setIcon(icon6)
        self.bt_4.setIconSize(QSize(40, 40))

        self.verticalLayout_81.addWidget(self.bt_4)


        self.horizontalLayout_32.addWidget(self.frame_147)

        self.horizontalLayout_32.setStretch(0, 1)
        self.horizontalLayout_32.setStretch(1, 4)
        self.horizontalLayout_32.setStretch(2, 5)

        self.verticalLayout_78.addWidget(self.frame_144, 0, Qt.AlignHCenter)


        self.verticalLayout_77.addWidget(self.frame_143)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_52 = QWidget()
        self.tab_52.setObjectName(u"tab_52")
        self.verticalLayout_153 = QVBoxLayout(self.tab_52)
        self.verticalLayout_153.setObjectName(u"verticalLayout_153")
        self.frame_186 = QFrame(self.tab_52)
        self.frame_186.setObjectName(u"frame_186")
        self.frame_186.setStyleSheet(u"QFrame {\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:2, fx:0.499682, fy:0.5, stop:0.0568182 rgba(15, 19, 46, 255), stop:0.863636 rgba(255, 255, 255, 255));\n"
"	border-radius: 60px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(255, 170, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(36, 36, 36);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(161, 107, 80);\n"
"	border-bottom-left-radius: 8px;\n"
"	\n"
"}\n"
"QLabel{\n"
"	background-color: transparent;\n"
"	color: rgb(255, 255, 255);\n"
""
                        "	font: 900 20pt \"Roboto Black\";\n"
"}\n"
"")
        self.frame_186.setFrameShape(QFrame.NoFrame)
        self.frame_186.setFrameShadow(QFrame.Raised)
        self.label_45 = QLabel(self.frame_186)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(390, 50, 391, 321))
        self.label_45.setStyleSheet(u"")
        self.label_45.setPixmap(QPixmap(u"assets/imgs/myLogo.jpg"))
        self.label_45.setScaledContents(True)
        self.label_46 = QLabel(self.frame_186)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(290, 370, 611, 41))
        self.label_47 = QLabel(self.frame_186)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(480, 450, 191, 41))
        self.label_48 = QLabel(self.frame_186)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(330, 490, 501, 41))
        self.bt_113 = QPushButton(self.frame_186)
        self.bt_113.setObjectName(u"bt_113")
        self.bt_113.setGeometry(QRect(474, 583, 201, 51))
        self.bt_113.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/assets/buttons/codesandbox.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_113.setIcon(icon7)
        self.bt_113.setIconSize(QSize(28, 28))

        self.verticalLayout_153.addWidget(self.frame_186)

        self.tabWidget.addTab(self.tab_52, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_5 = QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.tab_3)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_3 = QTabWidget(self.frame_3)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tabWidget_3.setStyleSheet(u"background-color: rgb(108, 170, 144);")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_8 = QVBoxLayout(self.tab_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_5 = QFrame(self.tab_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_5)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 20pt \"Poppins Black\";")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label)

        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u"assets/imgs/EmpClass.jpg"))
        self.label_2.setScaledContents(True)

        self.verticalLayout_9.addWidget(self.label_2)


        self.verticalLayout_8.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.tab_4)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QPushButton {\n"
"	border-top-left-radius: 15px;\n"
"	background-color: rgb(213, 156, 53);\n"
"	font: 700 11pt \"Segoe UI\";\n"
"	color: rgb(48, 48, 48);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffd495, stop: 0.7 #ffad76, stop: 1.0 #ffb665);\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_4)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.bt_5 = QPushButton(self.frame_4)
        self.bt_5.setObjectName(u"bt_5")
        self.bt_5.setMinimumSize(QSize(120, 30))
        self.bt_5.setMaximumSize(QSize(120, 120))
        self.bt_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_5.setIcon(icon7)
        self.bt_5.setIconSize(QSize(30, 30))

        self.verticalLayout_10.addWidget(self.bt_5, 0, Qt.AlignHCenter)


        self.verticalLayout_8.addWidget(self.frame_4)

        self.verticalLayout_8.setStretch(0, 8)
        self.verticalLayout_8.setStretch(1, 2)
        self.tabWidget_3.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.horizontalLayout_2 = QHBoxLayout(self.tab_5)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.tab_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_10)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.frame_10)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(163, 82, 0);\n"
"}\n"
"QPushButton {\n"
"border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_14)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_187 = QFrame(self.frame_14)
        self.frame_187.setObjectName(u"frame_187")
        self.frame_187.setMaximumSize(QSize(200, 195))
        self.frame_187.setFrameShape(QFrame.StyledPanel)
        self.frame_187.setFrameShadow(QFrame.Raised)
        self.verticalLayout_154 = QVBoxLayout(self.frame_187)
        self.verticalLayout_154.setSpacing(0)
        self.verticalLayout_154.setObjectName(u"verticalLayout_154")
        self.verticalLayout_154.setContentsMargins(0, 0, 0, 0)
        self.frame_188 = QFrame(self.frame_187)
        self.frame_188.setObjectName(u"frame_188")
        self.frame_188.setFrameShape(QFrame.StyledPanel)
        self.frame_188.setFrameShadow(QFrame.Raised)
        self.label_55 = QLabel(self.frame_188)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(0, 0, 181, 20))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(11)
        font.setBold(True)
        self.label_55.setFont(font)
        self.label_58 = QLabel(self.frame_188)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setGeometry(QRect(8, 10, 181, 51))
        self.label_58.setStyleSheet(u"color: rgb(255, 62, 23);\n"
"background-color:transparent;\n"
"font: 900 14pt \"Poppins Black\";")
        self.label_58.setAlignment(Qt.AlignCenter)

        self.verticalLayout_154.addWidget(self.frame_188)

        self.frame_189 = QFrame(self.frame_187)
        self.frame_189.setObjectName(u"frame_189")
        self.frame_189.setFrameShape(QFrame.StyledPanel)
        self.frame_189.setFrameShadow(QFrame.Raised)
        self.label_56 = QLabel(self.frame_189)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(0, 0, 181, 20))
        self.label_56.setFont(font)
        self.label_59 = QLabel(self.frame_189)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setGeometry(QRect(0, 10, 191, 51))
        self.label_59.setStyleSheet(u"color: rgb(255, 62, 23);\n"
"background-color:transparent;\n"
"font: 900 14pt \"Poppins Black\";")
        self.label_59.setAlignment(Qt.AlignCenter)

        self.verticalLayout_154.addWidget(self.frame_189)

        self.frame_190 = QFrame(self.frame_187)
        self.frame_190.setObjectName(u"frame_190")
        self.frame_190.setFrameShape(QFrame.StyledPanel)
        self.frame_190.setFrameShadow(QFrame.Raised)
        self.label_57 = QLabel(self.frame_190)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(0, 0, 181, 20))
        self.label_57.setFont(font)
        self.label_60 = QLabel(self.frame_190)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setGeometry(QRect(-2, 10, 201, 51))
        self.label_60.setStyleSheet(u"color: rgb(255, 62, 23);\n"
"background-color:transparent;\n"
"font: 900 14pt \"Poppins Black\";")
        self.label_60.setAlignment(Qt.AlignCenter)

        self.verticalLayout_154.addWidget(self.frame_190)


        self.verticalLayout_13.addWidget(self.frame_187)

        self.line_12 = QFrame(self.frame_14)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_13.addWidget(self.line_12)

        self.bt_6 = QPushButton(self.frame_14)
        self.bt_6.setObjectName(u"bt_6")
        self.bt_6.setMaximumSize(QSize(200, 40))
        self.bt_6.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icons/assets/buttons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_6.setIcon(icon8)
        self.bt_6.setIconSize(QSize(28, 30))

        self.verticalLayout_13.addWidget(self.bt_6)

        self.line = QFrame(self.frame_14)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_13.addWidget(self.line)

        self.bt_7 = QPushButton(self.frame_14)
        self.bt_7.setObjectName(u"bt_7")
        self.bt_7.setMaximumSize(QSize(200, 40))
        self.bt_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_7.setStyleSheet(u"padding-right: 20px;")
        icon9 = QIcon()
        icon9.addFile(u":/icons/assets/buttons/users.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_7.setIcon(icon9)
        self.bt_7.setIconSize(QSize(28, 30))

        self.verticalLayout_13.addWidget(self.bt_7)

        self.line_2 = QFrame(self.frame_14)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_13.addWidget(self.line_2)

        self.bt_8 = QPushButton(self.frame_14)
        self.bt_8.setObjectName(u"bt_8")
        self.bt_8.setMaximumSize(QSize(200, 40))
        self.bt_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_8.setStyleSheet(u"padding-right: 30px;")
        icon10 = QIcon()
        icon10.addFile(u":/icons/assets/buttons/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_8.setIcon(icon10)
        self.bt_8.setIconSize(QSize(28, 30))

        self.verticalLayout_13.addWidget(self.bt_8)

        self.line_3 = QFrame(self.frame_14)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_13.addWidget(self.line_3)

        self.bt_12 = QPushButton(self.frame_14)
        self.bt_12.setObjectName(u"bt_12")
        self.bt_12.setMaximumSize(QSize(200, 40))
        self.bt_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_12.setStyleSheet(u"padding-right: 58px;")
        icon11 = QIcon()
        icon11.addFile(u":/icons/assets/buttons/check-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_12.setIcon(icon11)
        self.bt_12.setIconSize(QSize(28, 30))

        self.verticalLayout_13.addWidget(self.bt_12)

        self.line_4 = QFrame(self.frame_14)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_13.addWidget(self.line_4)

        self.bt_9 = QPushButton(self.frame_14)
        self.bt_9.setObjectName(u"bt_9")
        self.bt_9.setMaximumSize(QSize(200, 40))
        self.bt_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_9.setStyleSheet(u"padding-right: 20px;")
        icon12 = QIcon()
        icon12.addFile(u":/icons/assets/buttons/book.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_9.setIcon(icon12)
        self.bt_9.setIconSize(QSize(28, 30))

        self.verticalLayout_13.addWidget(self.bt_9)

        self.line_5 = QFrame(self.frame_14)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_13.addWidget(self.line_5)

        self.bt_11 = QPushButton(self.frame_14)
        self.bt_11.setObjectName(u"bt_11")
        self.bt_11.setMaximumSize(QSize(200, 40))
        self.bt_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_11.setStyleSheet(u"padding-right:49px;")
        icon13 = QIcon()
        icon13.addFile(u":/icons/assets/buttons/clipboard.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_11.setIcon(icon13)
        self.bt_11.setIconSize(QSize(28, 30))

        self.verticalLayout_13.addWidget(self.bt_11)

        self.line_6 = QFrame(self.frame_14)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_13.addWidget(self.line_6)

        self.bt_10 = QPushButton(self.frame_14)
        self.bt_10.setObjectName(u"bt_10")
        self.bt_10.setMaximumSize(QSize(200, 40))
        self.bt_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_10.setStyleSheet(u"padding-right: 69px;")
        icon14 = QIcon()
        icon14.addFile(u":/icons/assets/buttons/mail.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_10.setIcon(icon14)
        self.bt_10.setIconSize(QSize(28, 30))

        self.verticalLayout_13.addWidget(self.bt_10)

        self.line_30 = QFrame(self.frame_14)
        self.line_30.setObjectName(u"line_30")
        self.line_30.setFrameShape(QFrame.HLine)
        self.line_30.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_13.addWidget(self.line_30)

        self.pushButton_17 = QPushButton(self.frame_14)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_17.setStyleSheet(u"padding-right: 80px;")
        icon15 = QIcon()
        icon15.addFile(u":/icons/assets/buttons/bar-chart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_17.setIcon(icon15)
        self.pushButton_17.setIconSize(QSize(28, 30))

        self.verticalLayout_13.addWidget(self.pushButton_17)

        self.line_31 = QFrame(self.frame_14)
        self.line_31.setObjectName(u"line_31")
        self.line_31.setFrameShape(QFrame.HLine)
        self.line_31.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_13.addWidget(self.line_31)

        self.pushButton_15 = QPushButton(self.frame_14)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMaximumSize(QSize(200, 40))
        self.pushButton_15.setCursor(QCursor(Qt.OpenHandCursor))
        self.pushButton_15.setStyleSheet(u"padding-right: 120px;")
        icon16 = QIcon()
        icon16.addFile(u":/icons/assets/buttons/chevrons-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_15.setIcon(icon16)
        self.pushButton_15.setIconSize(QSize(28, 28))

        self.verticalLayout_13.addWidget(self.pushButton_15)

        self.line_7 = QFrame(self.frame_14)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_13.addWidget(self.line_7)


        self.verticalLayout_12.addWidget(self.frame_14)


        self.horizontalLayout_3.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_8)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_11)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_4 = QTabWidget(self.frame_11)
        self.tabWidget_4.setObjectName(u"tabWidget_4")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.horizontalLayout_4 = QHBoxLayout(self.tab_6)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.tab_6)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_16)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.groupBox = QGroupBox(self.frame_16)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QComboBox{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QDateEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 900 12pt \"Roboto Black\";\n"
"}")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 30, 161, 31))
        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(190, 30, 171, 31))
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 150, 111, 31))
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 190, 101, 31))
        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(130, 190, 171, 31))
        self.comboBox_2 = QComboBox(self.groupBox)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(130, 230, 171, 31))
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 230, 101, 31))
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 280, 121, 31))
        self.textEdit = QTextEdit(self.groupBox)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(143, 270, 141, 71))
        self.lineEdit_20 = QLineEdit(self.groupBox)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setGeometry(QRect(130, 150, 171, 31))
        self.lineEdit_20.setClearButtonEnabled(True)
        self.lineEdit_9 = QLineEdit(self.groupBox)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(130, 110, 171, 31))
        self.lineEdit_9.setClearButtonEnabled(True)
        self.label_26 = QLabel(self.groupBox)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(30, 110, 91, 31))

        self.verticalLayout_15.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.frame_16)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QComboBox{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QDateEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 900 12pt \"Roboto Black\";\n"
"}")
        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 80, 131, 31))
        self.lineEdit_4 = QLineEdit(self.groupBox_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(170, 40, 191, 31))
        self.lineEdit_4.setClearButtonEnabled(True)
        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 40, 141, 31))
        self.lineEdit_5 = QLineEdit(self.groupBox_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(170, 80, 191, 31))
        self.lineEdit_5.setClearButtonEnabled(True)
        self.label_23 = QLabel(self.groupBox_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(20, 120, 131, 31))
        self.lineEdit_6 = QLineEdit(self.groupBox_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(170, 120, 191, 31))
        self.lineEdit_6.setClearButtonEnabled(True)

        self.verticalLayout_15.addWidget(self.groupBox_2)

        self.frame_18 = QFrame(self.frame_16)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(158, 158, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(255, 255, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_19)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.bt_13 = QPushButton(self.frame_19)
        self.bt_13.setObjectName(u"bt_13")
        self.bt_13.setMinimumSize(QSize(0, 40))
        self.bt_13.setMaximumSize(QSize(120, 60))
        icon17 = QIcon()
        icon17.addFile(u":/icons/assets/buttons/folder-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_13.setIcon(icon17)
        self.bt_13.setIconSize(QSize(20, 20))

        self.verticalLayout_16.addWidget(self.bt_13)


        self.horizontalLayout_5.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.frame_18)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_20)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.bt_14 = QPushButton(self.frame_20)
        self.bt_14.setObjectName(u"bt_14")
        self.bt_14.setMinimumSize(QSize(0, 40))
        self.bt_14.setMaximumSize(QSize(120, 60))
        icon18 = QIcon()
        icon18.addFile(u":/icons/assets/buttons/database.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_14.setIcon(icon18)
        self.bt_14.setIconSize(QSize(20, 20))

        self.verticalLayout_17.addWidget(self.bt_14)


        self.horizontalLayout_5.addWidget(self.frame_20)


        self.verticalLayout_15.addWidget(self.frame_18)

        self.verticalLayout_15.setStretch(0, 6)
        self.verticalLayout_15.setStretch(1, 3)
        self.verticalLayout_15.setStretch(2, 1)

        self.horizontalLayout_4.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.tab_6)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_17)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.tableWidget = QTableWidget(self.frame_17)
        if (self.tableWidget.columnCount() < 9):
            self.tableWidget.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"background-color: rgb(191, 191, 191);")

        self.verticalLayout_18.addWidget(self.tableWidget)


        self.horizontalLayout_4.addWidget(self.frame_17)

        self.horizontalLayout_4.setStretch(0, 5)
        self.horizontalLayout_4.setStretch(1, 4)
        self.tabWidget_4.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.horizontalLayout_7 = QHBoxLayout(self.tab_7)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.tab_7)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_21)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.groupBox_3 = QGroupBox(self.frame_21)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QComboBox{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QDateEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 900 12pt \"Roboto Black\";\n"
"}")
        self.label_24 = QLabel(self.groupBox_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(20, 30, 161, 31))
        self.lineEdit_7 = QLineEdit(self.groupBox_3)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(190, 30, 171, 31))
        self.lineEdit_7.setFrame(True)
        self.lineEdit_7.setClearButtonEnabled(True)
        self.label_25 = QLabel(self.groupBox_3)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(30, 100, 91, 31))
        self.lineEdit_8 = QLineEdit(self.groupBox_3)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(130, 100, 171, 31))
        self.lineEdit_8.setClearButtonEnabled(True)
        self.label_27 = QLabel(self.groupBox_3)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(20, 150, 111, 31))
        self.label_28 = QLabel(self.groupBox_3)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(20, 190, 101, 31))
        self.comboBox_4 = QComboBox(self.groupBox_3)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setGeometry(QRect(130, 230, 171, 31))
        self.label_29 = QLabel(self.groupBox_3)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(20, 230, 101, 31))
        self.label_30 = QLabel(self.groupBox_3)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(20, 280, 121, 31))
        self.textEdit_2 = QTextEdit(self.groupBox_3)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(143, 270, 141, 71))
        self.comboBox_3 = QComboBox(self.groupBox_3)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(130, 190, 171, 31))
        self.lineEdit_19 = QLineEdit(self.groupBox_3)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setGeometry(QRect(130, 150, 171, 31))
        self.lineEdit_19.setClearButtonEnabled(True)

        self.verticalLayout_19.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.frame_21)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QComboBox{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QDateEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 900 12pt \"Roboto Black\";\n"
"}")
        self.label_31 = QLabel(self.groupBox_4)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(20, 80, 131, 31))
        self.lineEdit_10 = QLineEdit(self.groupBox_4)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setGeometry(QRect(170, 40, 191, 31))
        self.lineEdit_10.setClearButtonEnabled(True)
        self.label_32 = QLabel(self.groupBox_4)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(20, 40, 141, 31))
        self.lineEdit_11 = QLineEdit(self.groupBox_4)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setGeometry(QRect(170, 80, 191, 31))
        self.lineEdit_11.setClearButtonEnabled(True)
        self.label_33 = QLabel(self.groupBox_4)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(20, 120, 131, 31))
        self.lineEdit_12 = QLineEdit(self.groupBox_4)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setGeometry(QRect(170, 120, 191, 31))
        self.lineEdit_12.setClearButtonEnabled(True)

        self.verticalLayout_19.addWidget(self.groupBox_4)

        self.frame_22 = QFrame(self.frame_21)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(158, 158, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(255, 255, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_23 = QFrame(self.frame_22)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_23)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.bt_15 = QPushButton(self.frame_23)
        self.bt_15.setObjectName(u"bt_15")
        self.bt_15.setMinimumSize(QSize(0, 40))
        self.bt_15.setMaximumSize(QSize(120, 60))
        self.bt_15.setCursor(QCursor(Qt.PointingHandCursor))
        icon19 = QIcon()
        icon19.addFile(u":/icons/assets/buttons/upload-cloud.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_15.setIcon(icon19)
        self.bt_15.setIconSize(QSize(20, 20))

        self.verticalLayout_20.addWidget(self.bt_15)


        self.horizontalLayout_6.addWidget(self.frame_23)

        self.frame_26 = QFrame(self.frame_22)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_26)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.bt_17 = QPushButton(self.frame_26)
        self.bt_17.setObjectName(u"bt_17")
        self.bt_17.setMinimumSize(QSize(0, 40))
        self.bt_17.setMaximumSize(QSize(120, 60))
        self.bt_17.setCursor(QCursor(Qt.PointingHandCursor))
        icon20 = QIcon()
        icon20.addFile(u":/icons/assets/buttons/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_17.setIcon(icon20)
        self.bt_17.setIconSize(QSize(28, 28))

        self.verticalLayout_23.addWidget(self.bt_17)


        self.horizontalLayout_6.addWidget(self.frame_26)

        self.frame_24 = QFrame(self.frame_22)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_24)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.bt_16 = QPushButton(self.frame_24)
        self.bt_16.setObjectName(u"bt_16")
        self.bt_16.setMinimumSize(QSize(0, 40))
        self.bt_16.setMaximumSize(QSize(120, 60))
        self.bt_16.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_16.setIcon(icon18)
        self.bt_16.setIconSize(QSize(20, 20))

        self.verticalLayout_21.addWidget(self.bt_16)


        self.horizontalLayout_6.addWidget(self.frame_24)


        self.verticalLayout_19.addWidget(self.frame_22)

        self.verticalLayout_19.setStretch(0, 6)
        self.verticalLayout_19.setStretch(1, 3)
        self.verticalLayout_19.setStretch(2, 1)

        self.horizontalLayout_7.addWidget(self.frame_21)

        self.frame_25 = QFrame(self.tab_7)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_25)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_27 = QFrame(self.frame_25)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(11, 153, 146);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(19, 255, 247);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 12pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_27.setFrameShape(QFrame.NoFrame)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_8.setSpacing(1)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.bt_29 = QPushButton(self.frame_27)
        self.bt_29.setObjectName(u"bt_29")
        self.bt_29.setMinimumSize(QSize(10, 40))
        self.bt_29.setMaximumSize(QSize(120, 30))
        self.bt_29.setCursor(QCursor(Qt.PointingHandCursor))
        icon21 = QIcon()
        icon21.addFile(u":/icons/assets/buttons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_29.setIcon(icon21)
        self.bt_29.setIconSize(QSize(28, 28))

        self.horizontalLayout_8.addWidget(self.bt_29)

        self.lineEdit_13 = QLineEdit(self.frame_27)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setMaximumSize(QSize(190, 30))
        self.lineEdit_13.setClearButtonEnabled(True)

        self.horizontalLayout_8.addWidget(self.lineEdit_13)


        self.verticalLayout_22.addWidget(self.frame_27)

        self.tableWidget_2 = QTableWidget(self.frame_25)
        if (self.tableWidget_2.columnCount() < 9):
            self.tableWidget_2.setColumnCount(9)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, __qtablewidgetitem17)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setStyleSheet(u"background-color: rgb(191, 191, 191);")

        self.verticalLayout_22.addWidget(self.tableWidget_2)

        self.verticalLayout_22.setStretch(0, 1)
        self.verticalLayout_22.setStretch(1, 9)

        self.horizontalLayout_7.addWidget(self.frame_25)

        self.horizontalLayout_7.setStretch(0, 7)
        self.horizontalLayout_7.setStretch(1, 5)
        self.tabWidget_4.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.horizontalLayout_9 = QHBoxLayout(self.tab_8)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_28 = QFrame(self.tab_8)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_28)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, -1, 0)
        self.groupBox_5 = QGroupBox(self.frame_28)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QComboBox{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QDateEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 900 12pt \"Roboto Black\";\n"
"}")
        self.label_34 = QLabel(self.groupBox_5)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(30, 100, 101, 31))
        self.label_35 = QLabel(self.groupBox_5)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(30, 150, 101, 31))
        self.lineEdit_14 = QLineEdit(self.groupBox_5)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setGeometry(QRect(140, 100, 171, 31))
        self.lineEdit_14.setClearButtonEnabled(True)
        self.comboBox_5 = QComboBox(self.groupBox_5)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setGeometry(QRect(140, 150, 171, 31))
        self.label_36 = QLabel(self.groupBox_5)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(30, 50, 161, 31))
        self.lineEdit_15 = QLineEdit(self.groupBox_5)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setGeometry(QRect(210, 50, 171, 31))
        self.lineEdit_15.setClearButtonEnabled(True)
        self.comboBox_6 = QComboBox(self.groupBox_5)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setGeometry(QRect(140, 200, 171, 31))
        self.label_37 = QLabel(self.groupBox_5)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(30, 200, 101, 31))
        self.comboBox_7 = QComboBox(self.groupBox_5)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setGeometry(QRect(140, 250, 171, 31))
        self.label_38 = QLabel(self.groupBox_5)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(30, 250, 101, 31))
        self.comboBox_8 = QComboBox(self.groupBox_5)
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.setObjectName(u"comboBox_8")
        self.comboBox_8.setGeometry(QRect(140, 300, 171, 31))
        self.label_39 = QLabel(self.groupBox_5)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(30, 300, 101, 31))
        self.label_40 = QLabel(self.groupBox_5)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(30, 350, 101, 31))
        self.lineEdit_26 = QLineEdit(self.groupBox_5)
        self.lineEdit_26.setObjectName(u"lineEdit_26")
        self.lineEdit_26.setGeometry(QRect(140, 350, 171, 31))
        self.lineEdit_26.setClearButtonEnabled(True)
        self.label_53 = QLabel(self.groupBox_5)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(30, 400, 101, 31))
        self.lineEdit_28 = QLineEdit(self.groupBox_5)
        self.lineEdit_28.setObjectName(u"lineEdit_28")
        self.lineEdit_28.setGeometry(QRect(140, 450, 171, 31))
        self.lineEdit_28.setClearButtonEnabled(True)
        self.label_54 = QLabel(self.groupBox_5)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(30, 450, 101, 31))
        self.comboBox_28 = QComboBox(self.groupBox_5)
        self.comboBox_28.addItem("")
        self.comboBox_28.addItem("")
        self.comboBox_28.addItem("")
        self.comboBox_28.addItem("")
        self.comboBox_28.addItem("")
        self.comboBox_28.addItem("")
        self.comboBox_28.addItem("")
        self.comboBox_28.addItem("")
        self.comboBox_28.addItem("")
        self.comboBox_28.setObjectName(u"comboBox_28")
        self.comboBox_28.setGeometry(QRect(140, 400, 171, 31))

        self.verticalLayout_24.addWidget(self.groupBox_5)

        self.frame_30 = QFrame(self.frame_28)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"	background-color: rgb(158, 158, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(255, 255, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_34 = QFrame(self.frame_30)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_34)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.bt_18 = QPushButton(self.frame_34)
        self.bt_18.setObjectName(u"bt_18")
        self.bt_18.setMaximumSize(QSize(120, 30))
        self.bt_18.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_18.setIcon(icon17)
        self.bt_18.setIconSize(QSize(20, 20))

        self.verticalLayout_25.addWidget(self.bt_18)


        self.horizontalLayout_10.addWidget(self.frame_34)

        self.frame_31 = QFrame(self.frame_30)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_31)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.bt_19 = QPushButton(self.frame_31)
        self.bt_19.setObjectName(u"bt_19")
        self.bt_19.setMaximumSize(QSize(120, 30))
        self.bt_19.setCursor(QCursor(Qt.PointingHandCursor))
        icon22 = QIcon()
        icon22.addFile(u":/icons/assets/buttons/edit-3.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_19.setIcon(icon22)
        self.bt_19.setIconSize(QSize(20, 20))

        self.verticalLayout_26.addWidget(self.bt_19)


        self.horizontalLayout_10.addWidget(self.frame_31)

        self.frame_32 = QFrame(self.frame_30)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_32)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.bt_20 = QPushButton(self.frame_32)
        self.bt_20.setObjectName(u"bt_20")
        self.bt_20.setMaximumSize(QSize(120, 30))
        self.bt_20.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_20.setIcon(icon20)
        self.bt_20.setIconSize(QSize(20, 20))

        self.verticalLayout_27.addWidget(self.bt_20)


        self.horizontalLayout_10.addWidget(self.frame_32)

        self.frame_33 = QFrame(self.frame_30)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_33)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.bt_21 = QPushButton(self.frame_33)
        self.bt_21.setObjectName(u"bt_21")
        self.bt_21.setMaximumSize(QSize(120, 30))
        self.bt_21.setCursor(QCursor(Qt.PointingHandCursor))
        icon23 = QIcon()
        icon23.addFile(u":/icons/assets/buttons/book-open.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_21.setIcon(icon23)
        self.bt_21.setIconSize(QSize(20, 20))

        self.verticalLayout_28.addWidget(self.bt_21)


        self.horizontalLayout_10.addWidget(self.frame_33)


        self.verticalLayout_24.addWidget(self.frame_30)

        self.verticalLayout_24.setStretch(0, 8)
        self.verticalLayout_24.setStretch(1, 2)

        self.horizontalLayout_9.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.tab_8)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_29)
        self.verticalLayout_29.setSpacing(1)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_35 = QFrame(self.frame_29)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(11, 153, 146);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(19, 255, 247);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 12pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_35.setFrameShape(QFrame.NoFrame)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_11.setSpacing(1)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.bt_30 = QPushButton(self.frame_35)
        self.bt_30.setObjectName(u"bt_30")
        self.bt_30.setMinimumSize(QSize(10, 40))
        self.bt_30.setMaximumSize(QSize(120, 30))
        self.bt_30.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_30.setIcon(icon21)
        self.bt_30.setIconSize(QSize(28, 28))

        self.horizontalLayout_11.addWidget(self.bt_30)

        self.lineEdit_16 = QLineEdit(self.frame_35)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setMaximumSize(QSize(190, 30))
        self.lineEdit_16.setClearButtonEnabled(True)

        self.horizontalLayout_11.addWidget(self.lineEdit_16)


        self.verticalLayout_29.addWidget(self.frame_35)

        self.tableWidget_3 = QTableWidget(self.frame_29)
        if (self.tableWidget_3.columnCount() < 9):
            self.tableWidget_3.setColumnCount(9)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(6, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(7, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(8, __qtablewidgetitem26)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setStyleSheet(u"background-color: rgb(191, 191, 191);")

        self.verticalLayout_29.addWidget(self.tableWidget_3)

        self.verticalLayout_29.setStretch(0, 1)
        self.verticalLayout_29.setStretch(1, 8)

        self.horizontalLayout_9.addWidget(self.frame_29)

        self.horizontalLayout_9.setStretch(0, 5)
        self.horizontalLayout_9.setStretch(1, 5)
        self.tabWidget_4.addTab(self.tab_8, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.horizontalLayout_12 = QHBoxLayout(self.tab_9)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_36 = QFrame(self.tab_9)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_36)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.groupBox_6 = QGroupBox(self.frame_36)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QComboBox{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QDateEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 900 12pt \"Roboto Black\";\n"
"}")
        self.label_41 = QLabel(self.groupBox_6)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(20, 100, 161, 31))
        self.label_42 = QLabel(self.groupBox_6)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(30, 180, 101, 31))
        self.lineEdit_17 = QLineEdit(self.groupBox_6)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setGeometry(QRect(210, 100, 171, 31))
        self.lineEdit_17.setClearButtonEnabled(True)
        self.comboBox_9 = QComboBox(self.groupBox_6)
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.setObjectName(u"comboBox_9")
        self.comboBox_9.setGeometry(QRect(180, 240, 171, 31))
        self.label_43 = QLabel(self.groupBox_6)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(60, 240, 101, 31))
        self.lineEdit_18 = QLineEdit(self.groupBox_6)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setGeometry(QRect(180, 180, 171, 31))
        self.lineEdit_18.setClearButtonEnabled(True)
        self.label_44 = QLabel(self.groupBox_6)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(60, 300, 101, 31))
        self.lineEdit_21 = QLineEdit(self.groupBox_6)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setGeometry(QRect(180, 300, 171, 31))
        self.lineEdit_21.setClearButtonEnabled(True)

        self.verticalLayout_31.addWidget(self.groupBox_6)

        self.frame_38 = QFrame(self.frame_36)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(158, 158, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(255, 255, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_39 = QFrame(self.frame_38)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_39)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.bt_22 = QPushButton(self.frame_39)
        self.bt_22.setObjectName(u"bt_22")
        self.bt_22.setMaximumSize(QSize(120, 30))
        self.bt_22.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_22.setIcon(icon17)
        self.bt_22.setIconSize(QSize(20, 20))

        self.verticalLayout_32.addWidget(self.bt_22)


        self.horizontalLayout_13.addWidget(self.frame_39)

        self.frame_41 = QFrame(self.frame_38)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_41)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.bt_24 = QPushButton(self.frame_41)
        self.bt_24.setObjectName(u"bt_24")
        self.bt_24.setMaximumSize(QSize(120, 30))
        self.bt_24.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_24.setIcon(icon22)
        self.bt_24.setIconSize(QSize(20, 20))

        self.verticalLayout_34.addWidget(self.bt_24)


        self.horizontalLayout_13.addWidget(self.frame_41)

        self.frame_42 = QFrame(self.frame_38)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_42)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.bt_25 = QPushButton(self.frame_42)
        self.bt_25.setObjectName(u"bt_25")
        self.bt_25.setMaximumSize(QSize(120, 30))
        self.bt_25.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_25.setIcon(icon20)
        self.bt_25.setIconSize(QSize(20, 20))

        self.verticalLayout_35.addWidget(self.bt_25)


        self.horizontalLayout_13.addWidget(self.frame_42)

        self.frame_40 = QFrame(self.frame_38)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_40)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.bt_23 = QPushButton(self.frame_40)
        self.bt_23.setObjectName(u"bt_23")
        self.bt_23.setMaximumSize(QSize(120, 30))
        self.bt_23.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_23.setIcon(icon23)
        self.bt_23.setIconSize(QSize(20, 20))

        self.verticalLayout_33.addWidget(self.bt_23)


        self.horizontalLayout_13.addWidget(self.frame_40)


        self.verticalLayout_31.addWidget(self.frame_38)

        self.verticalLayout_31.setStretch(0, 8)
        self.verticalLayout_31.setStretch(1, 1)

        self.horizontalLayout_12.addWidget(self.frame_36)

        self.frame_37 = QFrame(self.tab_9)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_37)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.tableWidget_4 = QTableWidget(self.frame_37)
        if (self.tableWidget_4.columnCount() < 4):
            self.tableWidget_4.setColumnCount(4)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, __qtablewidgetitem30)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setStyleSheet(u"background-color: rgb(191, 191, 191);")

        self.verticalLayout_30.addWidget(self.tableWidget_4)


        self.horizontalLayout_12.addWidget(self.frame_37)

        self.horizontalLayout_12.setStretch(0, 5)
        self.horizontalLayout_12.setStretch(1, 5)
        self.tabWidget_4.addTab(self.tab_9, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.horizontalLayout_14 = QHBoxLayout(self.tab_10)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_43 = QFrame(self.tab_10)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_43)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_36.addItem(self.verticalSpacer_2)

        self.frame_45 = QFrame(self.frame_43)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"}\n"
"QPushButton {\n"
"	background-color: transparent;\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(36, 36, 36);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(161, 107, 80);\n"
"	border-bottom-left-radius: 8px;\n"
"	\n"
"}\n"
"")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_45)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.line_10 = QFrame(self.frame_45)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_37.addWidget(self.line_10)

        self.bt_26 = QPushButton(self.frame_45)
        self.bt_26.setObjectName(u"bt_26")
        self.bt_26.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_37.addWidget(self.bt_26)

        self.line_9 = QFrame(self.frame_45)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_37.addWidget(self.line_9)

        self.bt_27 = QPushButton(self.frame_45)
        self.bt_27.setObjectName(u"bt_27")
        self.bt_27.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_37.addWidget(self.bt_27)

        self.line_8 = QFrame(self.frame_45)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_37.addWidget(self.line_8)

        self.bt_28 = QPushButton(self.frame_45)
        self.bt_28.setObjectName(u"bt_28")
        self.bt_28.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_37.addWidget(self.bt_28)

        self.line_11 = QFrame(self.frame_45)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_37.addWidget(self.line_11)


        self.verticalLayout_36.addWidget(self.frame_45)

        self.verticalSpacer = QSpacerItem(20, 89, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_36.addItem(self.verticalSpacer)

        self.verticalLayout_36.setStretch(0, 1)
        self.verticalLayout_36.setStretch(1, 5)
        self.verticalLayout_36.setStretch(2, 1)

        self.horizontalLayout_14.addWidget(self.frame_43)

        self.frame_44 = QFrame(self.tab_10)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_44)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_5 = QTabWidget(self.frame_44)
        self.tabWidget_5.setObjectName(u"tabWidget_5")
        self.tabWidget_5.setCursor(QCursor(Qt.ArrowCursor))
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.horizontalLayout_15 = QHBoxLayout(self.tab_11)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_47 = QFrame(self.tab_11)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_143 = QVBoxLayout(self.frame_47)
        self.verticalLayout_143.setObjectName(u"verticalLayout_143")
        self.groupBox_38 = QGroupBox(self.frame_47)
        self.groupBox_38.setObjectName(u"groupBox_38")
        self.groupBox_38.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QComboBox{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QDateEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 900 12pt \"Roboto Black\";\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 148, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(0, 213, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.label_258 = QLabel(self.groupBox_38)
        self.label_258.setObjectName(u"label_258")
        self.label_258.setGeometry(QRect(40, 320, 101, 31))
        self.comboBox_68 = QComboBox(self.groupBox_38)
        self.comboBox_68.addItem("")
        self.comboBox_68.addItem("")
        self.comboBox_68.addItem("")
        self.comboBox_68.setObjectName(u"comboBox_68")
        self.comboBox_68.setGeometry(QRect(400, 210, 141, 31))
        self.label_259 = QLabel(self.groupBox_38)
        self.label_259.setObjectName(u"label_259")
        self.label_259.setGeometry(QRect(340, 210, 61, 31))
        self.label_260 = QLabel(self.groupBox_38)
        self.label_260.setObjectName(u"label_260")
        self.label_260.setGeometry(QRect(70, 380, 51, 31))
        self.lineEdit_128 = QLineEdit(self.groupBox_38)
        self.lineEdit_128.setObjectName(u"lineEdit_128")
        self.lineEdit_128.setGeometry(QRect(140, 320, 161, 31))
        self.lineEdit_128.setClearButtonEnabled(True)
        self.lineEdit_129 = QLineEdit(self.groupBox_38)
        self.lineEdit_129.setObjectName(u"lineEdit_129")
        self.lineEdit_129.setGeometry(QRect(140, 160, 161, 31))
        self.lineEdit_129.setClearButtonEnabled(True)
        self.label_261 = QLabel(self.groupBox_38)
        self.label_261.setObjectName(u"label_261")
        self.label_261.setGeometry(QRect(30, 160, 111, 31))
        self.label_262 = QLabel(self.groupBox_38)
        self.label_262.setObjectName(u"label_262")
        self.label_262.setGeometry(QRect(340, 160, 131, 31))
        self.lineEdit_130 = QLineEdit(self.groupBox_38)
        self.lineEdit_130.setObjectName(u"lineEdit_130")
        self.lineEdit_130.setGeometry(QRect(480, 160, 151, 31))
        self.lineEdit_130.setClearButtonEnabled(True)
        self.label_263 = QLabel(self.groupBox_38)
        self.label_263.setObjectName(u"label_263")
        self.label_263.setGeometry(QRect(20, 220, 121, 31))
        self.lineEdit_131 = QLineEdit(self.groupBox_38)
        self.lineEdit_131.setObjectName(u"lineEdit_131")
        self.lineEdit_131.setGeometry(QRect(140, 210, 161, 31))
        self.lineEdit_131.setClearButtonEnabled(True)
        self.label_549 = QLabel(self.groupBox_38)
        self.label_549.setObjectName(u"label_549")
        self.label_549.setGeometry(QRect(30, 440, 101, 31))
        self.label_550 = QLabel(self.groupBox_38)
        self.label_550.setObjectName(u"label_550")
        self.label_550.setGeometry(QRect(180, 40, 381, 31))
        self.pushButton_9 = QPushButton(self.groupBox_38)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(430, 560, 81, 31))
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_9.setIcon(icon18)
        self.pushButton_9.setIconSize(QSize(28, 28))
        self.comboBox_10 = QComboBox(self.groupBox_38)
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.setObjectName(u"comboBox_10")
        self.comboBox_10.setGeometry(QRect(140, 380, 171, 31))
        self.comboBox_11 = QComboBox(self.groupBox_38)
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.setObjectName(u"comboBox_11")
        self.comboBox_11.setGeometry(QRect(140, 440, 171, 31))
        self.lineEdit_158 = QLineEdit(self.groupBox_38)
        self.lineEdit_158.setObjectName(u"lineEdit_158")
        self.lineEdit_158.setGeometry(QRect(150, 500, 161, 31))
        self.lineEdit_158.setClearButtonEnabled(True)
        self.label_1322 = QLabel(self.groupBox_38)
        self.label_1322.setObjectName(u"label_1322")
        self.label_1322.setGeometry(QRect(10, 500, 141, 31))
        self.label_1329 = QLabel(self.groupBox_38)
        self.label_1329.setObjectName(u"label_1329")
        self.label_1329.setGeometry(QRect(340, 380, 101, 31))
        self.lineEdit_165 = QLineEdit(self.groupBox_38)
        self.lineEdit_165.setObjectName(u"lineEdit_165")
        self.lineEdit_165.setGeometry(QRect(460, 380, 191, 31))
        self.lineEdit_165.setClearButtonEnabled(True)
        self.label_1330 = QLabel(self.groupBox_38)
        self.label_1330.setObjectName(u"label_1330")
        self.label_1330.setGeometry(QRect(350, 440, 141, 31))
        self.lineEdit_166 = QLineEdit(self.groupBox_38)
        self.lineEdit_166.setObjectName(u"lineEdit_166")
        self.lineEdit_166.setGeometry(QRect(490, 440, 191, 31))
        self.lineEdit_166.setClearButtonEnabled(True)
        self.label_1347 = QLabel(self.groupBox_38)
        self.label_1347.setObjectName(u"label_1347")
        self.label_1347.setGeometry(QRect(380, 320, 51, 31))
        self.lineEdit_183 = QLineEdit(self.groupBox_38)
        self.lineEdit_183.setObjectName(u"lineEdit_183")
        self.lineEdit_183.setGeometry(QRect(450, 320, 191, 31))
        self.lineEdit_183.setClearButtonEnabled(True)

        self.verticalLayout_143.addWidget(self.groupBox_38)


        self.horizontalLayout_15.addWidget(self.frame_47)

        self.tabWidget_5.addTab(self.tab_11, "")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.horizontalLayout_16 = QHBoxLayout(self.tab_12)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_48 = QFrame(self.tab_12)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_142 = QVBoxLayout(self.frame_48)
        self.verticalLayout_142.setObjectName(u"verticalLayout_142")
        self.groupBox_37 = QGroupBox(self.frame_48)
        self.groupBox_37.setObjectName(u"groupBox_37")
        self.groupBox_37.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QComboBox{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QDateEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 900 12pt \"Roboto Black\";\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 148, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(0, 213, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.label_252 = QLabel(self.groupBox_37)
        self.label_252.setObjectName(u"label_252")
        self.label_252.setGeometry(QRect(40, 320, 101, 31))
        self.comboBox_65 = QComboBox(self.groupBox_37)
        self.comboBox_65.addItem("")
        self.comboBox_65.addItem("")
        self.comboBox_65.addItem("")
        self.comboBox_65.setObjectName(u"comboBox_65")
        self.comboBox_65.setGeometry(QRect(400, 210, 141, 31))
        self.label_253 = QLabel(self.groupBox_37)
        self.label_253.setObjectName(u"label_253")
        self.label_253.setGeometry(QRect(340, 210, 61, 31))
        self.label_254 = QLabel(self.groupBox_37)
        self.label_254.setObjectName(u"label_254")
        self.label_254.setGeometry(QRect(70, 380, 51, 31))
        self.lineEdit_124 = QLineEdit(self.groupBox_37)
        self.lineEdit_124.setObjectName(u"lineEdit_124")
        self.lineEdit_124.setGeometry(QRect(140, 320, 161, 31))
        self.lineEdit_124.setClearButtonEnabled(True)
        self.lineEdit_125 = QLineEdit(self.groupBox_37)
        self.lineEdit_125.setObjectName(u"lineEdit_125")
        self.lineEdit_125.setGeometry(QRect(140, 160, 161, 31))
        self.lineEdit_125.setClearButtonEnabled(True)
        self.label_255 = QLabel(self.groupBox_37)
        self.label_255.setObjectName(u"label_255")
        self.label_255.setGeometry(QRect(30, 160, 111, 31))
        self.label_256 = QLabel(self.groupBox_37)
        self.label_256.setObjectName(u"label_256")
        self.label_256.setGeometry(QRect(340, 160, 131, 31))
        self.lineEdit_126 = QLineEdit(self.groupBox_37)
        self.lineEdit_126.setObjectName(u"lineEdit_126")
        self.lineEdit_126.setGeometry(QRect(480, 160, 151, 31))
        self.lineEdit_126.setClearButtonEnabled(True)
        self.label_257 = QLabel(self.groupBox_37)
        self.label_257.setObjectName(u"label_257")
        self.label_257.setGeometry(QRect(20, 220, 121, 31))
        self.lineEdit_127 = QLineEdit(self.groupBox_37)
        self.lineEdit_127.setObjectName(u"lineEdit_127")
        self.lineEdit_127.setGeometry(QRect(140, 210, 161, 31))
        self.lineEdit_127.setClearButtonEnabled(True)
        self.label_547 = QLabel(self.groupBox_37)
        self.label_547.setObjectName(u"label_547")
        self.label_547.setGeometry(QRect(30, 440, 101, 31))
        self.label_548 = QLabel(self.groupBox_37)
        self.label_548.setObjectName(u"label_548")
        self.label_548.setGeometry(QRect(180, 40, 381, 31))
        self.pushButton_8 = QPushButton(self.groupBox_37)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(410, 510, 81, 31))
        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_8.setIcon(icon18)
        self.pushButton_8.setIconSize(QSize(28, 28))
        self.comboBox_12 = QComboBox(self.groupBox_37)
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.setObjectName(u"comboBox_12")
        self.comboBox_12.setGeometry(QRect(140, 380, 171, 31))
        self.comboBox_13 = QComboBox(self.groupBox_37)
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.setObjectName(u"comboBox_13")
        self.comboBox_13.setGeometry(QRect(140, 440, 171, 31))
        self.lineEdit_156 = QLineEdit(self.groupBox_37)
        self.lineEdit_156.setObjectName(u"lineEdit_156")
        self.lineEdit_156.setGeometry(QRect(170, 500, 161, 31))
        self.lineEdit_156.setClearButtonEnabled(True)
        self.label_1319 = QLabel(self.groupBox_37)
        self.label_1319.setObjectName(u"label_1319")
        self.label_1319.setGeometry(QRect(40, 730, 101, 31))
        self.label_1320 = QLabel(self.groupBox_37)
        self.label_1320.setObjectName(u"label_1320")
        self.label_1320.setGeometry(QRect(30, 500, 141, 31))
        self.label_1331 = QLabel(self.groupBox_37)
        self.label_1331.setObjectName(u"label_1331")
        self.label_1331.setGeometry(QRect(350, 380, 101, 31))
        self.lineEdit_167 = QLineEdit(self.groupBox_37)
        self.lineEdit_167.setObjectName(u"lineEdit_167")
        self.lineEdit_167.setGeometry(QRect(470, 380, 191, 31))
        self.lineEdit_167.setClearButtonEnabled(True)
        self.lineEdit_168 = QLineEdit(self.groupBox_37)
        self.lineEdit_168.setObjectName(u"lineEdit_168")
        self.lineEdit_168.setGeometry(QRect(500, 440, 191, 31))
        self.lineEdit_168.setClearButtonEnabled(True)
        self.label_1332 = QLabel(self.groupBox_37)
        self.label_1332.setObjectName(u"label_1332")
        self.label_1332.setGeometry(QRect(360, 440, 141, 31))
        self.label_1348 = QLabel(self.groupBox_37)
        self.label_1348.setObjectName(u"label_1348")
        self.label_1348.setGeometry(QRect(380, 320, 51, 31))
        self.lineEdit_184 = QLineEdit(self.groupBox_37)
        self.lineEdit_184.setObjectName(u"lineEdit_184")
        self.lineEdit_184.setGeometry(QRect(450, 320, 191, 31))
        self.lineEdit_184.setClearButtonEnabled(True)

        self.verticalLayout_142.addWidget(self.groupBox_37)


        self.horizontalLayout_16.addWidget(self.frame_48)

        self.tabWidget_5.addTab(self.tab_12, "")
        self.tab_13 = QWidget()
        self.tab_13.setObjectName(u"tab_13")
        self.horizontalLayout_17 = QHBoxLayout(self.tab_13)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_49 = QFrame(self.tab_13)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.verticalLayout_141 = QVBoxLayout(self.frame_49)
        self.verticalLayout_141.setObjectName(u"verticalLayout_141")
        self.groupBox_36 = QGroupBox(self.frame_49)
        self.groupBox_36.setObjectName(u"groupBox_36")
        self.groupBox_36.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QComboBox{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QDateEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 900 12pt \"Roboto Black\";\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 148, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(0, 213, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.label_246 = QLabel(self.groupBox_36)
        self.label_246.setObjectName(u"label_246")
        self.label_246.setGeometry(QRect(40, 320, 101, 31))
        self.comboBox_62 = QComboBox(self.groupBox_36)
        self.comboBox_62.addItem("")
        self.comboBox_62.addItem("")
        self.comboBox_62.addItem("")
        self.comboBox_62.setObjectName(u"comboBox_62")
        self.comboBox_62.setGeometry(QRect(400, 210, 141, 31))
        self.label_247 = QLabel(self.groupBox_36)
        self.label_247.setObjectName(u"label_247")
        self.label_247.setGeometry(QRect(340, 210, 61, 31))
        self.label_248 = QLabel(self.groupBox_36)
        self.label_248.setObjectName(u"label_248")
        self.label_248.setGeometry(QRect(70, 380, 51, 31))
        self.lineEdit_120 = QLineEdit(self.groupBox_36)
        self.lineEdit_120.setObjectName(u"lineEdit_120")
        self.lineEdit_120.setGeometry(QRect(140, 320, 161, 31))
        self.lineEdit_120.setClearButtonEnabled(True)
        self.lineEdit_121 = QLineEdit(self.groupBox_36)
        self.lineEdit_121.setObjectName(u"lineEdit_121")
        self.lineEdit_121.setGeometry(QRect(140, 160, 161, 31))
        self.lineEdit_121.setClearButtonEnabled(True)
        self.label_249 = QLabel(self.groupBox_36)
        self.label_249.setObjectName(u"label_249")
        self.label_249.setGeometry(QRect(30, 160, 111, 31))
        self.label_250 = QLabel(self.groupBox_36)
        self.label_250.setObjectName(u"label_250")
        self.label_250.setGeometry(QRect(340, 160, 131, 31))
        self.lineEdit_122 = QLineEdit(self.groupBox_36)
        self.lineEdit_122.setObjectName(u"lineEdit_122")
        self.lineEdit_122.setGeometry(QRect(480, 160, 151, 31))
        self.lineEdit_122.setClearButtonEnabled(True)
        self.label_251 = QLabel(self.groupBox_36)
        self.label_251.setObjectName(u"label_251")
        self.label_251.setGeometry(QRect(20, 220, 121, 31))
        self.lineEdit_123 = QLineEdit(self.groupBox_36)
        self.lineEdit_123.setObjectName(u"lineEdit_123")
        self.lineEdit_123.setGeometry(QRect(140, 210, 161, 31))
        self.lineEdit_123.setClearButtonEnabled(True)
        self.label_545 = QLabel(self.groupBox_36)
        self.label_545.setObjectName(u"label_545")
        self.label_545.setGeometry(QRect(30, 440, 101, 31))
        self.label_546 = QLabel(self.groupBox_36)
        self.label_546.setObjectName(u"label_546")
        self.label_546.setGeometry(QRect(180, 40, 381, 31))
        self.pushButton_7 = QPushButton(self.groupBox_36)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(400, 510, 81, 31))
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_7.setIcon(icon18)
        self.pushButton_7.setIconSize(QSize(28, 28))
        self.comboBox_14 = QComboBox(self.groupBox_36)
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.setObjectName(u"comboBox_14")
        self.comboBox_14.setGeometry(QRect(140, 380, 171, 31))
        self.comboBox_15 = QComboBox(self.groupBox_36)
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.setObjectName(u"comboBox_15")
        self.comboBox_15.setGeometry(QRect(140, 440, 171, 31))
        self.lineEdit_157 = QLineEdit(self.groupBox_36)
        self.lineEdit_157.setObjectName(u"lineEdit_157")
        self.lineEdit_157.setGeometry(QRect(150, 500, 161, 31))
        self.lineEdit_157.setClearButtonEnabled(True)
        self.label_1321 = QLabel(self.groupBox_36)
        self.label_1321.setObjectName(u"label_1321")
        self.label_1321.setGeometry(QRect(10, 500, 141, 31))
        self.label_1333 = QLabel(self.groupBox_36)
        self.label_1333.setObjectName(u"label_1333")
        self.label_1333.setGeometry(QRect(360, 377, 101, 31))
        self.lineEdit_169 = QLineEdit(self.groupBox_36)
        self.lineEdit_169.setObjectName(u"lineEdit_169")
        self.lineEdit_169.setGeometry(QRect(480, 377, 191, 31))
        self.lineEdit_169.setClearButtonEnabled(True)
        self.lineEdit_170 = QLineEdit(self.groupBox_36)
        self.lineEdit_170.setObjectName(u"lineEdit_170")
        self.lineEdit_170.setGeometry(QRect(510, 437, 191, 31))
        self.lineEdit_170.setClearButtonEnabled(True)
        self.label_1334 = QLabel(self.groupBox_36)
        self.label_1334.setObjectName(u"label_1334")
        self.label_1334.setGeometry(QRect(370, 437, 141, 31))
        self.label_1349 = QLabel(self.groupBox_36)
        self.label_1349.setObjectName(u"label_1349")
        self.label_1349.setGeometry(QRect(410, 320, 51, 31))
        self.lineEdit_185 = QLineEdit(self.groupBox_36)
        self.lineEdit_185.setObjectName(u"lineEdit_185")
        self.lineEdit_185.setGeometry(QRect(480, 320, 191, 31))
        self.lineEdit_185.setClearButtonEnabled(True)

        self.verticalLayout_141.addWidget(self.groupBox_36)


        self.horizontalLayout_17.addWidget(self.frame_49)

        self.tabWidget_5.addTab(self.tab_13, "")
        self.tab_46 = QWidget()
        self.tab_46.setObjectName(u"tab_46")
        self.verticalLayout_146 = QVBoxLayout(self.tab_46)
        self.verticalLayout_146.setSpacing(0)
        self.verticalLayout_146.setObjectName(u"verticalLayout_146")
        self.verticalLayout_146.setContentsMargins(0, 0, 0, 0)
        self.frame_182 = QFrame(self.tab_46)
        self.frame_182.setObjectName(u"frame_182")
        self.frame_182.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(222, 222, 222);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 148, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(0, 213, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_182.setFrameShape(QFrame.StyledPanel)
        self.frame_182.setFrameShadow(QFrame.Raised)
        self.label_659 = QLabel(self.frame_182)
        self.label_659.setObjectName(u"label_659")
        self.label_659.setGeometry(QRect(180, 10, 311, 21))
        self.label_659.setStyleSheet(u"font: 900 14pt \"Roboto\";")
        self.label_659.setAlignment(Qt.AlignCenter)
        self.label_660 = QLabel(self.frame_182)
        self.label_660.setObjectName(u"label_660")
        self.label_660.setGeometry(QRect(210, 40, 141, 16))
        self.label_661 = QLabel(self.frame_182)
        self.label_661.setObjectName(u"label_661")
        self.label_661.setGeometry(QRect(440, 40, 171, 16))
        self.label_662 = QLabel(self.frame_182)
        self.label_662.setObjectName(u"label_662")
        self.label_662.setGeometry(QRect(220, 60, 221, 20))
        self.label_662.setAlignment(Qt.AlignCenter)
        self.label_663 = QLabel(self.frame_182)
        self.label_663.setObjectName(u"label_663")
        self.label_663.setGeometry(QRect(70, 100, 49, 16))
        self.line_157 = QFrame(self.frame_182)
        self.line_157.setObjectName(u"line_157")
        self.line_157.setGeometry(QRect(90, 80, 501, 16))
        self.line_157.setFrameShape(QFrame.HLine)
        self.line_157.setFrameShadow(QFrame.Sunken)
        self.label_664 = QLabel(self.frame_182)
        self.label_664.setObjectName(u"label_664")
        self.label_664.setGeometry(QRect(120, 100, 71, 16))
        self.label_664.setStyleSheet(u"color: rgb(163, 128, 21);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_665 = QLabel(self.frame_182)
        self.label_665.setObjectName(u"label_665")
        self.label_665.setGeometry(QRect(220, 100, 41, 16))
        self.label_666 = QLabel(self.frame_182)
        self.label_666.setObjectName(u"label_666")
        self.label_666.setGeometry(QRect(270, 100, 131, 16))
        self.label_666.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")
        self.label_666.setTextFormat(Qt.AutoText)
        self.label_666.setScaledContents(False)
        self.label_667 = QLabel(self.frame_182)
        self.label_667.setObjectName(u"label_667")
        self.label_667.setGeometry(QRect(80, 150, 91, 16))
        self.label_668 = QLabel(self.frame_182)
        self.label_668.setObjectName(u"label_668")
        self.label_668.setGeometry(QRect(160, 150, 71, 16))
        self.label_669 = QLabel(self.frame_182)
        self.label_669.setObjectName(u"label_669")
        self.label_669.setGeometry(QRect(270, 150, 101, 16))
        self.label_670 = QLabel(self.frame_182)
        self.label_670.setObjectName(u"label_670")
        self.label_670.setGeometry(QRect(370, 150, 61, 16))
        self.label_671 = QLabel(self.frame_182)
        self.label_671.setObjectName(u"label_671")
        self.label_671.setGeometry(QRect(430, 100, 49, 16))
        self.label_672 = QLabel(self.frame_182)
        self.label_672.setObjectName(u"label_672")
        self.label_672.setGeometry(QRect(470, 100, 91, 16))
        self.label_673 = QLabel(self.frame_182)
        self.label_673.setObjectName(u"label_673")
        self.label_673.setGeometry(QRect(470, 150, 49, 16))
        self.label_674 = QLabel(self.frame_182)
        self.label_674.setObjectName(u"label_674")
        self.label_674.setGeometry(QRect(510, 150, 71, 16))
        self.line_158 = QFrame(self.frame_182)
        self.line_158.setObjectName(u"line_158")
        self.line_158.setGeometry(QRect(20, 170, 631, 20))
        self.line_158.setFrameShape(QFrame.HLine)
        self.line_158.setFrameShadow(QFrame.Sunken)
        self.line_159 = QFrame(self.frame_182)
        self.line_159.setObjectName(u"line_159")
        self.line_159.setGeometry(QRect(120, 180, 20, 401))
        self.line_159.setFrameShadow(QFrame.Sunken)
        self.line_159.setFrameShape(QFrame.VLine)
        self.line_160 = QFrame(self.frame_182)
        self.line_160.setObjectName(u"line_160")
        self.line_160.setGeometry(QRect(240, 180, 20, 401))
        self.line_160.setFrameShape(QFrame.VLine)
        self.line_160.setFrameShadow(QFrame.Sunken)
        self.line_161 = QFrame(self.frame_182)
        self.line_161.setObjectName(u"line_161")
        self.line_161.setGeometry(QRect(350, 180, 20, 401))
        self.line_161.setFrameShape(QFrame.VLine)
        self.line_161.setFrameShadow(QFrame.Sunken)
        self.line_162 = QFrame(self.frame_182)
        self.line_162.setObjectName(u"line_162")
        self.line_162.setGeometry(QRect(10, 220, 641, 20))
        self.line_162.setFrameShape(QFrame.HLine)
        self.line_162.setFrameShadow(QFrame.Sunken)
        self.label_675 = QLabel(self.frame_182)
        self.label_675.setObjectName(u"label_675")
        self.label_675.setGeometry(QRect(40, 190, 71, 20))
        self.label_675.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_676 = QLabel(self.frame_182)
        self.label_676.setObjectName(u"label_676")
        self.label_676.setGeometry(QRect(140, 180, 101, 20))
        self.label_676.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_677 = QLabel(self.frame_182)
        self.label_677.setObjectName(u"label_677")
        self.label_677.setGeometry(QRect(170, 200, 31, 16))
        self.label_677.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_678 = QLabel(self.frame_182)
        self.label_678.setObjectName(u"label_678")
        self.label_678.setGeometry(QRect(490, 190, 51, 20))
        self.label_678.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_679 = QLabel(self.frame_182)
        self.label_679.setObjectName(u"label_679")
        self.label_679.setGeometry(QRect(560, 190, 81, 20))
        self.label_679.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_680 = QLabel(self.frame_182)
        self.label_680.setObjectName(u"label_680")
        self.label_680.setGeometry(QRect(10, 230, 101, 16))
        self.label_681 = QLabel(self.frame_182)
        self.label_681.setObjectName(u"label_681")
        self.label_681.setGeometry(QRect(10, 270, 111, 16))
        self.label_682 = QLabel(self.frame_182)
        self.label_682.setObjectName(u"label_682")
        self.label_682.setGeometry(QRect(10, 310, 111, 16))
        self.label_683 = QLabel(self.frame_182)
        self.label_683.setObjectName(u"label_683")
        self.label_683.setGeometry(QRect(10, 350, 111, 16))
        self.label_684 = QLabel(self.frame_182)
        self.label_684.setObjectName(u"label_684")
        self.label_684.setGeometry(QRect(10, 390, 71, 16))
        self.label_685 = QLabel(self.frame_182)
        self.label_685.setObjectName(u"label_685")
        self.label_685.setGeometry(QRect(10, 430, 71, 16))
        self.label_686 = QLabel(self.frame_182)
        self.label_686.setObjectName(u"label_686")
        self.label_686.setGeometry(QRect(10, 470, 81, 16))
        self.label_687 = QLabel(self.frame_182)
        self.label_687.setObjectName(u"label_687")
        self.label_687.setGeometry(QRect(10, 510, 91, 16))
        self.label_688 = QLabel(self.frame_182)
        self.label_688.setObjectName(u"label_688")
        self.label_688.setGeometry(QRect(10, 550, 71, 16))
        self.line_163 = QFrame(self.frame_182)
        self.line_163.setObjectName(u"line_163")
        self.line_163.setGeometry(QRect(10, 250, 641, 20))
        self.line_163.setFrameShape(QFrame.HLine)
        self.line_163.setFrameShadow(QFrame.Sunken)
        self.line_164 = QFrame(self.frame_182)
        self.line_164.setObjectName(u"line_164")
        self.line_164.setGeometry(QRect(10, 290, 641, 20))
        self.line_164.setFrameShape(QFrame.HLine)
        self.line_164.setFrameShadow(QFrame.Sunken)
        self.line_165 = QFrame(self.frame_182)
        self.line_165.setObjectName(u"line_165")
        self.line_165.setGeometry(QRect(10, 330, 641, 20))
        self.line_165.setFrameShape(QFrame.HLine)
        self.line_165.setFrameShadow(QFrame.Sunken)
        self.line_166 = QFrame(self.frame_182)
        self.line_166.setObjectName(u"line_166")
        self.line_166.setGeometry(QRect(10, 370, 641, 20))
        self.line_166.setFrameShadow(QFrame.Sunken)
        self.line_166.setFrameShape(QFrame.HLine)
        self.line_167 = QFrame(self.frame_182)
        self.line_167.setObjectName(u"line_167")
        self.line_167.setGeometry(QRect(10, 410, 641, 20))
        self.line_167.setFrameShape(QFrame.HLine)
        self.line_167.setFrameShadow(QFrame.Sunken)
        self.line_168 = QFrame(self.frame_182)
        self.line_168.setObjectName(u"line_168")
        self.line_168.setGeometry(QRect(10, 450, 641, 20))
        self.line_168.setFrameShape(QFrame.HLine)
        self.line_168.setFrameShadow(QFrame.Sunken)
        self.line_169 = QFrame(self.frame_182)
        self.line_169.setObjectName(u"line_169")
        self.line_169.setGeometry(QRect(10, 490, 641, 20))
        self.line_169.setFrameShape(QFrame.HLine)
        self.line_169.setFrameShadow(QFrame.Sunken)
        self.line_170 = QFrame(self.frame_182)
        self.line_170.setObjectName(u"line_170")
        self.line_170.setGeometry(QRect(10, 530, 641, 20))
        self.line_170.setFrameShape(QFrame.HLine)
        self.line_170.setFrameShadow(QFrame.Sunken)
        self.line_171 = QFrame(self.frame_182)
        self.line_171.setObjectName(u"line_171")
        self.line_171.setGeometry(QRect(10, 570, 641, 20))
        self.line_171.setFrameShape(QFrame.HLine)
        self.line_171.setFrameShadow(QFrame.Sunken)
        self.label_689 = QLabel(self.frame_182)
        self.label_689.setObjectName(u"label_689")
        self.label_689.setGeometry(QRect(50, 590, 71, 16))
        self.label_690 = QLabel(self.frame_182)
        self.label_690.setObjectName(u"label_690")
        self.label_690.setGeometry(QRect(120, 590, 49, 16))
        self.label_691 = QLabel(self.frame_182)
        self.label_691.setObjectName(u"label_691")
        self.label_691.setGeometry(QRect(200, 590, 41, 16))
        self.label_692 = QLabel(self.frame_182)
        self.label_692.setObjectName(u"label_692")
        self.label_692.setGeometry(QRect(240, 590, 49, 16))
        self.label_693 = QLabel(self.frame_182)
        self.label_693.setObjectName(u"label_693")
        self.label_693.setGeometry(QRect(370, 590, 81, 16))
        self.label_694 = QLabel(self.frame_182)
        self.label_694.setObjectName(u"label_694")
        self.label_694.setGeometry(QRect(450, 590, 49, 16))
        self.label_695 = QLabel(self.frame_182)
        self.label_695.setObjectName(u"label_695")
        self.label_695.setGeometry(QRect(100, 610, 181, 16))
        self.label_696 = QLabel(self.frame_182)
        self.label_696.setObjectName(u"label_696")
        self.label_696.setGeometry(QRect(50, 610, 51, 16))
        self.label_697 = QLabel(self.frame_182)
        self.label_697.setObjectName(u"label_697")
        self.label_697.setGeometry(QRect(380, 610, 41, 16))
        self.label_698 = QLabel(self.frame_182)
        self.label_698.setObjectName(u"label_698")
        self.label_698.setGeometry(QRect(430, 610, 181, 16))
        self.label_699 = QLabel(self.frame_182)
        self.label_699.setObjectName(u"label_699")
        self.label_699.setGeometry(QRect(50, 630, 131, 16))
        self.label_700 = QLabel(self.frame_182)
        self.label_700.setObjectName(u"label_700")
        self.label_700.setGeometry(QRect(190, 630, 191, 16))
        self.label_701 = QLabel(self.frame_182)
        self.label_701.setObjectName(u"label_701")
        self.label_701.setGeometry(QRect(510, 630, 81, 16))
        self.label_702 = QLabel(self.frame_182)
        self.label_702.setObjectName(u"label_702")
        self.label_702.setGeometry(QRect(450, 630, 61, 16))
        self.label_703 = QLabel(self.frame_182)
        self.label_703.setObjectName(u"label_703")
        self.label_703.setGeometry(QRect(50, 650, 101, 16))
        self.label_704 = QLabel(self.frame_182)
        self.label_704.setObjectName(u"label_704")
        self.label_704.setGeometry(QRect(150, 650, 231, 16))
        self.label_705 = QLabel(self.frame_182)
        self.label_705.setObjectName(u"label_705")
        self.label_705.setGeometry(QRect(510, 650, 81, 16))
        self.label_706 = QLabel(self.frame_182)
        self.label_706.setObjectName(u"label_706")
        self.label_706.setGeometry(QRect(450, 650, 61, 16))
        self.label_707 = QLabel(self.frame_182)
        self.label_707.setObjectName(u"label_707")
        self.label_707.setGeometry(QRect(260, 180, 91, 20))
        self.label_707.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_708 = QLabel(self.frame_182)
        self.label_708.setObjectName(u"label_708")
        self.label_708.setGeometry(QRect(290, 200, 31, 20))
        self.label_708.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_709 = QLabel(self.frame_182)
        self.label_709.setObjectName(u"label_709")
        self.label_709.setGeometry(QRect(370, 180, 101, 20))
        self.label_709.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_710 = QLabel(self.frame_182)
        self.label_710.setObjectName(u"label_710")
        self.label_710.setGeometry(QRect(400, 200, 41, 20))
        self.label_710.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.line_172 = QFrame(self.frame_182)
        self.line_172.setObjectName(u"line_172")
        self.line_172.setGeometry(QRect(470, 180, 20, 401))
        self.line_172.setFrameShape(QFrame.VLine)
        self.line_172.setFrameShadow(QFrame.Sunken)
        self.line_173 = QFrame(self.frame_182)
        self.line_173.setObjectName(u"line_173")
        self.line_173.setGeometry(QRect(540, 180, 20, 401))
        self.line_173.setFrameShape(QFrame.VLine)
        self.line_173.setFrameShadow(QFrame.Sunken)
        self.label_711 = QLabel(self.frame_182)
        self.label_711.setObjectName(u"label_711")
        self.label_711.setGeometry(QRect(170, 40, 31, 16))
        self.label_712 = QLabel(self.frame_182)
        self.label_712.setObjectName(u"label_712")
        self.label_712.setGeometry(QRect(390, 40, 49, 16))
        self.bt_109 = QPushButton(self.frame_182)
        self.bt_109.setObjectName(u"bt_109")
        self.bt_109.setGeometry(QRect(564, 13, 101, 41))
        self.bt_109.setCursor(QCursor(Qt.PointingHandCursor))
        icon24 = QIcon()
        icon24.addFile(u":/icons/assets/buttons/printer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_109.setIcon(icon24)
        self.bt_109.setIconSize(QSize(28, 28))
        self.label_713 = QLabel(self.frame_182)
        self.label_713.setObjectName(u"label_713")
        self.label_713.setGeometry(QRect(160, 230, 71, 16))
        self.label_714 = QLabel(self.frame_182)
        self.label_714.setObjectName(u"label_714")
        self.label_714.setGeometry(QRect(280, 230, 71, 16))
        self.label_715 = QLabel(self.frame_182)
        self.label_715.setObjectName(u"label_715")
        self.label_715.setGeometry(QRect(380, 230, 71, 16))
        self.label_716 = QLabel(self.frame_182)
        self.label_716.setObjectName(u"label_716")
        self.label_716.setGeometry(QRect(490, 230, 51, 16))
        self.label_717 = QLabel(self.frame_182)
        self.label_717.setObjectName(u"label_717")
        self.label_717.setGeometry(QRect(570, 230, 81, 16))
        self.label_718 = QLabel(self.frame_182)
        self.label_718.setObjectName(u"label_718")
        self.label_718.setGeometry(QRect(160, 270, 71, 16))
        self.label_719 = QLabel(self.frame_182)
        self.label_719.setObjectName(u"label_719")
        self.label_719.setGeometry(QRect(380, 270, 71, 16))
        self.label_720 = QLabel(self.frame_182)
        self.label_720.setObjectName(u"label_720")
        self.label_720.setGeometry(QRect(490, 270, 51, 16))
        self.label_721 = QLabel(self.frame_182)
        self.label_721.setObjectName(u"label_721")
        self.label_721.setGeometry(QRect(280, 270, 71, 16))
        self.label_722 = QLabel(self.frame_182)
        self.label_722.setObjectName(u"label_722")
        self.label_722.setGeometry(QRect(570, 270, 81, 16))
        self.label_723 = QLabel(self.frame_182)
        self.label_723.setObjectName(u"label_723")
        self.label_723.setGeometry(QRect(160, 310, 71, 16))
        self.label_724 = QLabel(self.frame_182)
        self.label_724.setObjectName(u"label_724")
        self.label_724.setGeometry(QRect(570, 310, 81, 16))
        self.label_725 = QLabel(self.frame_182)
        self.label_725.setObjectName(u"label_725")
        self.label_725.setGeometry(QRect(280, 310, 71, 16))
        self.label_726 = QLabel(self.frame_182)
        self.label_726.setObjectName(u"label_726")
        self.label_726.setGeometry(QRect(490, 310, 51, 16))
        self.label_727 = QLabel(self.frame_182)
        self.label_727.setObjectName(u"label_727")
        self.label_727.setGeometry(QRect(380, 310, 71, 16))
        self.label_728 = QLabel(self.frame_182)
        self.label_728.setObjectName(u"label_728")
        self.label_728.setGeometry(QRect(160, 350, 71, 16))
        self.label_729 = QLabel(self.frame_182)
        self.label_729.setObjectName(u"label_729")
        self.label_729.setGeometry(QRect(280, 350, 71, 16))
        self.label_730 = QLabel(self.frame_182)
        self.label_730.setObjectName(u"label_730")
        self.label_730.setGeometry(QRect(380, 350, 71, 16))
        self.label_731 = QLabel(self.frame_182)
        self.label_731.setObjectName(u"label_731")
        self.label_731.setGeometry(QRect(490, 350, 51, 16))
        self.label_732 = QLabel(self.frame_182)
        self.label_732.setObjectName(u"label_732")
        self.label_732.setGeometry(QRect(570, 350, 81, 16))
        self.label_733 = QLabel(self.frame_182)
        self.label_733.setObjectName(u"label_733")
        self.label_733.setGeometry(QRect(570, 390, 81, 16))
        self.label_734 = QLabel(self.frame_182)
        self.label_734.setObjectName(u"label_734")
        self.label_734.setGeometry(QRect(380, 390, 71, 16))
        self.label_735 = QLabel(self.frame_182)
        self.label_735.setObjectName(u"label_735")
        self.label_735.setGeometry(QRect(160, 390, 71, 16))
        self.label_736 = QLabel(self.frame_182)
        self.label_736.setObjectName(u"label_736")
        self.label_736.setGeometry(QRect(490, 390, 51, 16))
        self.label_737 = QLabel(self.frame_182)
        self.label_737.setObjectName(u"label_737")
        self.label_737.setGeometry(QRect(280, 390, 71, 16))
        self.label_738 = QLabel(self.frame_182)
        self.label_738.setObjectName(u"label_738")
        self.label_738.setGeometry(QRect(160, 430, 71, 16))
        self.label_739 = QLabel(self.frame_182)
        self.label_739.setObjectName(u"label_739")
        self.label_739.setGeometry(QRect(490, 430, 51, 16))
        self.label_740 = QLabel(self.frame_182)
        self.label_740.setObjectName(u"label_740")
        self.label_740.setGeometry(QRect(380, 430, 71, 16))
        self.label_741 = QLabel(self.frame_182)
        self.label_741.setObjectName(u"label_741")
        self.label_741.setGeometry(QRect(570, 430, 81, 16))
        self.label_742 = QLabel(self.frame_182)
        self.label_742.setObjectName(u"label_742")
        self.label_742.setGeometry(QRect(280, 430, 71, 16))
        self.label_743 = QLabel(self.frame_182)
        self.label_743.setObjectName(u"label_743")
        self.label_743.setGeometry(QRect(160, 470, 71, 16))
        self.label_744 = QLabel(self.frame_182)
        self.label_744.setObjectName(u"label_744")
        self.label_744.setGeometry(QRect(490, 470, 51, 16))
        self.label_745 = QLabel(self.frame_182)
        self.label_745.setObjectName(u"label_745")
        self.label_745.setGeometry(QRect(570, 470, 81, 16))
        self.label_746 = QLabel(self.frame_182)
        self.label_746.setObjectName(u"label_746")
        self.label_746.setGeometry(QRect(380, 470, 71, 16))
        self.label_747 = QLabel(self.frame_182)
        self.label_747.setObjectName(u"label_747")
        self.label_747.setGeometry(QRect(280, 470, 71, 16))
        self.label_748 = QLabel(self.frame_182)
        self.label_748.setObjectName(u"label_748")
        self.label_748.setGeometry(QRect(570, 510, 81, 16))
        self.label_749 = QLabel(self.frame_182)
        self.label_749.setObjectName(u"label_749")
        self.label_749.setGeometry(QRect(280, 510, 71, 16))
        self.label_750 = QLabel(self.frame_182)
        self.label_750.setObjectName(u"label_750")
        self.label_750.setGeometry(QRect(380, 510, 71, 16))
        self.label_751 = QLabel(self.frame_182)
        self.label_751.setObjectName(u"label_751")
        self.label_751.setGeometry(QRect(490, 510, 51, 16))
        self.label_752 = QLabel(self.frame_182)
        self.label_752.setObjectName(u"label_752")
        self.label_752.setGeometry(QRect(160, 510, 71, 16))
        self.label_753 = QLabel(self.frame_182)
        self.label_753.setObjectName(u"label_753")
        self.label_753.setGeometry(QRect(570, 550, 81, 16))
        self.label_754 = QLabel(self.frame_182)
        self.label_754.setObjectName(u"label_754")
        self.label_754.setGeometry(QRect(380, 550, 71, 16))
        self.label_755 = QLabel(self.frame_182)
        self.label_755.setObjectName(u"label_755")
        self.label_755.setGeometry(QRect(490, 550, 51, 16))
        self.label_756 = QLabel(self.frame_182)
        self.label_756.setObjectName(u"label_756")
        self.label_756.setGeometry(QRect(280, 550, 71, 16))
        self.label_757 = QLabel(self.frame_182)
        self.label_757.setObjectName(u"label_757")
        self.label_757.setGeometry(QRect(160, 550, 71, 16))
        self.line_162.raise_()
        self.label_710.raise_()
        self.label_659.raise_()
        self.label_660.raise_()
        self.label_661.raise_()
        self.label_662.raise_()
        self.label_663.raise_()
        self.line_157.raise_()
        self.label_664.raise_()
        self.label_665.raise_()
        self.label_666.raise_()
        self.label_667.raise_()
        self.label_668.raise_()
        self.label_669.raise_()
        self.label_670.raise_()
        self.label_671.raise_()
        self.label_672.raise_()
        self.label_673.raise_()
        self.label_674.raise_()
        self.line_158.raise_()
        self.line_159.raise_()
        self.line_160.raise_()
        self.line_161.raise_()
        self.label_675.raise_()
        self.label_676.raise_()
        self.label_678.raise_()
        self.label_679.raise_()
        self.label_680.raise_()
        self.label_681.raise_()
        self.label_682.raise_()
        self.label_683.raise_()
        self.label_684.raise_()
        self.label_685.raise_()
        self.label_686.raise_()
        self.label_687.raise_()
        self.label_688.raise_()
        self.line_163.raise_()
        self.line_164.raise_()
        self.line_165.raise_()
        self.line_166.raise_()
        self.line_167.raise_()
        self.line_168.raise_()
        self.line_169.raise_()
        self.line_170.raise_()
        self.line_171.raise_()
        self.label_689.raise_()
        self.label_690.raise_()
        self.label_691.raise_()
        self.label_692.raise_()
        self.label_693.raise_()
        self.label_694.raise_()
        self.label_695.raise_()
        self.label_696.raise_()
        self.label_697.raise_()
        self.label_698.raise_()
        self.label_699.raise_()
        self.label_700.raise_()
        self.label_701.raise_()
        self.label_702.raise_()
        self.label_703.raise_()
        self.label_704.raise_()
        self.label_705.raise_()
        self.label_706.raise_()
        self.label_707.raise_()
        self.label_708.raise_()
        self.label_709.raise_()
        self.line_172.raise_()
        self.line_173.raise_()
        self.label_711.raise_()
        self.label_712.raise_()
        self.bt_109.raise_()
        self.label_713.raise_()
        self.label_714.raise_()
        self.label_715.raise_()
        self.label_716.raise_()
        self.label_717.raise_()
        self.label_718.raise_()
        self.label_719.raise_()
        self.label_720.raise_()
        self.label_721.raise_()
        self.label_722.raise_()
        self.label_723.raise_()
        self.label_724.raise_()
        self.label_725.raise_()
        self.label_726.raise_()
        self.label_727.raise_()
        self.label_728.raise_()
        self.label_729.raise_()
        self.label_730.raise_()
        self.label_731.raise_()
        self.label_732.raise_()
        self.label_733.raise_()
        self.label_734.raise_()
        self.label_735.raise_()
        self.label_736.raise_()
        self.label_737.raise_()
        self.label_738.raise_()
        self.label_739.raise_()
        self.label_740.raise_()
        self.label_741.raise_()
        self.label_742.raise_()
        self.label_743.raise_()
        self.label_744.raise_()
        self.label_745.raise_()
        self.label_746.raise_()
        self.label_747.raise_()
        self.label_748.raise_()
        self.label_749.raise_()
        self.label_750.raise_()
        self.label_751.raise_()
        self.label_752.raise_()
        self.label_753.raise_()
        self.label_754.raise_()
        self.label_755.raise_()
        self.label_756.raise_()
        self.label_757.raise_()
        self.label_677.raise_()

        self.verticalLayout_146.addWidget(self.frame_182)

        self.tabWidget_5.addTab(self.tab_46, "")
        self.tab_47 = QWidget()
        self.tab_47.setObjectName(u"tab_47")
        self.verticalLayout_145 = QVBoxLayout(self.tab_47)
        self.verticalLayout_145.setSpacing(0)
        self.verticalLayout_145.setObjectName(u"verticalLayout_145")
        self.verticalLayout_145.setContentsMargins(0, 0, 0, 0)
        self.frame_181 = QFrame(self.tab_47)
        self.frame_181.setObjectName(u"frame_181")
        self.frame_181.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(222, 222, 222);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 148, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(0, 213, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"\n"
"")
        self.frame_181.setFrameShape(QFrame.StyledPanel)
        self.frame_181.setFrameShadow(QFrame.Raised)
        self.label_605 = QLabel(self.frame_181)
        self.label_605.setObjectName(u"label_605")
        self.label_605.setGeometry(QRect(180, 10, 311, 21))
        self.label_605.setStyleSheet(u"font: 900 14pt \"Roboto\";")
        self.label_605.setAlignment(Qt.AlignCenter)
        self.label_606 = QLabel(self.frame_181)
        self.label_606.setObjectName(u"label_606")
        self.label_606.setGeometry(QRect(210, 40, 141, 16))
        self.label_607 = QLabel(self.frame_181)
        self.label_607.setObjectName(u"label_607")
        self.label_607.setGeometry(QRect(440, 40, 171, 16))
        self.label_608 = QLabel(self.frame_181)
        self.label_608.setObjectName(u"label_608")
        self.label_608.setGeometry(QRect(220, 60, 221, 20))
        self.label_608.setAlignment(Qt.AlignCenter)
        self.label_609 = QLabel(self.frame_181)
        self.label_609.setObjectName(u"label_609")
        self.label_609.setGeometry(QRect(70, 100, 49, 16))
        self.line_140 = QFrame(self.frame_181)
        self.line_140.setObjectName(u"line_140")
        self.line_140.setGeometry(QRect(90, 80, 501, 16))
        self.line_140.setFrameShape(QFrame.HLine)
        self.line_140.setFrameShadow(QFrame.Sunken)
        self.label_610 = QLabel(self.frame_181)
        self.label_610.setObjectName(u"label_610")
        self.label_610.setGeometry(QRect(120, 100, 71, 16))
        self.label_610.setStyleSheet(u"color: rgb(202, 135, 0);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_611 = QLabel(self.frame_181)
        self.label_611.setObjectName(u"label_611")
        self.label_611.setGeometry(QRect(220, 100, 41, 16))
        self.label_612 = QLabel(self.frame_181)
        self.label_612.setObjectName(u"label_612")
        self.label_612.setGeometry(QRect(270, 100, 151, 16))
        self.label_612.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_612.setTextFormat(Qt.AutoText)
        self.label_612.setScaledContents(False)
        self.label_613 = QLabel(self.frame_181)
        self.label_613.setObjectName(u"label_613")
        self.label_613.setGeometry(QRect(80, 140, 91, 16))
        self.label_614 = QLabel(self.frame_181)
        self.label_614.setObjectName(u"label_614")
        self.label_614.setGeometry(QRect(160, 140, 71, 16))
        self.label_615 = QLabel(self.frame_181)
        self.label_615.setObjectName(u"label_615")
        self.label_615.setGeometry(QRect(270, 140, 101, 16))
        self.label_616 = QLabel(self.frame_181)
        self.label_616.setObjectName(u"label_616")
        self.label_616.setGeometry(QRect(370, 140, 61, 16))
        self.label_617 = QLabel(self.frame_181)
        self.label_617.setObjectName(u"label_617")
        self.label_617.setGeometry(QRect(430, 100, 49, 16))
        self.label_618 = QLabel(self.frame_181)
        self.label_618.setObjectName(u"label_618")
        self.label_618.setGeometry(QRect(470, 100, 91, 16))
        self.label_619 = QLabel(self.frame_181)
        self.label_619.setObjectName(u"label_619")
        self.label_619.setGeometry(QRect(460, 140, 49, 16))
        self.label_620 = QLabel(self.frame_181)
        self.label_620.setObjectName(u"label_620")
        self.label_620.setGeometry(QRect(500, 140, 71, 16))
        self.line_141 = QFrame(self.frame_181)
        self.line_141.setObjectName(u"line_141")
        self.line_141.setGeometry(QRect(20, 160, 631, 20))
        self.line_141.setFrameShape(QFrame.HLine)
        self.line_141.setFrameShadow(QFrame.Sunken)
        self.line_142 = QFrame(self.frame_181)
        self.line_142.setObjectName(u"line_142")
        self.line_142.setGeometry(QRect(120, 180, 20, 381))
        self.line_142.setFrameShadow(QFrame.Sunken)
        self.line_142.setFrameShape(QFrame.VLine)
        self.line_143 = QFrame(self.frame_181)
        self.line_143.setObjectName(u"line_143")
        self.line_143.setGeometry(QRect(240, 180, 20, 381))
        self.line_143.setFrameShape(QFrame.VLine)
        self.line_143.setFrameShadow(QFrame.Sunken)
        self.line_144 = QFrame(self.frame_181)
        self.line_144.setObjectName(u"line_144")
        self.line_144.setGeometry(QRect(350, 180, 20, 381))
        self.line_144.setFrameShape(QFrame.VLine)
        self.line_144.setFrameShadow(QFrame.Sunken)
        self.line_145 = QFrame(self.frame_181)
        self.line_145.setObjectName(u"line_145")
        self.line_145.setGeometry(QRect(10, 210, 641, 20))
        self.line_145.setFrameShape(QFrame.HLine)
        self.line_145.setFrameShadow(QFrame.Sunken)
        self.label_621 = QLabel(self.frame_181)
        self.label_621.setObjectName(u"label_621")
        self.label_621.setGeometry(QRect(40, 180, 71, 20))
        self.label_621.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_622 = QLabel(self.frame_181)
        self.label_622.setObjectName(u"label_622")
        self.label_622.setGeometry(QRect(140, 170, 101, 20))
        self.label_622.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_623 = QLabel(self.frame_181)
        self.label_623.setObjectName(u"label_623")
        self.label_623.setGeometry(QRect(170, 190, 31, 20))
        self.label_623.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_624 = QLabel(self.frame_181)
        self.label_624.setObjectName(u"label_624")
        self.label_624.setGeometry(QRect(490, 180, 51, 20))
        self.label_624.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_625 = QLabel(self.frame_181)
        self.label_625.setObjectName(u"label_625")
        self.label_625.setGeometry(QRect(560, 180, 81, 20))
        self.label_625.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_626 = QLabel(self.frame_181)
        self.label_626.setObjectName(u"label_626")
        self.label_626.setGeometry(QRect(20, 220, 101, 16))
        self.label_627 = QLabel(self.frame_181)
        self.label_627.setObjectName(u"label_627")
        self.label_627.setGeometry(QRect(10, 260, 111, 16))
        self.label_628 = QLabel(self.frame_181)
        self.label_628.setObjectName(u"label_628")
        self.label_628.setGeometry(QRect(10, 300, 111, 16))
        self.label_629 = QLabel(self.frame_181)
        self.label_629.setObjectName(u"label_629")
        self.label_629.setGeometry(QRect(10, 340, 111, 16))
        self.label_630 = QLabel(self.frame_181)
        self.label_630.setObjectName(u"label_630")
        self.label_630.setGeometry(QRect(10, 380, 71, 16))
        self.label_631 = QLabel(self.frame_181)
        self.label_631.setObjectName(u"label_631")
        self.label_631.setGeometry(QRect(10, 420, 71, 16))
        self.label_632 = QLabel(self.frame_181)
        self.label_632.setObjectName(u"label_632")
        self.label_632.setGeometry(QRect(10, 460, 81, 16))
        self.label_633 = QLabel(self.frame_181)
        self.label_633.setObjectName(u"label_633")
        self.label_633.setGeometry(QRect(10, 500, 91, 16))
        self.label_634 = QLabel(self.frame_181)
        self.label_634.setObjectName(u"label_634")
        self.label_634.setGeometry(QRect(10, 540, 71, 16))
        self.line_146 = QFrame(self.frame_181)
        self.line_146.setObjectName(u"line_146")
        self.line_146.setGeometry(QRect(10, 240, 641, 20))
        self.line_146.setFrameShape(QFrame.HLine)
        self.line_146.setFrameShadow(QFrame.Sunken)
        self.line_147 = QFrame(self.frame_181)
        self.line_147.setObjectName(u"line_147")
        self.line_147.setGeometry(QRect(10, 280, 641, 20))
        self.line_147.setFrameShape(QFrame.HLine)
        self.line_147.setFrameShadow(QFrame.Sunken)
        self.line_148 = QFrame(self.frame_181)
        self.line_148.setObjectName(u"line_148")
        self.line_148.setGeometry(QRect(10, 320, 641, 20))
        self.line_148.setFrameShape(QFrame.HLine)
        self.line_148.setFrameShadow(QFrame.Sunken)
        self.line_149 = QFrame(self.frame_181)
        self.line_149.setObjectName(u"line_149")
        self.line_149.setGeometry(QRect(10, 360, 641, 20))
        self.line_149.setFrameShadow(QFrame.Sunken)
        self.line_149.setFrameShape(QFrame.HLine)
        self.line_150 = QFrame(self.frame_181)
        self.line_150.setObjectName(u"line_150")
        self.line_150.setGeometry(QRect(10, 400, 641, 20))
        self.line_150.setFrameShape(QFrame.HLine)
        self.line_150.setFrameShadow(QFrame.Sunken)
        self.line_151 = QFrame(self.frame_181)
        self.line_151.setObjectName(u"line_151")
        self.line_151.setGeometry(QRect(10, 440, 641, 20))
        self.line_151.setFrameShape(QFrame.HLine)
        self.line_151.setFrameShadow(QFrame.Sunken)
        self.line_152 = QFrame(self.frame_181)
        self.line_152.setObjectName(u"line_152")
        self.line_152.setGeometry(QRect(10, 480, 641, 20))
        self.line_152.setFrameShape(QFrame.HLine)
        self.line_152.setFrameShadow(QFrame.Sunken)
        self.line_153 = QFrame(self.frame_181)
        self.line_153.setObjectName(u"line_153")
        self.line_153.setGeometry(QRect(10, 520, 641, 20))
        self.line_153.setFrameShape(QFrame.HLine)
        self.line_153.setFrameShadow(QFrame.Sunken)
        self.line_154 = QFrame(self.frame_181)
        self.line_154.setObjectName(u"line_154")
        self.line_154.setGeometry(QRect(10, 560, 641, 20))
        self.line_154.setFrameShape(QFrame.HLine)
        self.line_154.setFrameShadow(QFrame.Sunken)
        self.label_635 = QLabel(self.frame_181)
        self.label_635.setObjectName(u"label_635")
        self.label_635.setGeometry(QRect(50, 580, 71, 16))
        self.label_636 = QLabel(self.frame_181)
        self.label_636.setObjectName(u"label_636")
        self.label_636.setGeometry(QRect(120, 580, 49, 16))
        self.label_637 = QLabel(self.frame_181)
        self.label_637.setObjectName(u"label_637")
        self.label_637.setGeometry(QRect(200, 580, 41, 16))
        self.label_638 = QLabel(self.frame_181)
        self.label_638.setObjectName(u"label_638")
        self.label_638.setGeometry(QRect(240, 580, 49, 16))
        self.label_639 = QLabel(self.frame_181)
        self.label_639.setObjectName(u"label_639")
        self.label_639.setGeometry(QRect(370, 580, 81, 16))
        self.label_640 = QLabel(self.frame_181)
        self.label_640.setObjectName(u"label_640")
        self.label_640.setGeometry(QRect(450, 580, 49, 16))
        self.label_641 = QLabel(self.frame_181)
        self.label_641.setObjectName(u"label_641")
        self.label_641.setGeometry(QRect(100, 600, 181, 16))
        self.label_642 = QLabel(self.frame_181)
        self.label_642.setObjectName(u"label_642")
        self.label_642.setGeometry(QRect(50, 600, 51, 16))
        self.label_643 = QLabel(self.frame_181)
        self.label_643.setObjectName(u"label_643")
        self.label_643.setGeometry(QRect(380, 600, 41, 16))
        self.label_644 = QLabel(self.frame_181)
        self.label_644.setObjectName(u"label_644")
        self.label_644.setGeometry(QRect(430, 600, 181, 16))
        self.label_645 = QLabel(self.frame_181)
        self.label_645.setObjectName(u"label_645")
        self.label_645.setGeometry(QRect(50, 620, 131, 16))
        self.label_646 = QLabel(self.frame_181)
        self.label_646.setObjectName(u"label_646")
        self.label_646.setGeometry(QRect(190, 620, 191, 16))
        self.label_647 = QLabel(self.frame_181)
        self.label_647.setObjectName(u"label_647")
        self.label_647.setGeometry(QRect(510, 620, 81, 16))
        self.label_648 = QLabel(self.frame_181)
        self.label_648.setObjectName(u"label_648")
        self.label_648.setGeometry(QRect(450, 620, 61, 16))
        self.label_649 = QLabel(self.frame_181)
        self.label_649.setObjectName(u"label_649")
        self.label_649.setGeometry(QRect(50, 640, 101, 16))
        self.label_650 = QLabel(self.frame_181)
        self.label_650.setObjectName(u"label_650")
        self.label_650.setGeometry(QRect(150, 640, 231, 16))
        self.label_651 = QLabel(self.frame_181)
        self.label_651.setObjectName(u"label_651")
        self.label_651.setGeometry(QRect(510, 640, 81, 16))
        self.label_652 = QLabel(self.frame_181)
        self.label_652.setObjectName(u"label_652")
        self.label_652.setGeometry(QRect(450, 640, 61, 16))
        self.label_653 = QLabel(self.frame_181)
        self.label_653.setObjectName(u"label_653")
        self.label_653.setGeometry(QRect(260, 170, 91, 20))
        self.label_653.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_654 = QLabel(self.frame_181)
        self.label_654.setObjectName(u"label_654")
        self.label_654.setGeometry(QRect(290, 190, 31, 20))
        self.label_654.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_655 = QLabel(self.frame_181)
        self.label_655.setObjectName(u"label_655")
        self.label_655.setGeometry(QRect(370, 170, 101, 20))
        self.label_655.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_656 = QLabel(self.frame_181)
        self.label_656.setObjectName(u"label_656")
        self.label_656.setGeometry(QRect(400, 190, 41, 20))
        self.label_656.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.line_155 = QFrame(self.frame_181)
        self.line_155.setObjectName(u"line_155")
        self.line_155.setGeometry(QRect(470, 180, 20, 381))
        self.line_155.setFrameShape(QFrame.VLine)
        self.line_155.setFrameShadow(QFrame.Sunken)
        self.line_156 = QFrame(self.frame_181)
        self.line_156.setObjectName(u"line_156")
        self.line_156.setGeometry(QRect(540, 180, 20, 381))
        self.line_156.setFrameShape(QFrame.VLine)
        self.line_156.setFrameShadow(QFrame.Sunken)
        self.label_657 = QLabel(self.frame_181)
        self.label_657.setObjectName(u"label_657")
        self.label_657.setGeometry(QRect(170, 40, 31, 16))
        self.label_658 = QLabel(self.frame_181)
        self.label_658.setObjectName(u"label_658")
        self.label_658.setGeometry(QRect(390, 40, 49, 16))
        self.bt_108 = QPushButton(self.frame_181)
        self.bt_108.setObjectName(u"bt_108")
        self.bt_108.setGeometry(QRect(574, 13, 91, 41))
        self.bt_108.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_108.setIcon(icon24)
        self.bt_108.setIconSize(QSize(28, 28))
        self.label_758 = QLabel(self.frame_181)
        self.label_758.setObjectName(u"label_758")
        self.label_758.setGeometry(QRect(160, 230, 71, 16))
        self.label_759 = QLabel(self.frame_181)
        self.label_759.setObjectName(u"label_759")
        self.label_759.setGeometry(QRect(280, 230, 71, 16))
        self.label_760 = QLabel(self.frame_181)
        self.label_760.setObjectName(u"label_760")
        self.label_760.setGeometry(QRect(380, 230, 71, 16))
        self.label_761 = QLabel(self.frame_181)
        self.label_761.setObjectName(u"label_761")
        self.label_761.setGeometry(QRect(490, 230, 51, 16))
        self.label_762 = QLabel(self.frame_181)
        self.label_762.setObjectName(u"label_762")
        self.label_762.setGeometry(QRect(570, 230, 81, 16))
        self.label_763 = QLabel(self.frame_181)
        self.label_763.setObjectName(u"label_763")
        self.label_763.setGeometry(QRect(570, 270, 81, 16))
        self.label_764 = QLabel(self.frame_181)
        self.label_764.setObjectName(u"label_764")
        self.label_764.setGeometry(QRect(380, 270, 71, 16))
        self.label_765 = QLabel(self.frame_181)
        self.label_765.setObjectName(u"label_765")
        self.label_765.setGeometry(QRect(160, 270, 71, 16))
        self.label_766 = QLabel(self.frame_181)
        self.label_766.setObjectName(u"label_766")
        self.label_766.setGeometry(QRect(280, 270, 71, 16))
        self.label_767 = QLabel(self.frame_181)
        self.label_767.setObjectName(u"label_767")
        self.label_767.setGeometry(QRect(490, 270, 51, 16))
        self.label_768 = QLabel(self.frame_181)
        self.label_768.setObjectName(u"label_768")
        self.label_768.setGeometry(QRect(160, 310, 71, 16))
        self.label_769 = QLabel(self.frame_181)
        self.label_769.setObjectName(u"label_769")
        self.label_769.setGeometry(QRect(280, 310, 71, 16))
        self.label_770 = QLabel(self.frame_181)
        self.label_770.setObjectName(u"label_770")
        self.label_770.setGeometry(QRect(490, 310, 51, 16))
        self.label_771 = QLabel(self.frame_181)
        self.label_771.setObjectName(u"label_771")
        self.label_771.setGeometry(QRect(380, 310, 71, 16))
        self.label_772 = QLabel(self.frame_181)
        self.label_772.setObjectName(u"label_772")
        self.label_772.setGeometry(QRect(570, 310, 81, 16))
        self.label_773 = QLabel(self.frame_181)
        self.label_773.setObjectName(u"label_773")
        self.label_773.setGeometry(QRect(380, 350, 71, 16))
        self.label_774 = QLabel(self.frame_181)
        self.label_774.setObjectName(u"label_774")
        self.label_774.setGeometry(QRect(570, 350, 81, 16))
        self.label_775 = QLabel(self.frame_181)
        self.label_775.setObjectName(u"label_775")
        self.label_775.setGeometry(QRect(490, 350, 51, 16))
        self.label_776 = QLabel(self.frame_181)
        self.label_776.setObjectName(u"label_776")
        self.label_776.setGeometry(QRect(160, 350, 71, 16))
        self.label_777 = QLabel(self.frame_181)
        self.label_777.setObjectName(u"label_777")
        self.label_777.setGeometry(QRect(280, 350, 71, 16))
        self.label_778 = QLabel(self.frame_181)
        self.label_778.setObjectName(u"label_778")
        self.label_778.setGeometry(QRect(380, 380, 71, 16))
        self.label_779 = QLabel(self.frame_181)
        self.label_779.setObjectName(u"label_779")
        self.label_779.setGeometry(QRect(570, 380, 81, 16))
        self.label_780 = QLabel(self.frame_181)
        self.label_780.setObjectName(u"label_780")
        self.label_780.setGeometry(QRect(490, 380, 51, 16))
        self.label_781 = QLabel(self.frame_181)
        self.label_781.setObjectName(u"label_781")
        self.label_781.setGeometry(QRect(160, 380, 71, 16))
        self.label_782 = QLabel(self.frame_181)
        self.label_782.setObjectName(u"label_782")
        self.label_782.setGeometry(QRect(280, 380, 71, 16))
        self.label_783 = QLabel(self.frame_181)
        self.label_783.setObjectName(u"label_783")
        self.label_783.setGeometry(QRect(380, 420, 71, 16))
        self.label_784 = QLabel(self.frame_181)
        self.label_784.setObjectName(u"label_784")
        self.label_784.setGeometry(QRect(570, 420, 81, 16))
        self.label_785 = QLabel(self.frame_181)
        self.label_785.setObjectName(u"label_785")
        self.label_785.setGeometry(QRect(490, 420, 51, 16))
        self.label_786 = QLabel(self.frame_181)
        self.label_786.setObjectName(u"label_786")
        self.label_786.setGeometry(QRect(160, 420, 71, 16))
        self.label_787 = QLabel(self.frame_181)
        self.label_787.setObjectName(u"label_787")
        self.label_787.setGeometry(QRect(280, 420, 71, 16))
        self.label_788 = QLabel(self.frame_181)
        self.label_788.setObjectName(u"label_788")
        self.label_788.setGeometry(QRect(380, 460, 71, 16))
        self.label_789 = QLabel(self.frame_181)
        self.label_789.setObjectName(u"label_789")
        self.label_789.setGeometry(QRect(570, 460, 81, 16))
        self.label_790 = QLabel(self.frame_181)
        self.label_790.setObjectName(u"label_790")
        self.label_790.setGeometry(QRect(490, 460, 51, 16))
        self.label_791 = QLabel(self.frame_181)
        self.label_791.setObjectName(u"label_791")
        self.label_791.setGeometry(QRect(160, 460, 71, 16))
        self.label_792 = QLabel(self.frame_181)
        self.label_792.setObjectName(u"label_792")
        self.label_792.setGeometry(QRect(280, 460, 71, 16))
        self.label_793 = QLabel(self.frame_181)
        self.label_793.setObjectName(u"label_793")
        self.label_793.setGeometry(QRect(380, 500, 71, 16))
        self.label_794 = QLabel(self.frame_181)
        self.label_794.setObjectName(u"label_794")
        self.label_794.setGeometry(QRect(570, 500, 81, 16))
        self.label_795 = QLabel(self.frame_181)
        self.label_795.setObjectName(u"label_795")
        self.label_795.setGeometry(QRect(490, 500, 51, 16))
        self.label_796 = QLabel(self.frame_181)
        self.label_796.setObjectName(u"label_796")
        self.label_796.setGeometry(QRect(160, 500, 71, 16))
        self.label_797 = QLabel(self.frame_181)
        self.label_797.setObjectName(u"label_797")
        self.label_797.setGeometry(QRect(280, 500, 71, 16))
        self.label_798 = QLabel(self.frame_181)
        self.label_798.setObjectName(u"label_798")
        self.label_798.setGeometry(QRect(380, 540, 71, 16))
        self.label_799 = QLabel(self.frame_181)
        self.label_799.setObjectName(u"label_799")
        self.label_799.setGeometry(QRect(570, 540, 81, 16))
        self.label_800 = QLabel(self.frame_181)
        self.label_800.setObjectName(u"label_800")
        self.label_800.setGeometry(QRect(490, 540, 51, 16))
        self.label_801 = QLabel(self.frame_181)
        self.label_801.setObjectName(u"label_801")
        self.label_801.setGeometry(QRect(160, 540, 71, 16))
        self.label_802 = QLabel(self.frame_181)
        self.label_802.setObjectName(u"label_802")
        self.label_802.setGeometry(QRect(280, 540, 71, 16))

        self.verticalLayout_145.addWidget(self.frame_181)

        self.tabWidget_5.addTab(self.tab_47, "")
        self.tab_48 = QWidget()
        self.tab_48.setObjectName(u"tab_48")
        self.verticalLayout_144 = QVBoxLayout(self.tab_48)
        self.verticalLayout_144.setSpacing(0)
        self.verticalLayout_144.setObjectName(u"verticalLayout_144")
        self.verticalLayout_144.setContentsMargins(0, 0, 0, 0)
        self.frame_180 = QFrame(self.tab_48)
        self.frame_180.setObjectName(u"frame_180")
        self.frame_180.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(222, 222, 222);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 148, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(0, 213, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_180.setFrameShape(QFrame.StyledPanel)
        self.frame_180.setFrameShadow(QFrame.Raised)
        self.label_551 = QLabel(self.frame_180)
        self.label_551.setObjectName(u"label_551")
        self.label_551.setGeometry(QRect(180, 10, 311, 21))
        self.label_551.setStyleSheet(u"font: 900 14pt \"Roboto\";")
        self.label_551.setAlignment(Qt.AlignCenter)
        self.label_552 = QLabel(self.frame_180)
        self.label_552.setObjectName(u"label_552")
        self.label_552.setGeometry(QRect(210, 40, 141, 16))
        self.label_553 = QLabel(self.frame_180)
        self.label_553.setObjectName(u"label_553")
        self.label_553.setGeometry(QRect(440, 40, 171, 16))
        self.label_554 = QLabel(self.frame_180)
        self.label_554.setObjectName(u"label_554")
        self.label_554.setGeometry(QRect(220, 60, 221, 20))
        self.label_554.setAlignment(Qt.AlignCenter)
        self.label_555 = QLabel(self.frame_180)
        self.label_555.setObjectName(u"label_555")
        self.label_555.setGeometry(QRect(70, 100, 49, 16))
        self.line_123 = QFrame(self.frame_180)
        self.line_123.setObjectName(u"line_123")
        self.line_123.setGeometry(QRect(90, 80, 501, 16))
        self.line_123.setFrameShape(QFrame.HLine)
        self.line_123.setFrameShadow(QFrame.Sunken)
        self.label_556 = QLabel(self.frame_180)
        self.label_556.setObjectName(u"label_556")
        self.label_556.setGeometry(QRect(120, 100, 71, 16))
        self.label_556.setStyleSheet(u"color: rgb(173, 173, 0);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_557 = QLabel(self.frame_180)
        self.label_557.setObjectName(u"label_557")
        self.label_557.setGeometry(QRect(220, 100, 41, 16))
        self.label_558 = QLabel(self.frame_180)
        self.label_558.setObjectName(u"label_558")
        self.label_558.setGeometry(QRect(270, 100, 151, 16))
        self.label_558.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_558.setTextFormat(Qt.AutoText)
        self.label_558.setScaledContents(False)
        self.label_559 = QLabel(self.frame_180)
        self.label_559.setObjectName(u"label_559")
        self.label_559.setGeometry(QRect(80, 140, 91, 16))
        self.label_560 = QLabel(self.frame_180)
        self.label_560.setObjectName(u"label_560")
        self.label_560.setGeometry(QRect(160, 140, 71, 16))
        self.label_561 = QLabel(self.frame_180)
        self.label_561.setObjectName(u"label_561")
        self.label_561.setGeometry(QRect(270, 140, 101, 16))
        self.label_562 = QLabel(self.frame_180)
        self.label_562.setObjectName(u"label_562")
        self.label_562.setGeometry(QRect(370, 140, 61, 16))
        self.label_563 = QLabel(self.frame_180)
        self.label_563.setObjectName(u"label_563")
        self.label_563.setGeometry(QRect(430, 100, 49, 16))
        self.label_564 = QLabel(self.frame_180)
        self.label_564.setObjectName(u"label_564")
        self.label_564.setGeometry(QRect(470, 100, 91, 16))
        self.label_565 = QLabel(self.frame_180)
        self.label_565.setObjectName(u"label_565")
        self.label_565.setGeometry(QRect(460, 140, 49, 16))
        self.label_566 = QLabel(self.frame_180)
        self.label_566.setObjectName(u"label_566")
        self.label_566.setGeometry(QRect(500, 140, 71, 16))
        self.line_124 = QFrame(self.frame_180)
        self.line_124.setObjectName(u"line_124")
        self.line_124.setGeometry(QRect(20, 160, 631, 20))
        self.line_124.setFrameShape(QFrame.HLine)
        self.line_124.setFrameShadow(QFrame.Sunken)
        self.line_125 = QFrame(self.frame_180)
        self.line_125.setObjectName(u"line_125")
        self.line_125.setGeometry(QRect(120, 180, 20, 381))
        self.line_125.setFrameShadow(QFrame.Sunken)
        self.line_125.setFrameShape(QFrame.VLine)
        self.line_126 = QFrame(self.frame_180)
        self.line_126.setObjectName(u"line_126")
        self.line_126.setGeometry(QRect(240, 180, 20, 381))
        self.line_126.setFrameShape(QFrame.VLine)
        self.line_126.setFrameShadow(QFrame.Sunken)
        self.line_127 = QFrame(self.frame_180)
        self.line_127.setObjectName(u"line_127")
        self.line_127.setGeometry(QRect(350, 180, 20, 381))
        self.line_127.setFrameShape(QFrame.VLine)
        self.line_127.setFrameShadow(QFrame.Sunken)
        self.line_128 = QFrame(self.frame_180)
        self.line_128.setObjectName(u"line_128")
        self.line_128.setGeometry(QRect(10, 210, 641, 20))
        self.line_128.setFrameShape(QFrame.HLine)
        self.line_128.setFrameShadow(QFrame.Sunken)
        self.label_567 = QLabel(self.frame_180)
        self.label_567.setObjectName(u"label_567")
        self.label_567.setGeometry(QRect(40, 180, 71, 20))
        self.label_567.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_568 = QLabel(self.frame_180)
        self.label_568.setObjectName(u"label_568")
        self.label_568.setGeometry(QRect(140, 170, 101, 20))
        self.label_568.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_569 = QLabel(self.frame_180)
        self.label_569.setObjectName(u"label_569")
        self.label_569.setGeometry(QRect(170, 190, 31, 20))
        self.label_569.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_570 = QLabel(self.frame_180)
        self.label_570.setObjectName(u"label_570")
        self.label_570.setGeometry(QRect(490, 180, 51, 20))
        self.label_570.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_571 = QLabel(self.frame_180)
        self.label_571.setObjectName(u"label_571")
        self.label_571.setGeometry(QRect(560, 180, 81, 20))
        self.label_571.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_572 = QLabel(self.frame_180)
        self.label_572.setObjectName(u"label_572")
        self.label_572.setGeometry(QRect(10, 220, 101, 16))
        self.label_573 = QLabel(self.frame_180)
        self.label_573.setObjectName(u"label_573")
        self.label_573.setGeometry(QRect(10, 260, 111, 16))
        self.label_574 = QLabel(self.frame_180)
        self.label_574.setObjectName(u"label_574")
        self.label_574.setGeometry(QRect(10, 300, 111, 16))
        self.label_575 = QLabel(self.frame_180)
        self.label_575.setObjectName(u"label_575")
        self.label_575.setGeometry(QRect(10, 340, 111, 16))
        self.label_576 = QLabel(self.frame_180)
        self.label_576.setObjectName(u"label_576")
        self.label_576.setGeometry(QRect(10, 380, 71, 16))
        self.label_577 = QLabel(self.frame_180)
        self.label_577.setObjectName(u"label_577")
        self.label_577.setGeometry(QRect(10, 420, 71, 16))
        self.label_578 = QLabel(self.frame_180)
        self.label_578.setObjectName(u"label_578")
        self.label_578.setGeometry(QRect(10, 460, 81, 16))
        self.label_579 = QLabel(self.frame_180)
        self.label_579.setObjectName(u"label_579")
        self.label_579.setGeometry(QRect(10, 500, 121, 16))
        self.label_580 = QLabel(self.frame_180)
        self.label_580.setObjectName(u"label_580")
        self.label_580.setGeometry(QRect(10, 540, 71, 16))
        self.line_129 = QFrame(self.frame_180)
        self.line_129.setObjectName(u"line_129")
        self.line_129.setGeometry(QRect(10, 240, 641, 20))
        self.line_129.setFrameShape(QFrame.HLine)
        self.line_129.setFrameShadow(QFrame.Sunken)
        self.line_130 = QFrame(self.frame_180)
        self.line_130.setObjectName(u"line_130")
        self.line_130.setGeometry(QRect(10, 280, 641, 20))
        self.line_130.setFrameShape(QFrame.HLine)
        self.line_130.setFrameShadow(QFrame.Sunken)
        self.line_131 = QFrame(self.frame_180)
        self.line_131.setObjectName(u"line_131")
        self.line_131.setGeometry(QRect(10, 320, 641, 20))
        self.line_131.setFrameShape(QFrame.HLine)
        self.line_131.setFrameShadow(QFrame.Sunken)
        self.line_132 = QFrame(self.frame_180)
        self.line_132.setObjectName(u"line_132")
        self.line_132.setGeometry(QRect(10, 360, 641, 20))
        self.line_132.setFrameShadow(QFrame.Sunken)
        self.line_132.setFrameShape(QFrame.HLine)
        self.line_133 = QFrame(self.frame_180)
        self.line_133.setObjectName(u"line_133")
        self.line_133.setGeometry(QRect(10, 400, 641, 20))
        self.line_133.setFrameShape(QFrame.HLine)
        self.line_133.setFrameShadow(QFrame.Sunken)
        self.line_134 = QFrame(self.frame_180)
        self.line_134.setObjectName(u"line_134")
        self.line_134.setGeometry(QRect(10, 440, 641, 20))
        self.line_134.setFrameShape(QFrame.HLine)
        self.line_134.setFrameShadow(QFrame.Sunken)
        self.line_135 = QFrame(self.frame_180)
        self.line_135.setObjectName(u"line_135")
        self.line_135.setGeometry(QRect(10, 480, 641, 20))
        self.line_135.setFrameShape(QFrame.HLine)
        self.line_135.setFrameShadow(QFrame.Sunken)
        self.line_136 = QFrame(self.frame_180)
        self.line_136.setObjectName(u"line_136")
        self.line_136.setGeometry(QRect(10, 520, 641, 20))
        self.line_136.setFrameShape(QFrame.HLine)
        self.line_136.setFrameShadow(QFrame.Sunken)
        self.line_137 = QFrame(self.frame_180)
        self.line_137.setObjectName(u"line_137")
        self.line_137.setGeometry(QRect(10, 560, 641, 20))
        self.line_137.setFrameShape(QFrame.HLine)
        self.line_137.setFrameShadow(QFrame.Sunken)
        self.label_581 = QLabel(self.frame_180)
        self.label_581.setObjectName(u"label_581")
        self.label_581.setGeometry(QRect(50, 580, 71, 16))
        self.label_582 = QLabel(self.frame_180)
        self.label_582.setObjectName(u"label_582")
        self.label_582.setGeometry(QRect(120, 580, 49, 16))
        self.label_583 = QLabel(self.frame_180)
        self.label_583.setObjectName(u"label_583")
        self.label_583.setGeometry(QRect(200, 580, 41, 16))
        self.label_584 = QLabel(self.frame_180)
        self.label_584.setObjectName(u"label_584")
        self.label_584.setGeometry(QRect(240, 580, 49, 16))
        self.label_585 = QLabel(self.frame_180)
        self.label_585.setObjectName(u"label_585")
        self.label_585.setGeometry(QRect(370, 580, 81, 16))
        self.label_586 = QLabel(self.frame_180)
        self.label_586.setObjectName(u"label_586")
        self.label_586.setGeometry(QRect(450, 580, 49, 16))
        self.label_587 = QLabel(self.frame_180)
        self.label_587.setObjectName(u"label_587")
        self.label_587.setGeometry(QRect(100, 600, 181, 16))
        self.label_588 = QLabel(self.frame_180)
        self.label_588.setObjectName(u"label_588")
        self.label_588.setGeometry(QRect(50, 600, 51, 16))
        self.label_589 = QLabel(self.frame_180)
        self.label_589.setObjectName(u"label_589")
        self.label_589.setGeometry(QRect(380, 600, 41, 16))
        self.label_590 = QLabel(self.frame_180)
        self.label_590.setObjectName(u"label_590")
        self.label_590.setGeometry(QRect(430, 600, 181, 16))
        self.label_591 = QLabel(self.frame_180)
        self.label_591.setObjectName(u"label_591")
        self.label_591.setGeometry(QRect(50, 620, 131, 16))
        self.label_592 = QLabel(self.frame_180)
        self.label_592.setObjectName(u"label_592")
        self.label_592.setGeometry(QRect(190, 620, 191, 16))
        self.label_593 = QLabel(self.frame_180)
        self.label_593.setObjectName(u"label_593")
        self.label_593.setGeometry(QRect(510, 620, 81, 16))
        self.label_594 = QLabel(self.frame_180)
        self.label_594.setObjectName(u"label_594")
        self.label_594.setGeometry(QRect(450, 620, 61, 16))
        self.label_595 = QLabel(self.frame_180)
        self.label_595.setObjectName(u"label_595")
        self.label_595.setGeometry(QRect(50, 640, 101, 16))
        self.label_596 = QLabel(self.frame_180)
        self.label_596.setObjectName(u"label_596")
        self.label_596.setGeometry(QRect(150, 640, 231, 16))
        self.label_597 = QLabel(self.frame_180)
        self.label_597.setObjectName(u"label_597")
        self.label_597.setGeometry(QRect(510, 640, 81, 16))
        self.label_598 = QLabel(self.frame_180)
        self.label_598.setObjectName(u"label_598")
        self.label_598.setGeometry(QRect(450, 640, 61, 16))
        self.label_599 = QLabel(self.frame_180)
        self.label_599.setObjectName(u"label_599")
        self.label_599.setGeometry(QRect(260, 170, 91, 20))
        self.label_599.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_600 = QLabel(self.frame_180)
        self.label_600.setObjectName(u"label_600")
        self.label_600.setGeometry(QRect(290, 190, 31, 20))
        self.label_600.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_601 = QLabel(self.frame_180)
        self.label_601.setObjectName(u"label_601")
        self.label_601.setGeometry(QRect(370, 170, 101, 20))
        self.label_601.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_602 = QLabel(self.frame_180)
        self.label_602.setObjectName(u"label_602")
        self.label_602.setGeometry(QRect(400, 190, 41, 20))
        self.label_602.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.line_138 = QFrame(self.frame_180)
        self.line_138.setObjectName(u"line_138")
        self.line_138.setGeometry(QRect(470, 180, 20, 381))
        self.line_138.setFrameShape(QFrame.VLine)
        self.line_138.setFrameShadow(QFrame.Sunken)
        self.line_139 = QFrame(self.frame_180)
        self.line_139.setObjectName(u"line_139")
        self.line_139.setGeometry(QRect(540, 180, 20, 381))
        self.line_139.setFrameShape(QFrame.VLine)
        self.line_139.setFrameShadow(QFrame.Sunken)
        self.label_603 = QLabel(self.frame_180)
        self.label_603.setObjectName(u"label_603")
        self.label_603.setGeometry(QRect(170, 40, 31, 16))
        self.label_604 = QLabel(self.frame_180)
        self.label_604.setObjectName(u"label_604")
        self.label_604.setGeometry(QRect(390, 40, 49, 16))
        self.bt_107 = QPushButton(self.frame_180)
        self.bt_107.setObjectName(u"bt_107")
        self.bt_107.setGeometry(QRect(574, 13, 91, 41))
        self.bt_107.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_107.setIcon(icon24)
        self.bt_107.setIconSize(QSize(28, 28))
        self.label_803 = QLabel(self.frame_180)
        self.label_803.setObjectName(u"label_803")
        self.label_803.setGeometry(QRect(380, 230, 71, 16))
        self.label_804 = QLabel(self.frame_180)
        self.label_804.setObjectName(u"label_804")
        self.label_804.setGeometry(QRect(570, 230, 81, 16))
        self.label_805 = QLabel(self.frame_180)
        self.label_805.setObjectName(u"label_805")
        self.label_805.setGeometry(QRect(490, 230, 51, 16))
        self.label_806 = QLabel(self.frame_180)
        self.label_806.setObjectName(u"label_806")
        self.label_806.setGeometry(QRect(160, 230, 71, 16))
        self.label_807 = QLabel(self.frame_180)
        self.label_807.setObjectName(u"label_807")
        self.label_807.setGeometry(QRect(280, 230, 71, 16))
        self.label_808 = QLabel(self.frame_180)
        self.label_808.setObjectName(u"label_808")
        self.label_808.setGeometry(QRect(380, 260, 71, 16))
        self.label_809 = QLabel(self.frame_180)
        self.label_809.setObjectName(u"label_809")
        self.label_809.setGeometry(QRect(570, 260, 81, 16))
        self.label_810 = QLabel(self.frame_180)
        self.label_810.setObjectName(u"label_810")
        self.label_810.setGeometry(QRect(490, 260, 51, 16))
        self.label_811 = QLabel(self.frame_180)
        self.label_811.setObjectName(u"label_811")
        self.label_811.setGeometry(QRect(160, 260, 71, 16))
        self.label_812 = QLabel(self.frame_180)
        self.label_812.setObjectName(u"label_812")
        self.label_812.setGeometry(QRect(280, 260, 71, 16))
        self.label_813 = QLabel(self.frame_180)
        self.label_813.setObjectName(u"label_813")
        self.label_813.setGeometry(QRect(380, 300, 71, 16))
        self.label_814 = QLabel(self.frame_180)
        self.label_814.setObjectName(u"label_814")
        self.label_814.setGeometry(QRect(570, 300, 81, 16))
        self.label_815 = QLabel(self.frame_180)
        self.label_815.setObjectName(u"label_815")
        self.label_815.setGeometry(QRect(490, 300, 51, 16))
        self.label_816 = QLabel(self.frame_180)
        self.label_816.setObjectName(u"label_816")
        self.label_816.setGeometry(QRect(160, 300, 71, 16))
        self.label_817 = QLabel(self.frame_180)
        self.label_817.setObjectName(u"label_817")
        self.label_817.setGeometry(QRect(280, 300, 71, 16))
        self.label_818 = QLabel(self.frame_180)
        self.label_818.setObjectName(u"label_818")
        self.label_818.setGeometry(QRect(380, 340, 71, 16))
        self.label_819 = QLabel(self.frame_180)
        self.label_819.setObjectName(u"label_819")
        self.label_819.setGeometry(QRect(570, 340, 81, 16))
        self.label_820 = QLabel(self.frame_180)
        self.label_820.setObjectName(u"label_820")
        self.label_820.setGeometry(QRect(490, 340, 51, 16))
        self.label_821 = QLabel(self.frame_180)
        self.label_821.setObjectName(u"label_821")
        self.label_821.setGeometry(QRect(160, 340, 71, 16))
        self.label_822 = QLabel(self.frame_180)
        self.label_822.setObjectName(u"label_822")
        self.label_822.setGeometry(QRect(280, 340, 71, 16))
        self.label_823 = QLabel(self.frame_180)
        self.label_823.setObjectName(u"label_823")
        self.label_823.setGeometry(QRect(380, 380, 71, 16))
        self.label_824 = QLabel(self.frame_180)
        self.label_824.setObjectName(u"label_824")
        self.label_824.setGeometry(QRect(570, 380, 81, 16))
        self.label_825 = QLabel(self.frame_180)
        self.label_825.setObjectName(u"label_825")
        self.label_825.setGeometry(QRect(490, 380, 51, 16))
        self.label_826 = QLabel(self.frame_180)
        self.label_826.setObjectName(u"label_826")
        self.label_826.setGeometry(QRect(160, 380, 71, 16))
        self.label_827 = QLabel(self.frame_180)
        self.label_827.setObjectName(u"label_827")
        self.label_827.setGeometry(QRect(280, 380, 71, 16))
        self.label_828 = QLabel(self.frame_180)
        self.label_828.setObjectName(u"label_828")
        self.label_828.setGeometry(QRect(380, 420, 71, 16))
        self.label_829 = QLabel(self.frame_180)
        self.label_829.setObjectName(u"label_829")
        self.label_829.setGeometry(QRect(570, 420, 81, 16))
        self.label_830 = QLabel(self.frame_180)
        self.label_830.setObjectName(u"label_830")
        self.label_830.setGeometry(QRect(490, 420, 51, 16))
        self.label_831 = QLabel(self.frame_180)
        self.label_831.setObjectName(u"label_831")
        self.label_831.setGeometry(QRect(160, 420, 71, 16))
        self.label_832 = QLabel(self.frame_180)
        self.label_832.setObjectName(u"label_832")
        self.label_832.setGeometry(QRect(280, 420, 71, 16))
        self.label_833 = QLabel(self.frame_180)
        self.label_833.setObjectName(u"label_833")
        self.label_833.setGeometry(QRect(380, 460, 71, 16))
        self.label_834 = QLabel(self.frame_180)
        self.label_834.setObjectName(u"label_834")
        self.label_834.setGeometry(QRect(570, 460, 81, 16))
        self.label_835 = QLabel(self.frame_180)
        self.label_835.setObjectName(u"label_835")
        self.label_835.setGeometry(QRect(490, 460, 51, 16))
        self.label_836 = QLabel(self.frame_180)
        self.label_836.setObjectName(u"label_836")
        self.label_836.setGeometry(QRect(160, 460, 71, 16))
        self.label_837 = QLabel(self.frame_180)
        self.label_837.setObjectName(u"label_837")
        self.label_837.setGeometry(QRect(280, 460, 71, 16))
        self.label_838 = QLabel(self.frame_180)
        self.label_838.setObjectName(u"label_838")
        self.label_838.setGeometry(QRect(380, 500, 71, 16))
        self.label_839 = QLabel(self.frame_180)
        self.label_839.setObjectName(u"label_839")
        self.label_839.setGeometry(QRect(570, 500, 81, 16))
        self.label_840 = QLabel(self.frame_180)
        self.label_840.setObjectName(u"label_840")
        self.label_840.setGeometry(QRect(490, 500, 51, 16))
        self.label_841 = QLabel(self.frame_180)
        self.label_841.setObjectName(u"label_841")
        self.label_841.setGeometry(QRect(160, 500, 71, 16))
        self.label_842 = QLabel(self.frame_180)
        self.label_842.setObjectName(u"label_842")
        self.label_842.setGeometry(QRect(280, 500, 71, 16))
        self.label_843 = QLabel(self.frame_180)
        self.label_843.setObjectName(u"label_843")
        self.label_843.setGeometry(QRect(380, 540, 71, 16))
        self.label_844 = QLabel(self.frame_180)
        self.label_844.setObjectName(u"label_844")
        self.label_844.setGeometry(QRect(570, 540, 81, 16))
        self.label_845 = QLabel(self.frame_180)
        self.label_845.setObjectName(u"label_845")
        self.label_845.setGeometry(QRect(490, 540, 51, 16))
        self.label_846 = QLabel(self.frame_180)
        self.label_846.setObjectName(u"label_846")
        self.label_846.setGeometry(QRect(160, 540, 71, 16))
        self.label_847 = QLabel(self.frame_180)
        self.label_847.setObjectName(u"label_847")
        self.label_847.setGeometry(QRect(280, 540, 71, 16))

        self.verticalLayout_144.addWidget(self.frame_180)

        self.tabWidget_5.addTab(self.tab_48, "")

        self.verticalLayout_38.addWidget(self.tabWidget_5)


        self.horizontalLayout_14.addWidget(self.frame_44)

        self.horizontalLayout_14.setStretch(0, 2)
        self.horizontalLayout_14.setStretch(1, 8)
        self.tabWidget_4.addTab(self.tab_10, "")
        self.tab_14 = QWidget()
        self.tab_14.setObjectName(u"tab_14")
        self.verticalLayout_39 = QVBoxLayout(self.tab_14)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.frame_46 = QFrame(self.tab_14)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_46)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.frame_50 = QFrame(self.frame_46)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.groupBox_10 = QGroupBox(self.frame_50)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QComboBox{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QDateEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 900 12pt \"Roboto Black\";\n"
"}")
        self.horizontalLayout_19 = QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.frame_53 = QFrame(self.groupBox_10)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.NoFrame)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.label_116 = QLabel(self.frame_53)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setGeometry(QRect(20, 250, 81, 31))
        self.lineEdit_32 = QLineEdit(self.frame_53)
        self.lineEdit_32.setObjectName(u"lineEdit_32")
        self.lineEdit_32.setGeometry(QRect(110, 150, 161, 31))
        self.lineEdit_32.setClearButtonEnabled(True)
        self.comboBox_16 = QComboBox(self.frame_53)
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.setObjectName(u"comboBox_16")
        self.comboBox_16.setGeometry(QRect(100, 50, 171, 31))
        self.label_115 = QLabel(self.frame_53)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setGeometry(QRect(0, 0, 101, 31))
        self.lineEdit_31 = QLineEdit(self.frame_53)
        self.lineEdit_31.setObjectName(u"lineEdit_31")
        self.lineEdit_31.setGeometry(QRect(100, 200, 171, 31))
        self.lineEdit_31.setClearButtonEnabled(True)
        self.label_111 = QLabel(self.frame_53)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setGeometry(QRect(20, 200, 81, 31))
        self.label_114 = QLabel(self.frame_53)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setGeometry(QRect(0, 150, 101, 31))
        self.label_112 = QLabel(self.frame_53)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setGeometry(QRect(10, 100, 61, 31))
        self.comboBox_17 = QComboBox(self.frame_53)
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.comboBox_17.setObjectName(u"comboBox_17")
        self.comboBox_17.setGeometry(QRect(100, 100, 171, 31))
        self.lineEdit_33 = QLineEdit(self.frame_53)
        self.lineEdit_33.setObjectName(u"lineEdit_33")
        self.lineEdit_33.setGeometry(QRect(100, 0, 171, 31))
        self.lineEdit_33.setClearButtonEnabled(True)
        self.label_113 = QLabel(self.frame_53)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setGeometry(QRect(10, 50, 51, 31))
        self.lineEdit_56 = QLineEdit(self.frame_53)
        self.lineEdit_56.setObjectName(u"lineEdit_56")
        self.lineEdit_56.setGeometry(QRect(100, 250, 171, 31))
        self.lineEdit_56.setClearButtonEnabled(True)

        self.horizontalLayout_19.addWidget(self.frame_53)

        self.frame_54 = QFrame(self.groupBox_10)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMaximumSize(QSize(120, 500))
        self.frame_54.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(158, 158, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(255, 255, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_54.setFrameShape(QFrame.NoFrame)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.bt_33 = QPushButton(self.frame_54)
        self.bt_33.setObjectName(u"bt_33")
        self.bt_33.setGeometry(QRect(20, 170, 91, 30))
        self.bt_33.setMaximumSize(QSize(120, 30))
        self.bt_33.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_33.setIcon(icon20)
        self.bt_33.setIconSize(QSize(20, 20))
        self.bt_32 = QPushButton(self.frame_54)
        self.bt_32.setObjectName(u"bt_32")
        self.bt_32.setGeometry(QRect(20, 120, 89, 30))
        self.bt_32.setMaximumSize(QSize(120, 30))
        self.bt_32.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_32.setIcon(icon22)
        self.bt_32.setIconSize(QSize(20, 20))
        self.bt_31 = QPushButton(self.frame_54)
        self.bt_31.setObjectName(u"bt_31")
        self.bt_31.setGeometry(QRect(20, 70, 91, 30))
        self.bt_31.setMaximumSize(QSize(120, 30))
        self.bt_31.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_31.setIcon(icon17)
        self.bt_31.setIconSize(QSize(20, 20))
        self.bt_115 = QPushButton(self.frame_54)
        self.bt_115.setObjectName(u"bt_115")
        self.bt_115.setGeometry(QRect(20, 230, 91, 30))
        self.bt_115.setMaximumSize(QSize(120, 30))
        self.bt_115.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_115.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(158, 158, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(0, 170, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.bt_115.setIcon(icon21)
        self.bt_115.setIconSize(QSize(20, 20))

        self.horizontalLayout_19.addWidget(self.frame_54)


        self.horizontalLayout_18.addWidget(self.groupBox_10)

        self.groupBox_11 = QGroupBox(self.frame_50)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QComboBox{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QDateEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 900 12pt \"Roboto Black\";\n"
"}")
        self.verticalLayout_42 = QVBoxLayout(self.groupBox_11)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.frame_55 = QFrame(self.groupBox_11)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.label_118 = QLabel(self.frame_55)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setGeometry(QRect(40, 60, 51, 31))
        self.lineEdit_34 = QLineEdit(self.frame_55)
        self.lineEdit_34.setObjectName(u"lineEdit_34")
        self.lineEdit_34.setGeometry(QRect(130, 10, 171, 31))
        self.lineEdit_34.setClearButtonEnabled(True)
        self.comboBox_18 = QComboBox(self.frame_55)
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.setObjectName(u"comboBox_18")
        self.comboBox_18.setGeometry(QRect(130, 60, 171, 31))
        self.label_117 = QLabel(self.frame_55)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setGeometry(QRect(50, 190, 81, 31))
        self.lineEdit_35 = QLineEdit(self.frame_55)
        self.lineEdit_35.setObjectName(u"lineEdit_35")
        self.lineEdit_35.setGeometry(QRect(130, 140, 171, 31))
        self.lineEdit_35.setClearButtonEnabled(True)
        self.label_120 = QLabel(self.frame_55)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setGeometry(QRect(20, 140, 111, 31))
        self.label_119 = QLabel(self.frame_55)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setGeometry(QRect(30, 10, 101, 31))
        self.lineEdit_57 = QLineEdit(self.frame_55)
        self.lineEdit_57.setObjectName(u"lineEdit_57")
        self.lineEdit_57.setGeometry(QRect(130, 190, 171, 31))
        self.lineEdit_57.setClearButtonEnabled(True)
        self.comboBox_31 = QComboBox(self.frame_55)
        self.comboBox_31.addItem("")
        self.comboBox_31.addItem("")
        self.comboBox_31.setObjectName(u"comboBox_31")
        self.comboBox_31.setGeometry(QRect(130, 100, 171, 31))
        self.label_126 = QLabel(self.frame_55)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setGeometry(QRect(10, 100, 111, 31))
        self.bt_114 = QPushButton(self.frame_55)
        self.bt_114.setObjectName(u"bt_114")
        self.bt_114.setGeometry(QRect(350, 190, 80, 30))
        self.bt_114.setMaximumSize(QSize(120, 30))
        self.bt_114.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_114.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(158, 158, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(0, 170, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.bt_114.setIcon(icon24)
        self.bt_114.setIconSize(QSize(20, 20))
        self.bt_118 = QPushButton(self.frame_55)
        self.bt_118.setObjectName(u"bt_118")
        self.bt_118.setGeometry(QRect(330, 70, 91, 30))
        self.bt_118.setMaximumSize(QSize(120, 30))
        self.bt_118.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_118.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(158, 158, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(0, 170, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.bt_118.setIcon(icon21)
        self.bt_118.setIconSize(QSize(20, 20))

        self.verticalLayout_42.addWidget(self.frame_55)

        self.frame_56 = QFrame(self.groupBox_11)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(158, 158, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(255, 255, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.bt_34 = QPushButton(self.frame_56)
        self.bt_34.setObjectName(u"bt_34")
        self.bt_34.setGeometry(QRect(80, 20, 80, 30))
        self.bt_34.setMaximumSize(QSize(120, 30))
        self.bt_34.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_34.setIcon(icon17)
        self.bt_34.setIconSize(QSize(20, 20))
        self.bt_35 = QPushButton(self.frame_56)
        self.bt_35.setObjectName(u"bt_35")
        self.bt_35.setGeometry(QRect(180, 20, 89, 30))
        self.bt_35.setMaximumSize(QSize(120, 30))
        self.bt_35.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_35.setIcon(icon22)
        self.bt_35.setIconSize(QSize(20, 20))
        self.bt_36 = QPushButton(self.frame_56)
        self.bt_36.setObjectName(u"bt_36")
        self.bt_36.setGeometry(QRect(280, 20, 80, 30))
        self.bt_36.setMaximumSize(QSize(120, 30))
        self.bt_36.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_36.setIcon(icon20)
        self.bt_36.setIconSize(QSize(20, 20))

        self.verticalLayout_42.addWidget(self.frame_56)

        self.verticalLayout_42.setStretch(0, 8)
        self.verticalLayout_42.setStretch(1, 2)

        self.horizontalLayout_18.addWidget(self.groupBox_11)


        self.verticalLayout_40.addWidget(self.frame_50)

        self.frame_51 = QFrame(self.frame_46)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(158, 158, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(255, 255, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_51)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.frame_52 = QFrame(self.frame_51)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.frame_57 = QFrame(self.frame_52)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_57)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.tableWidget_5 = QTableWidget(self.frame_57)
        if (self.tableWidget_5.columnCount() < 6):
            self.tableWidget_5.setColumnCount(6)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(4, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(5, __qtablewidgetitem36)
        self.tableWidget_5.setObjectName(u"tableWidget_5")
        self.tableWidget_5.setStyleSheet(u"background-color: rgb(191, 191, 191);")

        self.verticalLayout_44.addWidget(self.tableWidget_5)


        self.horizontalLayout_20.addWidget(self.frame_57)

        self.frame_58 = QFrame(self.frame_52)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_58)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.tableWidget_6 = QTableWidget(self.frame_58)
        if (self.tableWidget_6.columnCount() < 5):
            self.tableWidget_6.setColumnCount(5)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(2, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(3, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(4, __qtablewidgetitem41)
        self.tableWidget_6.setObjectName(u"tableWidget_6")
        self.tableWidget_6.setStyleSheet(u"background-color: rgb(191, 191, 191);")

        self.verticalLayout_43.addWidget(self.tableWidget_6)


        self.horizontalLayout_20.addWidget(self.frame_58)


        self.verticalLayout_41.addWidget(self.frame_52)

        self.pushButton = QPushButton(self.frame_51)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(120, 30))
        self.pushButton.setMaximumSize(QSize(120, 60))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon25 = QIcon()
        icon25.addFile(u":/icons/assets/buttons/loader.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon25)
        self.pushButton.setIconSize(QSize(20, 20))

        self.verticalLayout_41.addWidget(self.pushButton, 0, Qt.AlignHCenter)


        self.verticalLayout_40.addWidget(self.frame_51)

        self.verticalLayout_40.setStretch(0, 5)
        self.verticalLayout_40.setStretch(1, 5)

        self.verticalLayout_39.addWidget(self.frame_46)

        self.tabWidget_4.addTab(self.tab_14, "")
        self.tab_15 = QWidget()
        self.tab_15.setObjectName(u"tab_15")
        self.verticalLayout_45 = QVBoxLayout(self.tab_15)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.frame_60 = QFrame(self.tab_15)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setStyleSheet(u"QPlainTextEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_60)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.frame_61 = QFrame(self.frame_60)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 900 12pt \"Roboto Black\";\n"
"}")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.lineEdit_36 = QLineEdit(self.frame_61)
        self.lineEdit_36.setObjectName(u"lineEdit_36")
        self.lineEdit_36.setGeometry(QRect(170, 10, 181, 31))
        self.label_121 = QLabel(self.frame_61)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setGeometry(QRect(30, 20, 141, 16))
        self.label_122 = QLabel(self.frame_61)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setGeometry(QRect(600, 20, 31, 16))
        self.lineEdit_37 = QLineEdit(self.frame_61)
        self.lineEdit_37.setObjectName(u"lineEdit_37")
        self.lineEdit_37.setGeometry(QRect(640, 10, 181, 31))

        self.verticalLayout_46.addWidget(self.frame_61)

        self.plainTextEdit = QPlainTextEdit(self.frame_60)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout_46.addWidget(self.plainTextEdit)

        self.verticalLayout_46.setStretch(0, 1)
        self.verticalLayout_46.setStretch(1, 8)

        self.verticalLayout_45.addWidget(self.frame_60)

        self.frame_59 = QFrame(self.tab_15)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 107, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(0, 170, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.frame_62 = QFrame(self.frame_59)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setMinimumSize(QSize(300, 100))
        self.frame_62.setMaximumSize(QSize(300, 100))
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_62)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.bt_37 = QPushButton(self.frame_62)
        self.bt_37.setObjectName(u"bt_37")
        self.bt_37.setMinimumSize(QSize(120, 30))
        self.bt_37.setMaximumSize(QSize(120, 40))

        self.verticalLayout_47.addWidget(self.bt_37)


        self.horizontalLayout_21.addWidget(self.frame_62, 0, Qt.AlignHCenter)


        self.verticalLayout_45.addWidget(self.frame_59)

        self.verticalLayout_45.setStretch(0, 8)
        self.verticalLayout_45.setStretch(1, 2)
        self.tabWidget_4.addTab(self.tab_15, "")
        self.tab_53 = QWidget()
        self.tab_53.setObjectName(u"tab_53")
        self.verticalLayout_157 = QVBoxLayout(self.tab_53)
        self.verticalLayout_157.setObjectName(u"verticalLayout_157")
        self.frame_199 = QFrame(self.tab_53)
        self.frame_199.setObjectName(u"frame_199")
        self.frame_199.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 900 12pt \"Roboto Black\";\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(158, 158, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(170, 170, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_199.setFrameShape(QFrame.StyledPanel)
        self.frame_199.setFrameShadow(QFrame.Raised)
        self.lineEdit_2 = QLineEdit(self.frame_199)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(220, 260, 181, 51))
        self.label_73 = QLabel(self.frame_199)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setGeometry(QRect(100, 280, 111, 20))
        self.label_74 = QLabel(self.frame_199)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setGeometry(QRect(130, 350, 91, 20))
        self.lineEdit_3 = QLineEdit(self.frame_199)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(220, 330, 181, 51))
        self.comboBox_30 = QComboBox(self.frame_199)
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.setObjectName(u"comboBox_30")
        self.comboBox_30.setGeometry(QRect(230, 190, 171, 41))
        self.comboBox_30.setCursor(QCursor(Qt.OpenHandCursor))
        self.label_75 = QLabel(self.frame_199)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setGeometry(QRect(100, 200, 121, 20))
        self.line_13 = QFrame(self.frame_199)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setGeometry(QRect(450, 0, 20, 661))
        self.line_13.setFrameShape(QFrame.VLine)
        self.line_13.setFrameShadow(QFrame.Sunken)
        self.label_76 = QLabel(self.frame_199)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setGeometry(QRect(490, 40, 121, 31))
        self.label_77 = QLabel(self.frame_199)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setGeometry(QRect(640, 40, 211, 31))
        self.label_77.setStyleSheet(u"color: rgb(135, 68, 0);\n"
"background-color: rgb(185, 185, 185);\n"
"font: 900 12pt \"Roboto\";")
        self.label_77.setAlignment(Qt.AlignCenter)
        self.label_78 = QLabel(self.frame_199)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setGeometry(QRect(640, 80, 211, 31))
        self.label_78.setStyleSheet(u"color: rgb(135, 68, 0);\n"
"background-color: rgb(185, 185, 185);\n"
"font: 900 12pt \"Roboto\";")
        self.label_78.setAlignment(Qt.AlignCenter)
        self.label_79 = QLabel(self.frame_199)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setGeometry(QRect(490, 80, 121, 31))
        self.line_14 = QFrame(self.frame_199)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setGeometry(QRect(457, 133, 411, 20))
        self.line_14.setFrameShape(QFrame.HLine)
        self.line_14.setFrameShadow(QFrame.Sunken)
        self.line_15 = QFrame(self.frame_199)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setGeometry(QRect(680, 300, 21, 171))
        self.line_15.setFrameShape(QFrame.VLine)
        self.line_15.setFrameShadow(QFrame.Sunken)
        self.line_16 = QFrame(self.frame_199)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setGeometry(QRect(457, 470, 401, 20))
        self.line_16.setFrameShape(QFrame.HLine)
        self.line_16.setFrameShadow(QFrame.Sunken)
        self.line_17 = QFrame(self.frame_199)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setGeometry(QRect(553, 490, 20, 171))
        self.line_17.setFrameShape(QFrame.VLine)
        self.line_17.setFrameShadow(QFrame.Sunken)
        self.line_29 = QFrame(self.frame_199)
        self.line_29.setObjectName(u"line_29")
        self.line_29.setGeometry(QRect(560, 616, 301, 16))
        self.line_29.setFrameShape(QFrame.HLine)
        self.line_29.setFrameShadow(QFrame.Sunken)
        self.label_80 = QLabel(self.frame_199)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setGeometry(QRect(490, 290, 161, 31))
        self.label_81 = QLabel(self.frame_199)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setGeometry(QRect(490, 340, 161, 31))
        self.label_82 = QLabel(self.frame_199)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setGeometry(QRect(490, 390, 161, 31))
        self.label_83 = QLabel(self.frame_199)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setGeometry(QRect(490, 430, 161, 31))
        self.label_84 = QLabel(self.frame_199)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setGeometry(QRect(490, 580, 51, 31))
        self.label_85 = QLabel(self.frame_199)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setGeometry(QRect(580, 630, 91, 31))
        self.label_86 = QLabel(self.frame_199)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setGeometry(QRect(570, 540, 111, 31))
        self.label_87 = QLabel(self.frame_199)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setGeometry(QRect(570, 590, 101, 31))
        self.label_88 = QLabel(self.frame_199)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setGeometry(QRect(570, 490, 101, 31))
        self.label_89 = QLabel(self.frame_199)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setGeometry(QRect(720, 290, 161, 31))
        self.label_89.setStyleSheet(u"color: rgb(229, 153, 0);")
        self.label_89.setAlignment(Qt.AlignCenter)
        self.label_90 = QLabel(self.frame_199)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setGeometry(QRect(720, 340, 161, 31))
        self.label_90.setStyleSheet(u"color: rgb(229, 153, 0);")
        self.label_90.setAlignment(Qt.AlignCenter)
        self.label_91 = QLabel(self.frame_199)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setGeometry(QRect(720, 390, 161, 31))
        self.label_91.setStyleSheet(u"color: rgb(229, 153, 0);")
        self.label_91.setAlignment(Qt.AlignCenter)
        self.label_92 = QLabel(self.frame_199)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setGeometry(QRect(700, 440, 201, 31))
        self.label_92.setStyleSheet(u"color: rgb(166, 166, 166);\n"
"background-color: rgb(170, 0, 0);\n"
"font: 900 12pt \"Roboto\";")
        self.label_92.setAlignment(Qt.AlignCenter)
        self.label_93 = QLabel(self.frame_199)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setGeometry(QRect(690, 490, 211, 31))
        self.label_93.setStyleSheet(u"color: rgb(0, 170, 0);\n"
"font: 900 12pt \"Roboto\";")
        self.label_93.setAlignment(Qt.AlignCenter)
        self.label_94 = QLabel(self.frame_199)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setGeometry(QRect(690, 540, 211, 31))
        self.label_94.setStyleSheet(u"color: rgb(0, 170, 0);\n"
"font: 900 12pt \"Roboto\";")
        self.label_94.setAlignment(Qt.AlignCenter)
        self.label_95 = QLabel(self.frame_199)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setGeometry(QRect(690, 590, 211, 31))
        self.label_95.setStyleSheet(u"color: rgb(0, 170, 0);\n"
"font: 900 12pt \"Roboto\";")
        self.label_95.setAlignment(Qt.AlignCenter)
        self.label_96 = QLabel(self.frame_199)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setGeometry(QRect(680, 630, 211, 31))
        self.label_96.setStyleSheet(u"background-color: rgb(156, 78, 0);\n"
"color: rgb(188, 188, 188);\n"
"font: 900 12pt \"Roboto\";")
        self.label_96.setAlignment(Qt.AlignCenter)
        self.line_39 = QFrame(self.frame_199)
        self.line_39.setObjectName(u"line_39")
        self.line_39.setGeometry(QRect(460, 420, 441, 16))
        self.line_39.setFrameShape(QFrame.HLine)
        self.line_39.setFrameShadow(QFrame.Sunken)
        self.line_40 = QFrame(self.frame_199)
        self.line_40.setObjectName(u"line_40")
        self.line_40.setGeometry(QRect(460, 370, 441, 16))
        self.line_40.setFrameShape(QFrame.HLine)
        self.line_40.setFrameShadow(QFrame.Sunken)
        self.line_41 = QFrame(self.frame_199)
        self.line_41.setObjectName(u"line_41")
        self.line_41.setGeometry(QRect(460, 320, 441, 16))
        self.line_41.setFrameShape(QFrame.HLine)
        self.line_41.setFrameShadow(QFrame.Sunken)
        self.label_97 = QLabel(self.frame_199)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setGeometry(QRect(110, 20, 201, 61))
        self.label_97.setAlignment(Qt.AlignCenter)
        self.pushButton_20 = QPushButton(self.frame_199)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setGeometry(QRect(10, 450, 191, 61))
        self.pushButton_20.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_21 = QPushButton(self.frame_199)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setGeometry(QRect(230, 450, 191, 61))
        self.pushButton_21.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_22 = QPushButton(self.frame_199)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setGeometry(QRect(140, 540, 191, 61))
        self.pushButton_22.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_157.addWidget(self.frame_199)

        self.tabWidget_4.addTab(self.tab_53, "")

        self.verticalLayout_14.addWidget(self.tabWidget_4)


        self.horizontalLayout_3.addWidget(self.frame_11)

        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 8)

        self.horizontalLayout_2.addWidget(self.frame_8)

        self.tabWidget_3.addTab(self.tab_5, "")

        self.verticalLayout_7.addWidget(self.tabWidget_3)


        self.verticalLayout_5.addWidget(self.frame_3)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_16 = QWidget()
        self.tab_16.setObjectName(u"tab_16")
        self.verticalLayout_92 = QVBoxLayout(self.tab_16)
        self.verticalLayout_92.setSpacing(0)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.verticalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.frame_63 = QFrame(self.tab_16)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_63)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_6 = QTabWidget(self.frame_63)
        self.tabWidget_6.setObjectName(u"tabWidget_6")
        self.tabWidget_6.setStyleSheet(u"background-color: rgb(108, 170, 144);")
        self.tab_17 = QWidget()
        self.tab_17.setObjectName(u"tab_17")
        self.verticalLayout_49 = QVBoxLayout(self.tab_17)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.frame_64 = QFrame(self.tab_17)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_64)
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.label_123 = QLabel(self.frame_64)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 20pt \"Poppins Black\";")
        self.label_123.setAlignment(Qt.AlignCenter)

        self.verticalLayout_50.addWidget(self.label_123)

        self.label_124 = QLabel(self.frame_64)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setPixmap(QPixmap(u"assets/imgs/cover31.jpg"))
        self.label_124.setScaledContents(True)

        self.verticalLayout_50.addWidget(self.label_124)


        self.verticalLayout_49.addWidget(self.frame_64)

        self.frame_65 = QFrame(self.tab_17)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setStyleSheet(u"QPushButton {\n"
"	border-top-left-radius: 15px;\n"
"	background-color: rgb(213, 156, 53);\n"
"	font: 700 11pt \"Segoe UI\";\n"
"	color: rgb(48, 48, 48);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffd495, stop: 0.7 #ffad76, stop: 1.0 #ffb665);\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_65.setFrameShape(QFrame.NoFrame)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_65)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.bt_38 = QPushButton(self.frame_65)
        self.bt_38.setObjectName(u"bt_38")
        self.bt_38.setMinimumSize(QSize(120, 30))
        self.bt_38.setMaximumSize(QSize(120, 120))
        self.bt_38.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_38.setIcon(icon7)
        self.bt_38.setIconSize(QSize(30, 30))

        self.verticalLayout_51.addWidget(self.bt_38, 0, Qt.AlignHCenter)


        self.verticalLayout_49.addWidget(self.frame_65)

        self.verticalLayout_49.setStretch(0, 8)
        self.verticalLayout_49.setStretch(1, 2)
        self.tabWidget_6.addTab(self.tab_17, "")
        self.tab_18 = QWidget()
        self.tab_18.setObjectName(u"tab_18")
        self.horizontalLayout_22 = QHBoxLayout(self.tab_18)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_66 = QFrame(self.tab_18)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_66)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_67 = QFrame(self.frame_66)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.frame_67)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.frame_68 = QFrame(self.frame_67)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(163, 82, 0);\n"
"}\n"
"QPushButton {\n"
"border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_68)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.frame_191 = QFrame(self.frame_68)
        self.frame_191.setObjectName(u"frame_191")
        self.frame_191.setMaximumSize(QSize(200, 195))
        self.frame_191.setFrameShape(QFrame.StyledPanel)
        self.frame_191.setFrameShadow(QFrame.Raised)
        self.verticalLayout_155 = QVBoxLayout(self.frame_191)
        self.verticalLayout_155.setSpacing(0)
        self.verticalLayout_155.setObjectName(u"verticalLayout_155")
        self.verticalLayout_155.setContentsMargins(0, 0, 0, 0)
        self.frame_192 = QFrame(self.frame_191)
        self.frame_192.setObjectName(u"frame_192")
        self.frame_192.setFrameShape(QFrame.StyledPanel)
        self.frame_192.setFrameShadow(QFrame.Raised)
        self.label_61 = QLabel(self.frame_192)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setGeometry(QRect(-2, 0, 181, 20))
        self.label_61.setFont(font)
        self.label_62 = QLabel(self.frame_192)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setGeometry(QRect(0, 10, 191, 51))
        self.label_62.setStyleSheet(u"color: rgb(255, 62, 23);\n"
"background-color:transparent;\n"
"font: 900 14pt \"Poppins Black\";")
        self.label_62.setAlignment(Qt.AlignCenter)

        self.verticalLayout_155.addWidget(self.frame_192)

        self.frame_193 = QFrame(self.frame_191)
        self.frame_193.setObjectName(u"frame_193")
        self.frame_193.setFrameShape(QFrame.StyledPanel)
        self.frame_193.setFrameShadow(QFrame.Raised)
        self.label_63 = QLabel(self.frame_193)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setGeometry(QRect(-2, 10, 201, 51))
        self.label_63.setStyleSheet(u"color: rgb(255, 62, 23);\n"
"background-color:transparent;\n"
"font: 900 14pt \"Poppins Black\";")
        self.label_63.setAlignment(Qt.AlignCenter)
        self.label_64 = QLabel(self.frame_193)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setGeometry(QRect(8, 0, 181, 20))
        self.label_64.setFont(font)

        self.verticalLayout_155.addWidget(self.frame_193)

        self.frame_194 = QFrame(self.frame_191)
        self.frame_194.setObjectName(u"frame_194")
        self.frame_194.setFrameShape(QFrame.StyledPanel)
        self.frame_194.setFrameShadow(QFrame.Raised)
        self.label_65 = QLabel(self.frame_194)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setGeometry(QRect(0, 0, 181, 20))
        self.label_65.setFont(font)
        self.label_66 = QLabel(self.frame_194)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setGeometry(QRect(0, 10, 191, 51))
        self.label_66.setStyleSheet(u"color: rgb(255, 62, 23);\n"
"background-color:transparent;\n"
"font: 900 14pt \"Poppins Black\";")
        self.label_66.setAlignment(Qt.AlignCenter)

        self.verticalLayout_155.addWidget(self.frame_194)


        self.verticalLayout_53.addWidget(self.frame_191)

        self.bt_39 = QPushButton(self.frame_68)
        self.bt_39.setObjectName(u"bt_39")
        self.bt_39.setMaximumSize(QSize(200, 40))
        self.bt_39.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_39.setIcon(icon8)
        self.bt_39.setIconSize(QSize(28, 30))

        self.verticalLayout_53.addWidget(self.bt_39)

        self.line_18 = QFrame(self.frame_68)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShape(QFrame.HLine)
        self.line_18.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_53.addWidget(self.line_18)

        self.bt_40 = QPushButton(self.frame_68)
        self.bt_40.setObjectName(u"bt_40")
        self.bt_40.setMaximumSize(QSize(200, 40))
        self.bt_40.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_40.setStyleSheet(u"padding-right: 20px;")
        self.bt_40.setIcon(icon9)
        self.bt_40.setIconSize(QSize(28, 30))

        self.verticalLayout_53.addWidget(self.bt_40)

        self.line_19 = QFrame(self.frame_68)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.HLine)
        self.line_19.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_53.addWidget(self.line_19)

        self.bt_41 = QPushButton(self.frame_68)
        self.bt_41.setObjectName(u"bt_41")
        self.bt_41.setMaximumSize(QSize(200, 40))
        self.bt_41.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_41.setStyleSheet(u"padding-right: 30px;")
        self.bt_41.setIcon(icon10)
        self.bt_41.setIconSize(QSize(28, 30))

        self.verticalLayout_53.addWidget(self.bt_41)

        self.line_20 = QFrame(self.frame_68)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setFrameShape(QFrame.HLine)
        self.line_20.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_53.addWidget(self.line_20)

        self.bt_42 = QPushButton(self.frame_68)
        self.bt_42.setObjectName(u"bt_42")
        self.bt_42.setMaximumSize(QSize(200, 40))
        self.bt_42.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_42.setStyleSheet(u"padding-right: 58px;")
        self.bt_42.setIcon(icon11)
        self.bt_42.setIconSize(QSize(28, 30))

        self.verticalLayout_53.addWidget(self.bt_42)

        self.line_21 = QFrame(self.frame_68)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setFrameShape(QFrame.HLine)
        self.line_21.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_53.addWidget(self.line_21)

        self.bt_43 = QPushButton(self.frame_68)
        self.bt_43.setObjectName(u"bt_43")
        self.bt_43.setMaximumSize(QSize(200, 40))
        self.bt_43.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_43.setStyleSheet(u"padding-right: 20px;")
        self.bt_43.setIcon(icon12)
        self.bt_43.setIconSize(QSize(28, 30))

        self.verticalLayout_53.addWidget(self.bt_43)

        self.line_22 = QFrame(self.frame_68)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setFrameShape(QFrame.HLine)
        self.line_22.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_53.addWidget(self.line_22)

        self.bt_44 = QPushButton(self.frame_68)
        self.bt_44.setObjectName(u"bt_44")
        self.bt_44.setMaximumSize(QSize(200, 40))
        self.bt_44.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_44.setStyleSheet(u"padding-right:49px;")
        self.bt_44.setIcon(icon13)
        self.bt_44.setIconSize(QSize(28, 30))

        self.verticalLayout_53.addWidget(self.bt_44)

        self.line_23 = QFrame(self.frame_68)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setFrameShape(QFrame.HLine)
        self.line_23.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_53.addWidget(self.line_23)

        self.bt_45 = QPushButton(self.frame_68)
        self.bt_45.setObjectName(u"bt_45")
        self.bt_45.setMaximumSize(QSize(200, 40))
        self.bt_45.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_45.setStyleSheet(u"padding-right: 69px;")
        self.bt_45.setIcon(icon14)
        self.bt_45.setIconSize(QSize(28, 30))

        self.verticalLayout_53.addWidget(self.bt_45)

        self.line_32 = QFrame(self.frame_68)
        self.line_32.setObjectName(u"line_32")
        self.line_32.setFrameShape(QFrame.HLine)
        self.line_32.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_53.addWidget(self.line_32)

        self.pushButton_18 = QPushButton(self.frame_68)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_18.setStyleSheet(u"padding-right: 80px;")
        self.pushButton_18.setIcon(icon15)
        self.pushButton_18.setIconSize(QSize(28, 30))

        self.verticalLayout_53.addWidget(self.pushButton_18)

        self.line_36 = QFrame(self.frame_68)
        self.line_36.setObjectName(u"line_36")
        self.line_36.setFrameShape(QFrame.HLine)
        self.line_36.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_53.addWidget(self.line_36)

        self.pushButton_16 = QPushButton(self.frame_68)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMaximumSize(QSize(200, 40))
        self.pushButton_16.setCursor(QCursor(Qt.OpenHandCursor))
        self.pushButton_16.setStyleSheet(u"padding-right: 120px;")
        self.pushButton_16.setIcon(icon16)
        self.pushButton_16.setIconSize(QSize(28, 28))

        self.verticalLayout_53.addWidget(self.pushButton_16)

        self.line_24 = QFrame(self.frame_68)
        self.line_24.setObjectName(u"line_24")
        self.line_24.setFrameShape(QFrame.HLine)
        self.line_24.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_53.addWidget(self.line_24)


        self.verticalLayout_52.addWidget(self.frame_68)


        self.horizontalLayout_23.addWidget(self.frame_67)

        self.frame_69 = QFrame(self.frame_66)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.frame_69)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_7 = QTabWidget(self.frame_69)
        self.tabWidget_7.setObjectName(u"tabWidget_7")
        self.tab_19 = QWidget()
        self.tab_19.setObjectName(u"tab_19")
        self.horizontalLayout_24 = QHBoxLayout(self.tab_19)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frame_70 = QFrame(self.tab_19)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_70)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.groupBox_12 = QGroupBox(self.frame_70)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QComboBox{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QDateEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 900 12pt \"Roboto Black\";\n"
"}")
        self.label_125 = QLabel(self.groupBox_12)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setGeometry(QRect(20, 30, 161, 31))
        self.lineEdit_38 = QLineEdit(self.groupBox_12)
        self.lineEdit_38.setObjectName(u"lineEdit_38")
        self.lineEdit_38.setGeometry(QRect(190, 30, 171, 31))
        self.label_128 = QLabel(self.groupBox_12)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setGeometry(QRect(20, 150, 111, 31))
        self.label_129 = QLabel(self.groupBox_12)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setGeometry(QRect(20, 190, 101, 31))
        self.comboBox_19 = QComboBox(self.groupBox_12)
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.setObjectName(u"comboBox_19")
        self.comboBox_19.setGeometry(QRect(130, 190, 171, 31))
        self.comboBox_20 = QComboBox(self.groupBox_12)
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.setObjectName(u"comboBox_20")
        self.comboBox_20.setGeometry(QRect(130, 230, 171, 31))
        self.label_130 = QLabel(self.groupBox_12)
        self.label_130.setObjectName(u"label_130")
        self.label_130.setGeometry(QRect(20, 230, 101, 31))
        self.label_131 = QLabel(self.groupBox_12)
        self.label_131.setObjectName(u"label_131")
        self.label_131.setGeometry(QRect(20, 280, 121, 31))
        self.textEdit_3 = QTextEdit(self.groupBox_12)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(143, 270, 141, 71))
        self.lineEdit_60 = QLineEdit(self.groupBox_12)
        self.lineEdit_60.setObjectName(u"lineEdit_60")
        self.lineEdit_60.setGeometry(QRect(130, 150, 171, 31))
        self.lineEdit_60.setClearButtonEnabled(True)
        self.lineEdit_22 = QLineEdit(self.groupBox_12)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setGeometry(QRect(130, 110, 171, 31))
        self.lineEdit_22.setClearButtonEnabled(True)
        self.label_49 = QLabel(self.groupBox_12)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(30, 110, 91, 31))

        self.verticalLayout_55.addWidget(self.groupBox_12)

        self.groupBox_13 = QGroupBox(self.frame_70)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QComboBox{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QDateEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 900 12pt \"Roboto Black\";\n"
"}")
        self.label_132 = QLabel(self.groupBox_13)
        self.label_132.setObjectName(u"label_132")
        self.label_132.setGeometry(QRect(20, 80, 131, 31))
        self.lineEdit_41 = QLineEdit(self.groupBox_13)
        self.lineEdit_41.setObjectName(u"lineEdit_41")
        self.lineEdit_41.setGeometry(QRect(170, 40, 191, 31))
        self.lineEdit_41.setClearButtonEnabled(True)
        self.label_133 = QLabel(self.groupBox_13)
        self.label_133.setObjectName(u"label_133")
        self.label_133.setGeometry(QRect(20, 40, 141, 31))
        self.lineEdit_42 = QLineEdit(self.groupBox_13)
        self.lineEdit_42.setObjectName(u"lineEdit_42")
        self.lineEdit_42.setGeometry(QRect(170, 80, 191, 31))
        self.lineEdit_42.setClearButtonEnabled(True)
        self.label_134 = QLabel(self.groupBox_13)
        self.label_134.setObjectName(u"label_134")
        self.label_134.setGeometry(QRect(20, 120, 131, 31))
        self.lineEdit_43 = QLineEdit(self.groupBox_13)
        self.lineEdit_43.setObjectName(u"lineEdit_43")
        self.lineEdit_43.setGeometry(QRect(170, 120, 191, 31))
        self.lineEdit_43.setClearButtonEnabled(True)

        self.verticalLayout_55.addWidget(self.groupBox_13)

        self.frame_71 = QFrame(self.frame_70)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(158, 158, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(255, 255, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_71)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.frame_72 = QFrame(self.frame_71)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.frame_72)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.bt_46 = QPushButton(self.frame_72)
        self.bt_46.setObjectName(u"bt_46")
        self.bt_46.setMinimumSize(QSize(0, 40))
        self.bt_46.setMaximumSize(QSize(120, 60))
        self.bt_46.setIcon(icon17)
        self.bt_46.setIconSize(QSize(20, 20))

        self.verticalLayout_56.addWidget(self.bt_46)


        self.horizontalLayout_25.addWidget(self.frame_72)

        self.frame_73 = QFrame(self.frame_71)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.frame_73)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.bt_47 = QPushButton(self.frame_73)
        self.bt_47.setObjectName(u"bt_47")
        self.bt_47.setMinimumSize(QSize(0, 40))
        self.bt_47.setMaximumSize(QSize(120, 60))
        self.bt_47.setIcon(icon18)
        self.bt_47.setIconSize(QSize(20, 20))

        self.verticalLayout_57.addWidget(self.bt_47)


        self.horizontalLayout_25.addWidget(self.frame_73)


        self.verticalLayout_55.addWidget(self.frame_71)

        self.verticalLayout_55.setStretch(0, 6)
        self.verticalLayout_55.setStretch(1, 3)
        self.verticalLayout_55.setStretch(2, 1)

        self.horizontalLayout_24.addWidget(self.frame_70)

        self.frame_74 = QFrame(self.tab_19)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.frame_74)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.tableWidget_7 = QTableWidget(self.frame_74)
        if (self.tableWidget_7.columnCount() < 9):
            self.tableWidget_7.setColumnCount(9)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(0, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(1, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(2, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(3, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(4, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(5, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(6, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(7, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(8, __qtablewidgetitem50)
        self.tableWidget_7.setObjectName(u"tableWidget_7")
        self.tableWidget_7.setStyleSheet(u"background-color: rgb(191, 191, 191);")

        self.verticalLayout_58.addWidget(self.tableWidget_7)


        self.horizontalLayout_24.addWidget(self.frame_74)

        self.horizontalLayout_24.setStretch(0, 5)
        self.horizontalLayout_24.setStretch(1, 4)
        self.tabWidget_7.addTab(self.tab_19, "")
        self.tab_20 = QWidget()
        self.tab_20.setObjectName(u"tab_20")
        self.horizontalLayout_26 = QHBoxLayout(self.tab_20)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_75 = QFrame(self.tab_20)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.frame_75)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.groupBox_14 = QGroupBox(self.frame_75)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.groupBox_14.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QComboBox{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QDateEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 900 12pt \"Roboto Black\";\n"
"}")
        self.label_135 = QLabel(self.groupBox_14)
        self.label_135.setObjectName(u"label_135")
        self.label_135.setGeometry(QRect(20, 30, 161, 31))
        self.lineEdit_44 = QLineEdit(self.groupBox_14)
        self.lineEdit_44.setObjectName(u"lineEdit_44")
        self.lineEdit_44.setGeometry(QRect(190, 30, 171, 31))
        self.lineEdit_44.setFrame(True)
        self.lineEdit_44.setClearButtonEnabled(True)
        self.label_138 = QLabel(self.groupBox_14)
        self.label_138.setObjectName(u"label_138")
        self.label_138.setGeometry(QRect(20, 150, 111, 31))
        self.label_139 = QLabel(self.groupBox_14)
        self.label_139.setObjectName(u"label_139")
        self.label_139.setGeometry(QRect(20, 190, 101, 31))
        self.comboBox_21 = QComboBox(self.groupBox_14)
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.setObjectName(u"comboBox_21")
        self.comboBox_21.setGeometry(QRect(130, 230, 171, 31))
        self.label_140 = QLabel(self.groupBox_14)
        self.label_140.setObjectName(u"label_140")
        self.label_140.setGeometry(QRect(20, 230, 101, 31))
        self.label_141 = QLabel(self.groupBox_14)
        self.label_141.setObjectName(u"label_141")
        self.label_141.setGeometry(QRect(20, 280, 121, 31))
        self.textEdit_4 = QTextEdit(self.groupBox_14)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(143, 270, 141, 71))
        self.comboBox_22 = QComboBox(self.groupBox_14)
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.setObjectName(u"comboBox_22")
        self.comboBox_22.setGeometry(QRect(130, 190, 171, 31))
        self.lineEdit_59 = QLineEdit(self.groupBox_14)
        self.lineEdit_59.setObjectName(u"lineEdit_59")
        self.lineEdit_59.setGeometry(QRect(130, 150, 171, 31))
        self.lineEdit_59.setClearButtonEnabled(True)
        self.lineEdit_23 = QLineEdit(self.groupBox_14)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        self.lineEdit_23.setGeometry(QRect(130, 110, 171, 31))
        self.lineEdit_23.setClearButtonEnabled(True)
        self.label_50 = QLabel(self.groupBox_14)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(30, 110, 91, 31))

        self.verticalLayout_59.addWidget(self.groupBox_14)

        self.groupBox_15 = QGroupBox(self.frame_75)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QComboBox{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QDateEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 900 12pt \"Roboto Black\";\n"
"}")
        self.label_142 = QLabel(self.groupBox_15)
        self.label_142.setObjectName(u"label_142")
        self.label_142.setGeometry(QRect(20, 80, 131, 31))
        self.lineEdit_47 = QLineEdit(self.groupBox_15)
        self.lineEdit_47.setObjectName(u"lineEdit_47")
        self.lineEdit_47.setGeometry(QRect(170, 40, 191, 31))
        self.lineEdit_47.setClearButtonEnabled(True)
        self.label_143 = QLabel(self.groupBox_15)
        self.label_143.setObjectName(u"label_143")
        self.label_143.setGeometry(QRect(20, 40, 141, 31))
        self.lineEdit_48 = QLineEdit(self.groupBox_15)
        self.lineEdit_48.setObjectName(u"lineEdit_48")
        self.lineEdit_48.setGeometry(QRect(170, 80, 191, 31))
        self.lineEdit_48.setClearButtonEnabled(True)
        self.label_144 = QLabel(self.groupBox_15)
        self.label_144.setObjectName(u"label_144")
        self.label_144.setGeometry(QRect(20, 120, 131, 31))
        self.lineEdit_49 = QLineEdit(self.groupBox_15)
        self.lineEdit_49.setObjectName(u"lineEdit_49")
        self.lineEdit_49.setGeometry(QRect(170, 120, 191, 31))
        self.lineEdit_49.setClearButtonEnabled(True)

        self.verticalLayout_59.addWidget(self.groupBox_15)

        self.frame_76 = QFrame(self.frame_75)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(158, 158, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(255, 255, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_76)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.frame_77 = QFrame(self.frame_76)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.frame_77)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.bt_48 = QPushButton(self.frame_77)
        self.bt_48.setObjectName(u"bt_48")
        self.bt_48.setMinimumSize(QSize(0, 40))
        self.bt_48.setMaximumSize(QSize(120, 60))
        self.bt_48.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_48.setIcon(icon19)
        self.bt_48.setIconSize(QSize(20, 20))

        self.verticalLayout_60.addWidget(self.bt_48)


        self.horizontalLayout_27.addWidget(self.frame_77)

        self.frame_78 = QFrame(self.frame_76)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.frame_78)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.bt_49 = QPushButton(self.frame_78)
        self.bt_49.setObjectName(u"bt_49")
        self.bt_49.setMinimumSize(QSize(0, 40))
        self.bt_49.setMaximumSize(QSize(120, 60))
        self.bt_49.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_49.setIcon(icon20)
        self.bt_49.setIconSize(QSize(28, 28))

        self.verticalLayout_61.addWidget(self.bt_49)


        self.horizontalLayout_27.addWidget(self.frame_78)

        self.frame_79 = QFrame(self.frame_76)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.frame_79)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.bt_50 = QPushButton(self.frame_79)
        self.bt_50.setObjectName(u"bt_50")
        self.bt_50.setMinimumSize(QSize(0, 40))
        self.bt_50.setMaximumSize(QSize(120, 60))
        self.bt_50.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_50.setIcon(icon18)
        self.bt_50.setIconSize(QSize(20, 20))

        self.verticalLayout_62.addWidget(self.bt_50)


        self.horizontalLayout_27.addWidget(self.frame_79)


        self.verticalLayout_59.addWidget(self.frame_76)

        self.verticalLayout_59.setStretch(0, 6)
        self.verticalLayout_59.setStretch(1, 3)
        self.verticalLayout_59.setStretch(2, 1)

        self.horizontalLayout_26.addWidget(self.frame_75)

        self.frame_80 = QFrame(self.tab_20)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setFrameShape(QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.verticalLayout_63 = QVBoxLayout(self.frame_80)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.frame_81 = QFrame(self.frame_80)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(11, 153, 146);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(19, 255, 247);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 12pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_81.setFrameShape(QFrame.NoFrame)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_81)
        self.horizontalLayout_28.setSpacing(1)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.bt_51 = QPushButton(self.frame_81)
        self.bt_51.setObjectName(u"bt_51")
        self.bt_51.setMinimumSize(QSize(10, 40))
        self.bt_51.setMaximumSize(QSize(120, 30))
        self.bt_51.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_51.setIcon(icon21)
        self.bt_51.setIconSize(QSize(28, 28))

        self.horizontalLayout_28.addWidget(self.bt_51)

        self.lineEdit_50 = QLineEdit(self.frame_81)
        self.lineEdit_50.setObjectName(u"lineEdit_50")
        self.lineEdit_50.setMaximumSize(QSize(190, 30))
        self.lineEdit_50.setClearButtonEnabled(True)

        self.horizontalLayout_28.addWidget(self.lineEdit_50)


        self.verticalLayout_63.addWidget(self.frame_81)

        self.tableWidget_8 = QTableWidget(self.frame_80)
        if (self.tableWidget_8.columnCount() < 9):
            self.tableWidget_8.setColumnCount(9)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(0, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(1, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(2, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(3, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(4, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(5, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(6, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(7, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(8, __qtablewidgetitem59)
        self.tableWidget_8.setObjectName(u"tableWidget_8")
        self.tableWidget_8.setStyleSheet(u"background-color: rgb(191, 191, 191);")

        self.verticalLayout_63.addWidget(self.tableWidget_8)

        self.verticalLayout_63.setStretch(0, 1)
        self.verticalLayout_63.setStretch(1, 9)

        self.horizontalLayout_26.addWidget(self.frame_80)

        self.horizontalLayout_26.setStretch(0, 7)
        self.horizontalLayout_26.setStretch(1, 5)
        self.tabWidget_7.addTab(self.tab_20, "")
        self.tab_21 = QWidget()
        self.tab_21.setObjectName(u"tab_21")
        self.horizontalLayout_29 = QHBoxLayout(self.tab_21)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_82 = QFrame(self.tab_21)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setFrameShape(QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Raised)
        self.verticalLayout_64 = QVBoxLayout(self.frame_82)
        self.verticalLayout_64.setSpacing(0)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(0, 0, -1, 0)
        self.groupBox_16 = QGroupBox(self.frame_82)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.groupBox_16.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QComboBox{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QDateEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 900 12pt \"Roboto Black\";\n"
"}")
        self.label_145 = QLabel(self.groupBox_16)
        self.label_145.setObjectName(u"label_145")
        self.label_145.setGeometry(QRect(30, 100, 101, 31))
        self.label_146 = QLabel(self.groupBox_16)
        self.label_146.setObjectName(u"label_146")
        self.label_146.setGeometry(QRect(30, 150, 101, 31))
        self.lineEdit_51 = QLineEdit(self.groupBox_16)
        self.lineEdit_51.setObjectName(u"lineEdit_51")
        self.lineEdit_51.setGeometry(QRect(140, 100, 171, 31))
        self.lineEdit_51.setClearButtonEnabled(True)
        self.label_147 = QLabel(self.groupBox_16)
        self.label_147.setObjectName(u"label_147")
        self.label_147.setGeometry(QRect(30, 50, 161, 31))
        self.lineEdit_52 = QLineEdit(self.groupBox_16)
        self.lineEdit_52.setObjectName(u"lineEdit_52")
        self.lineEdit_52.setGeometry(QRect(210, 50, 171, 31))
        self.lineEdit_52.setClearButtonEnabled(True)
        self.comboBox_24 = QComboBox(self.groupBox_16)
        self.comboBox_24.addItem("")
        self.comboBox_24.addItem("")
        self.comboBox_24.addItem("")
        self.comboBox_24.addItem("")
        self.comboBox_24.addItem("")
        self.comboBox_24.addItem("")
        self.comboBox_24.addItem("")
        self.comboBox_24.addItem("")
        self.comboBox_24.addItem("")
        self.comboBox_24.setObjectName(u"comboBox_24")
        self.comboBox_24.setGeometry(QRect(140, 200, 171, 31))
        self.label_148 = QLabel(self.groupBox_16)
        self.label_148.setObjectName(u"label_148")
        self.label_148.setGeometry(QRect(30, 200, 101, 31))
        self.comboBox_25 = QComboBox(self.groupBox_16)
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.setObjectName(u"comboBox_25")
        self.comboBox_25.setGeometry(QRect(140, 250, 171, 31))
        self.label_149 = QLabel(self.groupBox_16)
        self.label_149.setObjectName(u"label_149")
        self.label_149.setGeometry(QRect(30, 250, 101, 31))
        self.comboBox_26 = QComboBox(self.groupBox_16)
        self.comboBox_26.addItem("")
        self.comboBox_26.addItem("")
        self.comboBox_26.addItem("")
        self.comboBox_26.setObjectName(u"comboBox_26")
        self.comboBox_26.setGeometry(QRect(140, 300, 171, 31))
        self.label_150 = QLabel(self.groupBox_16)
        self.label_150.setObjectName(u"label_150")
        self.label_150.setGeometry(QRect(30, 300, 101, 31))
        self.label_151 = QLabel(self.groupBox_16)
        self.label_151.setObjectName(u"label_151")
        self.label_151.setGeometry(QRect(30, 350, 101, 31))
        self.comboBox_23 = QComboBox(self.groupBox_16)
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.setObjectName(u"comboBox_23")
        self.comboBox_23.setGeometry(QRect(140, 150, 171, 31))
        self.lineEdit_61 = QLineEdit(self.groupBox_16)
        self.lineEdit_61.setObjectName(u"lineEdit_61")
        self.lineEdit_61.setGeometry(QRect(140, 350, 171, 31))
        self.lineEdit_61.setClearButtonEnabled(True)
        self.lineEdit_62 = QLineEdit(self.groupBox_16)
        self.lineEdit_62.setObjectName(u"lineEdit_62")
        self.lineEdit_62.setGeometry(QRect(140, 450, 171, 31))
        self.lineEdit_62.setClearButtonEnabled(True)
        self.label_156 = QLabel(self.groupBox_16)
        self.label_156.setObjectName(u"label_156")
        self.label_156.setGeometry(QRect(30, 450, 101, 31))
        self.label_157 = QLabel(self.groupBox_16)
        self.label_157.setObjectName(u"label_157")
        self.label_157.setGeometry(QRect(30, 400, 101, 31))
        self.comboBox_29 = QComboBox(self.groupBox_16)
        self.comboBox_29.addItem("")
        self.comboBox_29.addItem("")
        self.comboBox_29.addItem("")
        self.comboBox_29.addItem("")
        self.comboBox_29.addItem("")
        self.comboBox_29.addItem("")
        self.comboBox_29.addItem("")
        self.comboBox_29.addItem("")
        self.comboBox_29.addItem("")
        self.comboBox_29.setObjectName(u"comboBox_29")
        self.comboBox_29.setGeometry(QRect(140, 400, 171, 31))

        self.verticalLayout_64.addWidget(self.groupBox_16)

        self.frame_83 = QFrame(self.frame_82)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"	background-color: rgb(158, 158, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(255, 255, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_83)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frame_84 = QFrame(self.frame_83)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.frame_84)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.bt_52 = QPushButton(self.frame_84)
        self.bt_52.setObjectName(u"bt_52")
        self.bt_52.setMaximumSize(QSize(120, 30))
        self.bt_52.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_52.setIcon(icon17)
        self.bt_52.setIconSize(QSize(20, 20))

        self.verticalLayout_65.addWidget(self.bt_52)


        self.horizontalLayout_30.addWidget(self.frame_84)

        self.frame_85 = QFrame(self.frame_83)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.verticalLayout_66 = QVBoxLayout(self.frame_85)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.bt_53 = QPushButton(self.frame_85)
        self.bt_53.setObjectName(u"bt_53")
        self.bt_53.setMaximumSize(QSize(120, 30))
        self.bt_53.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_53.setIcon(icon22)
        self.bt_53.setIconSize(QSize(20, 20))

        self.verticalLayout_66.addWidget(self.bt_53)


        self.horizontalLayout_30.addWidget(self.frame_85)

        self.frame_86 = QFrame(self.frame_83)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.verticalLayout_67 = QVBoxLayout(self.frame_86)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.bt_54 = QPushButton(self.frame_86)
        self.bt_54.setObjectName(u"bt_54")
        self.bt_54.setMaximumSize(QSize(120, 30))
        self.bt_54.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_54.setIcon(icon20)
        self.bt_54.setIconSize(QSize(20, 20))

        self.verticalLayout_67.addWidget(self.bt_54)


        self.horizontalLayout_30.addWidget(self.frame_86)

        self.frame_87 = QFrame(self.frame_83)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setFrameShape(QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Raised)
        self.verticalLayout_68 = QVBoxLayout(self.frame_87)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.bt_55 = QPushButton(self.frame_87)
        self.bt_55.setObjectName(u"bt_55")
        self.bt_55.setMaximumSize(QSize(120, 30))
        self.bt_55.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_55.setIcon(icon23)
        self.bt_55.setIconSize(QSize(20, 20))

        self.verticalLayout_68.addWidget(self.bt_55)


        self.horizontalLayout_30.addWidget(self.frame_87)


        self.verticalLayout_64.addWidget(self.frame_83)

        self.verticalLayout_64.setStretch(0, 8)
        self.verticalLayout_64.setStretch(1, 2)

        self.horizontalLayout_29.addWidget(self.frame_82)

        self.frame_88 = QFrame(self.tab_21)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Raised)
        self.verticalLayout_69 = QVBoxLayout(self.frame_88)
        self.verticalLayout_69.setSpacing(1)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.frame_89 = QFrame(self.frame_88)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(11, 153, 146);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(19, 255, 247);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 12pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_89.setFrameShape(QFrame.NoFrame)
        self.frame_89.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_89)
        self.horizontalLayout_31.setSpacing(1)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.bt_56 = QPushButton(self.frame_89)
        self.bt_56.setObjectName(u"bt_56")
        self.bt_56.setMinimumSize(QSize(10, 40))
        self.bt_56.setMaximumSize(QSize(120, 30))
        self.bt_56.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_56.setIcon(icon21)
        self.bt_56.setIconSize(QSize(28, 28))

        self.horizontalLayout_31.addWidget(self.bt_56)

        self.lineEdit_53 = QLineEdit(self.frame_89)
        self.lineEdit_53.setObjectName(u"lineEdit_53")
        self.lineEdit_53.setMaximumSize(QSize(190, 30))
        self.lineEdit_53.setClearButtonEnabled(True)

        self.horizontalLayout_31.addWidget(self.lineEdit_53)


        self.verticalLayout_69.addWidget(self.frame_89)

        self.tableWidget_9 = QTableWidget(self.frame_88)
        if (self.tableWidget_9.columnCount() < 9):
            self.tableWidget_9.setColumnCount(9)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(0, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(1, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(2, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(3, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(4, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(5, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(6, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(7, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(8, __qtablewidgetitem68)
        self.tableWidget_9.setObjectName(u"tableWidget_9")
        self.tableWidget_9.setStyleSheet(u"background-color: rgb(191, 191, 191);")

        self.verticalLayout_69.addWidget(self.tableWidget_9)

        self.verticalLayout_69.setStretch(0, 1)
        self.verticalLayout_69.setStretch(1, 8)

        self.horizontalLayout_29.addWidget(self.frame_88)

        self.horizontalLayout_29.setStretch(0, 5)
        self.horizontalLayout_29.setStretch(1, 5)
        self.tabWidget_7.addTab(self.tab_21, "")
        self.tab_22 = QWidget()
        self.tab_22.setObjectName(u"tab_22")
        self.horizontalLayout_33 = QHBoxLayout(self.tab_22)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.frame_90 = QFrame(self.tab_22)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setFrameShape(QFrame.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Raised)
        self.verticalLayout_70 = QVBoxLayout(self.frame_90)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.groupBox_17 = QGroupBox(self.frame_90)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.groupBox_17.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QComboBox{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QDateEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 900 12pt \"Roboto Black\";\n"
"}")
        self.label_152 = QLabel(self.groupBox_17)
        self.label_152.setObjectName(u"label_152")
        self.label_152.setGeometry(QRect(20, 100, 161, 31))
        self.label_153 = QLabel(self.groupBox_17)
        self.label_153.setObjectName(u"label_153")
        self.label_153.setGeometry(QRect(30, 180, 101, 31))
        self.lineEdit_54 = QLineEdit(self.groupBox_17)
        self.lineEdit_54.setObjectName(u"lineEdit_54")
        self.lineEdit_54.setGeometry(QRect(210, 100, 171, 31))
        self.lineEdit_54.setClearButtonEnabled(True)
        self.label_154 = QLabel(self.groupBox_17)
        self.label_154.setObjectName(u"label_154")
        self.label_154.setGeometry(QRect(60, 240, 101, 31))
        self.lineEdit_55 = QLineEdit(self.groupBox_17)
        self.lineEdit_55.setObjectName(u"lineEdit_55")
        self.lineEdit_55.setGeometry(QRect(180, 180, 171, 31))
        self.lineEdit_55.setClearButtonEnabled(True)
        self.label_155 = QLabel(self.groupBox_17)
        self.label_155.setObjectName(u"label_155")
        self.label_155.setGeometry(QRect(60, 300, 101, 31))
        self.comboBox_27 = QComboBox(self.groupBox_17)
        self.comboBox_27.addItem("")
        self.comboBox_27.addItem("")
        self.comboBox_27.addItem("")
        self.comboBox_27.addItem("")
        self.comboBox_27.addItem("")
        self.comboBox_27.addItem("")
        self.comboBox_27.addItem("")
        self.comboBox_27.addItem("")
        self.comboBox_27.addItem("")
        self.comboBox_27.setObjectName(u"comboBox_27")
        self.comboBox_27.setGeometry(QRect(180, 240, 171, 31))
        self.lineEdit_58 = QLineEdit(self.groupBox_17)
        self.lineEdit_58.setObjectName(u"lineEdit_58")
        self.lineEdit_58.setGeometry(QRect(180, 300, 171, 31))
        self.lineEdit_58.setClearButtonEnabled(True)

        self.verticalLayout_70.addWidget(self.groupBox_17)

        self.frame_91 = QFrame(self.frame_90)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(158, 158, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(255, 255, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_91.setFrameShape(QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_91)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.frame_92 = QFrame(self.frame_91)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setFrameShape(QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Raised)
        self.verticalLayout_71 = QVBoxLayout(self.frame_92)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.bt_57 = QPushButton(self.frame_92)
        self.bt_57.setObjectName(u"bt_57")
        self.bt_57.setMaximumSize(QSize(120, 30))
        self.bt_57.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_57.setIcon(icon17)
        self.bt_57.setIconSize(QSize(20, 20))

        self.verticalLayout_71.addWidget(self.bt_57)


        self.horizontalLayout_34.addWidget(self.frame_92)

        self.frame_93 = QFrame(self.frame_91)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setFrameShape(QFrame.StyledPanel)
        self.frame_93.setFrameShadow(QFrame.Raised)
        self.verticalLayout_72 = QVBoxLayout(self.frame_93)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.bt_58 = QPushButton(self.frame_93)
        self.bt_58.setObjectName(u"bt_58")
        self.bt_58.setMaximumSize(QSize(120, 30))
        self.bt_58.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_58.setIcon(icon22)
        self.bt_58.setIconSize(QSize(20, 20))

        self.verticalLayout_72.addWidget(self.bt_58)


        self.horizontalLayout_34.addWidget(self.frame_93)

        self.frame_94 = QFrame(self.frame_91)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setFrameShape(QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Raised)
        self.verticalLayout_73 = QVBoxLayout(self.frame_94)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.bt_59 = QPushButton(self.frame_94)
        self.bt_59.setObjectName(u"bt_59")
        self.bt_59.setMaximumSize(QSize(120, 30))
        self.bt_59.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_59.setIcon(icon20)
        self.bt_59.setIconSize(QSize(20, 20))

        self.verticalLayout_73.addWidget(self.bt_59)


        self.horizontalLayout_34.addWidget(self.frame_94)

        self.frame_95 = QFrame(self.frame_91)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setFrameShape(QFrame.StyledPanel)
        self.frame_95.setFrameShadow(QFrame.Raised)
        self.verticalLayout_74 = QVBoxLayout(self.frame_95)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.bt_60 = QPushButton(self.frame_95)
        self.bt_60.setObjectName(u"bt_60")
        self.bt_60.setMaximumSize(QSize(120, 30))
        self.bt_60.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_60.setIcon(icon23)
        self.bt_60.setIconSize(QSize(20, 20))

        self.verticalLayout_74.addWidget(self.bt_60)


        self.horizontalLayout_34.addWidget(self.frame_95)


        self.verticalLayout_70.addWidget(self.frame_91)

        self.verticalLayout_70.setStretch(0, 8)
        self.verticalLayout_70.setStretch(1, 1)

        self.horizontalLayout_33.addWidget(self.frame_90)

        self.frame_96 = QFrame(self.tab_22)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setFrameShape(QFrame.StyledPanel)
        self.frame_96.setFrameShadow(QFrame.Raised)
        self.verticalLayout_75 = QVBoxLayout(self.frame_96)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.tableWidget_10 = QTableWidget(self.frame_96)
        if (self.tableWidget_10.columnCount() < 4):
            self.tableWidget_10.setColumnCount(4)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(0, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(1, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(2, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(3, __qtablewidgetitem72)
        self.tableWidget_10.setObjectName(u"tableWidget_10")
        self.tableWidget_10.setStyleSheet(u"background-color: rgb(191, 191, 191);")

        self.verticalLayout_75.addWidget(self.tableWidget_10)


        self.horizontalLayout_33.addWidget(self.frame_96)

        self.horizontalLayout_33.setStretch(0, 5)
        self.horizontalLayout_33.setStretch(1, 5)
        self.tabWidget_7.addTab(self.tab_22, "")
        self.tab_23 = QWidget()
        self.tab_23.setObjectName(u"tab_23")
        self.horizontalLayout_35 = QHBoxLayout(self.tab_23)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.frame_97 = QFrame(self.tab_23)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setFrameShape(QFrame.StyledPanel)
        self.frame_97.setFrameShadow(QFrame.Raised)
        self.verticalLayout_76 = QVBoxLayout(self.frame_97)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_76.addItem(self.verticalSpacer_3)

        self.frame_98 = QFrame(self.frame_97)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"}\n"
"QPushButton {\n"
"	background-color: transparent;\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(36, 36, 36);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(161, 107, 80);\n"
"	border-bottom-left-radius: 8px;\n"
"	\n"
"}\n"
"")
        self.frame_98.setFrameShape(QFrame.StyledPanel)
        self.frame_98.setFrameShadow(QFrame.Raised)
        self.verticalLayout_79 = QVBoxLayout(self.frame_98)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.line_25 = QFrame(self.frame_98)
        self.line_25.setObjectName(u"line_25")
        self.line_25.setFrameShape(QFrame.HLine)
        self.line_25.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_79.addWidget(self.line_25)

        self.bt_61 = QPushButton(self.frame_98)
        self.bt_61.setObjectName(u"bt_61")
        self.bt_61.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_79.addWidget(self.bt_61)

        self.line_26 = QFrame(self.frame_98)
        self.line_26.setObjectName(u"line_26")
        self.line_26.setFrameShape(QFrame.HLine)
        self.line_26.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_79.addWidget(self.line_26)

        self.bt_62 = QPushButton(self.frame_98)
        self.bt_62.setObjectName(u"bt_62")
        self.bt_62.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_79.addWidget(self.bt_62)

        self.line_27 = QFrame(self.frame_98)
        self.line_27.setObjectName(u"line_27")
        self.line_27.setFrameShape(QFrame.HLine)
        self.line_27.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_79.addWidget(self.line_27)

        self.bt_63 = QPushButton(self.frame_98)
        self.bt_63.setObjectName(u"bt_63")
        self.bt_63.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_79.addWidget(self.bt_63)

        self.line_28 = QFrame(self.frame_98)
        self.line_28.setObjectName(u"line_28")
        self.line_28.setFrameShape(QFrame.HLine)
        self.line_28.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_79.addWidget(self.line_28)


        self.verticalLayout_76.addWidget(self.frame_98)

        self.verticalSpacer_4 = QSpacerItem(20, 89, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_76.addItem(self.verticalSpacer_4)

        self.verticalLayout_76.setStretch(0, 1)
        self.verticalLayout_76.setStretch(1, 5)
        self.verticalLayout_76.setStretch(2, 1)

        self.horizontalLayout_35.addWidget(self.frame_97)

        self.frame_99 = QFrame(self.tab_23)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setFrameShape(QFrame.StyledPanel)
        self.frame_99.setFrameShadow(QFrame.Raised)
        self.verticalLayout_82 = QVBoxLayout(self.frame_99)
        self.verticalLayout_82.setSpacing(0)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.verticalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_8 = QTabWidget(self.frame_99)
        self.tabWidget_8.setObjectName(u"tabWidget_8")
        self.tab_24 = QWidget()
        self.tab_24.setObjectName(u"tab_24")
        self.horizontalLayout_36 = QHBoxLayout(self.tab_24)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.frame_100 = QFrame(self.tab_24)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setFrameShape(QFrame.StyledPanel)
        self.frame_100.setFrameShadow(QFrame.Raised)
        self.verticalLayout_140 = QVBoxLayout(self.frame_100)
        self.verticalLayout_140.setObjectName(u"verticalLayout_140")
        self.groupBox_35 = QGroupBox(self.frame_100)
        self.groupBox_35.setObjectName(u"groupBox_35")
        self.groupBox_35.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QComboBox{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QDateEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 900 12pt \"Roboto Black\";\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 148, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(0, 213, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.label_240 = QLabel(self.groupBox_35)
        self.label_240.setObjectName(u"label_240")
        self.label_240.setGeometry(QRect(40, 320, 101, 31))
        self.comboBox_59 = QComboBox(self.groupBox_35)
        self.comboBox_59.addItem("")
        self.comboBox_59.addItem("")
        self.comboBox_59.addItem("")
        self.comboBox_59.setObjectName(u"comboBox_59")
        self.comboBox_59.setGeometry(QRect(400, 210, 141, 31))
        self.label_241 = QLabel(self.groupBox_35)
        self.label_241.setObjectName(u"label_241")
        self.label_241.setGeometry(QRect(340, 210, 61, 31))
        self.label_242 = QLabel(self.groupBox_35)
        self.label_242.setObjectName(u"label_242")
        self.label_242.setGeometry(QRect(40, 380, 51, 31))
        self.lineEdit_116 = QLineEdit(self.groupBox_35)
        self.lineEdit_116.setObjectName(u"lineEdit_116")
        self.lineEdit_116.setGeometry(QRect(140, 320, 161, 31))
        self.lineEdit_116.setClearButtonEnabled(True)
        self.lineEdit_117 = QLineEdit(self.groupBox_35)
        self.lineEdit_117.setObjectName(u"lineEdit_117")
        self.lineEdit_117.setGeometry(QRect(140, 160, 161, 31))
        self.lineEdit_117.setClearButtonEnabled(True)
        self.label_243 = QLabel(self.groupBox_35)
        self.label_243.setObjectName(u"label_243")
        self.label_243.setGeometry(QRect(30, 160, 111, 31))
        self.label_244 = QLabel(self.groupBox_35)
        self.label_244.setObjectName(u"label_244")
        self.label_244.setGeometry(QRect(340, 160, 131, 31))
        self.lineEdit_118 = QLineEdit(self.groupBox_35)
        self.lineEdit_118.setObjectName(u"lineEdit_118")
        self.lineEdit_118.setGeometry(QRect(480, 160, 151, 31))
        self.lineEdit_118.setClearButtonEnabled(True)
        self.label_245 = QLabel(self.groupBox_35)
        self.label_245.setObjectName(u"label_245")
        self.label_245.setGeometry(QRect(20, 220, 121, 31))
        self.lineEdit_119 = QLineEdit(self.groupBox_35)
        self.lineEdit_119.setObjectName(u"lineEdit_119")
        self.lineEdit_119.setGeometry(QRect(140, 210, 161, 31))
        self.lineEdit_119.setClearButtonEnabled(True)
        self.comboBox_60 = QComboBox(self.groupBox_35)
        self.comboBox_60.addItem("")
        self.comboBox_60.addItem("")
        self.comboBox_60.addItem("")
        self.comboBox_60.addItem("")
        self.comboBox_60.addItem("")
        self.comboBox_60.addItem("")
        self.comboBox_60.addItem("")
        self.comboBox_60.addItem("")
        self.comboBox_60.addItem("")
        self.comboBox_60.setObjectName(u"comboBox_60")
        self.comboBox_60.setGeometry(QRect(140, 380, 161, 31))
        self.label_543 = QLabel(self.groupBox_35)
        self.label_543.setObjectName(u"label_543")
        self.label_543.setGeometry(QRect(30, 440, 101, 31))
        self.comboBox_61 = QComboBox(self.groupBox_35)
        self.comboBox_61.addItem("")
        self.comboBox_61.addItem("")
        self.comboBox_61.addItem("")
        self.comboBox_61.addItem("")
        self.comboBox_61.addItem("")
        self.comboBox_61.addItem("")
        self.comboBox_61.addItem("")
        self.comboBox_61.addItem("")
        self.comboBox_61.addItem("")
        self.comboBox_61.setObjectName(u"comboBox_61")
        self.comboBox_61.setGeometry(QRect(140, 440, 161, 31))
        self.label_544 = QLabel(self.groupBox_35)
        self.label_544.setObjectName(u"label_544")
        self.label_544.setGeometry(QRect(180, 40, 381, 31))
        self.pushButton_6 = QPushButton(self.groupBox_35)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(390, 513, 81, 31))
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setIcon(icon18)
        self.pushButton_6.setIconSize(QSize(20, 20))
        self.lineEdit_159 = QLineEdit(self.groupBox_35)
        self.lineEdit_159.setObjectName(u"lineEdit_159")
        self.lineEdit_159.setGeometry(QRect(160, 490, 161, 31))
        self.lineEdit_159.setClearButtonEnabled(True)
        self.label_1323 = QLabel(self.groupBox_35)
        self.label_1323.setObjectName(u"label_1323")
        self.label_1323.setGeometry(QRect(20, 490, 141, 31))
        self.label_1335 = QLabel(self.groupBox_35)
        self.label_1335.setObjectName(u"label_1335")
        self.label_1335.setGeometry(QRect(350, 390, 101, 31))
        self.lineEdit_171 = QLineEdit(self.groupBox_35)
        self.lineEdit_171.setObjectName(u"lineEdit_171")
        self.lineEdit_171.setGeometry(QRect(470, 390, 191, 31))
        self.lineEdit_171.setClearButtonEnabled(True)
        self.lineEdit_172 = QLineEdit(self.groupBox_35)
        self.lineEdit_172.setObjectName(u"lineEdit_172")
        self.lineEdit_172.setGeometry(QRect(500, 450, 191, 31))
        self.lineEdit_172.setClearButtonEnabled(True)
        self.label_1336 = QLabel(self.groupBox_35)
        self.label_1336.setObjectName(u"label_1336")
        self.label_1336.setGeometry(QRect(360, 450, 141, 31))
        self.label_1350 = QLabel(self.groupBox_35)
        self.label_1350.setObjectName(u"label_1350")
        self.label_1350.setGeometry(QRect(390, 320, 51, 31))
        self.lineEdit_186 = QLineEdit(self.groupBox_35)
        self.lineEdit_186.setObjectName(u"lineEdit_186")
        self.lineEdit_186.setGeometry(QRect(460, 320, 191, 31))
        self.lineEdit_186.setClearButtonEnabled(True)

        self.verticalLayout_140.addWidget(self.groupBox_35)


        self.horizontalLayout_36.addWidget(self.frame_100)

        self.tabWidget_8.addTab(self.tab_24, "")
        self.tab_25 = QWidget()
        self.tab_25.setObjectName(u"tab_25")
        self.horizontalLayout_37 = QHBoxLayout(self.tab_25)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.frame_101 = QFrame(self.tab_25)
        self.frame_101.setObjectName(u"frame_101")
        self.frame_101.setFrameShape(QFrame.StyledPanel)
        self.frame_101.setFrameShadow(QFrame.Raised)
        self.verticalLayout_139 = QVBoxLayout(self.frame_101)
        self.verticalLayout_139.setObjectName(u"verticalLayout_139")
        self.groupBox_34 = QGroupBox(self.frame_101)
        self.groupBox_34.setObjectName(u"groupBox_34")
        self.groupBox_34.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QComboBox{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QDateEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 900 12pt \"Roboto Black\";\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 148, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(0, 213, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.label_234 = QLabel(self.groupBox_34)
        self.label_234.setObjectName(u"label_234")
        self.label_234.setGeometry(QRect(40, 320, 101, 31))
        self.comboBox_56 = QComboBox(self.groupBox_34)
        self.comboBox_56.addItem("")
        self.comboBox_56.addItem("")
        self.comboBox_56.addItem("")
        self.comboBox_56.setObjectName(u"comboBox_56")
        self.comboBox_56.setGeometry(QRect(400, 210, 141, 31))
        self.label_235 = QLabel(self.groupBox_34)
        self.label_235.setObjectName(u"label_235")
        self.label_235.setGeometry(QRect(340, 210, 61, 31))
        self.label_236 = QLabel(self.groupBox_34)
        self.label_236.setObjectName(u"label_236")
        self.label_236.setGeometry(QRect(40, 380, 51, 31))
        self.lineEdit_112 = QLineEdit(self.groupBox_34)
        self.lineEdit_112.setObjectName(u"lineEdit_112")
        self.lineEdit_112.setGeometry(QRect(140, 320, 161, 31))
        self.lineEdit_112.setClearButtonEnabled(True)
        self.lineEdit_113 = QLineEdit(self.groupBox_34)
        self.lineEdit_113.setObjectName(u"lineEdit_113")
        self.lineEdit_113.setGeometry(QRect(140, 160, 161, 31))
        self.lineEdit_113.setClearButtonEnabled(True)
        self.label_237 = QLabel(self.groupBox_34)
        self.label_237.setObjectName(u"label_237")
        self.label_237.setGeometry(QRect(30, 160, 111, 31))
        self.label_238 = QLabel(self.groupBox_34)
        self.label_238.setObjectName(u"label_238")
        self.label_238.setGeometry(QRect(340, 160, 131, 31))
        self.lineEdit_114 = QLineEdit(self.groupBox_34)
        self.lineEdit_114.setObjectName(u"lineEdit_114")
        self.lineEdit_114.setGeometry(QRect(480, 160, 151, 31))
        self.lineEdit_114.setClearButtonEnabled(True)
        self.label_239 = QLabel(self.groupBox_34)
        self.label_239.setObjectName(u"label_239")
        self.label_239.setGeometry(QRect(20, 220, 121, 31))
        self.lineEdit_115 = QLineEdit(self.groupBox_34)
        self.lineEdit_115.setObjectName(u"lineEdit_115")
        self.lineEdit_115.setGeometry(QRect(140, 210, 161, 31))
        self.lineEdit_115.setClearButtonEnabled(True)
        self.comboBox_57 = QComboBox(self.groupBox_34)
        self.comboBox_57.addItem("")
        self.comboBox_57.addItem("")
        self.comboBox_57.addItem("")
        self.comboBox_57.addItem("")
        self.comboBox_57.addItem("")
        self.comboBox_57.addItem("")
        self.comboBox_57.addItem("")
        self.comboBox_57.addItem("")
        self.comboBox_57.addItem("")
        self.comboBox_57.setObjectName(u"comboBox_57")
        self.comboBox_57.setGeometry(QRect(140, 380, 161, 31))
        self.label_541 = QLabel(self.groupBox_34)
        self.label_541.setObjectName(u"label_541")
        self.label_541.setGeometry(QRect(30, 440, 101, 31))
        self.comboBox_58 = QComboBox(self.groupBox_34)
        self.comboBox_58.addItem("")
        self.comboBox_58.addItem("")
        self.comboBox_58.addItem("")
        self.comboBox_58.addItem("")
        self.comboBox_58.addItem("")
        self.comboBox_58.addItem("")
        self.comboBox_58.addItem("")
        self.comboBox_58.addItem("")
        self.comboBox_58.addItem("")
        self.comboBox_58.setObjectName(u"comboBox_58")
        self.comboBox_58.setGeometry(QRect(140, 440, 161, 31))
        self.label_542 = QLabel(self.groupBox_34)
        self.label_542.setObjectName(u"label_542")
        self.label_542.setGeometry(QRect(180, 40, 381, 31))
        self.pushButton_5 = QPushButton(self.groupBox_34)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(400, 513, 81, 31))
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setIcon(icon18)
        self.pushButton_5.setIconSize(QSize(20, 20))
        self.lineEdit_160 = QLineEdit(self.groupBox_34)
        self.lineEdit_160.setObjectName(u"lineEdit_160")
        self.lineEdit_160.setGeometry(QRect(170, 490, 161, 31))
        self.lineEdit_160.setClearButtonEnabled(True)
        self.label_1324 = QLabel(self.groupBox_34)
        self.label_1324.setObjectName(u"label_1324")
        self.label_1324.setGeometry(QRect(30, 490, 141, 31))
        self.label_1337 = QLabel(self.groupBox_34)
        self.label_1337.setObjectName(u"label_1337")
        self.label_1337.setGeometry(QRect(350, 380, 101, 31))
        self.lineEdit_173 = QLineEdit(self.groupBox_34)
        self.lineEdit_173.setObjectName(u"lineEdit_173")
        self.lineEdit_173.setGeometry(QRect(470, 380, 191, 31))
        self.lineEdit_173.setClearButtonEnabled(True)
        self.lineEdit_174 = QLineEdit(self.groupBox_34)
        self.lineEdit_174.setObjectName(u"lineEdit_174")
        self.lineEdit_174.setGeometry(QRect(500, 440, 191, 31))
        self.lineEdit_174.setClearButtonEnabled(True)
        self.label_1338 = QLabel(self.groupBox_34)
        self.label_1338.setObjectName(u"label_1338")
        self.label_1338.setGeometry(QRect(360, 440, 141, 31))
        self.label_1351 = QLabel(self.groupBox_34)
        self.label_1351.setObjectName(u"label_1351")
        self.label_1351.setGeometry(QRect(400, 320, 51, 31))
        self.lineEdit_187 = QLineEdit(self.groupBox_34)
        self.lineEdit_187.setObjectName(u"lineEdit_187")
        self.lineEdit_187.setGeometry(QRect(470, 320, 191, 31))
        self.lineEdit_187.setClearButtonEnabled(True)

        self.verticalLayout_139.addWidget(self.groupBox_34)


        self.horizontalLayout_37.addWidget(self.frame_101)

        self.tabWidget_8.addTab(self.tab_25, "")
        self.tab_26 = QWidget()
        self.tab_26.setObjectName(u"tab_26")
        self.horizontalLayout_38 = QHBoxLayout(self.tab_26)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, -1, 0, 0)
        self.groupBox_20 = QGroupBox(self.tab_26)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.groupBox_20.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QComboBox{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QDateEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 900 12pt \"Roboto Black\";\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 148, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(0, 213, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.label_216 = QLabel(self.groupBox_20)
        self.label_216.setObjectName(u"label_216")
        self.label_216.setGeometry(QRect(40, 320, 101, 31))
        self.comboBox_32 = QComboBox(self.groupBox_20)
        self.comboBox_32.addItem("")
        self.comboBox_32.addItem("")
        self.comboBox_32.addItem("")
        self.comboBox_32.setObjectName(u"comboBox_32")
        self.comboBox_32.setGeometry(QRect(400, 210, 141, 31))
        self.label_217 = QLabel(self.groupBox_20)
        self.label_217.setObjectName(u"label_217")
        self.label_217.setGeometry(QRect(340, 210, 61, 31))
        self.label_218 = QLabel(self.groupBox_20)
        self.label_218.setObjectName(u"label_218")
        self.label_218.setGeometry(QRect(40, 380, 51, 31))
        self.lineEdit_64 = QLineEdit(self.groupBox_20)
        self.lineEdit_64.setObjectName(u"lineEdit_64")
        self.lineEdit_64.setGeometry(QRect(140, 320, 161, 31))
        self.lineEdit_64.setClearButtonEnabled(True)
        self.lineEdit_65 = QLineEdit(self.groupBox_20)
        self.lineEdit_65.setObjectName(u"lineEdit_65")
        self.lineEdit_65.setGeometry(QRect(140, 160, 161, 31))
        self.lineEdit_65.setClearButtonEnabled(True)
        self.label_219 = QLabel(self.groupBox_20)
        self.label_219.setObjectName(u"label_219")
        self.label_219.setGeometry(QRect(30, 160, 111, 31))
        self.label_220 = QLabel(self.groupBox_20)
        self.label_220.setObjectName(u"label_220")
        self.label_220.setGeometry(QRect(340, 160, 131, 31))
        self.lineEdit_66 = QLineEdit(self.groupBox_20)
        self.lineEdit_66.setObjectName(u"lineEdit_66")
        self.lineEdit_66.setGeometry(QRect(480, 160, 151, 31))
        self.lineEdit_66.setClearButtonEnabled(True)
        self.label_221 = QLabel(self.groupBox_20)
        self.label_221.setObjectName(u"label_221")
        self.label_221.setGeometry(QRect(20, 220, 121, 31))
        self.lineEdit_67 = QLineEdit(self.groupBox_20)
        self.lineEdit_67.setObjectName(u"lineEdit_67")
        self.lineEdit_67.setGeometry(QRect(140, 210, 161, 31))
        self.lineEdit_67.setClearButtonEnabled(True)
        self.comboBox_33 = QComboBox(self.groupBox_20)
        self.comboBox_33.addItem("")
        self.comboBox_33.addItem("")
        self.comboBox_33.addItem("")
        self.comboBox_33.addItem("")
        self.comboBox_33.addItem("")
        self.comboBox_33.addItem("")
        self.comboBox_33.addItem("")
        self.comboBox_33.addItem("")
        self.comboBox_33.addItem("")
        self.comboBox_33.setObjectName(u"comboBox_33")
        self.comboBox_33.setGeometry(QRect(140, 380, 161, 31))
        self.label_485 = QLabel(self.groupBox_20)
        self.label_485.setObjectName(u"label_485")
        self.label_485.setGeometry(QRect(30, 440, 101, 31))
        self.comboBox_55 = QComboBox(self.groupBox_20)
        self.comboBox_55.addItem("")
        self.comboBox_55.addItem("")
        self.comboBox_55.addItem("")
        self.comboBox_55.addItem("")
        self.comboBox_55.addItem("")
        self.comboBox_55.addItem("")
        self.comboBox_55.addItem("")
        self.comboBox_55.addItem("")
        self.comboBox_55.addItem("")
        self.comboBox_55.setObjectName(u"comboBox_55")
        self.comboBox_55.setGeometry(QRect(140, 440, 161, 31))
        self.label_486 = QLabel(self.groupBox_20)
        self.label_486.setObjectName(u"label_486")
        self.label_486.setGeometry(QRect(180, 40, 381, 31))
        self.pushButton_4 = QPushButton(self.groupBox_20)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(390, 513, 81, 31))
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setIcon(icon18)
        self.pushButton_4.setIconSize(QSize(20, 20))
        self.lineEdit_161 = QLineEdit(self.groupBox_20)
        self.lineEdit_161.setObjectName(u"lineEdit_161")
        self.lineEdit_161.setGeometry(QRect(170, 490, 161, 31))
        self.lineEdit_161.setClearButtonEnabled(True)
        self.label_1325 = QLabel(self.groupBox_20)
        self.label_1325.setObjectName(u"label_1325")
        self.label_1325.setGeometry(QRect(30, 490, 141, 31))
        self.label_1339 = QLabel(self.groupBox_20)
        self.label_1339.setObjectName(u"label_1339")
        self.label_1339.setGeometry(QRect(360, 380, 101, 31))
        self.lineEdit_175 = QLineEdit(self.groupBox_20)
        self.lineEdit_175.setObjectName(u"lineEdit_175")
        self.lineEdit_175.setGeometry(QRect(480, 380, 191, 31))
        self.lineEdit_175.setClearButtonEnabled(True)
        self.lineEdit_176 = QLineEdit(self.groupBox_20)
        self.lineEdit_176.setObjectName(u"lineEdit_176")
        self.lineEdit_176.setGeometry(QRect(510, 440, 191, 31))
        self.lineEdit_176.setClearButtonEnabled(True)
        self.label_1340 = QLabel(self.groupBox_20)
        self.label_1340.setObjectName(u"label_1340")
        self.label_1340.setGeometry(QRect(370, 440, 141, 31))
        self.label_1352 = QLabel(self.groupBox_20)
        self.label_1352.setObjectName(u"label_1352")
        self.label_1352.setGeometry(QRect(400, 330, 51, 31))
        self.lineEdit_188 = QLineEdit(self.groupBox_20)
        self.lineEdit_188.setObjectName(u"lineEdit_188")
        self.lineEdit_188.setGeometry(QRect(470, 330, 191, 31))
        self.lineEdit_188.setClearButtonEnabled(True)

        self.horizontalLayout_38.addWidget(self.groupBox_20)

        self.horizontalLayout_38.setStretch(0, 3)
        self.tabWidget_8.addTab(self.tab_26, "")
        self.tab_43 = QWidget()
        self.tab_43.setObjectName(u"tab_43")
        self.verticalLayout_137 = QVBoxLayout(self.tab_43)
        self.verticalLayout_137.setSpacing(0)
        self.verticalLayout_137.setObjectName(u"verticalLayout_137")
        self.verticalLayout_137.setContentsMargins(0, 0, 0, 0)
        self.frame_102 = QFrame(self.tab_43)
        self.frame_102.setObjectName(u"frame_102")
        self.frame_102.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(222, 222, 222);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 148, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(0, 213, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_102.setFrameShape(QFrame.StyledPanel)
        self.frame_102.setFrameShadow(QFrame.Raised)
        self.label_200 = QLabel(self.frame_102)
        self.label_200.setObjectName(u"label_200")
        self.label_200.setGeometry(QRect(180, 10, 311, 21))
        self.label_200.setStyleSheet(u"font: 900 14pt \"Roboto\";")
        self.label_200.setAlignment(Qt.AlignCenter)
        self.label_201 = QLabel(self.frame_102)
        self.label_201.setObjectName(u"label_201")
        self.label_201.setGeometry(QRect(210, 40, 141, 16))
        self.label_202 = QLabel(self.frame_102)
        self.label_202.setObjectName(u"label_202")
        self.label_202.setGeometry(QRect(440, 40, 171, 16))
        self.label_203 = QLabel(self.frame_102)
        self.label_203.setObjectName(u"label_203")
        self.label_203.setGeometry(QRect(220, 60, 221, 20))
        self.label_203.setAlignment(Qt.AlignCenter)
        self.label_204 = QLabel(self.frame_102)
        self.label_204.setObjectName(u"label_204")
        self.label_204.setGeometry(QRect(70, 100, 49, 16))
        self.line_33 = QFrame(self.frame_102)
        self.line_33.setObjectName(u"line_33")
        self.line_33.setGeometry(QRect(90, 80, 501, 16))
        self.line_33.setFrameShape(QFrame.HLine)
        self.line_33.setFrameShadow(QFrame.Sunken)
        self.label_205 = QLabel(self.frame_102)
        self.label_205.setObjectName(u"label_205")
        self.label_205.setGeometry(QRect(120, 100, 71, 16))
        self.label_205.setStyleSheet(u"color: rgb(161, 161, 0);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_206 = QLabel(self.frame_102)
        self.label_206.setObjectName(u"label_206")
        self.label_206.setGeometry(QRect(220, 100, 41, 16))
        self.label_207 = QLabel(self.frame_102)
        self.label_207.setObjectName(u"label_207")
        self.label_207.setGeometry(QRect(270, 100, 151, 16))
        self.label_207.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_207.setTextFormat(Qt.AutoText)
        self.label_207.setScaledContents(False)
        self.label_208 = QLabel(self.frame_102)
        self.label_208.setObjectName(u"label_208")
        self.label_208.setGeometry(QRect(80, 140, 91, 16))
        self.label_209 = QLabel(self.frame_102)
        self.label_209.setObjectName(u"label_209")
        self.label_209.setGeometry(QRect(160, 140, 71, 16))
        self.label_210 = QLabel(self.frame_102)
        self.label_210.setObjectName(u"label_210")
        self.label_210.setGeometry(QRect(260, 140, 101, 16))
        self.label_211 = QLabel(self.frame_102)
        self.label_211.setObjectName(u"label_211")
        self.label_211.setGeometry(QRect(360, 140, 61, 16))
        self.label_212 = QLabel(self.frame_102)
        self.label_212.setObjectName(u"label_212")
        self.label_212.setGeometry(QRect(430, 100, 49, 16))
        self.label_213 = QLabel(self.frame_102)
        self.label_213.setObjectName(u"label_213")
        self.label_213.setGeometry(QRect(470, 100, 91, 16))
        self.label_214 = QLabel(self.frame_102)
        self.label_214.setObjectName(u"label_214")
        self.label_214.setGeometry(QRect(460, 140, 49, 16))
        self.label_215 = QLabel(self.frame_102)
        self.label_215.setObjectName(u"label_215")
        self.label_215.setGeometry(QRect(500, 140, 71, 16))
        self.line_34 = QFrame(self.frame_102)
        self.line_34.setObjectName(u"line_34")
        self.line_34.setGeometry(QRect(20, 160, 631, 20))
        self.line_34.setFrameShape(QFrame.HLine)
        self.line_34.setFrameShadow(QFrame.Sunken)
        self.line_49 = QFrame(self.frame_102)
        self.line_49.setObjectName(u"line_49")
        self.line_49.setGeometry(QRect(120, 180, 20, 381))
        self.line_49.setFrameShadow(QFrame.Sunken)
        self.line_49.setFrameShape(QFrame.VLine)
        self.line_50 = QFrame(self.frame_102)
        self.line_50.setObjectName(u"line_50")
        self.line_50.setGeometry(QRect(240, 180, 20, 381))
        self.line_50.setFrameShape(QFrame.VLine)
        self.line_50.setFrameShadow(QFrame.Sunken)
        self.line_51 = QFrame(self.frame_102)
        self.line_51.setObjectName(u"line_51")
        self.line_51.setGeometry(QRect(350, 180, 20, 381))
        self.line_51.setFrameShape(QFrame.VLine)
        self.line_51.setFrameShadow(QFrame.Sunken)
        self.line_52 = QFrame(self.frame_102)
        self.line_52.setObjectName(u"line_52")
        self.line_52.setGeometry(QRect(10, 210, 641, 20))
        self.line_52.setFrameShape(QFrame.HLine)
        self.line_52.setFrameShadow(QFrame.Sunken)
        self.label_266 = QLabel(self.frame_102)
        self.label_266.setObjectName(u"label_266")
        self.label_266.setGeometry(QRect(40, 180, 71, 20))
        self.label_266.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_267 = QLabel(self.frame_102)
        self.label_267.setObjectName(u"label_267")
        self.label_267.setGeometry(QRect(140, 170, 101, 20))
        self.label_267.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_268 = QLabel(self.frame_102)
        self.label_268.setObjectName(u"label_268")
        self.label_268.setGeometry(QRect(170, 190, 31, 20))
        self.label_268.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_269 = QLabel(self.frame_102)
        self.label_269.setObjectName(u"label_269")
        self.label_269.setGeometry(QRect(490, 180, 51, 20))
        self.label_269.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_270 = QLabel(self.frame_102)
        self.label_270.setObjectName(u"label_270")
        self.label_270.setGeometry(QRect(560, 180, 81, 20))
        self.label_270.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_271 = QLabel(self.frame_102)
        self.label_271.setObjectName(u"label_271")
        self.label_271.setGeometry(QRect(10, 220, 101, 16))
        self.label_272 = QLabel(self.frame_102)
        self.label_272.setObjectName(u"label_272")
        self.label_272.setGeometry(QRect(10, 260, 111, 16))
        self.label_273 = QLabel(self.frame_102)
        self.label_273.setObjectName(u"label_273")
        self.label_273.setGeometry(QRect(10, 300, 111, 16))
        self.label_274 = QLabel(self.frame_102)
        self.label_274.setObjectName(u"label_274")
        self.label_274.setGeometry(QRect(10, 340, 111, 16))
        self.label_275 = QLabel(self.frame_102)
        self.label_275.setObjectName(u"label_275")
        self.label_275.setGeometry(QRect(10, 380, 71, 16))
        self.label_276 = QLabel(self.frame_102)
        self.label_276.setObjectName(u"label_276")
        self.label_276.setGeometry(QRect(10, 420, 71, 16))
        self.label_277 = QLabel(self.frame_102)
        self.label_277.setObjectName(u"label_277")
        self.label_277.setGeometry(QRect(10, 460, 81, 16))
        self.label_278 = QLabel(self.frame_102)
        self.label_278.setObjectName(u"label_278")
        self.label_278.setGeometry(QRect(10, 500, 91, 16))
        self.label_279 = QLabel(self.frame_102)
        self.label_279.setObjectName(u"label_279")
        self.label_279.setGeometry(QRect(10, 540, 71, 16))
        self.line_53 = QFrame(self.frame_102)
        self.line_53.setObjectName(u"line_53")
        self.line_53.setGeometry(QRect(10, 240, 641, 20))
        self.line_53.setFrameShape(QFrame.HLine)
        self.line_53.setFrameShadow(QFrame.Sunken)
        self.line_54 = QFrame(self.frame_102)
        self.line_54.setObjectName(u"line_54")
        self.line_54.setGeometry(QRect(10, 280, 641, 20))
        self.line_54.setFrameShape(QFrame.HLine)
        self.line_54.setFrameShadow(QFrame.Sunken)
        self.line_55 = QFrame(self.frame_102)
        self.line_55.setObjectName(u"line_55")
        self.line_55.setGeometry(QRect(10, 320, 641, 20))
        self.line_55.setFrameShape(QFrame.HLine)
        self.line_55.setFrameShadow(QFrame.Sunken)
        self.line_56 = QFrame(self.frame_102)
        self.line_56.setObjectName(u"line_56")
        self.line_56.setGeometry(QRect(10, 360, 641, 20))
        self.line_56.setFrameShadow(QFrame.Sunken)
        self.line_56.setFrameShape(QFrame.HLine)
        self.line_57 = QFrame(self.frame_102)
        self.line_57.setObjectName(u"line_57")
        self.line_57.setGeometry(QRect(10, 400, 641, 20))
        self.line_57.setFrameShape(QFrame.HLine)
        self.line_57.setFrameShadow(QFrame.Sunken)
        self.line_58 = QFrame(self.frame_102)
        self.line_58.setObjectName(u"line_58")
        self.line_58.setGeometry(QRect(10, 440, 641, 20))
        self.line_58.setFrameShape(QFrame.HLine)
        self.line_58.setFrameShadow(QFrame.Sunken)
        self.line_59 = QFrame(self.frame_102)
        self.line_59.setObjectName(u"line_59")
        self.line_59.setGeometry(QRect(10, 480, 641, 20))
        self.line_59.setFrameShape(QFrame.HLine)
        self.line_59.setFrameShadow(QFrame.Sunken)
        self.line_60 = QFrame(self.frame_102)
        self.line_60.setObjectName(u"line_60")
        self.line_60.setGeometry(QRect(10, 520, 641, 20))
        self.line_60.setFrameShape(QFrame.HLine)
        self.line_60.setFrameShadow(QFrame.Sunken)
        self.line_61 = QFrame(self.frame_102)
        self.line_61.setObjectName(u"line_61")
        self.line_61.setGeometry(QRect(10, 560, 641, 20))
        self.line_61.setFrameShape(QFrame.HLine)
        self.line_61.setFrameShadow(QFrame.Sunken)
        self.label_280 = QLabel(self.frame_102)
        self.label_280.setObjectName(u"label_280")
        self.label_280.setGeometry(QRect(50, 580, 71, 16))
        self.label_281 = QLabel(self.frame_102)
        self.label_281.setObjectName(u"label_281")
        self.label_281.setGeometry(QRect(120, 580, 49, 16))
        self.label_282 = QLabel(self.frame_102)
        self.label_282.setObjectName(u"label_282")
        self.label_282.setGeometry(QRect(200, 580, 41, 16))
        self.label_283 = QLabel(self.frame_102)
        self.label_283.setObjectName(u"label_283")
        self.label_283.setGeometry(QRect(240, 580, 49, 16))
        self.label_284 = QLabel(self.frame_102)
        self.label_284.setObjectName(u"label_284")
        self.label_284.setGeometry(QRect(370, 580, 81, 16))
        self.label_285 = QLabel(self.frame_102)
        self.label_285.setObjectName(u"label_285")
        self.label_285.setGeometry(QRect(450, 580, 49, 16))
        self.label_286 = QLabel(self.frame_102)
        self.label_286.setObjectName(u"label_286")
        self.label_286.setGeometry(QRect(100, 600, 181, 16))
        self.label_287 = QLabel(self.frame_102)
        self.label_287.setObjectName(u"label_287")
        self.label_287.setGeometry(QRect(50, 600, 51, 16))
        self.label_288 = QLabel(self.frame_102)
        self.label_288.setObjectName(u"label_288")
        self.label_288.setGeometry(QRect(380, 600, 41, 16))
        self.label_289 = QLabel(self.frame_102)
        self.label_289.setObjectName(u"label_289")
        self.label_289.setGeometry(QRect(430, 600, 181, 16))
        self.label_290 = QLabel(self.frame_102)
        self.label_290.setObjectName(u"label_290")
        self.label_290.setGeometry(QRect(50, 620, 131, 16))
        self.label_291 = QLabel(self.frame_102)
        self.label_291.setObjectName(u"label_291")
        self.label_291.setGeometry(QRect(190, 620, 191, 16))
        self.label_292 = QLabel(self.frame_102)
        self.label_292.setObjectName(u"label_292")
        self.label_292.setGeometry(QRect(510, 620, 81, 16))
        self.label_293 = QLabel(self.frame_102)
        self.label_293.setObjectName(u"label_293")
        self.label_293.setGeometry(QRect(450, 620, 61, 16))
        self.label_294 = QLabel(self.frame_102)
        self.label_294.setObjectName(u"label_294")
        self.label_294.setGeometry(QRect(50, 640, 101, 16))
        self.label_295 = QLabel(self.frame_102)
        self.label_295.setObjectName(u"label_295")
        self.label_295.setGeometry(QRect(150, 640, 231, 16))
        self.label_296 = QLabel(self.frame_102)
        self.label_296.setObjectName(u"label_296")
        self.label_296.setGeometry(QRect(510, 640, 81, 16))
        self.label_297 = QLabel(self.frame_102)
        self.label_297.setObjectName(u"label_297")
        self.label_297.setGeometry(QRect(450, 640, 61, 16))
        self.label_479 = QLabel(self.frame_102)
        self.label_479.setObjectName(u"label_479")
        self.label_479.setGeometry(QRect(260, 170, 91, 20))
        self.label_479.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_480 = QLabel(self.frame_102)
        self.label_480.setObjectName(u"label_480")
        self.label_480.setGeometry(QRect(290, 190, 31, 20))
        self.label_480.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_481 = QLabel(self.frame_102)
        self.label_481.setObjectName(u"label_481")
        self.label_481.setGeometry(QRect(370, 170, 101, 20))
        self.label_481.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_482 = QLabel(self.frame_102)
        self.label_482.setObjectName(u"label_482")
        self.label_482.setGeometry(QRect(400, 190, 41, 20))
        self.label_482.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.line_105 = QFrame(self.frame_102)
        self.line_105.setObjectName(u"line_105")
        self.line_105.setGeometry(QRect(470, 180, 20, 381))
        self.line_105.setFrameShape(QFrame.VLine)
        self.line_105.setFrameShadow(QFrame.Sunken)
        self.line_106 = QFrame(self.frame_102)
        self.line_106.setObjectName(u"line_106")
        self.line_106.setGeometry(QRect(540, 180, 20, 381))
        self.line_106.setFrameShape(QFrame.VLine)
        self.line_106.setFrameShadow(QFrame.Sunken)
        self.label_483 = QLabel(self.frame_102)
        self.label_483.setObjectName(u"label_483")
        self.label_483.setGeometry(QRect(170, 40, 31, 16))
        self.label_484 = QLabel(self.frame_102)
        self.label_484.setObjectName(u"label_484")
        self.label_484.setGeometry(QRect(390, 40, 49, 16))
        self.bt_105 = QPushButton(self.frame_102)
        self.bt_105.setObjectName(u"bt_105")
        self.bt_105.setGeometry(QRect(570, 13, 91, 31))
        self.bt_105.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_105.setIcon(icon24)
        self.bt_105.setIconSize(QSize(20, 20))
        self.label_200.raise_()
        self.label_201.raise_()
        self.label_202.raise_()
        self.label_203.raise_()
        self.label_204.raise_()
        self.line_33.raise_()
        self.label_205.raise_()
        self.label_206.raise_()
        self.label_207.raise_()
        self.label_208.raise_()
        self.label_209.raise_()
        self.label_210.raise_()
        self.label_211.raise_()
        self.label_212.raise_()
        self.label_213.raise_()
        self.label_214.raise_()
        self.label_215.raise_()
        self.line_34.raise_()
        self.line_52.raise_()
        self.label_266.raise_()
        self.label_267.raise_()
        self.label_268.raise_()
        self.label_269.raise_()
        self.label_270.raise_()
        self.label_271.raise_()
        self.label_272.raise_()
        self.label_273.raise_()
        self.label_274.raise_()
        self.label_275.raise_()
        self.label_276.raise_()
        self.label_277.raise_()
        self.label_278.raise_()
        self.label_279.raise_()
        self.line_53.raise_()
        self.line_54.raise_()
        self.line_55.raise_()
        self.line_56.raise_()
        self.line_57.raise_()
        self.line_58.raise_()
        self.line_59.raise_()
        self.line_60.raise_()
        self.line_61.raise_()
        self.label_280.raise_()
        self.label_281.raise_()
        self.label_282.raise_()
        self.label_283.raise_()
        self.label_284.raise_()
        self.label_285.raise_()
        self.label_286.raise_()
        self.label_287.raise_()
        self.label_288.raise_()
        self.label_289.raise_()
        self.label_290.raise_()
        self.label_291.raise_()
        self.label_292.raise_()
        self.label_293.raise_()
        self.label_294.raise_()
        self.label_295.raise_()
        self.label_296.raise_()
        self.label_297.raise_()
        self.label_479.raise_()
        self.label_480.raise_()
        self.label_481.raise_()
        self.label_482.raise_()
        self.line_105.raise_()
        self.line_106.raise_()
        self.line_49.raise_()
        self.line_51.raise_()
        self.line_50.raise_()
        self.label_483.raise_()
        self.label_484.raise_()
        self.bt_105.raise_()

        self.verticalLayout_137.addWidget(self.frame_102)

        self.tabWidget_8.addTab(self.tab_43, "")
        self.tab_44 = QWidget()
        self.tab_44.setObjectName(u"tab_44")
        self.verticalLayout_138 = QVBoxLayout(self.tab_44)
        self.verticalLayout_138.setSpacing(0)
        self.verticalLayout_138.setObjectName(u"verticalLayout_138")
        self.verticalLayout_138.setContentsMargins(0, 0, 0, 0)
        self.frame_179 = QFrame(self.tab_44)
        self.frame_179.setObjectName(u"frame_179")
        self.frame_179.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(222, 222, 222);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 148, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(0, 213, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_179.setFrameShape(QFrame.StyledPanel)
        self.frame_179.setFrameShadow(QFrame.Raised)
        self.label_487 = QLabel(self.frame_179)
        self.label_487.setObjectName(u"label_487")
        self.label_487.setGeometry(QRect(180, 10, 311, 21))
        self.label_487.setStyleSheet(u"font: 900 14pt \"Roboto\";")
        self.label_487.setAlignment(Qt.AlignCenter)
        self.label_488 = QLabel(self.frame_179)
        self.label_488.setObjectName(u"label_488")
        self.label_488.setGeometry(QRect(210, 40, 141, 16))
        self.label_489 = QLabel(self.frame_179)
        self.label_489.setObjectName(u"label_489")
        self.label_489.setGeometry(QRect(440, 40, 171, 16))
        self.label_490 = QLabel(self.frame_179)
        self.label_490.setObjectName(u"label_490")
        self.label_490.setGeometry(QRect(220, 60, 221, 20))
        self.label_490.setAlignment(Qt.AlignCenter)
        self.label_491 = QLabel(self.frame_179)
        self.label_491.setObjectName(u"label_491")
        self.label_491.setGeometry(QRect(70, 100, 49, 16))
        self.line_104 = QFrame(self.frame_179)
        self.line_104.setObjectName(u"line_104")
        self.line_104.setGeometry(QRect(90, 80, 501, 16))
        self.line_104.setFrameShape(QFrame.HLine)
        self.line_104.setFrameShadow(QFrame.Sunken)
        self.label_492 = QLabel(self.frame_179)
        self.label_492.setObjectName(u"label_492")
        self.label_492.setGeometry(QRect(120, 100, 71, 16))
        self.label_492.setStyleSheet(u"color: rgb(149, 149, 0);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_493 = QLabel(self.frame_179)
        self.label_493.setObjectName(u"label_493")
        self.label_493.setGeometry(QRect(220, 100, 41, 16))
        self.label_494 = QLabel(self.frame_179)
        self.label_494.setObjectName(u"label_494")
        self.label_494.setGeometry(QRect(270, 100, 151, 16))
        self.label_494.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_494.setTextFormat(Qt.AutoText)
        self.label_494.setScaledContents(False)
        self.label_495 = QLabel(self.frame_179)
        self.label_495.setObjectName(u"label_495")
        self.label_495.setGeometry(QRect(80, 140, 91, 16))
        self.label_496 = QLabel(self.frame_179)
        self.label_496.setObjectName(u"label_496")
        self.label_496.setGeometry(QRect(160, 140, 71, 16))
        self.label_497 = QLabel(self.frame_179)
        self.label_497.setObjectName(u"label_497")
        self.label_497.setGeometry(QRect(260, 140, 101, 16))
        self.label_498 = QLabel(self.frame_179)
        self.label_498.setObjectName(u"label_498")
        self.label_498.setGeometry(QRect(360, 140, 61, 16))
        self.label_499 = QLabel(self.frame_179)
        self.label_499.setObjectName(u"label_499")
        self.label_499.setGeometry(QRect(430, 100, 49, 16))
        self.label_500 = QLabel(self.frame_179)
        self.label_500.setObjectName(u"label_500")
        self.label_500.setGeometry(QRect(470, 100, 91, 16))
        self.label_501 = QLabel(self.frame_179)
        self.label_501.setObjectName(u"label_501")
        self.label_501.setGeometry(QRect(460, 140, 49, 16))
        self.label_502 = QLabel(self.frame_179)
        self.label_502.setObjectName(u"label_502")
        self.label_502.setGeometry(QRect(500, 140, 71, 16))
        self.line_107 = QFrame(self.frame_179)
        self.line_107.setObjectName(u"line_107")
        self.line_107.setGeometry(QRect(20, 160, 631, 20))
        self.line_107.setFrameShape(QFrame.HLine)
        self.line_107.setFrameShadow(QFrame.Sunken)
        self.line_108 = QFrame(self.frame_179)
        self.line_108.setObjectName(u"line_108")
        self.line_108.setGeometry(QRect(120, 180, 20, 381))
        self.line_108.setFrameShadow(QFrame.Sunken)
        self.line_108.setFrameShape(QFrame.VLine)
        self.line_109 = QFrame(self.frame_179)
        self.line_109.setObjectName(u"line_109")
        self.line_109.setGeometry(QRect(240, 180, 20, 381))
        self.line_109.setFrameShape(QFrame.VLine)
        self.line_109.setFrameShadow(QFrame.Sunken)
        self.line_110 = QFrame(self.frame_179)
        self.line_110.setObjectName(u"line_110")
        self.line_110.setGeometry(QRect(350, 180, 20, 381))
        self.line_110.setFrameShape(QFrame.VLine)
        self.line_110.setFrameShadow(QFrame.Sunken)
        self.line_111 = QFrame(self.frame_179)
        self.line_111.setObjectName(u"line_111")
        self.line_111.setGeometry(QRect(10, 210, 641, 20))
        self.line_111.setFrameShape(QFrame.HLine)
        self.line_111.setFrameShadow(QFrame.Sunken)
        self.label_503 = QLabel(self.frame_179)
        self.label_503.setObjectName(u"label_503")
        self.label_503.setGeometry(QRect(40, 180, 71, 20))
        self.label_503.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_504 = QLabel(self.frame_179)
        self.label_504.setObjectName(u"label_504")
        self.label_504.setGeometry(QRect(140, 170, 101, 20))
        self.label_504.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_505 = QLabel(self.frame_179)
        self.label_505.setObjectName(u"label_505")
        self.label_505.setGeometry(QRect(170, 190, 31, 20))
        self.label_505.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_506 = QLabel(self.frame_179)
        self.label_506.setObjectName(u"label_506")
        self.label_506.setGeometry(QRect(490, 180, 51, 20))
        self.label_506.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_507 = QLabel(self.frame_179)
        self.label_507.setObjectName(u"label_507")
        self.label_507.setGeometry(QRect(560, 180, 81, 20))
        self.label_507.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_508 = QLabel(self.frame_179)
        self.label_508.setObjectName(u"label_508")
        self.label_508.setGeometry(QRect(10, 220, 101, 16))
        self.label_509 = QLabel(self.frame_179)
        self.label_509.setObjectName(u"label_509")
        self.label_509.setGeometry(QRect(10, 260, 111, 16))
        self.label_510 = QLabel(self.frame_179)
        self.label_510.setObjectName(u"label_510")
        self.label_510.setGeometry(QRect(10, 300, 111, 16))
        self.label_511 = QLabel(self.frame_179)
        self.label_511.setObjectName(u"label_511")
        self.label_511.setGeometry(QRect(10, 340, 111, 16))
        self.label_512 = QLabel(self.frame_179)
        self.label_512.setObjectName(u"label_512")
        self.label_512.setGeometry(QRect(10, 380, 71, 16))
        self.label_513 = QLabel(self.frame_179)
        self.label_513.setObjectName(u"label_513")
        self.label_513.setGeometry(QRect(10, 420, 71, 16))
        self.label_514 = QLabel(self.frame_179)
        self.label_514.setObjectName(u"label_514")
        self.label_514.setGeometry(QRect(10, 460, 81, 16))
        self.label_515 = QLabel(self.frame_179)
        self.label_515.setObjectName(u"label_515")
        self.label_515.setGeometry(QRect(10, 500, 91, 16))
        self.label_516 = QLabel(self.frame_179)
        self.label_516.setObjectName(u"label_516")
        self.label_516.setGeometry(QRect(10, 540, 71, 16))
        self.line_112 = QFrame(self.frame_179)
        self.line_112.setObjectName(u"line_112")
        self.line_112.setGeometry(QRect(10, 240, 641, 20))
        self.line_112.setFrameShape(QFrame.HLine)
        self.line_112.setFrameShadow(QFrame.Sunken)
        self.line_113 = QFrame(self.frame_179)
        self.line_113.setObjectName(u"line_113")
        self.line_113.setGeometry(QRect(10, 280, 641, 20))
        self.line_113.setFrameShape(QFrame.HLine)
        self.line_113.setFrameShadow(QFrame.Sunken)
        self.line_114 = QFrame(self.frame_179)
        self.line_114.setObjectName(u"line_114")
        self.line_114.setGeometry(QRect(10, 320, 641, 20))
        self.line_114.setFrameShape(QFrame.HLine)
        self.line_114.setFrameShadow(QFrame.Sunken)
        self.line_115 = QFrame(self.frame_179)
        self.line_115.setObjectName(u"line_115")
        self.line_115.setGeometry(QRect(10, 360, 641, 20))
        self.line_115.setFrameShadow(QFrame.Sunken)
        self.line_115.setFrameShape(QFrame.HLine)
        self.line_116 = QFrame(self.frame_179)
        self.line_116.setObjectName(u"line_116")
        self.line_116.setGeometry(QRect(10, 400, 641, 20))
        self.line_116.setFrameShape(QFrame.HLine)
        self.line_116.setFrameShadow(QFrame.Sunken)
        self.line_117 = QFrame(self.frame_179)
        self.line_117.setObjectName(u"line_117")
        self.line_117.setGeometry(QRect(10, 440, 641, 20))
        self.line_117.setFrameShape(QFrame.HLine)
        self.line_117.setFrameShadow(QFrame.Sunken)
        self.line_118 = QFrame(self.frame_179)
        self.line_118.setObjectName(u"line_118")
        self.line_118.setGeometry(QRect(10, 480, 641, 20))
        self.line_118.setFrameShape(QFrame.HLine)
        self.line_118.setFrameShadow(QFrame.Sunken)
        self.line_119 = QFrame(self.frame_179)
        self.line_119.setObjectName(u"line_119")
        self.line_119.setGeometry(QRect(10, 520, 641, 20))
        self.line_119.setFrameShape(QFrame.HLine)
        self.line_119.setFrameShadow(QFrame.Sunken)
        self.line_120 = QFrame(self.frame_179)
        self.line_120.setObjectName(u"line_120")
        self.line_120.setGeometry(QRect(10, 560, 641, 20))
        self.line_120.setFrameShape(QFrame.HLine)
        self.line_120.setFrameShadow(QFrame.Sunken)
        self.label_517 = QLabel(self.frame_179)
        self.label_517.setObjectName(u"label_517")
        self.label_517.setGeometry(QRect(50, 580, 71, 16))
        self.label_518 = QLabel(self.frame_179)
        self.label_518.setObjectName(u"label_518")
        self.label_518.setGeometry(QRect(120, 580, 49, 16))
        self.label_519 = QLabel(self.frame_179)
        self.label_519.setObjectName(u"label_519")
        self.label_519.setGeometry(QRect(200, 580, 41, 16))
        self.label_520 = QLabel(self.frame_179)
        self.label_520.setObjectName(u"label_520")
        self.label_520.setGeometry(QRect(240, 580, 49, 16))
        self.label_521 = QLabel(self.frame_179)
        self.label_521.setObjectName(u"label_521")
        self.label_521.setGeometry(QRect(370, 580, 81, 16))
        self.label_522 = QLabel(self.frame_179)
        self.label_522.setObjectName(u"label_522")
        self.label_522.setGeometry(QRect(450, 580, 49, 16))
        self.label_523 = QLabel(self.frame_179)
        self.label_523.setObjectName(u"label_523")
        self.label_523.setGeometry(QRect(100, 600, 181, 16))
        self.label_524 = QLabel(self.frame_179)
        self.label_524.setObjectName(u"label_524")
        self.label_524.setGeometry(QRect(50, 600, 51, 16))
        self.label_525 = QLabel(self.frame_179)
        self.label_525.setObjectName(u"label_525")
        self.label_525.setGeometry(QRect(380, 600, 41, 16))
        self.label_526 = QLabel(self.frame_179)
        self.label_526.setObjectName(u"label_526")
        self.label_526.setGeometry(QRect(430, 600, 181, 16))
        self.label_527 = QLabel(self.frame_179)
        self.label_527.setObjectName(u"label_527")
        self.label_527.setGeometry(QRect(50, 620, 131, 16))
        self.label_528 = QLabel(self.frame_179)
        self.label_528.setObjectName(u"label_528")
        self.label_528.setGeometry(QRect(190, 620, 191, 16))
        self.label_529 = QLabel(self.frame_179)
        self.label_529.setObjectName(u"label_529")
        self.label_529.setGeometry(QRect(510, 620, 81, 16))
        self.label_530 = QLabel(self.frame_179)
        self.label_530.setObjectName(u"label_530")
        self.label_530.setGeometry(QRect(450, 620, 61, 16))
        self.label_531 = QLabel(self.frame_179)
        self.label_531.setObjectName(u"label_531")
        self.label_531.setGeometry(QRect(50, 640, 101, 16))
        self.label_532 = QLabel(self.frame_179)
        self.label_532.setObjectName(u"label_532")
        self.label_532.setGeometry(QRect(150, 640, 231, 16))
        self.label_533 = QLabel(self.frame_179)
        self.label_533.setObjectName(u"label_533")
        self.label_533.setGeometry(QRect(510, 640, 81, 16))
        self.label_534 = QLabel(self.frame_179)
        self.label_534.setObjectName(u"label_534")
        self.label_534.setGeometry(QRect(450, 640, 61, 16))
        self.label_535 = QLabel(self.frame_179)
        self.label_535.setObjectName(u"label_535")
        self.label_535.setGeometry(QRect(260, 170, 91, 20))
        self.label_535.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_536 = QLabel(self.frame_179)
        self.label_536.setObjectName(u"label_536")
        self.label_536.setGeometry(QRect(290, 190, 31, 20))
        self.label_536.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_537 = QLabel(self.frame_179)
        self.label_537.setObjectName(u"label_537")
        self.label_537.setGeometry(QRect(370, 170, 101, 20))
        self.label_537.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_538 = QLabel(self.frame_179)
        self.label_538.setObjectName(u"label_538")
        self.label_538.setGeometry(QRect(400, 190, 41, 20))
        self.label_538.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.line_121 = QFrame(self.frame_179)
        self.line_121.setObjectName(u"line_121")
        self.line_121.setGeometry(QRect(470, 180, 20, 381))
        self.line_121.setFrameShape(QFrame.VLine)
        self.line_121.setFrameShadow(QFrame.Sunken)
        self.line_122 = QFrame(self.frame_179)
        self.line_122.setObjectName(u"line_122")
        self.line_122.setGeometry(QRect(540, 180, 20, 381))
        self.line_122.setFrameShape(QFrame.VLine)
        self.line_122.setFrameShadow(QFrame.Sunken)
        self.label_539 = QLabel(self.frame_179)
        self.label_539.setObjectName(u"label_539")
        self.label_539.setGeometry(QRect(170, 40, 31, 16))
        self.label_540 = QLabel(self.frame_179)
        self.label_540.setObjectName(u"label_540")
        self.label_540.setGeometry(QRect(390, 40, 49, 16))
        self.bt_106 = QPushButton(self.frame_179)
        self.bt_106.setObjectName(u"bt_106")
        self.bt_106.setGeometry(QRect(584, 13, 81, 41))
        self.bt_106.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_106.setIcon(icon24)
        self.bt_106.setIconSize(QSize(20, 20))

        self.verticalLayout_138.addWidget(self.frame_179)

        self.tabWidget_8.addTab(self.tab_44, "")
        self.tab_45 = QWidget()
        self.tab_45.setObjectName(u"tab_45")
        self.verticalLayout_160 = QVBoxLayout(self.tab_45)
        self.verticalLayout_160.setObjectName(u"verticalLayout_160")
        self.frame_202 = QFrame(self.tab_45)
        self.frame_202.setObjectName(u"frame_202")
        self.frame_202.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(222, 222, 222);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 148, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(0, 213, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_202.setFrameShape(QFrame.StyledPanel)
        self.frame_202.setFrameShadow(QFrame.Raised)
        self.label_1016 = QLabel(self.frame_202)
        self.label_1016.setObjectName(u"label_1016")
        self.label_1016.setGeometry(QRect(180, 10, 311, 21))
        self.label_1016.setStyleSheet(u"font: 900 14pt \"Roboto\";")
        self.label_1016.setAlignment(Qt.AlignCenter)
        self.label_1117 = QLabel(self.frame_202)
        self.label_1117.setObjectName(u"label_1117")
        self.label_1117.setGeometry(QRect(210, 40, 141, 16))
        self.label_1118 = QLabel(self.frame_202)
        self.label_1118.setObjectName(u"label_1118")
        self.label_1118.setGeometry(QRect(440, 40, 171, 16))
        self.label_1119 = QLabel(self.frame_202)
        self.label_1119.setObjectName(u"label_1119")
        self.label_1119.setGeometry(QRect(220, 60, 221, 20))
        self.label_1119.setAlignment(Qt.AlignCenter)
        self.label_1120 = QLabel(self.frame_202)
        self.label_1120.setObjectName(u"label_1120")
        self.label_1120.setGeometry(QRect(70, 100, 49, 16))
        self.line_233 = QFrame(self.frame_202)
        self.line_233.setObjectName(u"line_233")
        self.line_233.setGeometry(QRect(90, 80, 501, 16))
        self.line_233.setFrameShape(QFrame.HLine)
        self.line_233.setFrameShadow(QFrame.Sunken)
        self.label_1121 = QLabel(self.frame_202)
        self.label_1121.setObjectName(u"label_1121")
        self.label_1121.setGeometry(QRect(120, 100, 71, 16))
        self.label_1121.setStyleSheet(u"color: rgb(149, 149, 0);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_1122 = QLabel(self.frame_202)
        self.label_1122.setObjectName(u"label_1122")
        self.label_1122.setGeometry(QRect(220, 100, 41, 16))
        self.label_1123 = QLabel(self.frame_202)
        self.label_1123.setObjectName(u"label_1123")
        self.label_1123.setGeometry(QRect(270, 100, 151, 16))
        self.label_1123.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_1123.setTextFormat(Qt.AutoText)
        self.label_1123.setScaledContents(False)
        self.label_1124 = QLabel(self.frame_202)
        self.label_1124.setObjectName(u"label_1124")
        self.label_1124.setGeometry(QRect(80, 140, 91, 16))
        self.label_1125 = QLabel(self.frame_202)
        self.label_1125.setObjectName(u"label_1125")
        self.label_1125.setGeometry(QRect(160, 140, 71, 16))
        self.label_1126 = QLabel(self.frame_202)
        self.label_1126.setObjectName(u"label_1126")
        self.label_1126.setGeometry(QRect(260, 140, 101, 16))
        self.label_1127 = QLabel(self.frame_202)
        self.label_1127.setObjectName(u"label_1127")
        self.label_1127.setGeometry(QRect(360, 140, 61, 16))
        self.label_1128 = QLabel(self.frame_202)
        self.label_1128.setObjectName(u"label_1128")
        self.label_1128.setGeometry(QRect(430, 100, 49, 16))
        self.label_1129 = QLabel(self.frame_202)
        self.label_1129.setObjectName(u"label_1129")
        self.label_1129.setGeometry(QRect(470, 100, 91, 16))
        self.label_1130 = QLabel(self.frame_202)
        self.label_1130.setObjectName(u"label_1130")
        self.label_1130.setGeometry(QRect(460, 140, 49, 16))
        self.label_1131 = QLabel(self.frame_202)
        self.label_1131.setObjectName(u"label_1131")
        self.label_1131.setGeometry(QRect(500, 140, 71, 16))
        self.line_234 = QFrame(self.frame_202)
        self.line_234.setObjectName(u"line_234")
        self.line_234.setGeometry(QRect(20, 160, 631, 20))
        self.line_234.setFrameShape(QFrame.HLine)
        self.line_234.setFrameShadow(QFrame.Sunken)
        self.line_235 = QFrame(self.frame_202)
        self.line_235.setObjectName(u"line_235")
        self.line_235.setGeometry(QRect(120, 180, 20, 381))
        self.line_235.setFrameShadow(QFrame.Sunken)
        self.line_235.setFrameShape(QFrame.VLine)
        self.line_236 = QFrame(self.frame_202)
        self.line_236.setObjectName(u"line_236")
        self.line_236.setGeometry(QRect(240, 180, 20, 381))
        self.line_236.setFrameShape(QFrame.VLine)
        self.line_236.setFrameShadow(QFrame.Sunken)
        self.line_237 = QFrame(self.frame_202)
        self.line_237.setObjectName(u"line_237")
        self.line_237.setGeometry(QRect(350, 180, 20, 381))
        self.line_237.setFrameShape(QFrame.VLine)
        self.line_237.setFrameShadow(QFrame.Sunken)
        self.line_238 = QFrame(self.frame_202)
        self.line_238.setObjectName(u"line_238")
        self.line_238.setGeometry(QRect(10, 210, 641, 20))
        self.line_238.setFrameShape(QFrame.HLine)
        self.line_238.setFrameShadow(QFrame.Sunken)
        self.label_1132 = QLabel(self.frame_202)
        self.label_1132.setObjectName(u"label_1132")
        self.label_1132.setGeometry(QRect(40, 180, 71, 20))
        self.label_1132.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_1133 = QLabel(self.frame_202)
        self.label_1133.setObjectName(u"label_1133")
        self.label_1133.setGeometry(QRect(140, 170, 101, 20))
        self.label_1133.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_1134 = QLabel(self.frame_202)
        self.label_1134.setObjectName(u"label_1134")
        self.label_1134.setGeometry(QRect(170, 190, 31, 20))
        self.label_1134.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_1135 = QLabel(self.frame_202)
        self.label_1135.setObjectName(u"label_1135")
        self.label_1135.setGeometry(QRect(490, 180, 51, 20))
        self.label_1135.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_1136 = QLabel(self.frame_202)
        self.label_1136.setObjectName(u"label_1136")
        self.label_1136.setGeometry(QRect(560, 180, 81, 20))
        self.label_1136.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_1137 = QLabel(self.frame_202)
        self.label_1137.setObjectName(u"label_1137")
        self.label_1137.setGeometry(QRect(10, 220, 101, 16))
        self.label_1138 = QLabel(self.frame_202)
        self.label_1138.setObjectName(u"label_1138")
        self.label_1138.setGeometry(QRect(10, 260, 111, 16))
        self.label_1139 = QLabel(self.frame_202)
        self.label_1139.setObjectName(u"label_1139")
        self.label_1139.setGeometry(QRect(10, 300, 111, 16))
        self.label_1140 = QLabel(self.frame_202)
        self.label_1140.setObjectName(u"label_1140")
        self.label_1140.setGeometry(QRect(10, 340, 111, 16))
        self.label_1141 = QLabel(self.frame_202)
        self.label_1141.setObjectName(u"label_1141")
        self.label_1141.setGeometry(QRect(10, 380, 71, 16))
        self.label_1142 = QLabel(self.frame_202)
        self.label_1142.setObjectName(u"label_1142")
        self.label_1142.setGeometry(QRect(10, 420, 71, 16))
        self.label_1143 = QLabel(self.frame_202)
        self.label_1143.setObjectName(u"label_1143")
        self.label_1143.setGeometry(QRect(10, 460, 81, 16))
        self.label_1144 = QLabel(self.frame_202)
        self.label_1144.setObjectName(u"label_1144")
        self.label_1144.setGeometry(QRect(10, 500, 91, 16))
        self.label_1145 = QLabel(self.frame_202)
        self.label_1145.setObjectName(u"label_1145")
        self.label_1145.setGeometry(QRect(10, 540, 71, 16))
        self.line_239 = QFrame(self.frame_202)
        self.line_239.setObjectName(u"line_239")
        self.line_239.setGeometry(QRect(10, 240, 641, 20))
        self.line_239.setFrameShape(QFrame.HLine)
        self.line_239.setFrameShadow(QFrame.Sunken)
        self.line_240 = QFrame(self.frame_202)
        self.line_240.setObjectName(u"line_240")
        self.line_240.setGeometry(QRect(10, 280, 641, 20))
        self.line_240.setFrameShape(QFrame.HLine)
        self.line_240.setFrameShadow(QFrame.Sunken)
        self.line_241 = QFrame(self.frame_202)
        self.line_241.setObjectName(u"line_241")
        self.line_241.setGeometry(QRect(10, 320, 641, 20))
        self.line_241.setFrameShape(QFrame.HLine)
        self.line_241.setFrameShadow(QFrame.Sunken)
        self.line_242 = QFrame(self.frame_202)
        self.line_242.setObjectName(u"line_242")
        self.line_242.setGeometry(QRect(10, 360, 641, 20))
        self.line_242.setFrameShadow(QFrame.Sunken)
        self.line_242.setFrameShape(QFrame.HLine)
        self.line_243 = QFrame(self.frame_202)
        self.line_243.setObjectName(u"line_243")
        self.line_243.setGeometry(QRect(10, 400, 641, 20))
        self.line_243.setFrameShape(QFrame.HLine)
        self.line_243.setFrameShadow(QFrame.Sunken)
        self.line_244 = QFrame(self.frame_202)
        self.line_244.setObjectName(u"line_244")
        self.line_244.setGeometry(QRect(10, 440, 641, 20))
        self.line_244.setFrameShape(QFrame.HLine)
        self.line_244.setFrameShadow(QFrame.Sunken)
        self.line_245 = QFrame(self.frame_202)
        self.line_245.setObjectName(u"line_245")
        self.line_245.setGeometry(QRect(10, 480, 641, 20))
        self.line_245.setFrameShape(QFrame.HLine)
        self.line_245.setFrameShadow(QFrame.Sunken)
        self.line_246 = QFrame(self.frame_202)
        self.line_246.setObjectName(u"line_246")
        self.line_246.setGeometry(QRect(10, 520, 641, 20))
        self.line_246.setFrameShape(QFrame.HLine)
        self.line_246.setFrameShadow(QFrame.Sunken)
        self.line_247 = QFrame(self.frame_202)
        self.line_247.setObjectName(u"line_247")
        self.line_247.setGeometry(QRect(10, 560, 641, 20))
        self.line_247.setFrameShape(QFrame.HLine)
        self.line_247.setFrameShadow(QFrame.Sunken)
        self.label_1146 = QLabel(self.frame_202)
        self.label_1146.setObjectName(u"label_1146")
        self.label_1146.setGeometry(QRect(50, 580, 71, 16))
        self.label_1147 = QLabel(self.frame_202)
        self.label_1147.setObjectName(u"label_1147")
        self.label_1147.setGeometry(QRect(120, 580, 49, 16))
        self.label_1148 = QLabel(self.frame_202)
        self.label_1148.setObjectName(u"label_1148")
        self.label_1148.setGeometry(QRect(200, 580, 41, 16))
        self.label_1149 = QLabel(self.frame_202)
        self.label_1149.setObjectName(u"label_1149")
        self.label_1149.setGeometry(QRect(240, 580, 49, 16))
        self.label_1150 = QLabel(self.frame_202)
        self.label_1150.setObjectName(u"label_1150")
        self.label_1150.setGeometry(QRect(370, 580, 81, 16))
        self.label_1151 = QLabel(self.frame_202)
        self.label_1151.setObjectName(u"label_1151")
        self.label_1151.setGeometry(QRect(450, 580, 49, 16))
        self.label_1152 = QLabel(self.frame_202)
        self.label_1152.setObjectName(u"label_1152")
        self.label_1152.setGeometry(QRect(100, 600, 181, 16))
        self.label_1153 = QLabel(self.frame_202)
        self.label_1153.setObjectName(u"label_1153")
        self.label_1153.setGeometry(QRect(50, 600, 51, 16))
        self.label_1154 = QLabel(self.frame_202)
        self.label_1154.setObjectName(u"label_1154")
        self.label_1154.setGeometry(QRect(380, 600, 41, 16))
        self.label_1155 = QLabel(self.frame_202)
        self.label_1155.setObjectName(u"label_1155")
        self.label_1155.setGeometry(QRect(430, 600, 181, 16))
        self.label_1156 = QLabel(self.frame_202)
        self.label_1156.setObjectName(u"label_1156")
        self.label_1156.setGeometry(QRect(50, 620, 131, 16))
        self.label_1157 = QLabel(self.frame_202)
        self.label_1157.setObjectName(u"label_1157")
        self.label_1157.setGeometry(QRect(190, 620, 191, 16))
        self.label_1158 = QLabel(self.frame_202)
        self.label_1158.setObjectName(u"label_1158")
        self.label_1158.setGeometry(QRect(510, 620, 81, 16))
        self.label_1159 = QLabel(self.frame_202)
        self.label_1159.setObjectName(u"label_1159")
        self.label_1159.setGeometry(QRect(450, 620, 61, 16))
        self.label_1160 = QLabel(self.frame_202)
        self.label_1160.setObjectName(u"label_1160")
        self.label_1160.setGeometry(QRect(50, 640, 101, 16))
        self.label_1161 = QLabel(self.frame_202)
        self.label_1161.setObjectName(u"label_1161")
        self.label_1161.setGeometry(QRect(150, 640, 231, 16))
        self.label_1162 = QLabel(self.frame_202)
        self.label_1162.setObjectName(u"label_1162")
        self.label_1162.setGeometry(QRect(510, 640, 81, 16))
        self.label_1163 = QLabel(self.frame_202)
        self.label_1163.setObjectName(u"label_1163")
        self.label_1163.setGeometry(QRect(450, 640, 61, 16))
        self.label_1164 = QLabel(self.frame_202)
        self.label_1164.setObjectName(u"label_1164")
        self.label_1164.setGeometry(QRect(260, 170, 91, 20))
        self.label_1164.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_1165 = QLabel(self.frame_202)
        self.label_1165.setObjectName(u"label_1165")
        self.label_1165.setGeometry(QRect(290, 190, 31, 20))
        self.label_1165.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_1166 = QLabel(self.frame_202)
        self.label_1166.setObjectName(u"label_1166")
        self.label_1166.setGeometry(QRect(370, 170, 101, 20))
        self.label_1166.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_1167 = QLabel(self.frame_202)
        self.label_1167.setObjectName(u"label_1167")
        self.label_1167.setGeometry(QRect(400, 190, 41, 20))
        self.label_1167.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.line_248 = QFrame(self.frame_202)
        self.line_248.setObjectName(u"line_248")
        self.line_248.setGeometry(QRect(470, 180, 20, 381))
        self.line_248.setFrameShape(QFrame.VLine)
        self.line_248.setFrameShadow(QFrame.Sunken)
        self.line_249 = QFrame(self.frame_202)
        self.line_249.setObjectName(u"line_249")
        self.line_249.setGeometry(QRect(540, 180, 20, 381))
        self.line_249.setFrameShape(QFrame.VLine)
        self.line_249.setFrameShadow(QFrame.Sunken)
        self.label_1168 = QLabel(self.frame_202)
        self.label_1168.setObjectName(u"label_1168")
        self.label_1168.setGeometry(QRect(170, 40, 31, 16))
        self.label_1169 = QLabel(self.frame_202)
        self.label_1169.setObjectName(u"label_1169")
        self.label_1169.setGeometry(QRect(390, 40, 49, 16))
        self.bt_124 = QPushButton(self.frame_202)
        self.bt_124.setObjectName(u"bt_124")
        self.bt_124.setGeometry(QRect(584, 13, 81, 41))
        self.bt_124.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_124.setIcon(icon24)
        self.bt_124.setIconSize(QSize(20, 20))

        self.verticalLayout_160.addWidget(self.frame_202)

        self.tabWidget_8.addTab(self.tab_45, "")

        self.verticalLayout_82.addWidget(self.tabWidget_8)


        self.horizontalLayout_35.addWidget(self.frame_99)

        self.horizontalLayout_35.setStretch(0, 2)
        self.horizontalLayout_35.setStretch(1, 8)
        self.tabWidget_7.addTab(self.tab_23, "")
        self.tab_27 = QWidget()
        self.tab_27.setObjectName(u"tab_27")
        self.verticalLayout_83 = QVBoxLayout(self.tab_27)
        self.verticalLayout_83.setSpacing(0)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.verticalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.frame_103 = QFrame(self.tab_27)
        self.frame_103.setObjectName(u"frame_103")
        self.frame_103.setFrameShape(QFrame.StyledPanel)
        self.frame_103.setFrameShadow(QFrame.Raised)
        self.verticalLayout_84 = QVBoxLayout(self.frame_103)
        self.verticalLayout_84.setSpacing(0)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.verticalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.frame_104 = QFrame(self.frame_103)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setFrameShape(QFrame.StyledPanel)
        self.frame_104.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_104)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.groupBox_21 = QGroupBox(self.frame_104)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.groupBox_21.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QComboBox{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QDateEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 900 12pt \"Roboto Black\";\n"
"}")
        self.horizontalLayout_40 = QHBoxLayout(self.groupBox_21)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.frame_105 = QFrame(self.groupBox_21)
        self.frame_105.setObjectName(u"frame_105")
        self.frame_105.setFrameShape(QFrame.NoFrame)
        self.frame_105.setFrameShadow(QFrame.Raised)
        self.label_222 = QLabel(self.frame_105)
        self.label_222.setObjectName(u"label_222")
        self.label_222.setGeometry(QRect(20, 250, 81, 31))
        self.lineEdit_68 = QLineEdit(self.frame_105)
        self.lineEdit_68.setObjectName(u"lineEdit_68")
        self.lineEdit_68.setGeometry(QRect(110, 150, 161, 31))
        self.lineEdit_68.setClearButtonEnabled(True)
        self.label_223 = QLabel(self.frame_105)
        self.label_223.setObjectName(u"label_223")
        self.label_223.setGeometry(QRect(0, 0, 101, 31))
        self.lineEdit_69 = QLineEdit(self.frame_105)
        self.lineEdit_69.setObjectName(u"lineEdit_69")
        self.lineEdit_69.setGeometry(QRect(100, 200, 171, 31))
        self.lineEdit_69.setClearButtonEnabled(True)
        self.label_224 = QLabel(self.frame_105)
        self.label_224.setObjectName(u"label_224")
        self.label_224.setGeometry(QRect(20, 200, 81, 31))
        self.label_225 = QLabel(self.frame_105)
        self.label_225.setObjectName(u"label_225")
        self.label_225.setGeometry(QRect(0, 150, 101, 31))
        self.label_226 = QLabel(self.frame_105)
        self.label_226.setObjectName(u"label_226")
        self.label_226.setGeometry(QRect(10, 100, 61, 31))
        self.comboBox_35 = QComboBox(self.frame_105)
        self.comboBox_35.addItem("")
        self.comboBox_35.addItem("")
        self.comboBox_35.addItem("")
        self.comboBox_35.setObjectName(u"comboBox_35")
        self.comboBox_35.setGeometry(QRect(100, 100, 171, 31))
        self.lineEdit_70 = QLineEdit(self.frame_105)
        self.lineEdit_70.setObjectName(u"lineEdit_70")
        self.lineEdit_70.setGeometry(QRect(100, 0, 171, 31))
        self.lineEdit_70.setClearButtonEnabled(True)
        self.label_227 = QLabel(self.frame_105)
        self.label_227.setObjectName(u"label_227")
        self.label_227.setGeometry(QRect(10, 50, 51, 31))
        self.comboBox_34 = QComboBox(self.frame_105)
        self.comboBox_34.addItem("")
        self.comboBox_34.addItem("")
        self.comboBox_34.addItem("")
        self.comboBox_34.addItem("")
        self.comboBox_34.addItem("")
        self.comboBox_34.addItem("")
        self.comboBox_34.addItem("")
        self.comboBox_34.addItem("")
        self.comboBox_34.addItem("")
        self.comboBox_34.setObjectName(u"comboBox_34")
        self.comboBox_34.setGeometry(QRect(100, 50, 171, 31))
        self.lineEdit_94 = QLineEdit(self.frame_105)
        self.lineEdit_94.setObjectName(u"lineEdit_94")
        self.lineEdit_94.setGeometry(QRect(100, 250, 171, 31))
        self.lineEdit_94.setClearButtonEnabled(True)

        self.horizontalLayout_40.addWidget(self.frame_105)

        self.frame_106 = QFrame(self.groupBox_21)
        self.frame_106.setObjectName(u"frame_106")
        self.frame_106.setMaximumSize(QSize(120, 500))
        self.frame_106.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(158, 158, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(255, 255, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_106.setFrameShape(QFrame.NoFrame)
        self.frame_106.setFrameShadow(QFrame.Raised)
        self.bt_64 = QPushButton(self.frame_106)
        self.bt_64.setObjectName(u"bt_64")
        self.bt_64.setGeometry(QRect(20, 170, 91, 30))
        self.bt_64.setMaximumSize(QSize(120, 30))
        self.bt_64.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_64.setIcon(icon20)
        self.bt_64.setIconSize(QSize(20, 20))
        self.bt_65 = QPushButton(self.frame_106)
        self.bt_65.setObjectName(u"bt_65")
        self.bt_65.setGeometry(QRect(20, 120, 89, 30))
        self.bt_65.setMaximumSize(QSize(120, 30))
        self.bt_65.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_65.setIcon(icon22)
        self.bt_65.setIconSize(QSize(20, 20))
        self.bt_66 = QPushButton(self.frame_106)
        self.bt_66.setObjectName(u"bt_66")
        self.bt_66.setGeometry(QRect(20, 70, 91, 30))
        self.bt_66.setMaximumSize(QSize(120, 30))
        self.bt_66.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_66.setIcon(icon17)
        self.bt_66.setIconSize(QSize(20, 20))
        self.bt_119 = QPushButton(self.frame_106)
        self.bt_119.setObjectName(u"bt_119")
        self.bt_119.setGeometry(QRect(20, 230, 91, 30))
        self.bt_119.setMaximumSize(QSize(120, 30))
        self.bt_119.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_119.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(158, 158, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(0, 170, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.bt_119.setIcon(icon21)
        self.bt_119.setIconSize(QSize(20, 20))

        self.horizontalLayout_40.addWidget(self.frame_106)


        self.horizontalLayout_39.addWidget(self.groupBox_21)

        self.groupBox_22 = QGroupBox(self.frame_104)
        self.groupBox_22.setObjectName(u"groupBox_22")
        self.groupBox_22.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QComboBox{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QDateEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 900 12pt \"Roboto Black\";\n"
"}")
        self.verticalLayout_85 = QVBoxLayout(self.groupBox_22)
        self.verticalLayout_85.setSpacing(0)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.verticalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.frame_107 = QFrame(self.groupBox_22)
        self.frame_107.setObjectName(u"frame_107")
        self.frame_107.setFrameShape(QFrame.StyledPanel)
        self.frame_107.setFrameShadow(QFrame.Raised)
        self.label_228 = QLabel(self.frame_107)
        self.label_228.setObjectName(u"label_228")
        self.label_228.setGeometry(QRect(40, 40, 51, 31))
        self.lineEdit_71 = QLineEdit(self.frame_107)
        self.lineEdit_71.setObjectName(u"lineEdit_71")
        self.lineEdit_71.setGeometry(QRect(130, 0, 171, 31))
        self.lineEdit_71.setClearButtonEnabled(True)
        self.label_229 = QLabel(self.frame_107)
        self.label_229.setObjectName(u"label_229")
        self.label_229.setGeometry(QRect(50, 190, 81, 31))
        self.lineEdit_72 = QLineEdit(self.frame_107)
        self.lineEdit_72.setObjectName(u"lineEdit_72")
        self.lineEdit_72.setGeometry(QRect(130, 140, 171, 31))
        self.lineEdit_72.setClearButtonEnabled(True)
        self.label_230 = QLabel(self.frame_107)
        self.label_230.setObjectName(u"label_230")
        self.label_230.setGeometry(QRect(20, 140, 111, 31))
        self.label_231 = QLabel(self.frame_107)
        self.label_231.setObjectName(u"label_231")
        self.label_231.setGeometry(QRect(30, 0, 101, 31))
        self.comboBox_36 = QComboBox(self.frame_107)
        self.comboBox_36.addItem("")
        self.comboBox_36.addItem("")
        self.comboBox_36.addItem("")
        self.comboBox_36.addItem("")
        self.comboBox_36.addItem("")
        self.comboBox_36.addItem("")
        self.comboBox_36.addItem("")
        self.comboBox_36.addItem("")
        self.comboBox_36.addItem("")
        self.comboBox_36.setObjectName(u"comboBox_36")
        self.comboBox_36.setGeometry(QRect(130, 40, 171, 31))
        self.lineEdit_93 = QLineEdit(self.frame_107)
        self.lineEdit_93.setObjectName(u"lineEdit_93")
        self.lineEdit_93.setGeometry(QRect(130, 190, 171, 31))
        self.lineEdit_93.setClearButtonEnabled(True)
        self.comboBox_47 = QComboBox(self.frame_107)
        self.comboBox_47.addItem("")
        self.comboBox_47.addItem("")
        self.comboBox_47.setObjectName(u"comboBox_47")
        self.comboBox_47.setGeometry(QRect(130, 90, 171, 31))
        self.label_127 = QLabel(self.frame_107)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setGeometry(QRect(10, 90, 111, 31))
        self.bt_116 = QPushButton(self.frame_107)
        self.bt_116.setObjectName(u"bt_116")
        self.bt_116.setGeometry(QRect(340, 200, 80, 30))
        self.bt_116.setMaximumSize(QSize(120, 30))
        self.bt_116.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_116.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(158, 158, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(0, 170, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.bt_116.setIcon(icon24)
        self.bt_116.setIconSize(QSize(20, 20))
        self.bt_120 = QPushButton(self.frame_107)
        self.bt_120.setObjectName(u"bt_120")
        self.bt_120.setGeometry(QRect(330, 90, 91, 30))
        self.bt_120.setMaximumSize(QSize(120, 30))
        self.bt_120.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_120.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(158, 158, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(0, 170, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.bt_120.setIcon(icon21)
        self.bt_120.setIconSize(QSize(20, 20))

        self.verticalLayout_85.addWidget(self.frame_107)

        self.frame_108 = QFrame(self.groupBox_22)
        self.frame_108.setObjectName(u"frame_108")
        self.frame_108.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(158, 158, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(255, 255, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_108.setFrameShape(QFrame.StyledPanel)
        self.frame_108.setFrameShadow(QFrame.Raised)
        self.bt_67 = QPushButton(self.frame_108)
        self.bt_67.setObjectName(u"bt_67")
        self.bt_67.setGeometry(QRect(80, 20, 80, 30))
        self.bt_67.setMaximumSize(QSize(120, 30))
        self.bt_67.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_67.setIcon(icon17)
        self.bt_67.setIconSize(QSize(20, 20))
        self.bt_68 = QPushButton(self.frame_108)
        self.bt_68.setObjectName(u"bt_68")
        self.bt_68.setGeometry(QRect(180, 20, 89, 30))
        self.bt_68.setMaximumSize(QSize(120, 30))
        self.bt_68.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_68.setIcon(icon22)
        self.bt_68.setIconSize(QSize(20, 20))
        self.bt_69 = QPushButton(self.frame_108)
        self.bt_69.setObjectName(u"bt_69")
        self.bt_69.setGeometry(QRect(280, 20, 80, 30))
        self.bt_69.setMaximumSize(QSize(120, 30))
        self.bt_69.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_69.setIcon(icon20)
        self.bt_69.setIconSize(QSize(20, 20))

        self.verticalLayout_85.addWidget(self.frame_108)

        self.verticalLayout_85.setStretch(0, 8)
        self.verticalLayout_85.setStretch(1, 2)

        self.horizontalLayout_39.addWidget(self.groupBox_22)


        self.verticalLayout_84.addWidget(self.frame_104)

        self.frame_109 = QFrame(self.frame_103)
        self.frame_109.setObjectName(u"frame_109")
        self.frame_109.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(158, 158, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(255, 255, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_109.setFrameShape(QFrame.StyledPanel)
        self.frame_109.setFrameShadow(QFrame.Raised)
        self.verticalLayout_86 = QVBoxLayout(self.frame_109)
        self.verticalLayout_86.setSpacing(0)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.verticalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.frame_110 = QFrame(self.frame_109)
        self.frame_110.setObjectName(u"frame_110")
        self.frame_110.setFrameShape(QFrame.StyledPanel)
        self.frame_110.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_110)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.frame_111 = QFrame(self.frame_110)
        self.frame_111.setObjectName(u"frame_111")
        self.frame_111.setFrameShape(QFrame.StyledPanel)
        self.frame_111.setFrameShadow(QFrame.Raised)
        self.verticalLayout_87 = QVBoxLayout(self.frame_111)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.tableWidget_11 = QTableWidget(self.frame_111)
        if (self.tableWidget_11.columnCount() < 6):
            self.tableWidget_11.setColumnCount(6)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(0, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(1, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(2, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(3, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(4, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(5, __qtablewidgetitem78)
        self.tableWidget_11.setObjectName(u"tableWidget_11")
        self.tableWidget_11.setStyleSheet(u"background-color: rgb(191, 191, 191);")

        self.verticalLayout_87.addWidget(self.tableWidget_11)


        self.horizontalLayout_41.addWidget(self.frame_111)

        self.frame_112 = QFrame(self.frame_110)
        self.frame_112.setObjectName(u"frame_112")
        self.frame_112.setFrameShape(QFrame.StyledPanel)
        self.frame_112.setFrameShadow(QFrame.Raised)
        self.verticalLayout_88 = QVBoxLayout(self.frame_112)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.tableWidget_12 = QTableWidget(self.frame_112)
        if (self.tableWidget_12.columnCount() < 5):
            self.tableWidget_12.setColumnCount(5)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(0, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(1, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(2, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(3, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(4, __qtablewidgetitem83)
        self.tableWidget_12.setObjectName(u"tableWidget_12")
        self.tableWidget_12.setStyleSheet(u"background-color: rgb(191, 191, 191);")

        self.verticalLayout_88.addWidget(self.tableWidget_12)


        self.horizontalLayout_41.addWidget(self.frame_112)


        self.verticalLayout_86.addWidget(self.frame_110)

        self.pushButton_2 = QPushButton(self.frame_109)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(120, 30))
        self.pushButton_2.setMaximumSize(QSize(120, 60))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setIcon(icon25)
        self.pushButton_2.setIconSize(QSize(20, 20))

        self.verticalLayout_86.addWidget(self.pushButton_2, 0, Qt.AlignHCenter)


        self.verticalLayout_84.addWidget(self.frame_109)

        self.verticalLayout_84.setStretch(0, 5)
        self.verticalLayout_84.setStretch(1, 5)

        self.verticalLayout_83.addWidget(self.frame_103)

        self.tabWidget_7.addTab(self.tab_27, "")
        self.tab_28 = QWidget()
        self.tab_28.setObjectName(u"tab_28")
        self.verticalLayout_89 = QVBoxLayout(self.tab_28)
        self.verticalLayout_89.setSpacing(0)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.verticalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.frame_113 = QFrame(self.tab_28)
        self.frame_113.setObjectName(u"frame_113")
        self.frame_113.setStyleSheet(u"\n"
"QPlainTextEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}")
        self.frame_113.setFrameShape(QFrame.StyledPanel)
        self.frame_113.setFrameShadow(QFrame.Raised)
        self.verticalLayout_90 = QVBoxLayout(self.frame_113)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.frame_114 = QFrame(self.frame_113)
        self.frame_114.setObjectName(u"frame_114")
        self.frame_114.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 900 12pt \"Roboto Black\";\n"
"}")
        self.frame_114.setFrameShape(QFrame.StyledPanel)
        self.frame_114.setFrameShadow(QFrame.Raised)
        self.lineEdit_73 = QLineEdit(self.frame_114)
        self.lineEdit_73.setObjectName(u"lineEdit_73")
        self.lineEdit_73.setGeometry(QRect(170, 10, 181, 31))
        self.label_232 = QLabel(self.frame_114)
        self.label_232.setObjectName(u"label_232")
        self.label_232.setGeometry(QRect(30, 20, 141, 16))
        self.label_233 = QLabel(self.frame_114)
        self.label_233.setObjectName(u"label_233")
        self.label_233.setGeometry(QRect(600, 20, 31, 16))
        self.lineEdit_74 = QLineEdit(self.frame_114)
        self.lineEdit_74.setObjectName(u"lineEdit_74")
        self.lineEdit_74.setGeometry(QRect(640, 10, 181, 31))

        self.verticalLayout_90.addWidget(self.frame_114)

        self.plainTextEdit_2 = QPlainTextEdit(self.frame_113)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")

        self.verticalLayout_90.addWidget(self.plainTextEdit_2)

        self.verticalLayout_90.setStretch(0, 1)
        self.verticalLayout_90.setStretch(1, 8)

        self.verticalLayout_89.addWidget(self.frame_113)

        self.frame_115 = QFrame(self.tab_28)
        self.frame_115.setObjectName(u"frame_115")
        self.frame_115.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 107, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(0, 170, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_115.setFrameShape(QFrame.StyledPanel)
        self.frame_115.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_115)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.frame_116 = QFrame(self.frame_115)
        self.frame_116.setObjectName(u"frame_116")
        self.frame_116.setMinimumSize(QSize(300, 100))
        self.frame_116.setMaximumSize(QSize(300, 100))
        self.frame_116.setFrameShape(QFrame.StyledPanel)
        self.frame_116.setFrameShadow(QFrame.Raised)
        self.verticalLayout_91 = QVBoxLayout(self.frame_116)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.bt_70 = QPushButton(self.frame_116)
        self.bt_70.setObjectName(u"bt_70")
        self.bt_70.setMinimumSize(QSize(120, 30))
        self.bt_70.setMaximumSize(QSize(120, 40))
        self.bt_70.setIcon(icon14)
        self.bt_70.setIconSize(QSize(20, 20))

        self.verticalLayout_91.addWidget(self.bt_70)


        self.horizontalLayout_42.addWidget(self.frame_116, 0, Qt.AlignHCenter)


        self.verticalLayout_89.addWidget(self.frame_115)

        self.verticalLayout_89.setStretch(0, 8)
        self.verticalLayout_89.setStretch(1, 2)
        self.tabWidget_7.addTab(self.tab_28, "")
        self.tab_54 = QWidget()
        self.tab_54.setObjectName(u"tab_54")
        self.verticalLayout_158 = QVBoxLayout(self.tab_54)
        self.verticalLayout_158.setObjectName(u"verticalLayout_158")
        self.frame_200 = QFrame(self.tab_54)
        self.frame_200.setObjectName(u"frame_200")
        self.frame_200.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 900 12pt \"Roboto Black\";\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(158, 158, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(170, 170, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_200.setFrameShape(QFrame.StyledPanel)
        self.frame_200.setFrameShadow(QFrame.Raised)
        self.lineEdit_27 = QLineEdit(self.frame_200)
        self.lineEdit_27.setObjectName(u"lineEdit_27")
        self.lineEdit_27.setGeometry(QRect(220, 260, 181, 51))
        self.label_98 = QLabel(self.frame_200)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setGeometry(QRect(100, 280, 111, 20))
        self.label_99 = QLabel(self.frame_200)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setGeometry(QRect(130, 350, 91, 20))
        self.lineEdit_29 = QLineEdit(self.frame_200)
        self.lineEdit_29.setObjectName(u"lineEdit_29")
        self.lineEdit_29.setGeometry(QRect(220, 330, 181, 51))
        self.comboBox_49 = QComboBox(self.frame_200)
        self.comboBox_49.addItem("")
        self.comboBox_49.addItem("")
        self.comboBox_49.addItem("")
        self.comboBox_49.setObjectName(u"comboBox_49")
        self.comboBox_49.setGeometry(QRect(230, 190, 171, 41))
        self.comboBox_49.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_100 = QLabel(self.frame_200)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setGeometry(QRect(100, 200, 121, 20))
        self.line_42 = QFrame(self.frame_200)
        self.line_42.setObjectName(u"line_42")
        self.line_42.setGeometry(QRect(450, 0, 20, 661))
        self.line_42.setFrameShape(QFrame.VLine)
        self.line_42.setFrameShadow(QFrame.Sunken)
        self.label_101 = QLabel(self.frame_200)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setGeometry(QRect(490, 40, 121, 31))
        self.label_102 = QLabel(self.frame_200)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setGeometry(QRect(640, 40, 211, 31))
        self.label_102.setStyleSheet(u"color: rgb(135, 68, 0);\n"
"background-color: rgb(185, 185, 185);\n"
"font: 900 12pt \"Roboto\";")
        self.label_102.setAlignment(Qt.AlignCenter)
        self.label_103 = QLabel(self.frame_200)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setGeometry(QRect(640, 80, 211, 31))
        self.label_103.setStyleSheet(u"color: rgb(135, 68, 0);\n"
"background-color: rgb(185, 185, 185);\n"
"font: 900 12pt \"Roboto\";")
        self.label_103.setAlignment(Qt.AlignCenter)
        self.label_104 = QLabel(self.frame_200)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setGeometry(QRect(490, 80, 121, 31))
        self.line_43 = QFrame(self.frame_200)
        self.line_43.setObjectName(u"line_43")
        self.line_43.setGeometry(QRect(457, 133, 411, 20))
        self.line_43.setFrameShape(QFrame.HLine)
        self.line_43.setFrameShadow(QFrame.Sunken)
        self.line_44 = QFrame(self.frame_200)
        self.line_44.setObjectName(u"line_44")
        self.line_44.setGeometry(QRect(680, 300, 21, 171))
        self.line_44.setFrameShape(QFrame.VLine)
        self.line_44.setFrameShadow(QFrame.Sunken)
        self.line_45 = QFrame(self.frame_200)
        self.line_45.setObjectName(u"line_45")
        self.line_45.setGeometry(QRect(457, 470, 401, 20))
        self.line_45.setFrameShape(QFrame.HLine)
        self.line_45.setFrameShadow(QFrame.Sunken)
        self.line_46 = QFrame(self.frame_200)
        self.line_46.setObjectName(u"line_46")
        self.line_46.setGeometry(QRect(553, 490, 20, 171))
        self.line_46.setFrameShape(QFrame.VLine)
        self.line_46.setFrameShadow(QFrame.Sunken)
        self.line_47 = QFrame(self.frame_200)
        self.line_47.setObjectName(u"line_47")
        self.line_47.setGeometry(QRect(560, 616, 301, 16))
        self.line_47.setFrameShape(QFrame.HLine)
        self.line_47.setFrameShadow(QFrame.Sunken)
        self.label_105 = QLabel(self.frame_200)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setGeometry(QRect(490, 290, 161, 31))
        self.label_106 = QLabel(self.frame_200)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setGeometry(QRect(490, 340, 161, 31))
        self.label_107 = QLabel(self.frame_200)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setGeometry(QRect(490, 390, 161, 31))
        self.label_108 = QLabel(self.frame_200)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setGeometry(QRect(490, 430, 161, 31))
        self.label_109 = QLabel(self.frame_200)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setGeometry(QRect(490, 580, 51, 31))
        self.label_110 = QLabel(self.frame_200)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setGeometry(QRect(580, 630, 91, 31))
        self.label_137 = QLabel(self.frame_200)
        self.label_137.setObjectName(u"label_137")
        self.label_137.setGeometry(QRect(570, 540, 111, 31))
        self.label_158 = QLabel(self.frame_200)
        self.label_158.setObjectName(u"label_158")
        self.label_158.setGeometry(QRect(570, 590, 101, 31))
        self.label_159 = QLabel(self.frame_200)
        self.label_159.setObjectName(u"label_159")
        self.label_159.setGeometry(QRect(570, 490, 101, 31))
        self.label_160 = QLabel(self.frame_200)
        self.label_160.setObjectName(u"label_160")
        self.label_160.setGeometry(QRect(720, 290, 161, 31))
        self.label_160.setStyleSheet(u"color: rgb(229, 153, 0);")
        self.label_160.setAlignment(Qt.AlignCenter)
        self.label_161 = QLabel(self.frame_200)
        self.label_161.setObjectName(u"label_161")
        self.label_161.setGeometry(QRect(720, 340, 161, 31))
        self.label_161.setStyleSheet(u"color: rgb(229, 153, 0);")
        self.label_161.setAlignment(Qt.AlignCenter)
        self.label_162 = QLabel(self.frame_200)
        self.label_162.setObjectName(u"label_162")
        self.label_162.setGeometry(QRect(720, 390, 161, 31))
        self.label_162.setStyleSheet(u"color: rgb(229, 153, 0);")
        self.label_162.setAlignment(Qt.AlignCenter)
        self.label_163 = QLabel(self.frame_200)
        self.label_163.setObjectName(u"label_163")
        self.label_163.setGeometry(QRect(700, 440, 201, 31))
        self.label_163.setStyleSheet(u"color: rgb(166, 166, 166);\n"
"background-color: rgb(170, 0, 0);\n"
"font: 900 12pt \"Roboto\";")
        self.label_163.setAlignment(Qt.AlignCenter)
        self.label_164 = QLabel(self.frame_200)
        self.label_164.setObjectName(u"label_164")
        self.label_164.setGeometry(QRect(690, 490, 211, 31))
        self.label_164.setStyleSheet(u"color: rgb(0, 170, 0);\n"
"font: 900 12pt \"Roboto\";")
        self.label_164.setAlignment(Qt.AlignCenter)
        self.label_165 = QLabel(self.frame_200)
        self.label_165.setObjectName(u"label_165")
        self.label_165.setGeometry(QRect(690, 540, 211, 31))
        self.label_165.setStyleSheet(u"color: rgb(0, 170, 0);\n"
"font: 900 12pt \"Roboto\";")
        self.label_165.setAlignment(Qt.AlignCenter)
        self.label_166 = QLabel(self.frame_200)
        self.label_166.setObjectName(u"label_166")
        self.label_166.setGeometry(QRect(690, 590, 211, 31))
        self.label_166.setStyleSheet(u"color: rgb(0, 170, 0);\n"
"font: 900 12pt \"Roboto\";")
        self.label_166.setAlignment(Qt.AlignCenter)
        self.label_167 = QLabel(self.frame_200)
        self.label_167.setObjectName(u"label_167")
        self.label_167.setGeometry(QRect(680, 630, 211, 31))
        self.label_167.setStyleSheet(u"background-color: rgb(156, 78, 0);\n"
"color: rgb(188, 188, 188);\n"
"font: 900 12pt \"Roboto\";")
        self.label_167.setAlignment(Qt.AlignCenter)
        self.line_48 = QFrame(self.frame_200)
        self.line_48.setObjectName(u"line_48")
        self.line_48.setGeometry(QRect(460, 420, 441, 16))
        self.line_48.setFrameShape(QFrame.HLine)
        self.line_48.setFrameShadow(QFrame.Sunken)
        self.line_72 = QFrame(self.frame_200)
        self.line_72.setObjectName(u"line_72")
        self.line_72.setGeometry(QRect(460, 370, 441, 16))
        self.line_72.setFrameShape(QFrame.HLine)
        self.line_72.setFrameShadow(QFrame.Sunken)
        self.line_73 = QFrame(self.frame_200)
        self.line_73.setObjectName(u"line_73")
        self.line_73.setGeometry(QRect(460, 320, 441, 16))
        self.line_73.setFrameShape(QFrame.HLine)
        self.line_73.setFrameShadow(QFrame.Sunken)
        self.label_168 = QLabel(self.frame_200)
        self.label_168.setObjectName(u"label_168")
        self.label_168.setGeometry(QRect(110, 20, 201, 61))
        self.label_168.setAlignment(Qt.AlignCenter)
        self.pushButton_23 = QPushButton(self.frame_200)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setGeometry(QRect(30, 470, 191, 61))
        self.pushButton_23.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_24 = QPushButton(self.frame_200)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setGeometry(QRect(250, 470, 191, 61))
        self.pushButton_24.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_25 = QPushButton(self.frame_200)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setGeometry(QRect(160, 560, 191, 61))
        self.pushButton_25.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_158.addWidget(self.frame_200)

        self.tabWidget_7.addTab(self.tab_54, "")

        self.verticalLayout_54.addWidget(self.tabWidget_7)


        self.horizontalLayout_23.addWidget(self.frame_69)

        self.horizontalLayout_23.setStretch(0, 2)
        self.horizontalLayout_23.setStretch(1, 8)

        self.horizontalLayout_22.addWidget(self.frame_66)

        self.tabWidget_6.addTab(self.tab_18, "")

        self.verticalLayout_48.addWidget(self.tabWidget_6)


        self.verticalLayout_92.addWidget(self.frame_63)

        self.tabWidget.addTab(self.tab_16, "")
        self.tab_29 = QWidget()
        self.tab_29.setObjectName(u"tab_29")
        self.verticalLayout_133 = QVBoxLayout(self.tab_29)
        self.verticalLayout_133.setSpacing(0)
        self.verticalLayout_133.setObjectName(u"verticalLayout_133")
        self.verticalLayout_133.setContentsMargins(0, 0, 0, 0)
        self.frame_117 = QFrame(self.tab_29)
        self.frame_117.setObjectName(u"frame_117")
        self.frame_117.setFrameShape(QFrame.StyledPanel)
        self.frame_117.setFrameShadow(QFrame.Raised)
        self.verticalLayout_93 = QVBoxLayout(self.frame_117)
        self.verticalLayout_93.setSpacing(0)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.verticalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_9 = QTabWidget(self.frame_117)
        self.tabWidget_9.setObjectName(u"tabWidget_9")
        self.tabWidget_9.setStyleSheet(u"background-color: rgb(108, 170, 144);")
        self.tab_30 = QWidget()
        self.tab_30.setObjectName(u"tab_30")
        self.verticalLayout_94 = QVBoxLayout(self.tab_30)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.frame_118 = QFrame(self.tab_30)
        self.frame_118.setObjectName(u"frame_118")
        self.frame_118.setFrameShape(QFrame.StyledPanel)
        self.frame_118.setFrameShadow(QFrame.Raised)
        self.verticalLayout_95 = QVBoxLayout(self.frame_118)
        self.verticalLayout_95.setSpacing(0)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.verticalLayout_95.setContentsMargins(0, 0, 0, 0)
        self.label_298 = QLabel(self.frame_118)
        self.label_298.setObjectName(u"label_298")
        self.label_298.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 20pt \"Poppins Black\";")
        self.label_298.setAlignment(Qt.AlignCenter)

        self.verticalLayout_95.addWidget(self.label_298)

        self.label_299 = QLabel(self.frame_118)
        self.label_299.setObjectName(u"label_299")
        self.label_299.setPixmap(QPixmap(u"assets/imgs/cover.jpg"))
        self.label_299.setScaledContents(True)

        self.verticalLayout_95.addWidget(self.label_299)


        self.verticalLayout_94.addWidget(self.frame_118)

        self.frame_119 = QFrame(self.tab_30)
        self.frame_119.setObjectName(u"frame_119")
        self.frame_119.setStyleSheet(u"QPushButton {\n"
"	border-top-left-radius: 15px;\n"
"	background-color: rgb(213, 156, 53);\n"
"	font: 700 11pt \"Segoe UI\";\n"
"	color: rgb(48, 48, 48);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffd495, stop: 0.7 #ffad76, stop: 1.0 #ffb665);\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_119.setFrameShape(QFrame.NoFrame)
        self.frame_119.setFrameShadow(QFrame.Raised)
        self.verticalLayout_96 = QVBoxLayout(self.frame_119)
        self.verticalLayout_96.setSpacing(0)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.verticalLayout_96.setContentsMargins(0, 0, 0, 0)
        self.bt_71 = QPushButton(self.frame_119)
        self.bt_71.setObjectName(u"bt_71")
        self.bt_71.setMinimumSize(QSize(120, 30))
        self.bt_71.setMaximumSize(QSize(120, 120))
        self.bt_71.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_71.setIcon(icon7)
        self.bt_71.setIconSize(QSize(30, 30))

        self.verticalLayout_96.addWidget(self.bt_71, 0, Qt.AlignHCenter)


        self.verticalLayout_94.addWidget(self.frame_119)

        self.verticalLayout_94.setStretch(0, 8)
        self.verticalLayout_94.setStretch(1, 2)
        self.tabWidget_9.addTab(self.tab_30, "")
        self.tab_31 = QWidget()
        self.tab_31.setObjectName(u"tab_31")
        self.horizontalLayout_43 = QHBoxLayout(self.tab_31)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.frame_120 = QFrame(self.tab_31)
        self.frame_120.setObjectName(u"frame_120")
        self.frame_120.setFrameShape(QFrame.StyledPanel)
        self.frame_120.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_120)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.frame_121 = QFrame(self.frame_120)
        self.frame_121.setObjectName(u"frame_121")
        self.frame_121.setFrameShape(QFrame.StyledPanel)
        self.frame_121.setFrameShadow(QFrame.Raised)
        self.verticalLayout_97 = QVBoxLayout(self.frame_121)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.verticalLayout_97.setContentsMargins(0, 0, 0, 0)
        self.frame_122 = QFrame(self.frame_121)
        self.frame_122.setObjectName(u"frame_122")
        self.frame_122.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(163, 82, 0);\n"
"}\n"
"QPushButton {\n"
"border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_122.setFrameShape(QFrame.StyledPanel)
        self.frame_122.setFrameShadow(QFrame.Raised)
        self.verticalLayout_98 = QVBoxLayout(self.frame_122)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.frame_195 = QFrame(self.frame_122)
        self.frame_195.setObjectName(u"frame_195")
        self.frame_195.setMaximumSize(QSize(200, 195))
        self.frame_195.setFrameShape(QFrame.StyledPanel)
        self.frame_195.setFrameShadow(QFrame.Raised)
        self.verticalLayout_156 = QVBoxLayout(self.frame_195)
        self.verticalLayout_156.setSpacing(0)
        self.verticalLayout_156.setObjectName(u"verticalLayout_156")
        self.verticalLayout_156.setContentsMargins(0, 0, 0, 0)
        self.frame_197 = QFrame(self.frame_195)
        self.frame_197.setObjectName(u"frame_197")
        self.frame_197.setFrameShape(QFrame.StyledPanel)
        self.frame_197.setFrameShadow(QFrame.Raised)
        self.label_67 = QLabel(self.frame_197)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setGeometry(QRect(-2, 0, 191, 20))
        self.label_67.setFont(font)
        self.label_68 = QLabel(self.frame_197)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setGeometry(QRect(0, 10, 191, 51))
        self.label_68.setStyleSheet(u"color: rgb(255, 62, 23);\n"
"background-color:transparent;\n"
"font: 900 14pt \"Poppins Black\";")
        self.label_68.setAlignment(Qt.AlignCenter)

        self.verticalLayout_156.addWidget(self.frame_197)

        self.frame_198 = QFrame(self.frame_195)
        self.frame_198.setObjectName(u"frame_198")
        self.frame_198.setFrameShape(QFrame.StyledPanel)
        self.frame_198.setFrameShadow(QFrame.Raised)
        self.label_69 = QLabel(self.frame_198)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setGeometry(QRect(0, 0, 191, 20))
        self.label_69.setFont(font)
        self.label_70 = QLabel(self.frame_198)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setGeometry(QRect(0, 10, 191, 51))
        self.label_70.setStyleSheet(u"color: rgb(255, 62, 23);\n"
"background-color:transparent;\n"
"font: 900 14pt \"Poppins Black\";")
        self.label_70.setAlignment(Qt.AlignCenter)

        self.verticalLayout_156.addWidget(self.frame_198)

        self.frame_196 = QFrame(self.frame_195)
        self.frame_196.setObjectName(u"frame_196")
        self.frame_196.setFrameShape(QFrame.StyledPanel)
        self.frame_196.setFrameShadow(QFrame.Raised)
        self.label_71 = QLabel(self.frame_196)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setGeometry(QRect(0, 0, 191, 20))
        self.label_71.setFont(font)
        self.label_72 = QLabel(self.frame_196)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setGeometry(QRect(0, 10, 191, 61))
        self.label_72.setStyleSheet(u"color: rgb(255, 62, 23);\n"
"background-color:transparent;\n"
"font: 900 14pt \"Poppins Black\";")
        self.label_72.setAlignment(Qt.AlignCenter)

        self.verticalLayout_156.addWidget(self.frame_196)


        self.verticalLayout_98.addWidget(self.frame_195)

        self.bt_72 = QPushButton(self.frame_122)
        self.bt_72.setObjectName(u"bt_72")
        self.bt_72.setMaximumSize(QSize(200, 40))
        self.bt_72.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_72.setIcon(icon8)
        self.bt_72.setIconSize(QSize(28, 30))

        self.verticalLayout_98.addWidget(self.bt_72)

        self.line_35 = QFrame(self.frame_122)
        self.line_35.setObjectName(u"line_35")
        self.line_35.setFrameShape(QFrame.HLine)
        self.line_35.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_98.addWidget(self.line_35)

        self.bt_73 = QPushButton(self.frame_122)
        self.bt_73.setObjectName(u"bt_73")
        self.bt_73.setMaximumSize(QSize(200, 40))
        self.bt_73.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_73.setStyleSheet(u"padding-right: 20px;")
        self.bt_73.setIcon(icon9)
        self.bt_73.setIconSize(QSize(28, 30))

        self.verticalLayout_98.addWidget(self.bt_73)

        self.line_62 = QFrame(self.frame_122)
        self.line_62.setObjectName(u"line_62")
        self.line_62.setFrameShape(QFrame.HLine)
        self.line_62.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_98.addWidget(self.line_62)

        self.bt_74 = QPushButton(self.frame_122)
        self.bt_74.setObjectName(u"bt_74")
        self.bt_74.setMaximumSize(QSize(200, 40))
        self.bt_74.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_74.setStyleSheet(u"padding-right: 30px;")
        self.bt_74.setIcon(icon10)
        self.bt_74.setIconSize(QSize(28, 30))

        self.verticalLayout_98.addWidget(self.bt_74)

        self.line_63 = QFrame(self.frame_122)
        self.line_63.setObjectName(u"line_63")
        self.line_63.setFrameShape(QFrame.HLine)
        self.line_63.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_98.addWidget(self.line_63)

        self.bt_75 = QPushButton(self.frame_122)
        self.bt_75.setObjectName(u"bt_75")
        self.bt_75.setMaximumSize(QSize(200, 40))
        self.bt_75.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_75.setStyleSheet(u"padding-right: 58px;")
        self.bt_75.setIcon(icon11)
        self.bt_75.setIconSize(QSize(28, 30))

        self.verticalLayout_98.addWidget(self.bt_75)

        self.line_64 = QFrame(self.frame_122)
        self.line_64.setObjectName(u"line_64")
        self.line_64.setFrameShape(QFrame.HLine)
        self.line_64.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_98.addWidget(self.line_64)

        self.bt_76 = QPushButton(self.frame_122)
        self.bt_76.setObjectName(u"bt_76")
        self.bt_76.setMaximumSize(QSize(200, 40))
        self.bt_76.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_76.setStyleSheet(u"padding-right: 20px;")
        self.bt_76.setIcon(icon12)
        self.bt_76.setIconSize(QSize(28, 30))

        self.verticalLayout_98.addWidget(self.bt_76)

        self.line_65 = QFrame(self.frame_122)
        self.line_65.setObjectName(u"line_65")
        self.line_65.setFrameShape(QFrame.HLine)
        self.line_65.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_98.addWidget(self.line_65)

        self.bt_77 = QPushButton(self.frame_122)
        self.bt_77.setObjectName(u"bt_77")
        self.bt_77.setMaximumSize(QSize(200, 40))
        self.bt_77.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_77.setStyleSheet(u"padding-right:49px;")
        self.bt_77.setIcon(icon13)
        self.bt_77.setIconSize(QSize(28, 30))

        self.verticalLayout_98.addWidget(self.bt_77)

        self.line_66 = QFrame(self.frame_122)
        self.line_66.setObjectName(u"line_66")
        self.line_66.setFrameShape(QFrame.HLine)
        self.line_66.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_98.addWidget(self.line_66)

        self.bt_78 = QPushButton(self.frame_122)
        self.bt_78.setObjectName(u"bt_78")
        self.bt_78.setMaximumSize(QSize(200, 40))
        self.bt_78.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_78.setStyleSheet(u"padding-right: 69px;")
        self.bt_78.setIcon(icon14)
        self.bt_78.setIconSize(QSize(28, 30))

        self.verticalLayout_98.addWidget(self.bt_78)

        self.line_38 = QFrame(self.frame_122)
        self.line_38.setObjectName(u"line_38")
        self.line_38.setFrameShape(QFrame.HLine)
        self.line_38.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_98.addWidget(self.line_38)

        self.pushButton_19 = QPushButton(self.frame_122)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_19.setStyleSheet(u"padding-right: 80px;")
        self.pushButton_19.setIcon(icon15)
        self.pushButton_19.setIconSize(QSize(28, 30))

        self.verticalLayout_98.addWidget(self.pushButton_19)

        self.line_37 = QFrame(self.frame_122)
        self.line_37.setObjectName(u"line_37")
        self.line_37.setFrameShape(QFrame.HLine)
        self.line_37.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_98.addWidget(self.line_37)

        self.pushButton_14 = QPushButton(self.frame_122)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMaximumSize(QSize(200, 40))
        self.pushButton_14.setCursor(QCursor(Qt.OpenHandCursor))
        self.pushButton_14.setStyleSheet(u"padding-right: 120px;")
        self.pushButton_14.setIcon(icon16)
        self.pushButton_14.setIconSize(QSize(28, 28))

        self.verticalLayout_98.addWidget(self.pushButton_14)

        self.line_67 = QFrame(self.frame_122)
        self.line_67.setObjectName(u"line_67")
        self.line_67.setFrameShape(QFrame.HLine)
        self.line_67.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_98.addWidget(self.line_67)


        self.verticalLayout_97.addWidget(self.frame_122)


        self.horizontalLayout_44.addWidget(self.frame_121)

        self.frame_123 = QFrame(self.frame_120)
        self.frame_123.setObjectName(u"frame_123")
        self.frame_123.setFrameShape(QFrame.StyledPanel)
        self.frame_123.setFrameShadow(QFrame.Raised)
        self.verticalLayout_99 = QVBoxLayout(self.frame_123)
        self.verticalLayout_99.setSpacing(0)
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
        self.verticalLayout_99.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_10 = QTabWidget(self.frame_123)
        self.tabWidget_10.setObjectName(u"tabWidget_10")
        self.tab_32 = QWidget()
        self.tab_32.setObjectName(u"tab_32")
        self.horizontalLayout_45 = QHBoxLayout(self.tab_32)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.frame_124 = QFrame(self.tab_32)
        self.frame_124.setObjectName(u"frame_124")
        self.frame_124.setFrameShape(QFrame.StyledPanel)
        self.frame_124.setFrameShadow(QFrame.Raised)
        self.verticalLayout_100 = QVBoxLayout(self.frame_124)
        self.verticalLayout_100.setObjectName(u"verticalLayout_100")
        self.groupBox_23 = QGroupBox(self.frame_124)
        self.groupBox_23.setObjectName(u"groupBox_23")
        self.groupBox_23.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QComboBox{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QDateEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 900 12pt \"Roboto Black\";\n"
"}")
        self.label_300 = QLabel(self.groupBox_23)
        self.label_300.setObjectName(u"label_300")
        self.label_300.setGeometry(QRect(20, 30, 161, 31))
        self.lineEdit_75 = QLineEdit(self.groupBox_23)
        self.lineEdit_75.setObjectName(u"lineEdit_75")
        self.lineEdit_75.setGeometry(QRect(190, 30, 171, 31))
        self.label_303 = QLabel(self.groupBox_23)
        self.label_303.setObjectName(u"label_303")
        self.label_303.setGeometry(QRect(20, 150, 111, 31))
        self.label_304 = QLabel(self.groupBox_23)
        self.label_304.setObjectName(u"label_304")
        self.label_304.setGeometry(QRect(20, 190, 101, 31))
        self.comboBox_37 = QComboBox(self.groupBox_23)
        self.comboBox_37.addItem("")
        self.comboBox_37.addItem("")
        self.comboBox_37.addItem("")
        self.comboBox_37.addItem("")
        self.comboBox_37.addItem("")
        self.comboBox_37.addItem("")
        self.comboBox_37.addItem("")
        self.comboBox_37.addItem("")
        self.comboBox_37.addItem("")
        self.comboBox_37.addItem("")
        self.comboBox_37.addItem("")
        self.comboBox_37.addItem("")
        self.comboBox_37.addItem("")
        self.comboBox_37.addItem("")
        self.comboBox_37.setObjectName(u"comboBox_37")
        self.comboBox_37.setGeometry(QRect(130, 190, 171, 31))
        self.comboBox_38 = QComboBox(self.groupBox_23)
        self.comboBox_38.addItem("")
        self.comboBox_38.addItem("")
        self.comboBox_38.setObjectName(u"comboBox_38")
        self.comboBox_38.setGeometry(QRect(130, 230, 171, 31))
        self.label_305 = QLabel(self.groupBox_23)
        self.label_305.setObjectName(u"label_305")
        self.label_305.setGeometry(QRect(20, 230, 101, 31))
        self.label_306 = QLabel(self.groupBox_23)
        self.label_306.setObjectName(u"label_306")
        self.label_306.setGeometry(QRect(20, 280, 121, 31))
        self.textEdit_5 = QTextEdit(self.groupBox_23)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setGeometry(QRect(143, 270, 141, 71))
        self.lineEdit_95 = QLineEdit(self.groupBox_23)
        self.lineEdit_95.setObjectName(u"lineEdit_95")
        self.lineEdit_95.setGeometry(QRect(130, 150, 171, 31))
        self.lineEdit_95.setClearButtonEnabled(True)
        self.lineEdit_24 = QLineEdit(self.groupBox_23)
        self.lineEdit_24.setObjectName(u"lineEdit_24")
        self.lineEdit_24.setGeometry(QRect(130, 110, 171, 31))
        self.lineEdit_24.setClearButtonEnabled(True)
        self.label_51 = QLabel(self.groupBox_23)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(30, 110, 91, 31))

        self.verticalLayout_100.addWidget(self.groupBox_23)

        self.groupBox_24 = QGroupBox(self.frame_124)
        self.groupBox_24.setObjectName(u"groupBox_24")
        self.groupBox_24.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QComboBox{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QDateEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 900 12pt \"Roboto Black\";\n"
"}")
        self.label_307 = QLabel(self.groupBox_24)
        self.label_307.setObjectName(u"label_307")
        self.label_307.setGeometry(QRect(20, 80, 131, 31))
        self.lineEdit_78 = QLineEdit(self.groupBox_24)
        self.lineEdit_78.setObjectName(u"lineEdit_78")
        self.lineEdit_78.setGeometry(QRect(170, 40, 191, 31))
        self.lineEdit_78.setClearButtonEnabled(True)
        self.label_308 = QLabel(self.groupBox_24)
        self.label_308.setObjectName(u"label_308")
        self.label_308.setGeometry(QRect(20, 40, 141, 31))
        self.lineEdit_79 = QLineEdit(self.groupBox_24)
        self.lineEdit_79.setObjectName(u"lineEdit_79")
        self.lineEdit_79.setGeometry(QRect(170, 80, 191, 31))
        self.lineEdit_79.setClearButtonEnabled(True)
        self.label_309 = QLabel(self.groupBox_24)
        self.label_309.setObjectName(u"label_309")
        self.label_309.setGeometry(QRect(20, 120, 131, 31))
        self.lineEdit_80 = QLineEdit(self.groupBox_24)
        self.lineEdit_80.setObjectName(u"lineEdit_80")
        self.lineEdit_80.setGeometry(QRect(170, 120, 191, 31))
        self.lineEdit_80.setClearButtonEnabled(True)

        self.verticalLayout_100.addWidget(self.groupBox_24)

        self.frame_125 = QFrame(self.frame_124)
        self.frame_125.setObjectName(u"frame_125")
        self.frame_125.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(158, 158, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(255, 255, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_125.setFrameShape(QFrame.StyledPanel)
        self.frame_125.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_125)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.frame_126 = QFrame(self.frame_125)
        self.frame_126.setObjectName(u"frame_126")
        self.frame_126.setFrameShape(QFrame.StyledPanel)
        self.frame_126.setFrameShadow(QFrame.Raised)
        self.verticalLayout_101 = QVBoxLayout(self.frame_126)
        self.verticalLayout_101.setObjectName(u"verticalLayout_101")
        self.bt_79 = QPushButton(self.frame_126)
        self.bt_79.setObjectName(u"bt_79")
        self.bt_79.setMinimumSize(QSize(0, 40))
        self.bt_79.setMaximumSize(QSize(120, 60))
        self.bt_79.setIcon(icon17)
        self.bt_79.setIconSize(QSize(20, 20))

        self.verticalLayout_101.addWidget(self.bt_79)


        self.horizontalLayout_46.addWidget(self.frame_126)

        self.frame_127 = QFrame(self.frame_125)
        self.frame_127.setObjectName(u"frame_127")
        self.frame_127.setFrameShape(QFrame.StyledPanel)
        self.frame_127.setFrameShadow(QFrame.Raised)
        self.verticalLayout_102 = QVBoxLayout(self.frame_127)
        self.verticalLayout_102.setObjectName(u"verticalLayout_102")
        self.bt_80 = QPushButton(self.frame_127)
        self.bt_80.setObjectName(u"bt_80")
        self.bt_80.setMinimumSize(QSize(0, 40))
        self.bt_80.setMaximumSize(QSize(120, 60))
        self.bt_80.setIcon(icon18)
        self.bt_80.setIconSize(QSize(20, 20))

        self.verticalLayout_102.addWidget(self.bt_80)


        self.horizontalLayout_46.addWidget(self.frame_127)


        self.verticalLayout_100.addWidget(self.frame_125)

        self.verticalLayout_100.setStretch(0, 6)
        self.verticalLayout_100.setStretch(1, 3)
        self.verticalLayout_100.setStretch(2, 1)

        self.horizontalLayout_45.addWidget(self.frame_124)

        self.frame_128 = QFrame(self.tab_32)
        self.frame_128.setObjectName(u"frame_128")
        self.frame_128.setFrameShape(QFrame.StyledPanel)
        self.frame_128.setFrameShadow(QFrame.Raised)
        self.verticalLayout_103 = QVBoxLayout(self.frame_128)
        self.verticalLayout_103.setObjectName(u"verticalLayout_103")
        self.tableWidget_13 = QTableWidget(self.frame_128)
        if (self.tableWidget_13.columnCount() < 9):
            self.tableWidget_13.setColumnCount(9)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(0, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(1, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(2, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(3, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(4, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(5, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(6, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(7, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(8, __qtablewidgetitem92)
        self.tableWidget_13.setObjectName(u"tableWidget_13")
        self.tableWidget_13.setStyleSheet(u"background-color: rgb(191, 191, 191);")

        self.verticalLayout_103.addWidget(self.tableWidget_13)


        self.horizontalLayout_45.addWidget(self.frame_128)

        self.horizontalLayout_45.setStretch(0, 5)
        self.horizontalLayout_45.setStretch(1, 4)
        self.tabWidget_10.addTab(self.tab_32, "")
        self.tab_33 = QWidget()
        self.tab_33.setObjectName(u"tab_33")
        self.horizontalLayout_47 = QHBoxLayout(self.tab_33)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.frame_129 = QFrame(self.tab_33)
        self.frame_129.setObjectName(u"frame_129")
        self.frame_129.setFrameShape(QFrame.StyledPanel)
        self.frame_129.setFrameShadow(QFrame.Raised)
        self.verticalLayout_104 = QVBoxLayout(self.frame_129)
        self.verticalLayout_104.setObjectName(u"verticalLayout_104")
        self.groupBox_25 = QGroupBox(self.frame_129)
        self.groupBox_25.setObjectName(u"groupBox_25")
        self.groupBox_25.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QComboBox{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QDateEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 900 12pt \"Roboto Black\";\n"
"}")
        self.label_310 = QLabel(self.groupBox_25)
        self.label_310.setObjectName(u"label_310")
        self.label_310.setGeometry(QRect(20, 30, 161, 31))
        self.lineEdit_81 = QLineEdit(self.groupBox_25)
        self.lineEdit_81.setObjectName(u"lineEdit_81")
        self.lineEdit_81.setGeometry(QRect(190, 30, 171, 31))
        self.lineEdit_81.setFrame(True)
        self.lineEdit_81.setClearButtonEnabled(True)
        self.label_313 = QLabel(self.groupBox_25)
        self.label_313.setObjectName(u"label_313")
        self.label_313.setGeometry(QRect(20, 150, 111, 31))
        self.label_314 = QLabel(self.groupBox_25)
        self.label_314.setObjectName(u"label_314")
        self.label_314.setGeometry(QRect(20, 190, 101, 31))
        self.comboBox_39 = QComboBox(self.groupBox_25)
        self.comboBox_39.addItem("")
        self.comboBox_39.addItem("")
        self.comboBox_39.setObjectName(u"comboBox_39")
        self.comboBox_39.setGeometry(QRect(130, 230, 171, 31))
        self.label_315 = QLabel(self.groupBox_25)
        self.label_315.setObjectName(u"label_315")
        self.label_315.setGeometry(QRect(20, 230, 101, 31))
        self.label_316 = QLabel(self.groupBox_25)
        self.label_316.setObjectName(u"label_316")
        self.label_316.setGeometry(QRect(20, 280, 121, 31))
        self.textEdit_6 = QTextEdit(self.groupBox_25)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setGeometry(QRect(143, 270, 141, 71))
        self.comboBox_40 = QComboBox(self.groupBox_25)
        self.comboBox_40.addItem("")
        self.comboBox_40.addItem("")
        self.comboBox_40.addItem("")
        self.comboBox_40.addItem("")
        self.comboBox_40.addItem("")
        self.comboBox_40.addItem("")
        self.comboBox_40.addItem("")
        self.comboBox_40.addItem("")
        self.comboBox_40.addItem("")
        self.comboBox_40.setObjectName(u"comboBox_40")
        self.comboBox_40.setGeometry(QRect(130, 190, 171, 31))
        self.lineEdit_96 = QLineEdit(self.groupBox_25)
        self.lineEdit_96.setObjectName(u"lineEdit_96")
        self.lineEdit_96.setGeometry(QRect(130, 150, 171, 31))
        self.lineEdit_96.setClearButtonEnabled(True)
        self.lineEdit_25 = QLineEdit(self.groupBox_25)
        self.lineEdit_25.setObjectName(u"lineEdit_25")
        self.lineEdit_25.setGeometry(QRect(130, 100, 171, 31))
        self.lineEdit_25.setClearButtonEnabled(True)
        self.label_52 = QLabel(self.groupBox_25)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(30, 100, 91, 31))

        self.verticalLayout_104.addWidget(self.groupBox_25)

        self.groupBox_26 = QGroupBox(self.frame_129)
        self.groupBox_26.setObjectName(u"groupBox_26")
        self.groupBox_26.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QComboBox{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QDateEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 900 12pt \"Roboto Black\";\n"
"}")
        self.label_317 = QLabel(self.groupBox_26)
        self.label_317.setObjectName(u"label_317")
        self.label_317.setGeometry(QRect(20, 80, 131, 31))
        self.lineEdit_84 = QLineEdit(self.groupBox_26)
        self.lineEdit_84.setObjectName(u"lineEdit_84")
        self.lineEdit_84.setGeometry(QRect(170, 40, 191, 31))
        self.lineEdit_84.setClearButtonEnabled(True)
        self.label_318 = QLabel(self.groupBox_26)
        self.label_318.setObjectName(u"label_318")
        self.label_318.setGeometry(QRect(20, 40, 141, 31))
        self.lineEdit_85 = QLineEdit(self.groupBox_26)
        self.lineEdit_85.setObjectName(u"lineEdit_85")
        self.lineEdit_85.setGeometry(QRect(170, 80, 191, 31))
        self.lineEdit_85.setClearButtonEnabled(True)
        self.label_319 = QLabel(self.groupBox_26)
        self.label_319.setObjectName(u"label_319")
        self.label_319.setGeometry(QRect(20, 120, 131, 31))
        self.lineEdit_86 = QLineEdit(self.groupBox_26)
        self.lineEdit_86.setObjectName(u"lineEdit_86")
        self.lineEdit_86.setGeometry(QRect(170, 120, 191, 31))
        self.lineEdit_86.setClearButtonEnabled(True)

        self.verticalLayout_104.addWidget(self.groupBox_26)

        self.frame_130 = QFrame(self.frame_129)
        self.frame_130.setObjectName(u"frame_130")
        self.frame_130.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(158, 158, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(255, 255, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_130.setFrameShape(QFrame.StyledPanel)
        self.frame_130.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_130)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.frame_131 = QFrame(self.frame_130)
        self.frame_131.setObjectName(u"frame_131")
        self.frame_131.setFrameShape(QFrame.StyledPanel)
        self.frame_131.setFrameShadow(QFrame.Raised)
        self.verticalLayout_105 = QVBoxLayout(self.frame_131)
        self.verticalLayout_105.setObjectName(u"verticalLayout_105")
        self.bt_81 = QPushButton(self.frame_131)
        self.bt_81.setObjectName(u"bt_81")
        self.bt_81.setMinimumSize(QSize(0, 40))
        self.bt_81.setMaximumSize(QSize(120, 60))
        self.bt_81.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_81.setIcon(icon19)
        self.bt_81.setIconSize(QSize(20, 20))

        self.verticalLayout_105.addWidget(self.bt_81)


        self.horizontalLayout_48.addWidget(self.frame_131)

        self.frame_132 = QFrame(self.frame_130)
        self.frame_132.setObjectName(u"frame_132")
        self.frame_132.setFrameShape(QFrame.StyledPanel)
        self.frame_132.setFrameShadow(QFrame.Raised)
        self.verticalLayout_106 = QVBoxLayout(self.frame_132)
        self.verticalLayout_106.setObjectName(u"verticalLayout_106")
        self.bt_82 = QPushButton(self.frame_132)
        self.bt_82.setObjectName(u"bt_82")
        self.bt_82.setMinimumSize(QSize(0, 40))
        self.bt_82.setMaximumSize(QSize(120, 60))
        self.bt_82.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_82.setIcon(icon20)
        self.bt_82.setIconSize(QSize(28, 28))

        self.verticalLayout_106.addWidget(self.bt_82)


        self.horizontalLayout_48.addWidget(self.frame_132)

        self.frame_133 = QFrame(self.frame_130)
        self.frame_133.setObjectName(u"frame_133")
        self.frame_133.setFrameShape(QFrame.StyledPanel)
        self.frame_133.setFrameShadow(QFrame.Raised)
        self.verticalLayout_107 = QVBoxLayout(self.frame_133)
        self.verticalLayout_107.setObjectName(u"verticalLayout_107")
        self.bt_83 = QPushButton(self.frame_133)
        self.bt_83.setObjectName(u"bt_83")
        self.bt_83.setMinimumSize(QSize(0, 40))
        self.bt_83.setMaximumSize(QSize(120, 60))
        self.bt_83.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_83.setIcon(icon18)
        self.bt_83.setIconSize(QSize(20, 20))

        self.verticalLayout_107.addWidget(self.bt_83)


        self.horizontalLayout_48.addWidget(self.frame_133)


        self.verticalLayout_104.addWidget(self.frame_130)

        self.verticalLayout_104.setStretch(0, 6)
        self.verticalLayout_104.setStretch(1, 3)
        self.verticalLayout_104.setStretch(2, 1)

        self.horizontalLayout_47.addWidget(self.frame_129)

        self.frame_134 = QFrame(self.tab_33)
        self.frame_134.setObjectName(u"frame_134")
        self.frame_134.setFrameShape(QFrame.StyledPanel)
        self.frame_134.setFrameShadow(QFrame.Raised)
        self.verticalLayout_108 = QVBoxLayout(self.frame_134)
        self.verticalLayout_108.setObjectName(u"verticalLayout_108")
        self.frame_135 = QFrame(self.frame_134)
        self.frame_135.setObjectName(u"frame_135")
        self.frame_135.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(11, 153, 146);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(19, 255, 247);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 12pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_135.setFrameShape(QFrame.NoFrame)
        self.frame_135.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_135)
        self.horizontalLayout_49.setSpacing(1)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.bt_84 = QPushButton(self.frame_135)
        self.bt_84.setObjectName(u"bt_84")
        self.bt_84.setMinimumSize(QSize(10, 40))
        self.bt_84.setMaximumSize(QSize(120, 30))
        self.bt_84.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_84.setIcon(icon21)
        self.bt_84.setIconSize(QSize(28, 28))

        self.horizontalLayout_49.addWidget(self.bt_84)

        self.lineEdit_87 = QLineEdit(self.frame_135)
        self.lineEdit_87.setObjectName(u"lineEdit_87")
        self.lineEdit_87.setMaximumSize(QSize(190, 30))
        self.lineEdit_87.setClearButtonEnabled(True)

        self.horizontalLayout_49.addWidget(self.lineEdit_87)


        self.verticalLayout_108.addWidget(self.frame_135)

        self.tableWidget_14 = QTableWidget(self.frame_134)
        if (self.tableWidget_14.columnCount() < 9):
            self.tableWidget_14.setColumnCount(9)
        __qtablewidgetitem93 = QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(0, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(1, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(2, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(3, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(4, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(5, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(6, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(7, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(8, __qtablewidgetitem101)
        self.tableWidget_14.setObjectName(u"tableWidget_14")
        self.tableWidget_14.setStyleSheet(u"background-color: rgb(191, 191, 191);")

        self.verticalLayout_108.addWidget(self.tableWidget_14)

        self.verticalLayout_108.setStretch(0, 1)
        self.verticalLayout_108.setStretch(1, 9)

        self.horizontalLayout_47.addWidget(self.frame_134)

        self.horizontalLayout_47.setStretch(0, 7)
        self.horizontalLayout_47.setStretch(1, 5)
        self.tabWidget_10.addTab(self.tab_33, "")
        self.tab_34 = QWidget()
        self.tab_34.setObjectName(u"tab_34")
        self.horizontalLayout_50 = QHBoxLayout(self.tab_34)
        self.horizontalLayout_50.setSpacing(0)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.frame_136 = QFrame(self.tab_34)
        self.frame_136.setObjectName(u"frame_136")
        self.frame_136.setFrameShape(QFrame.StyledPanel)
        self.frame_136.setFrameShadow(QFrame.Raised)
        self.verticalLayout_109 = QVBoxLayout(self.frame_136)
        self.verticalLayout_109.setSpacing(0)
        self.verticalLayout_109.setObjectName(u"verticalLayout_109")
        self.verticalLayout_109.setContentsMargins(0, 0, -1, 0)
        self.groupBox_27 = QGroupBox(self.frame_136)
        self.groupBox_27.setObjectName(u"groupBox_27")
        self.groupBox_27.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QComboBox{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QDateEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 900 12pt \"Roboto Black\";\n"
"}")
        self.label_320 = QLabel(self.groupBox_27)
        self.label_320.setObjectName(u"label_320")
        self.label_320.setGeometry(QRect(30, 100, 101, 31))
        self.label_321 = QLabel(self.groupBox_27)
        self.label_321.setObjectName(u"label_321")
        self.label_321.setGeometry(QRect(30, 150, 101, 31))
        self.lineEdit_88 = QLineEdit(self.groupBox_27)
        self.lineEdit_88.setObjectName(u"lineEdit_88")
        self.lineEdit_88.setGeometry(QRect(140, 100, 171, 31))
        self.lineEdit_88.setClearButtonEnabled(True)
        self.label_322 = QLabel(self.groupBox_27)
        self.label_322.setObjectName(u"label_322")
        self.label_322.setGeometry(QRect(30, 50, 161, 31))
        self.lineEdit_89 = QLineEdit(self.groupBox_27)
        self.lineEdit_89.setObjectName(u"lineEdit_89")
        self.lineEdit_89.setGeometry(QRect(210, 50, 171, 31))
        self.lineEdit_89.setClearButtonEnabled(True)
        self.comboBox_41 = QComboBox(self.groupBox_27)
        self.comboBox_41.addItem("")
        self.comboBox_41.addItem("")
        self.comboBox_41.addItem("")
        self.comboBox_41.addItem("")
        self.comboBox_41.addItem("")
        self.comboBox_41.addItem("")
        self.comboBox_41.addItem("")
        self.comboBox_41.addItem("")
        self.comboBox_41.addItem("")
        self.comboBox_41.setObjectName(u"comboBox_41")
        self.comboBox_41.setGeometry(QRect(140, 200, 171, 31))
        self.label_323 = QLabel(self.groupBox_27)
        self.label_323.setObjectName(u"label_323")
        self.label_323.setGeometry(QRect(30, 200, 101, 31))
        self.comboBox_42 = QComboBox(self.groupBox_27)
        self.comboBox_42.addItem("")
        self.comboBox_42.addItem("")
        self.comboBox_42.addItem("")
        self.comboBox_42.setObjectName(u"comboBox_42")
        self.comboBox_42.setGeometry(QRect(140, 250, 171, 31))
        self.label_324 = QLabel(self.groupBox_27)
        self.label_324.setObjectName(u"label_324")
        self.label_324.setGeometry(QRect(30, 250, 101, 31))
        self.comboBox_43 = QComboBox(self.groupBox_27)
        self.comboBox_43.addItem("")
        self.comboBox_43.addItem("")
        self.comboBox_43.addItem("")
        self.comboBox_43.setObjectName(u"comboBox_43")
        self.comboBox_43.setGeometry(QRect(140, 300, 171, 31))
        self.label_325 = QLabel(self.groupBox_27)
        self.label_325.setObjectName(u"label_325")
        self.label_325.setGeometry(QRect(30, 300, 101, 31))
        self.label_326 = QLabel(self.groupBox_27)
        self.label_326.setObjectName(u"label_326")
        self.label_326.setGeometry(QRect(30, 350, 101, 31))
        self.comboBox_44 = QComboBox(self.groupBox_27)
        self.comboBox_44.addItem("")
        self.comboBox_44.addItem("")
        self.comboBox_44.addItem("")
        self.comboBox_44.addItem("")
        self.comboBox_44.addItem("")
        self.comboBox_44.addItem("")
        self.comboBox_44.addItem("")
        self.comboBox_44.addItem("")
        self.comboBox_44.addItem("")
        self.comboBox_44.setObjectName(u"comboBox_44")
        self.comboBox_44.setGeometry(QRect(140, 150, 171, 31))
        self.lineEdit_98 = QLineEdit(self.groupBox_27)
        self.lineEdit_98.setObjectName(u"lineEdit_98")
        self.lineEdit_98.setGeometry(QRect(140, 350, 171, 31))
        self.lineEdit_98.setClearButtonEnabled(True)
        self.label_347 = QLabel(self.groupBox_27)
        self.label_347.setObjectName(u"label_347")
        self.label_347.setGeometry(QRect(30, 400, 101, 31))
        self.label_348 = QLabel(self.groupBox_27)
        self.label_348.setObjectName(u"label_348")
        self.label_348.setGeometry(QRect(30, 450, 101, 31))
        self.lineEdit_99 = QLineEdit(self.groupBox_27)
        self.lineEdit_99.setObjectName(u"lineEdit_99")
        self.lineEdit_99.setGeometry(QRect(140, 450, 171, 31))
        self.lineEdit_99.setClearButtonEnabled(True)
        self.comboBox_46 = QComboBox(self.groupBox_27)
        self.comboBox_46.addItem("")
        self.comboBox_46.addItem("")
        self.comboBox_46.addItem("")
        self.comboBox_46.addItem("")
        self.comboBox_46.addItem("")
        self.comboBox_46.addItem("")
        self.comboBox_46.addItem("")
        self.comboBox_46.addItem("")
        self.comboBox_46.addItem("")
        self.comboBox_46.setObjectName(u"comboBox_46")
        self.comboBox_46.setGeometry(QRect(140, 400, 171, 31))

        self.verticalLayout_109.addWidget(self.groupBox_27)

        self.frame_137 = QFrame(self.frame_136)
        self.frame_137.setObjectName(u"frame_137")
        self.frame_137.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"	background-color: rgb(158, 158, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(255, 255, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_137.setFrameShape(QFrame.StyledPanel)
        self.frame_137.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_137)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.frame_138 = QFrame(self.frame_137)
        self.frame_138.setObjectName(u"frame_138")
        self.frame_138.setFrameShape(QFrame.StyledPanel)
        self.frame_138.setFrameShadow(QFrame.Raised)
        self.verticalLayout_110 = QVBoxLayout(self.frame_138)
        self.verticalLayout_110.setObjectName(u"verticalLayout_110")
        self.bt_85 = QPushButton(self.frame_138)
        self.bt_85.setObjectName(u"bt_85")
        self.bt_85.setMaximumSize(QSize(120, 30))
        self.bt_85.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_85.setIcon(icon17)
        self.bt_85.setIconSize(QSize(20, 20))

        self.verticalLayout_110.addWidget(self.bt_85)


        self.horizontalLayout_51.addWidget(self.frame_138)

        self.frame_139 = QFrame(self.frame_137)
        self.frame_139.setObjectName(u"frame_139")
        self.frame_139.setFrameShape(QFrame.StyledPanel)
        self.frame_139.setFrameShadow(QFrame.Raised)
        self.verticalLayout_111 = QVBoxLayout(self.frame_139)
        self.verticalLayout_111.setObjectName(u"verticalLayout_111")
        self.bt_86 = QPushButton(self.frame_139)
        self.bt_86.setObjectName(u"bt_86")
        self.bt_86.setMaximumSize(QSize(120, 30))
        self.bt_86.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_86.setIcon(icon22)
        self.bt_86.setIconSize(QSize(20, 20))

        self.verticalLayout_111.addWidget(self.bt_86)


        self.horizontalLayout_51.addWidget(self.frame_139)

        self.frame_140 = QFrame(self.frame_137)
        self.frame_140.setObjectName(u"frame_140")
        self.frame_140.setFrameShape(QFrame.StyledPanel)
        self.frame_140.setFrameShadow(QFrame.Raised)
        self.verticalLayout_112 = QVBoxLayout(self.frame_140)
        self.verticalLayout_112.setObjectName(u"verticalLayout_112")
        self.bt_87 = QPushButton(self.frame_140)
        self.bt_87.setObjectName(u"bt_87")
        self.bt_87.setMaximumSize(QSize(120, 30))
        self.bt_87.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_87.setIcon(icon20)
        self.bt_87.setIconSize(QSize(20, 20))

        self.verticalLayout_112.addWidget(self.bt_87)


        self.horizontalLayout_51.addWidget(self.frame_140)

        self.frame_141 = QFrame(self.frame_137)
        self.frame_141.setObjectName(u"frame_141")
        self.frame_141.setFrameShape(QFrame.StyledPanel)
        self.frame_141.setFrameShadow(QFrame.Raised)
        self.verticalLayout_113 = QVBoxLayout(self.frame_141)
        self.verticalLayout_113.setObjectName(u"verticalLayout_113")
        self.bt_88 = QPushButton(self.frame_141)
        self.bt_88.setObjectName(u"bt_88")
        self.bt_88.setMaximumSize(QSize(120, 30))
        self.bt_88.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_88.setIcon(icon23)
        self.bt_88.setIconSize(QSize(20, 20))

        self.verticalLayout_113.addWidget(self.bt_88)


        self.horizontalLayout_51.addWidget(self.frame_141)


        self.verticalLayout_109.addWidget(self.frame_137)

        self.verticalLayout_109.setStretch(0, 8)
        self.verticalLayout_109.setStretch(1, 2)

        self.horizontalLayout_50.addWidget(self.frame_136)

        self.frame_142 = QFrame(self.tab_34)
        self.frame_142.setObjectName(u"frame_142")
        self.frame_142.setFrameShape(QFrame.StyledPanel)
        self.frame_142.setFrameShadow(QFrame.Raised)
        self.verticalLayout_114 = QVBoxLayout(self.frame_142)
        self.verticalLayout_114.setSpacing(1)
        self.verticalLayout_114.setObjectName(u"verticalLayout_114")
        self.verticalLayout_114.setContentsMargins(0, 0, 0, 0)
        self.frame_146 = QFrame(self.frame_142)
        self.frame_146.setObjectName(u"frame_146")
        self.frame_146.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(11, 153, 146);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(19, 255, 247);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 12pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_146.setFrameShape(QFrame.NoFrame)
        self.frame_146.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_146)
        self.horizontalLayout_52.setSpacing(1)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.bt_89 = QPushButton(self.frame_146)
        self.bt_89.setObjectName(u"bt_89")
        self.bt_89.setMinimumSize(QSize(10, 40))
        self.bt_89.setMaximumSize(QSize(120, 30))
        self.bt_89.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_89.setIcon(icon21)
        self.bt_89.setIconSize(QSize(28, 28))

        self.horizontalLayout_52.addWidget(self.bt_89)

        self.lineEdit_90 = QLineEdit(self.frame_146)
        self.lineEdit_90.setObjectName(u"lineEdit_90")
        self.lineEdit_90.setMaximumSize(QSize(190, 30))
        self.lineEdit_90.setClearButtonEnabled(True)

        self.horizontalLayout_52.addWidget(self.lineEdit_90)


        self.verticalLayout_114.addWidget(self.frame_146)

        self.tableWidget_15 = QTableWidget(self.frame_142)
        if (self.tableWidget_15.columnCount() < 9):
            self.tableWidget_15.setColumnCount(9)
        __qtablewidgetitem102 = QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(0, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(1, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(2, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(3, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(4, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(5, __qtablewidgetitem107)
        __qtablewidgetitem108 = QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(6, __qtablewidgetitem108)
        __qtablewidgetitem109 = QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(7, __qtablewidgetitem109)
        __qtablewidgetitem110 = QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(8, __qtablewidgetitem110)
        self.tableWidget_15.setObjectName(u"tableWidget_15")
        self.tableWidget_15.setStyleSheet(u"background-color: rgb(191, 191, 191);")

        self.verticalLayout_114.addWidget(self.tableWidget_15)

        self.verticalLayout_114.setStretch(0, 1)
        self.verticalLayout_114.setStretch(1, 8)

        self.horizontalLayout_50.addWidget(self.frame_142)

        self.horizontalLayout_50.setStretch(0, 5)
        self.horizontalLayout_50.setStretch(1, 5)
        self.tabWidget_10.addTab(self.tab_34, "")
        self.tab_35 = QWidget()
        self.tab_35.setObjectName(u"tab_35")
        self.horizontalLayout_53 = QHBoxLayout(self.tab_35)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.frame_148 = QFrame(self.tab_35)
        self.frame_148.setObjectName(u"frame_148")
        self.frame_148.setFrameShape(QFrame.StyledPanel)
        self.frame_148.setFrameShadow(QFrame.Raised)
        self.verticalLayout_115 = QVBoxLayout(self.frame_148)
        self.verticalLayout_115.setObjectName(u"verticalLayout_115")
        self.groupBox_28 = QGroupBox(self.frame_148)
        self.groupBox_28.setObjectName(u"groupBox_28")
        self.groupBox_28.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QComboBox{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QDateEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 900 12pt \"Roboto Black\";\n"
"}")
        self.label_327 = QLabel(self.groupBox_28)
        self.label_327.setObjectName(u"label_327")
        self.label_327.setGeometry(QRect(20, 100, 161, 31))
        self.label_328 = QLabel(self.groupBox_28)
        self.label_328.setObjectName(u"label_328")
        self.label_328.setGeometry(QRect(30, 180, 101, 31))
        self.lineEdit_91 = QLineEdit(self.groupBox_28)
        self.lineEdit_91.setObjectName(u"lineEdit_91")
        self.lineEdit_91.setGeometry(QRect(210, 100, 171, 31))
        self.lineEdit_91.setClearButtonEnabled(True)
        self.label_329 = QLabel(self.groupBox_28)
        self.label_329.setObjectName(u"label_329")
        self.label_329.setGeometry(QRect(60, 240, 101, 31))
        self.lineEdit_92 = QLineEdit(self.groupBox_28)
        self.lineEdit_92.setObjectName(u"lineEdit_92")
        self.lineEdit_92.setGeometry(QRect(180, 180, 171, 31))
        self.lineEdit_92.setClearButtonEnabled(True)
        self.label_330 = QLabel(self.groupBox_28)
        self.label_330.setObjectName(u"label_330")
        self.label_330.setGeometry(QRect(60, 300, 101, 31))
        self.comboBox_45 = QComboBox(self.groupBox_28)
        self.comboBox_45.addItem("")
        self.comboBox_45.addItem("")
        self.comboBox_45.addItem("")
        self.comboBox_45.addItem("")
        self.comboBox_45.addItem("")
        self.comboBox_45.addItem("")
        self.comboBox_45.addItem("")
        self.comboBox_45.addItem("")
        self.comboBox_45.addItem("")
        self.comboBox_45.setObjectName(u"comboBox_45")
        self.comboBox_45.setGeometry(QRect(180, 240, 171, 31))
        self.lineEdit_97 = QLineEdit(self.groupBox_28)
        self.lineEdit_97.setObjectName(u"lineEdit_97")
        self.lineEdit_97.setGeometry(QRect(180, 300, 171, 31))
        self.lineEdit_97.setClearButtonEnabled(True)

        self.verticalLayout_115.addWidget(self.groupBox_28)

        self.frame_149 = QFrame(self.frame_148)
        self.frame_149.setObjectName(u"frame_149")
        self.frame_149.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(158, 158, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(255, 255, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_149.setFrameShape(QFrame.StyledPanel)
        self.frame_149.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.frame_149)
        self.horizontalLayout_54.setSpacing(0)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.frame_150 = QFrame(self.frame_149)
        self.frame_150.setObjectName(u"frame_150")
        self.frame_150.setFrameShape(QFrame.StyledPanel)
        self.frame_150.setFrameShadow(QFrame.Raised)
        self.verticalLayout_116 = QVBoxLayout(self.frame_150)
        self.verticalLayout_116.setObjectName(u"verticalLayout_116")
        self.bt_90 = QPushButton(self.frame_150)
        self.bt_90.setObjectName(u"bt_90")
        self.bt_90.setMaximumSize(QSize(120, 30))
        self.bt_90.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_90.setIcon(icon17)
        self.bt_90.setIconSize(QSize(20, 20))

        self.verticalLayout_116.addWidget(self.bt_90)


        self.horizontalLayout_54.addWidget(self.frame_150)

        self.frame_151 = QFrame(self.frame_149)
        self.frame_151.setObjectName(u"frame_151")
        self.frame_151.setFrameShape(QFrame.StyledPanel)
        self.frame_151.setFrameShadow(QFrame.Raised)
        self.verticalLayout_117 = QVBoxLayout(self.frame_151)
        self.verticalLayout_117.setObjectName(u"verticalLayout_117")
        self.bt_91 = QPushButton(self.frame_151)
        self.bt_91.setObjectName(u"bt_91")
        self.bt_91.setMaximumSize(QSize(120, 30))
        self.bt_91.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_91.setIcon(icon22)
        self.bt_91.setIconSize(QSize(20, 20))

        self.verticalLayout_117.addWidget(self.bt_91)


        self.horizontalLayout_54.addWidget(self.frame_151)

        self.frame_152 = QFrame(self.frame_149)
        self.frame_152.setObjectName(u"frame_152")
        self.frame_152.setFrameShape(QFrame.StyledPanel)
        self.frame_152.setFrameShadow(QFrame.Raised)
        self.verticalLayout_118 = QVBoxLayout(self.frame_152)
        self.verticalLayout_118.setObjectName(u"verticalLayout_118")
        self.bt_92 = QPushButton(self.frame_152)
        self.bt_92.setObjectName(u"bt_92")
        self.bt_92.setMaximumSize(QSize(120, 30))
        self.bt_92.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_92.setIcon(icon20)
        self.bt_92.setIconSize(QSize(20, 20))

        self.verticalLayout_118.addWidget(self.bt_92)


        self.horizontalLayout_54.addWidget(self.frame_152)

        self.frame_153 = QFrame(self.frame_149)
        self.frame_153.setObjectName(u"frame_153")
        self.frame_153.setFrameShape(QFrame.StyledPanel)
        self.frame_153.setFrameShadow(QFrame.Raised)
        self.verticalLayout_119 = QVBoxLayout(self.frame_153)
        self.verticalLayout_119.setObjectName(u"verticalLayout_119")
        self.bt_93 = QPushButton(self.frame_153)
        self.bt_93.setObjectName(u"bt_93")
        self.bt_93.setMaximumSize(QSize(120, 30))
        self.bt_93.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_93.setIcon(icon23)
        self.bt_93.setIconSize(QSize(20, 20))

        self.verticalLayout_119.addWidget(self.bt_93)


        self.horizontalLayout_54.addWidget(self.frame_153)


        self.verticalLayout_115.addWidget(self.frame_149)

        self.verticalLayout_115.setStretch(0, 8)
        self.verticalLayout_115.setStretch(1, 1)

        self.horizontalLayout_53.addWidget(self.frame_148)

        self.frame_154 = QFrame(self.tab_35)
        self.frame_154.setObjectName(u"frame_154")
        self.frame_154.setFrameShape(QFrame.StyledPanel)
        self.frame_154.setFrameShadow(QFrame.Raised)
        self.verticalLayout_120 = QVBoxLayout(self.frame_154)
        self.verticalLayout_120.setObjectName(u"verticalLayout_120")
        self.tableWidget_16 = QTableWidget(self.frame_154)
        if (self.tableWidget_16.columnCount() < 4):
            self.tableWidget_16.setColumnCount(4)
        __qtablewidgetitem111 = QTableWidgetItem()
        self.tableWidget_16.setHorizontalHeaderItem(0, __qtablewidgetitem111)
        __qtablewidgetitem112 = QTableWidgetItem()
        self.tableWidget_16.setHorizontalHeaderItem(1, __qtablewidgetitem112)
        __qtablewidgetitem113 = QTableWidgetItem()
        self.tableWidget_16.setHorizontalHeaderItem(2, __qtablewidgetitem113)
        __qtablewidgetitem114 = QTableWidgetItem()
        self.tableWidget_16.setHorizontalHeaderItem(3, __qtablewidgetitem114)
        self.tableWidget_16.setObjectName(u"tableWidget_16")
        self.tableWidget_16.setStyleSheet(u"background-color: rgb(191, 191, 191);")

        self.verticalLayout_120.addWidget(self.tableWidget_16)


        self.horizontalLayout_53.addWidget(self.frame_154)

        self.horizontalLayout_53.setStretch(0, 5)
        self.horizontalLayout_53.setStretch(1, 5)
        self.tabWidget_10.addTab(self.tab_35, "")
        self.tab_36 = QWidget()
        self.tab_36.setObjectName(u"tab_36")
        self.horizontalLayout_55 = QHBoxLayout(self.tab_36)
        self.horizontalLayout_55.setSpacing(0)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.frame_155 = QFrame(self.tab_36)
        self.frame_155.setObjectName(u"frame_155")
        self.frame_155.setFrameShape(QFrame.StyledPanel)
        self.frame_155.setFrameShadow(QFrame.Raised)
        self.verticalLayout_121 = QVBoxLayout(self.frame_155)
        self.verticalLayout_121.setObjectName(u"verticalLayout_121")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_121.addItem(self.verticalSpacer_5)

        self.frame_156 = QFrame(self.frame_155)
        self.frame_156.setObjectName(u"frame_156")
        self.frame_156.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"}\n"
"QPushButton {\n"
"	background-color: transparent;\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(36, 36, 36);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(161, 107, 80);\n"
"	border-bottom-left-radius: 8px;\n"
"	\n"
"}\n"
"")
        self.frame_156.setFrameShape(QFrame.StyledPanel)
        self.frame_156.setFrameShadow(QFrame.Raised)
        self.verticalLayout_122 = QVBoxLayout(self.frame_156)
        self.verticalLayout_122.setObjectName(u"verticalLayout_122")
        self.line_68 = QFrame(self.frame_156)
        self.line_68.setObjectName(u"line_68")
        self.line_68.setFrameShape(QFrame.HLine)
        self.line_68.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_122.addWidget(self.line_68)

        self.bt_94 = QPushButton(self.frame_156)
        self.bt_94.setObjectName(u"bt_94")
        self.bt_94.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_122.addWidget(self.bt_94)

        self.line_69 = QFrame(self.frame_156)
        self.line_69.setObjectName(u"line_69")
        self.line_69.setFrameShape(QFrame.HLine)
        self.line_69.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_122.addWidget(self.line_69)

        self.bt_95 = QPushButton(self.frame_156)
        self.bt_95.setObjectName(u"bt_95")
        self.bt_95.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_122.addWidget(self.bt_95)

        self.line_70 = QFrame(self.frame_156)
        self.line_70.setObjectName(u"line_70")
        self.line_70.setFrameShape(QFrame.HLine)
        self.line_70.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_122.addWidget(self.line_70)

        self.bt_96 = QPushButton(self.frame_156)
        self.bt_96.setObjectName(u"bt_96")
        self.bt_96.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_122.addWidget(self.bt_96)

        self.line_71 = QFrame(self.frame_156)
        self.line_71.setObjectName(u"line_71")
        self.line_71.setFrameShape(QFrame.HLine)
        self.line_71.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_122.addWidget(self.line_71)


        self.verticalLayout_121.addWidget(self.frame_156)

        self.verticalSpacer_6 = QSpacerItem(20, 89, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_121.addItem(self.verticalSpacer_6)

        self.verticalLayout_121.setStretch(0, 1)
        self.verticalLayout_121.setStretch(1, 5)
        self.verticalLayout_121.setStretch(2, 1)

        self.horizontalLayout_55.addWidget(self.frame_155)

        self.frame_157 = QFrame(self.tab_36)
        self.frame_157.setObjectName(u"frame_157")
        self.frame_157.setFrameShape(QFrame.StyledPanel)
        self.frame_157.setFrameShadow(QFrame.Raised)
        self.verticalLayout_123 = QVBoxLayout(self.frame_157)
        self.verticalLayout_123.setSpacing(0)
        self.verticalLayout_123.setObjectName(u"verticalLayout_123")
        self.verticalLayout_123.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_11 = QTabWidget(self.frame_157)
        self.tabWidget_11.setObjectName(u"tabWidget_11")
        self.tab_37 = QWidget()
        self.tab_37.setObjectName(u"tab_37")
        self.horizontalLayout_56 = QHBoxLayout(self.tab_37)
        self.horizontalLayout_56.setSpacing(0)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.frame_158 = QFrame(self.tab_37)
        self.frame_158.setObjectName(u"frame_158")
        self.frame_158.setFrameShape(QFrame.StyledPanel)
        self.frame_158.setFrameShadow(QFrame.Raised)
        self.verticalLayout_147 = QVBoxLayout(self.frame_158)
        self.verticalLayout_147.setObjectName(u"verticalLayout_147")
        self.groupBox_39 = QGroupBox(self.frame_158)
        self.groupBox_39.setObjectName(u"groupBox_39")
        self.groupBox_39.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QComboBox{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QDateEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 900 12pt \"Roboto Black\";\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 148, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(0, 213, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.label_264 = QLabel(self.groupBox_39)
        self.label_264.setObjectName(u"label_264")
        self.label_264.setGeometry(QRect(40, 320, 101, 31))
        self.comboBox_63 = QComboBox(self.groupBox_39)
        self.comboBox_63.addItem("")
        self.comboBox_63.addItem("")
        self.comboBox_63.addItem("")
        self.comboBox_63.setObjectName(u"comboBox_63")
        self.comboBox_63.setGeometry(QRect(400, 210, 141, 31))
        self.label_265 = QLabel(self.groupBox_39)
        self.label_265.setObjectName(u"label_265")
        self.label_265.setGeometry(QRect(340, 210, 61, 31))
        self.label_331 = QLabel(self.groupBox_39)
        self.label_331.setObjectName(u"label_331")
        self.label_331.setGeometry(QRect(40, 380, 51, 31))
        self.lineEdit_132 = QLineEdit(self.groupBox_39)
        self.lineEdit_132.setObjectName(u"lineEdit_132")
        self.lineEdit_132.setGeometry(QRect(140, 320, 161, 31))
        self.lineEdit_132.setClearButtonEnabled(True)
        self.lineEdit_133 = QLineEdit(self.groupBox_39)
        self.lineEdit_133.setObjectName(u"lineEdit_133")
        self.lineEdit_133.setGeometry(QRect(140, 160, 161, 31))
        self.lineEdit_133.setClearButtonEnabled(True)
        self.label_332 = QLabel(self.groupBox_39)
        self.label_332.setObjectName(u"label_332")
        self.label_332.setGeometry(QRect(30, 160, 111, 31))
        self.label_333 = QLabel(self.groupBox_39)
        self.label_333.setObjectName(u"label_333")
        self.label_333.setGeometry(QRect(340, 160, 131, 31))
        self.lineEdit_134 = QLineEdit(self.groupBox_39)
        self.lineEdit_134.setObjectName(u"lineEdit_134")
        self.lineEdit_134.setGeometry(QRect(480, 160, 151, 31))
        self.lineEdit_134.setClearButtonEnabled(True)
        self.label_334 = QLabel(self.groupBox_39)
        self.label_334.setObjectName(u"label_334")
        self.label_334.setGeometry(QRect(20, 220, 121, 31))
        self.lineEdit_135 = QLineEdit(self.groupBox_39)
        self.lineEdit_135.setObjectName(u"lineEdit_135")
        self.lineEdit_135.setGeometry(QRect(140, 210, 161, 31))
        self.lineEdit_135.setClearButtonEnabled(True)
        self.comboBox_64 = QComboBox(self.groupBox_39)
        self.comboBox_64.addItem("")
        self.comboBox_64.addItem("")
        self.comboBox_64.addItem("")
        self.comboBox_64.addItem("")
        self.comboBox_64.addItem("")
        self.comboBox_64.addItem("")
        self.comboBox_64.addItem("")
        self.comboBox_64.addItem("")
        self.comboBox_64.addItem("")
        self.comboBox_64.setObjectName(u"comboBox_64")
        self.comboBox_64.setGeometry(QRect(140, 380, 161, 31))
        self.label_848 = QLabel(self.groupBox_39)
        self.label_848.setObjectName(u"label_848")
        self.label_848.setGeometry(QRect(30, 440, 101, 31))
        self.comboBox_66 = QComboBox(self.groupBox_39)
        self.comboBox_66.addItem("")
        self.comboBox_66.addItem("")
        self.comboBox_66.addItem("")
        self.comboBox_66.addItem("")
        self.comboBox_66.addItem("")
        self.comboBox_66.addItem("")
        self.comboBox_66.addItem("")
        self.comboBox_66.addItem("")
        self.comboBox_66.addItem("")
        self.comboBox_66.setObjectName(u"comboBox_66")
        self.comboBox_66.setGeometry(QRect(140, 440, 161, 31))
        self.label_849 = QLabel(self.groupBox_39)
        self.label_849.setObjectName(u"label_849")
        self.label_849.setGeometry(QRect(180, 40, 381, 31))
        self.pushButton_10 = QPushButton(self.groupBox_39)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(400, 513, 91, 41))
        self.pushButton_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_10.setIcon(icon18)
        self.pushButton_10.setIconSize(QSize(20, 20))
        self.pushButton_10.setAutoDefault(True)
        self.lineEdit_162 = QLineEdit(self.groupBox_39)
        self.lineEdit_162.setObjectName(u"lineEdit_162")
        self.lineEdit_162.setGeometry(QRect(170, 490, 161, 31))
        self.lineEdit_162.setClearButtonEnabled(True)
        self.label_1326 = QLabel(self.groupBox_39)
        self.label_1326.setObjectName(u"label_1326")
        self.label_1326.setGeometry(QRect(30, 490, 141, 31))
        self.label_1341 = QLabel(self.groupBox_39)
        self.label_1341.setObjectName(u"label_1341")
        self.label_1341.setGeometry(QRect(350, 380, 101, 31))
        self.lineEdit_177 = QLineEdit(self.groupBox_39)
        self.lineEdit_177.setObjectName(u"lineEdit_177")
        self.lineEdit_177.setGeometry(QRect(470, 380, 191, 31))
        self.lineEdit_177.setClearButtonEnabled(True)
        self.lineEdit_178 = QLineEdit(self.groupBox_39)
        self.lineEdit_178.setObjectName(u"lineEdit_178")
        self.lineEdit_178.setGeometry(QRect(500, 440, 191, 31))
        self.lineEdit_178.setClearButtonEnabled(True)
        self.label_1342 = QLabel(self.groupBox_39)
        self.label_1342.setObjectName(u"label_1342")
        self.label_1342.setGeometry(QRect(360, 440, 141, 31))
        self.label_1355 = QLabel(self.groupBox_39)
        self.label_1355.setObjectName(u"label_1355")
        self.label_1355.setGeometry(QRect(390, 320, 51, 31))
        self.lineEdit_191 = QLineEdit(self.groupBox_39)
        self.lineEdit_191.setObjectName(u"lineEdit_191")
        self.lineEdit_191.setGeometry(QRect(460, 320, 191, 31))
        self.lineEdit_191.setClearButtonEnabled(True)

        self.verticalLayout_147.addWidget(self.groupBox_39)


        self.horizontalLayout_56.addWidget(self.frame_158)

        self.tabWidget_11.addTab(self.tab_37, "")
        self.tab_38 = QWidget()
        self.tab_38.setObjectName(u"tab_38")
        self.horizontalLayout_57 = QHBoxLayout(self.tab_38)
        self.horizontalLayout_57.setSpacing(0)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.frame_159 = QFrame(self.tab_38)
        self.frame_159.setObjectName(u"frame_159")
        self.frame_159.setFrameShape(QFrame.StyledPanel)
        self.frame_159.setFrameShadow(QFrame.Raised)
        self.verticalLayout_148 = QVBoxLayout(self.frame_159)
        self.verticalLayout_148.setObjectName(u"verticalLayout_148")
        self.groupBox_40 = QGroupBox(self.frame_159)
        self.groupBox_40.setObjectName(u"groupBox_40")
        self.groupBox_40.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QComboBox{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QDateEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 900 12pt \"Roboto Black\";\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 148, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(0, 213, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.label_335 = QLabel(self.groupBox_40)
        self.label_335.setObjectName(u"label_335")
        self.label_335.setGeometry(QRect(40, 320, 101, 31))
        self.comboBox_67 = QComboBox(self.groupBox_40)
        self.comboBox_67.addItem("")
        self.comboBox_67.addItem("")
        self.comboBox_67.addItem("")
        self.comboBox_67.setObjectName(u"comboBox_67")
        self.comboBox_67.setGeometry(QRect(400, 210, 141, 31))
        self.label_336 = QLabel(self.groupBox_40)
        self.label_336.setObjectName(u"label_336")
        self.label_336.setGeometry(QRect(340, 210, 61, 31))
        self.label_337 = QLabel(self.groupBox_40)
        self.label_337.setObjectName(u"label_337")
        self.label_337.setGeometry(QRect(40, 380, 51, 31))
        self.lineEdit_136 = QLineEdit(self.groupBox_40)
        self.lineEdit_136.setObjectName(u"lineEdit_136")
        self.lineEdit_136.setGeometry(QRect(140, 320, 161, 31))
        self.lineEdit_136.setClearButtonEnabled(True)
        self.lineEdit_137 = QLineEdit(self.groupBox_40)
        self.lineEdit_137.setObjectName(u"lineEdit_137")
        self.lineEdit_137.setGeometry(QRect(140, 160, 161, 31))
        self.lineEdit_137.setClearButtonEnabled(True)
        self.label_338 = QLabel(self.groupBox_40)
        self.label_338.setObjectName(u"label_338")
        self.label_338.setGeometry(QRect(30, 160, 111, 31))
        self.label_339 = QLabel(self.groupBox_40)
        self.label_339.setObjectName(u"label_339")
        self.label_339.setGeometry(QRect(340, 160, 131, 31))
        self.lineEdit_138 = QLineEdit(self.groupBox_40)
        self.lineEdit_138.setObjectName(u"lineEdit_138")
        self.lineEdit_138.setGeometry(QRect(480, 160, 151, 31))
        self.lineEdit_138.setClearButtonEnabled(True)
        self.label_340 = QLabel(self.groupBox_40)
        self.label_340.setObjectName(u"label_340")
        self.label_340.setGeometry(QRect(20, 220, 121, 31))
        self.lineEdit_139 = QLineEdit(self.groupBox_40)
        self.lineEdit_139.setObjectName(u"lineEdit_139")
        self.lineEdit_139.setGeometry(QRect(140, 210, 161, 31))
        self.lineEdit_139.setClearButtonEnabled(True)
        self.comboBox_69 = QComboBox(self.groupBox_40)
        self.comboBox_69.addItem("")
        self.comboBox_69.addItem("")
        self.comboBox_69.addItem("")
        self.comboBox_69.addItem("")
        self.comboBox_69.addItem("")
        self.comboBox_69.addItem("")
        self.comboBox_69.addItem("")
        self.comboBox_69.addItem("")
        self.comboBox_69.addItem("")
        self.comboBox_69.setObjectName(u"comboBox_69")
        self.comboBox_69.setGeometry(QRect(140, 380, 161, 31))
        self.label_850 = QLabel(self.groupBox_40)
        self.label_850.setObjectName(u"label_850")
        self.label_850.setGeometry(QRect(30, 440, 101, 31))
        self.comboBox_70 = QComboBox(self.groupBox_40)
        self.comboBox_70.addItem("")
        self.comboBox_70.addItem("")
        self.comboBox_70.addItem("")
        self.comboBox_70.addItem("")
        self.comboBox_70.addItem("")
        self.comboBox_70.addItem("")
        self.comboBox_70.addItem("")
        self.comboBox_70.addItem("")
        self.comboBox_70.addItem("")
        self.comboBox_70.setObjectName(u"comboBox_70")
        self.comboBox_70.setGeometry(QRect(140, 440, 161, 31))
        self.label_851 = QLabel(self.groupBox_40)
        self.label_851.setObjectName(u"label_851")
        self.label_851.setGeometry(QRect(180, 40, 381, 31))
        self.pushButton_11 = QPushButton(self.groupBox_40)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(380, 550, 101, 51))
        self.pushButton_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_11.setIcon(icon18)
        self.pushButton_11.setIconSize(QSize(20, 20))
        self.lineEdit_163 = QLineEdit(self.groupBox_40)
        self.lineEdit_163.setObjectName(u"lineEdit_163")
        self.lineEdit_163.setGeometry(QRect(170, 500, 161, 31))
        self.lineEdit_163.setClearButtonEnabled(True)
        self.label_1327 = QLabel(self.groupBox_40)
        self.label_1327.setObjectName(u"label_1327")
        self.label_1327.setGeometry(QRect(30, 500, 141, 31))
        self.label_1343 = QLabel(self.groupBox_40)
        self.label_1343.setObjectName(u"label_1343")
        self.label_1343.setGeometry(QRect(350, 380, 101, 31))
        self.lineEdit_179 = QLineEdit(self.groupBox_40)
        self.lineEdit_179.setObjectName(u"lineEdit_179")
        self.lineEdit_179.setGeometry(QRect(470, 380, 191, 31))
        self.lineEdit_179.setClearButtonEnabled(True)
        self.lineEdit_180 = QLineEdit(self.groupBox_40)
        self.lineEdit_180.setObjectName(u"lineEdit_180")
        self.lineEdit_180.setGeometry(QRect(500, 440, 191, 31))
        self.lineEdit_180.setClearButtonEnabled(True)
        self.label_1344 = QLabel(self.groupBox_40)
        self.label_1344.setObjectName(u"label_1344")
        self.label_1344.setGeometry(QRect(360, 440, 141, 31))
        self.label_1354 = QLabel(self.groupBox_40)
        self.label_1354.setObjectName(u"label_1354")
        self.label_1354.setGeometry(QRect(390, 320, 51, 31))
        self.lineEdit_190 = QLineEdit(self.groupBox_40)
        self.lineEdit_190.setObjectName(u"lineEdit_190")
        self.lineEdit_190.setGeometry(QRect(460, 320, 191, 31))
        self.lineEdit_190.setClearButtonEnabled(True)

        self.verticalLayout_148.addWidget(self.groupBox_40)


        self.horizontalLayout_57.addWidget(self.frame_159)

        self.tabWidget_11.addTab(self.tab_38, "")
        self.tab_39 = QWidget()
        self.tab_39.setObjectName(u"tab_39")
        self.horizontalLayout_58 = QHBoxLayout(self.tab_39)
        self.horizontalLayout_58.setSpacing(0)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.frame_160 = QFrame(self.tab_39)
        self.frame_160.setObjectName(u"frame_160")
        self.frame_160.setFrameShape(QFrame.StyledPanel)
        self.frame_160.setFrameShadow(QFrame.Raised)
        self.verticalLayout_149 = QVBoxLayout(self.frame_160)
        self.verticalLayout_149.setObjectName(u"verticalLayout_149")
        self.groupBox_41 = QGroupBox(self.frame_160)
        self.groupBox_41.setObjectName(u"groupBox_41")
        self.groupBox_41.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QComboBox{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QDateEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 14pt \"Rockwell\";\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 900 12pt \"Roboto Black\";\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 148, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(0, 213, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.label_341 = QLabel(self.groupBox_41)
        self.label_341.setObjectName(u"label_341")
        self.label_341.setGeometry(QRect(40, 320, 101, 31))
        self.comboBox_71 = QComboBox(self.groupBox_41)
        self.comboBox_71.addItem("")
        self.comboBox_71.addItem("")
        self.comboBox_71.addItem("")
        self.comboBox_71.setObjectName(u"comboBox_71")
        self.comboBox_71.setGeometry(QRect(400, 210, 141, 31))
        self.label_342 = QLabel(self.groupBox_41)
        self.label_342.setObjectName(u"label_342")
        self.label_342.setGeometry(QRect(340, 210, 61, 31))
        self.label_343 = QLabel(self.groupBox_41)
        self.label_343.setObjectName(u"label_343")
        self.label_343.setGeometry(QRect(40, 380, 51, 31))
        self.lineEdit_140 = QLineEdit(self.groupBox_41)
        self.lineEdit_140.setObjectName(u"lineEdit_140")
        self.lineEdit_140.setGeometry(QRect(140, 320, 161, 31))
        self.lineEdit_140.setClearButtonEnabled(True)
        self.lineEdit_141 = QLineEdit(self.groupBox_41)
        self.lineEdit_141.setObjectName(u"lineEdit_141")
        self.lineEdit_141.setGeometry(QRect(140, 160, 161, 31))
        self.lineEdit_141.setClearButtonEnabled(True)
        self.label_344 = QLabel(self.groupBox_41)
        self.label_344.setObjectName(u"label_344")
        self.label_344.setGeometry(QRect(30, 160, 111, 31))
        self.label_345 = QLabel(self.groupBox_41)
        self.label_345.setObjectName(u"label_345")
        self.label_345.setGeometry(QRect(340, 160, 131, 31))
        self.lineEdit_142 = QLineEdit(self.groupBox_41)
        self.lineEdit_142.setObjectName(u"lineEdit_142")
        self.lineEdit_142.setGeometry(QRect(480, 160, 151, 31))
        self.lineEdit_142.setClearButtonEnabled(True)
        self.label_346 = QLabel(self.groupBox_41)
        self.label_346.setObjectName(u"label_346")
        self.label_346.setGeometry(QRect(20, 220, 121, 31))
        self.lineEdit_143 = QLineEdit(self.groupBox_41)
        self.lineEdit_143.setObjectName(u"lineEdit_143")
        self.lineEdit_143.setGeometry(QRect(140, 210, 161, 31))
        self.lineEdit_143.setClearButtonEnabled(True)
        self.comboBox_72 = QComboBox(self.groupBox_41)
        self.comboBox_72.addItem("")
        self.comboBox_72.addItem("")
        self.comboBox_72.addItem("")
        self.comboBox_72.addItem("")
        self.comboBox_72.addItem("")
        self.comboBox_72.addItem("")
        self.comboBox_72.addItem("")
        self.comboBox_72.addItem("")
        self.comboBox_72.addItem("")
        self.comboBox_72.setObjectName(u"comboBox_72")
        self.comboBox_72.setGeometry(QRect(140, 380, 161, 31))
        self.label_852 = QLabel(self.groupBox_41)
        self.label_852.setObjectName(u"label_852")
        self.label_852.setGeometry(QRect(30, 440, 101, 31))
        self.comboBox_73 = QComboBox(self.groupBox_41)
        self.comboBox_73.addItem("")
        self.comboBox_73.addItem("")
        self.comboBox_73.addItem("")
        self.comboBox_73.addItem("")
        self.comboBox_73.addItem("")
        self.comboBox_73.addItem("")
        self.comboBox_73.addItem("")
        self.comboBox_73.addItem("")
        self.comboBox_73.addItem("")
        self.comboBox_73.setObjectName(u"comboBox_73")
        self.comboBox_73.setGeometry(QRect(140, 440, 161, 31))
        self.label_853 = QLabel(self.groupBox_41)
        self.label_853.setObjectName(u"label_853")
        self.label_853.setGeometry(QRect(180, 40, 381, 31))
        self.pushButton_12 = QPushButton(self.groupBox_41)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(390, 540, 91, 41))
        self.pushButton_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_12.setIcon(icon18)
        self.pushButton_12.setIconSize(QSize(20, 20))
        self.lineEdit_164 = QLineEdit(self.groupBox_41)
        self.lineEdit_164.setObjectName(u"lineEdit_164")
        self.lineEdit_164.setGeometry(QRect(170, 490, 161, 31))
        self.lineEdit_164.setClearButtonEnabled(True)
        self.label_1328 = QLabel(self.groupBox_41)
        self.label_1328.setObjectName(u"label_1328")
        self.label_1328.setGeometry(QRect(30, 490, 141, 31))
        self.label_1345 = QLabel(self.groupBox_41)
        self.label_1345.setObjectName(u"label_1345")
        self.label_1345.setGeometry(QRect(350, 380, 101, 31))
        self.lineEdit_181 = QLineEdit(self.groupBox_41)
        self.lineEdit_181.setObjectName(u"lineEdit_181")
        self.lineEdit_181.setGeometry(QRect(470, 380, 191, 31))
        self.lineEdit_181.setClearButtonEnabled(True)
        self.lineEdit_182 = QLineEdit(self.groupBox_41)
        self.lineEdit_182.setObjectName(u"lineEdit_182")
        self.lineEdit_182.setGeometry(QRect(500, 440, 191, 31))
        self.lineEdit_182.setClearButtonEnabled(True)
        self.label_1346 = QLabel(self.groupBox_41)
        self.label_1346.setObjectName(u"label_1346")
        self.label_1346.setGeometry(QRect(360, 440, 141, 31))
        self.label_1353 = QLabel(self.groupBox_41)
        self.label_1353.setObjectName(u"label_1353")
        self.label_1353.setGeometry(QRect(390, 320, 51, 31))
        self.lineEdit_189 = QLineEdit(self.groupBox_41)
        self.lineEdit_189.setObjectName(u"lineEdit_189")
        self.lineEdit_189.setGeometry(QRect(460, 320, 191, 31))
        self.lineEdit_189.setClearButtonEnabled(True)

        self.verticalLayout_149.addWidget(self.groupBox_41)


        self.horizontalLayout_58.addWidget(self.frame_160)

        self.tabWidget_11.addTab(self.tab_39, "")
        self.tab_49 = QWidget()
        self.tab_49.setObjectName(u"tab_49")
        self.verticalLayout_152 = QVBoxLayout(self.tab_49)
        self.verticalLayout_152.setSpacing(0)
        self.verticalLayout_152.setObjectName(u"verticalLayout_152")
        self.verticalLayout_152.setContentsMargins(0, 0, 0, 0)
        self.frame_185 = QFrame(self.tab_49)
        self.frame_185.setObjectName(u"frame_185")
        self.frame_185.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(222, 222, 222);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 148, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(0, 213, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_185.setFrameShape(QFrame.StyledPanel)
        self.frame_185.setFrameShadow(QFrame.Raised)
        self.label_962 = QLabel(self.frame_185)
        self.label_962.setObjectName(u"label_962")
        self.label_962.setGeometry(QRect(180, 10, 311, 21))
        self.label_962.setStyleSheet(u"font: 900 14pt \"Roboto\";")
        self.label_962.setAlignment(Qt.AlignCenter)
        self.label_963 = QLabel(self.frame_185)
        self.label_963.setObjectName(u"label_963")
        self.label_963.setGeometry(QRect(210, 40, 141, 16))
        self.label_964 = QLabel(self.frame_185)
        self.label_964.setObjectName(u"label_964")
        self.label_964.setGeometry(QRect(440, 40, 171, 16))
        self.label_965 = QLabel(self.frame_185)
        self.label_965.setObjectName(u"label_965")
        self.label_965.setGeometry(QRect(220, 60, 221, 20))
        self.label_965.setAlignment(Qt.AlignCenter)
        self.label_966 = QLabel(self.frame_185)
        self.label_966.setObjectName(u"label_966")
        self.label_966.setGeometry(QRect(70, 100, 49, 16))
        self.line_208 = QFrame(self.frame_185)
        self.line_208.setObjectName(u"line_208")
        self.line_208.setGeometry(QRect(90, 80, 501, 16))
        self.line_208.setFrameShape(QFrame.HLine)
        self.line_208.setFrameShadow(QFrame.Sunken)
        self.label_967 = QLabel(self.frame_185)
        self.label_967.setObjectName(u"label_967")
        self.label_967.setGeometry(QRect(120, 100, 71, 16))
        self.label_967.setStyleSheet(u"color: rgb(161, 161, 0);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_968 = QLabel(self.frame_185)
        self.label_968.setObjectName(u"label_968")
        self.label_968.setGeometry(QRect(220, 100, 41, 16))
        self.label_969 = QLabel(self.frame_185)
        self.label_969.setObjectName(u"label_969")
        self.label_969.setGeometry(QRect(270, 100, 141, 16))
        self.label_969.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_969.setTextFormat(Qt.AutoText)
        self.label_969.setScaledContents(False)
        self.label_970 = QLabel(self.frame_185)
        self.label_970.setObjectName(u"label_970")
        self.label_970.setGeometry(QRect(80, 140, 91, 16))
        self.label_971 = QLabel(self.frame_185)
        self.label_971.setObjectName(u"label_971")
        self.label_971.setGeometry(QRect(160, 140, 71, 16))
        self.label_972 = QLabel(self.frame_185)
        self.label_972.setObjectName(u"label_972")
        self.label_972.setGeometry(QRect(270, 140, 101, 16))
        self.label_973 = QLabel(self.frame_185)
        self.label_973.setObjectName(u"label_973")
        self.label_973.setGeometry(QRect(370, 140, 61, 16))
        self.label_974 = QLabel(self.frame_185)
        self.label_974.setObjectName(u"label_974")
        self.label_974.setGeometry(QRect(430, 100, 49, 16))
        self.label_975 = QLabel(self.frame_185)
        self.label_975.setObjectName(u"label_975")
        self.label_975.setGeometry(QRect(470, 100, 91, 16))
        self.label_976 = QLabel(self.frame_185)
        self.label_976.setObjectName(u"label_976")
        self.label_976.setGeometry(QRect(460, 140, 49, 16))
        self.label_977 = QLabel(self.frame_185)
        self.label_977.setObjectName(u"label_977")
        self.label_977.setGeometry(QRect(500, 140, 71, 16))
        self.line_209 = QFrame(self.frame_185)
        self.line_209.setObjectName(u"line_209")
        self.line_209.setGeometry(QRect(20, 160, 631, 20))
        self.line_209.setFrameShape(QFrame.HLine)
        self.line_209.setFrameShadow(QFrame.Sunken)
        self.line_210 = QFrame(self.frame_185)
        self.line_210.setObjectName(u"line_210")
        self.line_210.setGeometry(QRect(120, 180, 20, 381))
        self.line_210.setFrameShadow(QFrame.Sunken)
        self.line_210.setFrameShape(QFrame.VLine)
        self.line_211 = QFrame(self.frame_185)
        self.line_211.setObjectName(u"line_211")
        self.line_211.setGeometry(QRect(240, 180, 20, 381))
        self.line_211.setFrameShape(QFrame.VLine)
        self.line_211.setFrameShadow(QFrame.Sunken)
        self.line_212 = QFrame(self.frame_185)
        self.line_212.setObjectName(u"line_212")
        self.line_212.setGeometry(QRect(350, 180, 20, 381))
        self.line_212.setFrameShape(QFrame.VLine)
        self.line_212.setFrameShadow(QFrame.Sunken)
        self.line_213 = QFrame(self.frame_185)
        self.line_213.setObjectName(u"line_213")
        self.line_213.setGeometry(QRect(10, 210, 641, 20))
        self.line_213.setFrameShape(QFrame.HLine)
        self.line_213.setFrameShadow(QFrame.Sunken)
        self.label_978 = QLabel(self.frame_185)
        self.label_978.setObjectName(u"label_978")
        self.label_978.setGeometry(QRect(40, 180, 71, 20))
        self.label_978.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_979 = QLabel(self.frame_185)
        self.label_979.setObjectName(u"label_979")
        self.label_979.setGeometry(QRect(140, 170, 101, 20))
        self.label_979.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_980 = QLabel(self.frame_185)
        self.label_980.setObjectName(u"label_980")
        self.label_980.setGeometry(QRect(170, 190, 31, 20))
        self.label_980.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_981 = QLabel(self.frame_185)
        self.label_981.setObjectName(u"label_981")
        self.label_981.setGeometry(QRect(490, 180, 51, 20))
        self.label_981.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_982 = QLabel(self.frame_185)
        self.label_982.setObjectName(u"label_982")
        self.label_982.setGeometry(QRect(560, 180, 81, 20))
        self.label_982.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_983 = QLabel(self.frame_185)
        self.label_983.setObjectName(u"label_983")
        self.label_983.setGeometry(QRect(10, 220, 101, 16))
        self.label_984 = QLabel(self.frame_185)
        self.label_984.setObjectName(u"label_984")
        self.label_984.setGeometry(QRect(10, 260, 111, 16))
        self.label_985 = QLabel(self.frame_185)
        self.label_985.setObjectName(u"label_985")
        self.label_985.setGeometry(QRect(10, 300, 111, 16))
        self.label_986 = QLabel(self.frame_185)
        self.label_986.setObjectName(u"label_986")
        self.label_986.setGeometry(QRect(10, 340, 111, 16))
        self.label_987 = QLabel(self.frame_185)
        self.label_987.setObjectName(u"label_987")
        self.label_987.setGeometry(QRect(10, 380, 71, 16))
        self.label_988 = QLabel(self.frame_185)
        self.label_988.setObjectName(u"label_988")
        self.label_988.setGeometry(QRect(10, 420, 71, 16))
        self.label_989 = QLabel(self.frame_185)
        self.label_989.setObjectName(u"label_989")
        self.label_989.setGeometry(QRect(10, 460, 81, 16))
        self.label_990 = QLabel(self.frame_185)
        self.label_990.setObjectName(u"label_990")
        self.label_990.setGeometry(QRect(10, 500, 91, 16))
        self.label_991 = QLabel(self.frame_185)
        self.label_991.setObjectName(u"label_991")
        self.label_991.setGeometry(QRect(10, 540, 71, 16))
        self.line_214 = QFrame(self.frame_185)
        self.line_214.setObjectName(u"line_214")
        self.line_214.setGeometry(QRect(10, 240, 641, 20))
        self.line_214.setFrameShape(QFrame.HLine)
        self.line_214.setFrameShadow(QFrame.Sunken)
        self.line_215 = QFrame(self.frame_185)
        self.line_215.setObjectName(u"line_215")
        self.line_215.setGeometry(QRect(10, 280, 641, 20))
        self.line_215.setFrameShape(QFrame.HLine)
        self.line_215.setFrameShadow(QFrame.Sunken)
        self.line_216 = QFrame(self.frame_185)
        self.line_216.setObjectName(u"line_216")
        self.line_216.setGeometry(QRect(10, 320, 641, 20))
        self.line_216.setFrameShape(QFrame.HLine)
        self.line_216.setFrameShadow(QFrame.Sunken)
        self.line_217 = QFrame(self.frame_185)
        self.line_217.setObjectName(u"line_217")
        self.line_217.setGeometry(QRect(10, 360, 641, 20))
        self.line_217.setFrameShadow(QFrame.Sunken)
        self.line_217.setFrameShape(QFrame.HLine)
        self.line_218 = QFrame(self.frame_185)
        self.line_218.setObjectName(u"line_218")
        self.line_218.setGeometry(QRect(10, 400, 641, 20))
        self.line_218.setFrameShape(QFrame.HLine)
        self.line_218.setFrameShadow(QFrame.Sunken)
        self.line_219 = QFrame(self.frame_185)
        self.line_219.setObjectName(u"line_219")
        self.line_219.setGeometry(QRect(10, 440, 641, 20))
        self.line_219.setFrameShape(QFrame.HLine)
        self.line_219.setFrameShadow(QFrame.Sunken)
        self.line_220 = QFrame(self.frame_185)
        self.line_220.setObjectName(u"line_220")
        self.line_220.setGeometry(QRect(10, 480, 641, 20))
        self.line_220.setFrameShape(QFrame.HLine)
        self.line_220.setFrameShadow(QFrame.Sunken)
        self.line_221 = QFrame(self.frame_185)
        self.line_221.setObjectName(u"line_221")
        self.line_221.setGeometry(QRect(10, 520, 641, 20))
        self.line_221.setFrameShape(QFrame.HLine)
        self.line_221.setFrameShadow(QFrame.Sunken)
        self.line_222 = QFrame(self.frame_185)
        self.line_222.setObjectName(u"line_222")
        self.line_222.setGeometry(QRect(10, 560, 641, 20))
        self.line_222.setFrameShape(QFrame.HLine)
        self.line_222.setFrameShadow(QFrame.Sunken)
        self.label_992 = QLabel(self.frame_185)
        self.label_992.setObjectName(u"label_992")
        self.label_992.setGeometry(QRect(50, 580, 71, 16))
        self.label_993 = QLabel(self.frame_185)
        self.label_993.setObjectName(u"label_993")
        self.label_993.setGeometry(QRect(120, 580, 49, 16))
        self.label_994 = QLabel(self.frame_185)
        self.label_994.setObjectName(u"label_994")
        self.label_994.setGeometry(QRect(200, 580, 41, 16))
        self.label_995 = QLabel(self.frame_185)
        self.label_995.setObjectName(u"label_995")
        self.label_995.setGeometry(QRect(240, 580, 49, 16))
        self.label_996 = QLabel(self.frame_185)
        self.label_996.setObjectName(u"label_996")
        self.label_996.setGeometry(QRect(370, 580, 81, 16))
        self.label_997 = QLabel(self.frame_185)
        self.label_997.setObjectName(u"label_997")
        self.label_997.setGeometry(QRect(450, 580, 49, 16))
        self.label_998 = QLabel(self.frame_185)
        self.label_998.setObjectName(u"label_998")
        self.label_998.setGeometry(QRect(100, 600, 181, 16))
        self.label_999 = QLabel(self.frame_185)
        self.label_999.setObjectName(u"label_999")
        self.label_999.setGeometry(QRect(50, 600, 51, 16))
        self.label_1000 = QLabel(self.frame_185)
        self.label_1000.setObjectName(u"label_1000")
        self.label_1000.setGeometry(QRect(380, 600, 41, 16))
        self.label_1001 = QLabel(self.frame_185)
        self.label_1001.setObjectName(u"label_1001")
        self.label_1001.setGeometry(QRect(430, 600, 181, 16))
        self.label_1002 = QLabel(self.frame_185)
        self.label_1002.setObjectName(u"label_1002")
        self.label_1002.setGeometry(QRect(50, 620, 131, 16))
        self.label_1003 = QLabel(self.frame_185)
        self.label_1003.setObjectName(u"label_1003")
        self.label_1003.setGeometry(QRect(190, 620, 191, 16))
        self.label_1004 = QLabel(self.frame_185)
        self.label_1004.setObjectName(u"label_1004")
        self.label_1004.setGeometry(QRect(510, 620, 81, 16))
        self.label_1005 = QLabel(self.frame_185)
        self.label_1005.setObjectName(u"label_1005")
        self.label_1005.setGeometry(QRect(450, 620, 61, 16))
        self.label_1006 = QLabel(self.frame_185)
        self.label_1006.setObjectName(u"label_1006")
        self.label_1006.setGeometry(QRect(50, 640, 101, 16))
        self.label_1007 = QLabel(self.frame_185)
        self.label_1007.setObjectName(u"label_1007")
        self.label_1007.setGeometry(QRect(150, 640, 231, 16))
        self.label_1008 = QLabel(self.frame_185)
        self.label_1008.setObjectName(u"label_1008")
        self.label_1008.setGeometry(QRect(510, 640, 81, 16))
        self.label_1009 = QLabel(self.frame_185)
        self.label_1009.setObjectName(u"label_1009")
        self.label_1009.setGeometry(QRect(450, 640, 61, 16))
        self.label_1010 = QLabel(self.frame_185)
        self.label_1010.setObjectName(u"label_1010")
        self.label_1010.setGeometry(QRect(260, 170, 91, 20))
        self.label_1010.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_1011 = QLabel(self.frame_185)
        self.label_1011.setObjectName(u"label_1011")
        self.label_1011.setGeometry(QRect(290, 190, 31, 20))
        self.label_1011.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_1012 = QLabel(self.frame_185)
        self.label_1012.setObjectName(u"label_1012")
        self.label_1012.setGeometry(QRect(370, 170, 101, 20))
        self.label_1012.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_1013 = QLabel(self.frame_185)
        self.label_1013.setObjectName(u"label_1013")
        self.label_1013.setGeometry(QRect(400, 190, 41, 20))
        self.label_1013.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.line_223 = QFrame(self.frame_185)
        self.line_223.setObjectName(u"line_223")
        self.line_223.setGeometry(QRect(470, 180, 20, 381))
        self.line_223.setFrameShape(QFrame.VLine)
        self.line_223.setFrameShadow(QFrame.Sunken)
        self.line_224 = QFrame(self.frame_185)
        self.line_224.setObjectName(u"line_224")
        self.line_224.setGeometry(QRect(540, 180, 20, 381))
        self.line_224.setFrameShape(QFrame.VLine)
        self.line_224.setFrameShadow(QFrame.Sunken)
        self.label_1014 = QLabel(self.frame_185)
        self.label_1014.setObjectName(u"label_1014")
        self.label_1014.setGeometry(QRect(170, 40, 31, 16))
        self.label_1015 = QLabel(self.frame_185)
        self.label_1015.setObjectName(u"label_1015")
        self.label_1015.setGeometry(QRect(390, 40, 49, 16))
        self.bt_112 = QPushButton(self.frame_185)
        self.bt_112.setObjectName(u"bt_112")
        self.bt_112.setGeometry(QRect(574, 13, 91, 31))
        self.bt_112.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_112.setIcon(icon24)
        self.bt_112.setIconSize(QSize(20, 20))

        self.verticalLayout_152.addWidget(self.frame_185)

        self.tabWidget_11.addTab(self.tab_49, "")
        self.tab_50 = QWidget()
        self.tab_50.setObjectName(u"tab_50")
        self.verticalLayout_151 = QVBoxLayout(self.tab_50)
        self.verticalLayout_151.setSpacing(0)
        self.verticalLayout_151.setObjectName(u"verticalLayout_151")
        self.verticalLayout_151.setContentsMargins(0, 0, 0, 0)
        self.frame_184 = QFrame(self.tab_50)
        self.frame_184.setObjectName(u"frame_184")
        self.frame_184.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(222, 222, 222);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 148, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(0, 213, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_184.setFrameShape(QFrame.StyledPanel)
        self.frame_184.setFrameShadow(QFrame.Raised)
        self.label_908 = QLabel(self.frame_184)
        self.label_908.setObjectName(u"label_908")
        self.label_908.setGeometry(QRect(180, 10, 311, 21))
        self.label_908.setStyleSheet(u"font: 900 14pt \"Roboto\";")
        self.label_908.setAlignment(Qt.AlignCenter)
        self.label_909 = QLabel(self.frame_184)
        self.label_909.setObjectName(u"label_909")
        self.label_909.setGeometry(QRect(210, 40, 141, 16))
        self.label_910 = QLabel(self.frame_184)
        self.label_910.setObjectName(u"label_910")
        self.label_910.setGeometry(QRect(440, 40, 171, 16))
        self.label_911 = QLabel(self.frame_184)
        self.label_911.setObjectName(u"label_911")
        self.label_911.setGeometry(QRect(220, 60, 221, 20))
        self.label_911.setAlignment(Qt.AlignCenter)
        self.label_912 = QLabel(self.frame_184)
        self.label_912.setObjectName(u"label_912")
        self.label_912.setGeometry(QRect(70, 100, 49, 16))
        self.line_191 = QFrame(self.frame_184)
        self.line_191.setObjectName(u"line_191")
        self.line_191.setGeometry(QRect(90, 80, 501, 16))
        self.line_191.setFrameShape(QFrame.HLine)
        self.line_191.setFrameShadow(QFrame.Sunken)
        self.label_913 = QLabel(self.frame_184)
        self.label_913.setObjectName(u"label_913")
        self.label_913.setGeometry(QRect(120, 100, 71, 16))
        self.label_913.setStyleSheet(u"color: rgb(161, 161, 0);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_914 = QLabel(self.frame_184)
        self.label_914.setObjectName(u"label_914")
        self.label_914.setGeometry(QRect(220, 100, 41, 16))
        self.label_915 = QLabel(self.frame_184)
        self.label_915.setObjectName(u"label_915")
        self.label_915.setGeometry(QRect(270, 100, 151, 16))
        self.label_915.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_915.setTextFormat(Qt.AutoText)
        self.label_915.setScaledContents(False)
        self.label_916 = QLabel(self.frame_184)
        self.label_916.setObjectName(u"label_916")
        self.label_916.setGeometry(QRect(80, 140, 91, 16))
        self.label_917 = QLabel(self.frame_184)
        self.label_917.setObjectName(u"label_917")
        self.label_917.setGeometry(QRect(160, 140, 71, 16))
        self.label_918 = QLabel(self.frame_184)
        self.label_918.setObjectName(u"label_918")
        self.label_918.setGeometry(QRect(270, 140, 101, 16))
        self.label_919 = QLabel(self.frame_184)
        self.label_919.setObjectName(u"label_919")
        self.label_919.setGeometry(QRect(370, 140, 61, 16))
        self.label_920 = QLabel(self.frame_184)
        self.label_920.setObjectName(u"label_920")
        self.label_920.setGeometry(QRect(430, 100, 49, 16))
        self.label_921 = QLabel(self.frame_184)
        self.label_921.setObjectName(u"label_921")
        self.label_921.setGeometry(QRect(470, 100, 91, 16))
        self.label_922 = QLabel(self.frame_184)
        self.label_922.setObjectName(u"label_922")
        self.label_922.setGeometry(QRect(460, 140, 49, 16))
        self.label_923 = QLabel(self.frame_184)
        self.label_923.setObjectName(u"label_923")
        self.label_923.setGeometry(QRect(500, 140, 71, 16))
        self.line_192 = QFrame(self.frame_184)
        self.line_192.setObjectName(u"line_192")
        self.line_192.setGeometry(QRect(20, 160, 631, 20))
        self.line_192.setFrameShape(QFrame.HLine)
        self.line_192.setFrameShadow(QFrame.Sunken)
        self.line_193 = QFrame(self.frame_184)
        self.line_193.setObjectName(u"line_193")
        self.line_193.setGeometry(QRect(120, 180, 20, 381))
        self.line_193.setFrameShadow(QFrame.Sunken)
        self.line_193.setFrameShape(QFrame.VLine)
        self.line_194 = QFrame(self.frame_184)
        self.line_194.setObjectName(u"line_194")
        self.line_194.setGeometry(QRect(240, 180, 20, 381))
        self.line_194.setFrameShape(QFrame.VLine)
        self.line_194.setFrameShadow(QFrame.Sunken)
        self.line_195 = QFrame(self.frame_184)
        self.line_195.setObjectName(u"line_195")
        self.line_195.setGeometry(QRect(350, 180, 20, 381))
        self.line_195.setFrameShape(QFrame.VLine)
        self.line_195.setFrameShadow(QFrame.Sunken)
        self.line_196 = QFrame(self.frame_184)
        self.line_196.setObjectName(u"line_196")
        self.line_196.setGeometry(QRect(10, 210, 641, 20))
        self.line_196.setFrameShape(QFrame.HLine)
        self.line_196.setFrameShadow(QFrame.Sunken)
        self.label_924 = QLabel(self.frame_184)
        self.label_924.setObjectName(u"label_924")
        self.label_924.setGeometry(QRect(40, 180, 71, 20))
        self.label_924.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_925 = QLabel(self.frame_184)
        self.label_925.setObjectName(u"label_925")
        self.label_925.setGeometry(QRect(140, 170, 101, 20))
        self.label_925.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_926 = QLabel(self.frame_184)
        self.label_926.setObjectName(u"label_926")
        self.label_926.setGeometry(QRect(170, 190, 31, 20))
        self.label_926.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_927 = QLabel(self.frame_184)
        self.label_927.setObjectName(u"label_927")
        self.label_927.setGeometry(QRect(490, 180, 51, 20))
        self.label_927.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_928 = QLabel(self.frame_184)
        self.label_928.setObjectName(u"label_928")
        self.label_928.setGeometry(QRect(560, 180, 81, 20))
        self.label_928.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_929 = QLabel(self.frame_184)
        self.label_929.setObjectName(u"label_929")
        self.label_929.setGeometry(QRect(10, 220, 101, 16))
        self.label_930 = QLabel(self.frame_184)
        self.label_930.setObjectName(u"label_930")
        self.label_930.setGeometry(QRect(10, 260, 111, 16))
        self.label_931 = QLabel(self.frame_184)
        self.label_931.setObjectName(u"label_931")
        self.label_931.setGeometry(QRect(10, 300, 111, 16))
        self.label_932 = QLabel(self.frame_184)
        self.label_932.setObjectName(u"label_932")
        self.label_932.setGeometry(QRect(10, 340, 111, 16))
        self.label_933 = QLabel(self.frame_184)
        self.label_933.setObjectName(u"label_933")
        self.label_933.setGeometry(QRect(10, 380, 71, 16))
        self.label_934 = QLabel(self.frame_184)
        self.label_934.setObjectName(u"label_934")
        self.label_934.setGeometry(QRect(10, 420, 71, 16))
        self.label_935 = QLabel(self.frame_184)
        self.label_935.setObjectName(u"label_935")
        self.label_935.setGeometry(QRect(10, 460, 81, 16))
        self.label_936 = QLabel(self.frame_184)
        self.label_936.setObjectName(u"label_936")
        self.label_936.setGeometry(QRect(10, 500, 91, 16))
        self.label_937 = QLabel(self.frame_184)
        self.label_937.setObjectName(u"label_937")
        self.label_937.setGeometry(QRect(20, 540, 71, 16))
        self.line_197 = QFrame(self.frame_184)
        self.line_197.setObjectName(u"line_197")
        self.line_197.setGeometry(QRect(10, 240, 641, 20))
        self.line_197.setFrameShape(QFrame.HLine)
        self.line_197.setFrameShadow(QFrame.Sunken)
        self.line_198 = QFrame(self.frame_184)
        self.line_198.setObjectName(u"line_198")
        self.line_198.setGeometry(QRect(10, 280, 641, 20))
        self.line_198.setFrameShape(QFrame.HLine)
        self.line_198.setFrameShadow(QFrame.Sunken)
        self.line_199 = QFrame(self.frame_184)
        self.line_199.setObjectName(u"line_199")
        self.line_199.setGeometry(QRect(10, 320, 641, 20))
        self.line_199.setFrameShape(QFrame.HLine)
        self.line_199.setFrameShadow(QFrame.Sunken)
        self.line_200 = QFrame(self.frame_184)
        self.line_200.setObjectName(u"line_200")
        self.line_200.setGeometry(QRect(10, 360, 641, 20))
        self.line_200.setFrameShadow(QFrame.Sunken)
        self.line_200.setFrameShape(QFrame.HLine)
        self.line_201 = QFrame(self.frame_184)
        self.line_201.setObjectName(u"line_201")
        self.line_201.setGeometry(QRect(10, 400, 641, 20))
        self.line_201.setFrameShape(QFrame.HLine)
        self.line_201.setFrameShadow(QFrame.Sunken)
        self.line_202 = QFrame(self.frame_184)
        self.line_202.setObjectName(u"line_202")
        self.line_202.setGeometry(QRect(10, 440, 641, 20))
        self.line_202.setFrameShape(QFrame.HLine)
        self.line_202.setFrameShadow(QFrame.Sunken)
        self.line_203 = QFrame(self.frame_184)
        self.line_203.setObjectName(u"line_203")
        self.line_203.setGeometry(QRect(10, 480, 641, 20))
        self.line_203.setFrameShape(QFrame.HLine)
        self.line_203.setFrameShadow(QFrame.Sunken)
        self.line_204 = QFrame(self.frame_184)
        self.line_204.setObjectName(u"line_204")
        self.line_204.setGeometry(QRect(10, 560, 641, 20))
        self.line_204.setFrameShape(QFrame.HLine)
        self.line_204.setFrameShadow(QFrame.Sunken)
        self.line_205 = QFrame(self.frame_184)
        self.line_205.setObjectName(u"line_205")
        self.line_205.setGeometry(QRect(10, 520, 641, 20))
        self.line_205.setFrameShape(QFrame.HLine)
        self.line_205.setFrameShadow(QFrame.Sunken)
        self.label_938 = QLabel(self.frame_184)
        self.label_938.setObjectName(u"label_938")
        self.label_938.setGeometry(QRect(50, 580, 71, 16))
        self.label_939 = QLabel(self.frame_184)
        self.label_939.setObjectName(u"label_939")
        self.label_939.setGeometry(QRect(120, 580, 49, 16))
        self.label_940 = QLabel(self.frame_184)
        self.label_940.setObjectName(u"label_940")
        self.label_940.setGeometry(QRect(200, 580, 41, 16))
        self.label_941 = QLabel(self.frame_184)
        self.label_941.setObjectName(u"label_941")
        self.label_941.setGeometry(QRect(240, 580, 49, 16))
        self.label_942 = QLabel(self.frame_184)
        self.label_942.setObjectName(u"label_942")
        self.label_942.setGeometry(QRect(370, 580, 81, 16))
        self.label_943 = QLabel(self.frame_184)
        self.label_943.setObjectName(u"label_943")
        self.label_943.setGeometry(QRect(450, 580, 49, 16))
        self.label_944 = QLabel(self.frame_184)
        self.label_944.setObjectName(u"label_944")
        self.label_944.setGeometry(QRect(100, 600, 181, 16))
        self.label_945 = QLabel(self.frame_184)
        self.label_945.setObjectName(u"label_945")
        self.label_945.setGeometry(QRect(50, 600, 51, 16))
        self.label_946 = QLabel(self.frame_184)
        self.label_946.setObjectName(u"label_946")
        self.label_946.setGeometry(QRect(380, 600, 41, 16))
        self.label_947 = QLabel(self.frame_184)
        self.label_947.setObjectName(u"label_947")
        self.label_947.setGeometry(QRect(430, 600, 181, 16))
        self.label_948 = QLabel(self.frame_184)
        self.label_948.setObjectName(u"label_948")
        self.label_948.setGeometry(QRect(50, 620, 131, 16))
        self.label_949 = QLabel(self.frame_184)
        self.label_949.setObjectName(u"label_949")
        self.label_949.setGeometry(QRect(190, 620, 191, 16))
        self.label_950 = QLabel(self.frame_184)
        self.label_950.setObjectName(u"label_950")
        self.label_950.setGeometry(QRect(510, 620, 81, 16))
        self.label_951 = QLabel(self.frame_184)
        self.label_951.setObjectName(u"label_951")
        self.label_951.setGeometry(QRect(450, 620, 61, 16))
        self.label_952 = QLabel(self.frame_184)
        self.label_952.setObjectName(u"label_952")
        self.label_952.setGeometry(QRect(50, 640, 101, 16))
        self.label_953 = QLabel(self.frame_184)
        self.label_953.setObjectName(u"label_953")
        self.label_953.setGeometry(QRect(150, 640, 231, 16))
        self.label_954 = QLabel(self.frame_184)
        self.label_954.setObjectName(u"label_954")
        self.label_954.setGeometry(QRect(510, 640, 81, 16))
        self.label_955 = QLabel(self.frame_184)
        self.label_955.setObjectName(u"label_955")
        self.label_955.setGeometry(QRect(450, 640, 61, 16))
        self.label_956 = QLabel(self.frame_184)
        self.label_956.setObjectName(u"label_956")
        self.label_956.setGeometry(QRect(260, 170, 91, 20))
        self.label_956.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_957 = QLabel(self.frame_184)
        self.label_957.setObjectName(u"label_957")
        self.label_957.setGeometry(QRect(290, 190, 31, 20))
        self.label_957.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_958 = QLabel(self.frame_184)
        self.label_958.setObjectName(u"label_958")
        self.label_958.setGeometry(QRect(370, 170, 101, 20))
        self.label_958.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_959 = QLabel(self.frame_184)
        self.label_959.setObjectName(u"label_959")
        self.label_959.setGeometry(QRect(400, 190, 41, 20))
        self.label_959.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.line_206 = QFrame(self.frame_184)
        self.line_206.setObjectName(u"line_206")
        self.line_206.setGeometry(QRect(470, 180, 20, 381))
        self.line_206.setFrameShape(QFrame.VLine)
        self.line_206.setFrameShadow(QFrame.Sunken)
        self.line_207 = QFrame(self.frame_184)
        self.line_207.setObjectName(u"line_207")
        self.line_207.setGeometry(QRect(540, 180, 20, 381))
        self.line_207.setFrameShape(QFrame.VLine)
        self.line_207.setFrameShadow(QFrame.Sunken)
        self.label_960 = QLabel(self.frame_184)
        self.label_960.setObjectName(u"label_960")
        self.label_960.setGeometry(QRect(170, 40, 31, 16))
        self.label_961 = QLabel(self.frame_184)
        self.label_961.setObjectName(u"label_961")
        self.label_961.setGeometry(QRect(390, 40, 49, 16))
        self.bt_111 = QPushButton(self.frame_184)
        self.bt_111.setObjectName(u"bt_111")
        self.bt_111.setGeometry(QRect(584, 13, 81, 31))
        self.bt_111.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_111.setIcon(icon24)
        self.bt_111.setIconSize(QSize(20, 20))

        self.verticalLayout_151.addWidget(self.frame_184)

        self.tabWidget_11.addTab(self.tab_50, "")
        self.tab_51 = QWidget()
        self.tab_51.setObjectName(u"tab_51")
        self.verticalLayout_150 = QVBoxLayout(self.tab_51)
        self.verticalLayout_150.setSpacing(0)
        self.verticalLayout_150.setObjectName(u"verticalLayout_150")
        self.verticalLayout_150.setContentsMargins(0, 0, 0, 0)
        self.frame_183 = QFrame(self.tab_51)
        self.frame_183.setObjectName(u"frame_183")
        self.frame_183.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(222, 222, 222);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 148, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(0, 213, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_183.setFrameShape(QFrame.StyledPanel)
        self.frame_183.setFrameShadow(QFrame.Raised)
        self.label_854 = QLabel(self.frame_183)
        self.label_854.setObjectName(u"label_854")
        self.label_854.setGeometry(QRect(180, 10, 311, 21))
        self.label_854.setStyleSheet(u"font: 900 14pt \"Roboto\";")
        self.label_854.setAlignment(Qt.AlignCenter)
        self.label_855 = QLabel(self.frame_183)
        self.label_855.setObjectName(u"label_855")
        self.label_855.setGeometry(QRect(210, 40, 141, 16))
        self.label_856 = QLabel(self.frame_183)
        self.label_856.setObjectName(u"label_856")
        self.label_856.setGeometry(QRect(440, 40, 171, 16))
        self.label_857 = QLabel(self.frame_183)
        self.label_857.setObjectName(u"label_857")
        self.label_857.setGeometry(QRect(220, 60, 221, 20))
        self.label_857.setAlignment(Qt.AlignCenter)
        self.label_858 = QLabel(self.frame_183)
        self.label_858.setObjectName(u"label_858")
        self.label_858.setGeometry(QRect(70, 100, 49, 16))
        self.line_174 = QFrame(self.frame_183)
        self.line_174.setObjectName(u"line_174")
        self.line_174.setGeometry(QRect(90, 80, 501, 16))
        self.line_174.setFrameShape(QFrame.HLine)
        self.line_174.setFrameShadow(QFrame.Sunken)
        self.label_859 = QLabel(self.frame_183)
        self.label_859.setObjectName(u"label_859")
        self.label_859.setGeometry(QRect(120, 100, 71, 16))
        self.label_859.setStyleSheet(u"color: rgb(161, 161, 0);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_860 = QLabel(self.frame_183)
        self.label_860.setObjectName(u"label_860")
        self.label_860.setGeometry(QRect(220, 100, 41, 16))
        self.label_861 = QLabel(self.frame_183)
        self.label_861.setObjectName(u"label_861")
        self.label_861.setGeometry(QRect(270, 100, 151, 16))
        self.label_861.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_861.setTextFormat(Qt.AutoText)
        self.label_861.setScaledContents(False)
        self.label_862 = QLabel(self.frame_183)
        self.label_862.setObjectName(u"label_862")
        self.label_862.setGeometry(QRect(80, 140, 91, 16))
        self.label_863 = QLabel(self.frame_183)
        self.label_863.setObjectName(u"label_863")
        self.label_863.setGeometry(QRect(160, 140, 71, 16))
        self.label_864 = QLabel(self.frame_183)
        self.label_864.setObjectName(u"label_864")
        self.label_864.setGeometry(QRect(270, 140, 101, 16))
        self.label_865 = QLabel(self.frame_183)
        self.label_865.setObjectName(u"label_865")
        self.label_865.setGeometry(QRect(370, 140, 61, 16))
        self.label_866 = QLabel(self.frame_183)
        self.label_866.setObjectName(u"label_866")
        self.label_866.setGeometry(QRect(430, 100, 49, 16))
        self.label_867 = QLabel(self.frame_183)
        self.label_867.setObjectName(u"label_867")
        self.label_867.setGeometry(QRect(470, 100, 91, 16))
        self.label_868 = QLabel(self.frame_183)
        self.label_868.setObjectName(u"label_868")
        self.label_868.setGeometry(QRect(460, 140, 49, 16))
        self.label_869 = QLabel(self.frame_183)
        self.label_869.setObjectName(u"label_869")
        self.label_869.setGeometry(QRect(500, 140, 71, 16))
        self.line_175 = QFrame(self.frame_183)
        self.line_175.setObjectName(u"line_175")
        self.line_175.setGeometry(QRect(20, 160, 631, 20))
        self.line_175.setFrameShape(QFrame.HLine)
        self.line_175.setFrameShadow(QFrame.Sunken)
        self.line_176 = QFrame(self.frame_183)
        self.line_176.setObjectName(u"line_176")
        self.line_176.setGeometry(QRect(120, 180, 20, 381))
        self.line_176.setFrameShadow(QFrame.Sunken)
        self.line_176.setFrameShape(QFrame.VLine)
        self.line_177 = QFrame(self.frame_183)
        self.line_177.setObjectName(u"line_177")
        self.line_177.setGeometry(QRect(240, 180, 20, 381))
        self.line_177.setFrameShape(QFrame.VLine)
        self.line_177.setFrameShadow(QFrame.Sunken)
        self.line_178 = QFrame(self.frame_183)
        self.line_178.setObjectName(u"line_178")
        self.line_178.setGeometry(QRect(350, 180, 20, 381))
        self.line_178.setFrameShape(QFrame.VLine)
        self.line_178.setFrameShadow(QFrame.Sunken)
        self.line_179 = QFrame(self.frame_183)
        self.line_179.setObjectName(u"line_179")
        self.line_179.setGeometry(QRect(10, 210, 641, 20))
        self.line_179.setFrameShape(QFrame.HLine)
        self.line_179.setFrameShadow(QFrame.Sunken)
        self.label_870 = QLabel(self.frame_183)
        self.label_870.setObjectName(u"label_870")
        self.label_870.setGeometry(QRect(40, 180, 71, 20))
        self.label_870.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_871 = QLabel(self.frame_183)
        self.label_871.setObjectName(u"label_871")
        self.label_871.setGeometry(QRect(140, 170, 101, 20))
        self.label_871.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_872 = QLabel(self.frame_183)
        self.label_872.setObjectName(u"label_872")
        self.label_872.setGeometry(QRect(170, 190, 31, 20))
        self.label_872.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_873 = QLabel(self.frame_183)
        self.label_873.setObjectName(u"label_873")
        self.label_873.setGeometry(QRect(490, 180, 51, 20))
        self.label_873.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_874 = QLabel(self.frame_183)
        self.label_874.setObjectName(u"label_874")
        self.label_874.setGeometry(QRect(560, 180, 81, 20))
        self.label_874.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_875 = QLabel(self.frame_183)
        self.label_875.setObjectName(u"label_875")
        self.label_875.setGeometry(QRect(10, 220, 101, 16))
        self.label_876 = QLabel(self.frame_183)
        self.label_876.setObjectName(u"label_876")
        self.label_876.setGeometry(QRect(10, 260, 111, 16))
        self.label_877 = QLabel(self.frame_183)
        self.label_877.setObjectName(u"label_877")
        self.label_877.setGeometry(QRect(10, 300, 111, 16))
        self.label_878 = QLabel(self.frame_183)
        self.label_878.setObjectName(u"label_878")
        self.label_878.setGeometry(QRect(10, 340, 111, 16))
        self.label_879 = QLabel(self.frame_183)
        self.label_879.setObjectName(u"label_879")
        self.label_879.setGeometry(QRect(10, 380, 71, 16))
        self.label_880 = QLabel(self.frame_183)
        self.label_880.setObjectName(u"label_880")
        self.label_880.setGeometry(QRect(10, 420, 71, 16))
        self.label_881 = QLabel(self.frame_183)
        self.label_881.setObjectName(u"label_881")
        self.label_881.setGeometry(QRect(10, 460, 81, 16))
        self.label_882 = QLabel(self.frame_183)
        self.label_882.setObjectName(u"label_882")
        self.label_882.setGeometry(QRect(10, 500, 91, 16))
        self.label_883 = QLabel(self.frame_183)
        self.label_883.setObjectName(u"label_883")
        self.label_883.setGeometry(QRect(10, 540, 71, 16))
        self.line_180 = QFrame(self.frame_183)
        self.line_180.setObjectName(u"line_180")
        self.line_180.setGeometry(QRect(10, 240, 641, 20))
        self.line_180.setFrameShape(QFrame.HLine)
        self.line_180.setFrameShadow(QFrame.Sunken)
        self.line_181 = QFrame(self.frame_183)
        self.line_181.setObjectName(u"line_181")
        self.line_181.setGeometry(QRect(10, 280, 641, 20))
        self.line_181.setFrameShape(QFrame.HLine)
        self.line_181.setFrameShadow(QFrame.Sunken)
        self.line_182 = QFrame(self.frame_183)
        self.line_182.setObjectName(u"line_182")
        self.line_182.setGeometry(QRect(10, 320, 641, 20))
        self.line_182.setFrameShape(QFrame.HLine)
        self.line_182.setFrameShadow(QFrame.Sunken)
        self.line_183 = QFrame(self.frame_183)
        self.line_183.setObjectName(u"line_183")
        self.line_183.setGeometry(QRect(10, 360, 641, 20))
        self.line_183.setFrameShadow(QFrame.Sunken)
        self.line_183.setFrameShape(QFrame.HLine)
        self.line_184 = QFrame(self.frame_183)
        self.line_184.setObjectName(u"line_184")
        self.line_184.setGeometry(QRect(10, 400, 641, 20))
        self.line_184.setFrameShape(QFrame.HLine)
        self.line_184.setFrameShadow(QFrame.Sunken)
        self.line_185 = QFrame(self.frame_183)
        self.line_185.setObjectName(u"line_185")
        self.line_185.setGeometry(QRect(10, 440, 641, 20))
        self.line_185.setFrameShape(QFrame.HLine)
        self.line_185.setFrameShadow(QFrame.Sunken)
        self.line_186 = QFrame(self.frame_183)
        self.line_186.setObjectName(u"line_186")
        self.line_186.setGeometry(QRect(10, 480, 641, 20))
        self.line_186.setFrameShape(QFrame.HLine)
        self.line_186.setFrameShadow(QFrame.Sunken)
        self.line_187 = QFrame(self.frame_183)
        self.line_187.setObjectName(u"line_187")
        self.line_187.setGeometry(QRect(10, 520, 641, 20))
        self.line_187.setFrameShape(QFrame.HLine)
        self.line_187.setFrameShadow(QFrame.Sunken)
        self.line_188 = QFrame(self.frame_183)
        self.line_188.setObjectName(u"line_188")
        self.line_188.setGeometry(QRect(10, 560, 641, 20))
        self.line_188.setFrameShape(QFrame.HLine)
        self.line_188.setFrameShadow(QFrame.Sunken)
        self.label_884 = QLabel(self.frame_183)
        self.label_884.setObjectName(u"label_884")
        self.label_884.setGeometry(QRect(50, 580, 71, 16))
        self.label_885 = QLabel(self.frame_183)
        self.label_885.setObjectName(u"label_885")
        self.label_885.setGeometry(QRect(120, 580, 49, 16))
        self.label_886 = QLabel(self.frame_183)
        self.label_886.setObjectName(u"label_886")
        self.label_886.setGeometry(QRect(200, 580, 41, 16))
        self.label_887 = QLabel(self.frame_183)
        self.label_887.setObjectName(u"label_887")
        self.label_887.setGeometry(QRect(240, 580, 49, 16))
        self.label_888 = QLabel(self.frame_183)
        self.label_888.setObjectName(u"label_888")
        self.label_888.setGeometry(QRect(370, 580, 81, 16))
        self.label_889 = QLabel(self.frame_183)
        self.label_889.setObjectName(u"label_889")
        self.label_889.setGeometry(QRect(450, 580, 49, 16))
        self.label_890 = QLabel(self.frame_183)
        self.label_890.setObjectName(u"label_890")
        self.label_890.setGeometry(QRect(100, 600, 181, 16))
        self.label_891 = QLabel(self.frame_183)
        self.label_891.setObjectName(u"label_891")
        self.label_891.setGeometry(QRect(50, 600, 51, 16))
        self.label_892 = QLabel(self.frame_183)
        self.label_892.setObjectName(u"label_892")
        self.label_892.setGeometry(QRect(380, 600, 41, 16))
        self.label_893 = QLabel(self.frame_183)
        self.label_893.setObjectName(u"label_893")
        self.label_893.setGeometry(QRect(430, 600, 181, 16))
        self.label_894 = QLabel(self.frame_183)
        self.label_894.setObjectName(u"label_894")
        self.label_894.setGeometry(QRect(50, 620, 131, 16))
        self.label_895 = QLabel(self.frame_183)
        self.label_895.setObjectName(u"label_895")
        self.label_895.setGeometry(QRect(190, 620, 191, 16))
        self.label_896 = QLabel(self.frame_183)
        self.label_896.setObjectName(u"label_896")
        self.label_896.setGeometry(QRect(510, 620, 81, 16))
        self.label_897 = QLabel(self.frame_183)
        self.label_897.setObjectName(u"label_897")
        self.label_897.setGeometry(QRect(450, 620, 61, 16))
        self.label_898 = QLabel(self.frame_183)
        self.label_898.setObjectName(u"label_898")
        self.label_898.setGeometry(QRect(50, 640, 101, 16))
        self.label_899 = QLabel(self.frame_183)
        self.label_899.setObjectName(u"label_899")
        self.label_899.setGeometry(QRect(150, 640, 231, 16))
        self.label_900 = QLabel(self.frame_183)
        self.label_900.setObjectName(u"label_900")
        self.label_900.setGeometry(QRect(510, 640, 81, 16))
        self.label_901 = QLabel(self.frame_183)
        self.label_901.setObjectName(u"label_901")
        self.label_901.setGeometry(QRect(450, 640, 61, 16))
        self.label_902 = QLabel(self.frame_183)
        self.label_902.setObjectName(u"label_902")
        self.label_902.setGeometry(QRect(260, 170, 91, 20))
        self.label_902.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_903 = QLabel(self.frame_183)
        self.label_903.setObjectName(u"label_903")
        self.label_903.setGeometry(QRect(290, 190, 31, 20))
        self.label_903.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_904 = QLabel(self.frame_183)
        self.label_904.setObjectName(u"label_904")
        self.label_904.setGeometry(QRect(370, 170, 101, 20))
        self.label_904.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_905 = QLabel(self.frame_183)
        self.label_905.setObjectName(u"label_905")
        self.label_905.setGeometry(QRect(400, 190, 41, 20))
        self.label_905.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.line_189 = QFrame(self.frame_183)
        self.line_189.setObjectName(u"line_189")
        self.line_189.setGeometry(QRect(470, 180, 20, 381))
        self.line_189.setFrameShape(QFrame.VLine)
        self.line_189.setFrameShadow(QFrame.Sunken)
        self.line_190 = QFrame(self.frame_183)
        self.line_190.setObjectName(u"line_190")
        self.line_190.setGeometry(QRect(540, 180, 20, 381))
        self.line_190.setFrameShape(QFrame.VLine)
        self.line_190.setFrameShadow(QFrame.Sunken)
        self.label_906 = QLabel(self.frame_183)
        self.label_906.setObjectName(u"label_906")
        self.label_906.setGeometry(QRect(170, 40, 31, 16))
        self.label_907 = QLabel(self.frame_183)
        self.label_907.setObjectName(u"label_907")
        self.label_907.setGeometry(QRect(390, 40, 49, 16))
        self.bt_110 = QPushButton(self.frame_183)
        self.bt_110.setObjectName(u"bt_110")
        self.bt_110.setGeometry(QRect(574, 13, 91, 31))
        self.bt_110.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_110.setIcon(icon24)
        self.bt_110.setIconSize(QSize(20, 20))

        self.verticalLayout_150.addWidget(self.frame_183)

        self.tabWidget_11.addTab(self.tab_51, "")

        self.verticalLayout_123.addWidget(self.tabWidget_11)


        self.horizontalLayout_55.addWidget(self.frame_157)

        self.horizontalLayout_55.setStretch(0, 2)
        self.horizontalLayout_55.setStretch(1, 8)
        self.tabWidget_10.addTab(self.tab_36, "")
        self.tab_40 = QWidget()
        self.tab_40.setObjectName(u"tab_40")
        self.verticalLayout_124 = QVBoxLayout(self.tab_40)
        self.verticalLayout_124.setSpacing(0)
        self.verticalLayout_124.setObjectName(u"verticalLayout_124")
        self.verticalLayout_124.setContentsMargins(0, 0, 0, 0)
        self.frame_161 = QFrame(self.tab_40)
        self.frame_161.setObjectName(u"frame_161")
        self.frame_161.setFrameShape(QFrame.StyledPanel)
        self.frame_161.setFrameShadow(QFrame.Raised)
        self.verticalLayout_125 = QVBoxLayout(self.frame_161)
        self.verticalLayout_125.setSpacing(0)
        self.verticalLayout_125.setObjectName(u"verticalLayout_125")
        self.verticalLayout_125.setContentsMargins(0, 0, 0, 0)
        self.frame_162 = QFrame(self.frame_161)
        self.frame_162.setObjectName(u"frame_162")
        self.frame_162.setFrameShape(QFrame.StyledPanel)
        self.frame_162.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.frame_162)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.groupBox_32 = QGroupBox(self.frame_162)
        self.groupBox_32.setObjectName(u"groupBox_32")
        self.groupBox_32.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QComboBox{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QDateEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 900 12pt \"Roboto Black\";\n"
"}")
        self.horizontalLayout_60 = QHBoxLayout(self.groupBox_32)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.frame_163 = QFrame(self.groupBox_32)
        self.frame_163.setObjectName(u"frame_163")
        self.frame_163.setFrameShape(QFrame.NoFrame)
        self.frame_163.setFrameShadow(QFrame.Raised)
        self.label_461 = QLabel(self.frame_163)
        self.label_461.setObjectName(u"label_461")
        self.label_461.setGeometry(QRect(20, 250, 81, 31))
        self.lineEdit_105 = QLineEdit(self.frame_163)
        self.lineEdit_105.setObjectName(u"lineEdit_105")
        self.lineEdit_105.setGeometry(QRect(110, 150, 161, 31))
        self.lineEdit_105.setClearButtonEnabled(True)
        self.label_462 = QLabel(self.frame_163)
        self.label_462.setObjectName(u"label_462")
        self.label_462.setGeometry(QRect(0, 0, 101, 31))
        self.lineEdit_106 = QLineEdit(self.frame_163)
        self.lineEdit_106.setObjectName(u"lineEdit_106")
        self.lineEdit_106.setGeometry(QRect(100, 200, 171, 31))
        self.lineEdit_106.setClearButtonEnabled(True)
        self.label_463 = QLabel(self.frame_163)
        self.label_463.setObjectName(u"label_463")
        self.label_463.setGeometry(QRect(20, 200, 81, 31))
        self.label_464 = QLabel(self.frame_163)
        self.label_464.setObjectName(u"label_464")
        self.label_464.setGeometry(QRect(0, 150, 101, 31))
        self.label_465 = QLabel(self.frame_163)
        self.label_465.setObjectName(u"label_465")
        self.label_465.setGeometry(QRect(10, 100, 61, 31))
        self.comboBox_52 = QComboBox(self.frame_163)
        self.comboBox_52.addItem("")
        self.comboBox_52.addItem("")
        self.comboBox_52.addItem("")
        self.comboBox_52.setObjectName(u"comboBox_52")
        self.comboBox_52.setGeometry(QRect(100, 100, 171, 31))
        self.lineEdit_107 = QLineEdit(self.frame_163)
        self.lineEdit_107.setObjectName(u"lineEdit_107")
        self.lineEdit_107.setGeometry(QRect(100, 0, 171, 31))
        self.lineEdit_107.setClearButtonEnabled(True)
        self.label_466 = QLabel(self.frame_163)
        self.label_466.setObjectName(u"label_466")
        self.label_466.setGeometry(QRect(10, 50, 51, 31))
        self.comboBox_53 = QComboBox(self.frame_163)
        self.comboBox_53.addItem("")
        self.comboBox_53.addItem("")
        self.comboBox_53.addItem("")
        self.comboBox_53.addItem("")
        self.comboBox_53.addItem("")
        self.comboBox_53.addItem("")
        self.comboBox_53.addItem("")
        self.comboBox_53.addItem("")
        self.comboBox_53.addItem("")
        self.comboBox_53.setObjectName(u"comboBox_53")
        self.comboBox_53.setGeometry(QRect(100, 50, 171, 31))
        self.lineEdit_144 = QLineEdit(self.frame_163)
        self.lineEdit_144.setObjectName(u"lineEdit_144")
        self.lineEdit_144.setGeometry(QRect(100, 250, 171, 31))
        self.lineEdit_144.setClearButtonEnabled(True)

        self.horizontalLayout_60.addWidget(self.frame_163)

        self.frame_164 = QFrame(self.groupBox_32)
        self.frame_164.setObjectName(u"frame_164")
        self.frame_164.setMaximumSize(QSize(120, 500))
        self.frame_164.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(158, 158, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(255, 255, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_164.setFrameShape(QFrame.NoFrame)
        self.frame_164.setFrameShadow(QFrame.Raised)
        self.bt_97 = QPushButton(self.frame_164)
        self.bt_97.setObjectName(u"bt_97")
        self.bt_97.setGeometry(QRect(20, 170, 91, 30))
        self.bt_97.setMaximumSize(QSize(120, 30))
        self.bt_97.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_97.setIcon(icon20)
        self.bt_97.setIconSize(QSize(20, 20))
        self.bt_98 = QPushButton(self.frame_164)
        self.bt_98.setObjectName(u"bt_98")
        self.bt_98.setGeometry(QRect(20, 120, 89, 30))
        self.bt_98.setMaximumSize(QSize(120, 30))
        self.bt_98.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_98.setIcon(icon22)
        self.bt_98.setIconSize(QSize(20, 20))
        self.bt_99 = QPushButton(self.frame_164)
        self.bt_99.setObjectName(u"bt_99")
        self.bt_99.setGeometry(QRect(20, 70, 91, 30))
        self.bt_99.setMaximumSize(QSize(120, 30))
        self.bt_99.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_99.setIcon(icon17)
        self.bt_99.setIconSize(QSize(20, 20))
        self.bt_121 = QPushButton(self.frame_164)
        self.bt_121.setObjectName(u"bt_121")
        self.bt_121.setGeometry(QRect(20, 230, 91, 30))
        self.bt_121.setMaximumSize(QSize(120, 30))
        self.bt_121.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_121.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(158, 158, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(0, 170, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.bt_121.setIcon(icon21)
        self.bt_121.setIconSize(QSize(20, 20))

        self.horizontalLayout_60.addWidget(self.frame_164)


        self.horizontalLayout_59.addWidget(self.groupBox_32)

        self.groupBox_33 = QGroupBox(self.frame_162)
        self.groupBox_33.setObjectName(u"groupBox_33")
        self.groupBox_33.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QComboBox{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QDateEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 14pt \"Rockwell\";\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 900 12pt \"Roboto Black\";\n"
"}")
        self.verticalLayout_126 = QVBoxLayout(self.groupBox_33)
        self.verticalLayout_126.setSpacing(0)
        self.verticalLayout_126.setObjectName(u"verticalLayout_126")
        self.verticalLayout_126.setContentsMargins(0, 0, 0, 0)
        self.frame_165 = QFrame(self.groupBox_33)
        self.frame_165.setObjectName(u"frame_165")
        self.frame_165.setFrameShape(QFrame.StyledPanel)
        self.frame_165.setFrameShadow(QFrame.Raised)
        self.label_467 = QLabel(self.frame_165)
        self.label_467.setObjectName(u"label_467")
        self.label_467.setGeometry(QRect(40, 60, 51, 31))
        self.lineEdit_108 = QLineEdit(self.frame_165)
        self.lineEdit_108.setObjectName(u"lineEdit_108")
        self.lineEdit_108.setGeometry(QRect(130, 10, 171, 31))
        self.lineEdit_108.setClearButtonEnabled(True)
        self.label_468 = QLabel(self.frame_165)
        self.label_468.setObjectName(u"label_468")
        self.label_468.setGeometry(QRect(50, 190, 81, 31))
        self.lineEdit_109 = QLineEdit(self.frame_165)
        self.lineEdit_109.setObjectName(u"lineEdit_109")
        self.lineEdit_109.setGeometry(QRect(130, 140, 171, 31))
        self.lineEdit_109.setClearButtonEnabled(True)
        self.label_469 = QLabel(self.frame_165)
        self.label_469.setObjectName(u"label_469")
        self.label_469.setGeometry(QRect(20, 140, 111, 31))
        self.label_470 = QLabel(self.frame_165)
        self.label_470.setObjectName(u"label_470")
        self.label_470.setGeometry(QRect(30, 10, 101, 31))
        self.comboBox_54 = QComboBox(self.frame_165)
        self.comboBox_54.addItem("")
        self.comboBox_54.addItem("")
        self.comboBox_54.addItem("")
        self.comboBox_54.addItem("")
        self.comboBox_54.addItem("")
        self.comboBox_54.addItem("")
        self.comboBox_54.addItem("")
        self.comboBox_54.addItem("")
        self.comboBox_54.addItem("")
        self.comboBox_54.setObjectName(u"comboBox_54")
        self.comboBox_54.setGeometry(QRect(130, 60, 171, 31))
        self.lineEdit_145 = QLineEdit(self.frame_165)
        self.lineEdit_145.setObjectName(u"lineEdit_145")
        self.lineEdit_145.setGeometry(QRect(130, 190, 171, 31))
        self.lineEdit_145.setClearButtonEnabled(True)
        self.comboBox_48 = QComboBox(self.frame_165)
        self.comboBox_48.addItem("")
        self.comboBox_48.addItem("")
        self.comboBox_48.setObjectName(u"comboBox_48")
        self.comboBox_48.setGeometry(QRect(130, 100, 171, 31))
        self.label_136 = QLabel(self.frame_165)
        self.label_136.setObjectName(u"label_136")
        self.label_136.setGeometry(QRect(10, 100, 111, 31))
        self.bt_117 = QPushButton(self.frame_165)
        self.bt_117.setObjectName(u"bt_117")
        self.bt_117.setGeometry(QRect(350, 170, 80, 30))
        self.bt_117.setMaximumSize(QSize(120, 30))
        self.bt_117.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_117.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(158, 158, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(0, 170, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.bt_117.setIcon(icon24)
        self.bt_117.setIconSize(QSize(20, 20))
        self.bt_122 = QPushButton(self.frame_165)
        self.bt_122.setObjectName(u"bt_122")
        self.bt_122.setGeometry(QRect(340, 80, 91, 30))
        self.bt_122.setMaximumSize(QSize(120, 30))
        self.bt_122.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_122.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(158, 158, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(0, 170, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.bt_122.setIcon(icon21)
        self.bt_122.setIconSize(QSize(20, 20))

        self.verticalLayout_126.addWidget(self.frame_165)

        self.frame_166 = QFrame(self.groupBox_33)
        self.frame_166.setObjectName(u"frame_166")
        self.frame_166.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(158, 158, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(255, 255, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_166.setFrameShape(QFrame.StyledPanel)
        self.frame_166.setFrameShadow(QFrame.Raised)
        self.bt_100 = QPushButton(self.frame_166)
        self.bt_100.setObjectName(u"bt_100")
        self.bt_100.setGeometry(QRect(80, 20, 80, 30))
        self.bt_100.setMaximumSize(QSize(120, 30))
        self.bt_100.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_100.setIcon(icon17)
        self.bt_100.setIconSize(QSize(20, 20))
        self.bt_101 = QPushButton(self.frame_166)
        self.bt_101.setObjectName(u"bt_101")
        self.bt_101.setGeometry(QRect(180, 20, 89, 30))
        self.bt_101.setMaximumSize(QSize(120, 30))
        self.bt_101.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_101.setIcon(icon22)
        self.bt_101.setIconSize(QSize(20, 20))
        self.bt_102 = QPushButton(self.frame_166)
        self.bt_102.setObjectName(u"bt_102")
        self.bt_102.setGeometry(QRect(280, 20, 80, 30))
        self.bt_102.setMaximumSize(QSize(120, 30))
        self.bt_102.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_102.setIcon(icon20)
        self.bt_102.setIconSize(QSize(20, 20))

        self.verticalLayout_126.addWidget(self.frame_166)

        self.verticalLayout_126.setStretch(0, 8)
        self.verticalLayout_126.setStretch(1, 2)

        self.horizontalLayout_59.addWidget(self.groupBox_33)


        self.verticalLayout_125.addWidget(self.frame_162)

        self.frame_167 = QFrame(self.frame_161)
        self.frame_167.setObjectName(u"frame_167")
        self.frame_167.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(158, 158, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(255, 255, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_167.setFrameShape(QFrame.StyledPanel)
        self.frame_167.setFrameShadow(QFrame.Raised)
        self.verticalLayout_127 = QVBoxLayout(self.frame_167)
        self.verticalLayout_127.setSpacing(0)
        self.verticalLayout_127.setObjectName(u"verticalLayout_127")
        self.verticalLayout_127.setContentsMargins(0, 0, 0, 0)
        self.frame_168 = QFrame(self.frame_167)
        self.frame_168.setObjectName(u"frame_168")
        self.frame_168.setFrameShape(QFrame.StyledPanel)
        self.frame_168.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.frame_168)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.frame_169 = QFrame(self.frame_168)
        self.frame_169.setObjectName(u"frame_169")
        self.frame_169.setFrameShape(QFrame.StyledPanel)
        self.frame_169.setFrameShadow(QFrame.Raised)
        self.verticalLayout_128 = QVBoxLayout(self.frame_169)
        self.verticalLayout_128.setObjectName(u"verticalLayout_128")
        self.tableWidget_17 = QTableWidget(self.frame_169)
        if (self.tableWidget_17.columnCount() < 6):
            self.tableWidget_17.setColumnCount(6)
        __qtablewidgetitem115 = QTableWidgetItem()
        self.tableWidget_17.setHorizontalHeaderItem(0, __qtablewidgetitem115)
        __qtablewidgetitem116 = QTableWidgetItem()
        self.tableWidget_17.setHorizontalHeaderItem(1, __qtablewidgetitem116)
        __qtablewidgetitem117 = QTableWidgetItem()
        self.tableWidget_17.setHorizontalHeaderItem(2, __qtablewidgetitem117)
        __qtablewidgetitem118 = QTableWidgetItem()
        self.tableWidget_17.setHorizontalHeaderItem(3, __qtablewidgetitem118)
        __qtablewidgetitem119 = QTableWidgetItem()
        self.tableWidget_17.setHorizontalHeaderItem(4, __qtablewidgetitem119)
        __qtablewidgetitem120 = QTableWidgetItem()
        self.tableWidget_17.setHorizontalHeaderItem(5, __qtablewidgetitem120)
        self.tableWidget_17.setObjectName(u"tableWidget_17")
        self.tableWidget_17.setStyleSheet(u"background-color: rgb(191, 191, 191);")

        self.verticalLayout_128.addWidget(self.tableWidget_17)


        self.horizontalLayout_61.addWidget(self.frame_169)

        self.frame_170 = QFrame(self.frame_168)
        self.frame_170.setObjectName(u"frame_170")
        self.frame_170.setFrameShape(QFrame.StyledPanel)
        self.frame_170.setFrameShadow(QFrame.Raised)
        self.verticalLayout_129 = QVBoxLayout(self.frame_170)
        self.verticalLayout_129.setObjectName(u"verticalLayout_129")
        self.tableWidget_18 = QTableWidget(self.frame_170)
        if (self.tableWidget_18.columnCount() < 5):
            self.tableWidget_18.setColumnCount(5)
        __qtablewidgetitem121 = QTableWidgetItem()
        self.tableWidget_18.setHorizontalHeaderItem(0, __qtablewidgetitem121)
        __qtablewidgetitem122 = QTableWidgetItem()
        self.tableWidget_18.setHorizontalHeaderItem(1, __qtablewidgetitem122)
        __qtablewidgetitem123 = QTableWidgetItem()
        self.tableWidget_18.setHorizontalHeaderItem(2, __qtablewidgetitem123)
        __qtablewidgetitem124 = QTableWidgetItem()
        self.tableWidget_18.setHorizontalHeaderItem(3, __qtablewidgetitem124)
        __qtablewidgetitem125 = QTableWidgetItem()
        self.tableWidget_18.setHorizontalHeaderItem(4, __qtablewidgetitem125)
        self.tableWidget_18.setObjectName(u"tableWidget_18")
        self.tableWidget_18.setStyleSheet(u"background-color: rgb(191, 191, 191);")

        self.verticalLayout_129.addWidget(self.tableWidget_18)


        self.horizontalLayout_61.addWidget(self.frame_170)


        self.verticalLayout_127.addWidget(self.frame_168)

        self.pushButton_3 = QPushButton(self.frame_167)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(120, 30))
        self.pushButton_3.setMaximumSize(QSize(120, 60))
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setIcon(icon25)
        self.pushButton_3.setIconSize(QSize(20, 20))

        self.verticalLayout_127.addWidget(self.pushButton_3, 0, Qt.AlignHCenter)


        self.verticalLayout_125.addWidget(self.frame_167)

        self.verticalLayout_125.setStretch(0, 5)
        self.verticalLayout_125.setStretch(1, 5)

        self.verticalLayout_124.addWidget(self.frame_161)

        self.tabWidget_10.addTab(self.tab_40, "")
        self.tab_41 = QWidget()
        self.tab_41.setObjectName(u"tab_41")
        self.verticalLayout_130 = QVBoxLayout(self.tab_41)
        self.verticalLayout_130.setSpacing(0)
        self.verticalLayout_130.setObjectName(u"verticalLayout_130")
        self.verticalLayout_130.setContentsMargins(0, 0, 0, 0)
        self.frame_171 = QFrame(self.tab_41)
        self.frame_171.setObjectName(u"frame_171")
        self.frame_171.setStyleSheet(u"\n"
"QPlainTextEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}")
        self.frame_171.setFrameShape(QFrame.StyledPanel)
        self.frame_171.setFrameShadow(QFrame.Raised)
        self.verticalLayout_131 = QVBoxLayout(self.frame_171)
        self.verticalLayout_131.setObjectName(u"verticalLayout_131")
        self.frame_172 = QFrame(self.frame_171)
        self.frame_172.setObjectName(u"frame_172")
        self.frame_172.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 900 12pt \"Roboto Black\";\n"
"}")
        self.frame_172.setFrameShape(QFrame.StyledPanel)
        self.frame_172.setFrameShadow(QFrame.Raised)
        self.lineEdit_110 = QLineEdit(self.frame_172)
        self.lineEdit_110.setObjectName(u"lineEdit_110")
        self.lineEdit_110.setGeometry(QRect(170, 10, 181, 31))
        self.label_471 = QLabel(self.frame_172)
        self.label_471.setObjectName(u"label_471")
        self.label_471.setGeometry(QRect(30, 20, 141, 16))
        self.label_472 = QLabel(self.frame_172)
        self.label_472.setObjectName(u"label_472")
        self.label_472.setGeometry(QRect(600, 20, 31, 16))
        self.lineEdit_111 = QLineEdit(self.frame_172)
        self.lineEdit_111.setObjectName(u"lineEdit_111")
        self.lineEdit_111.setGeometry(QRect(640, 10, 181, 31))

        self.verticalLayout_131.addWidget(self.frame_172)

        self.plainTextEdit_3 = QPlainTextEdit(self.frame_171)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")

        self.verticalLayout_131.addWidget(self.plainTextEdit_3)

        self.verticalLayout_131.setStretch(0, 1)
        self.verticalLayout_131.setStretch(1, 8)

        self.verticalLayout_130.addWidget(self.frame_171)

        self.frame_173 = QFrame(self.tab_41)
        self.frame_173.setObjectName(u"frame_173")
        self.frame_173.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 107, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(0, 170, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_173.setFrameShape(QFrame.StyledPanel)
        self.frame_173.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.frame_173)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.frame_174 = QFrame(self.frame_173)
        self.frame_174.setObjectName(u"frame_174")
        self.frame_174.setMinimumSize(QSize(300, 100))
        self.frame_174.setMaximumSize(QSize(300, 100))
        self.frame_174.setFrameShape(QFrame.StyledPanel)
        self.frame_174.setFrameShadow(QFrame.Raised)
        self.verticalLayout_132 = QVBoxLayout(self.frame_174)
        self.verticalLayout_132.setObjectName(u"verticalLayout_132")
        self.bt_103 = QPushButton(self.frame_174)
        self.bt_103.setObjectName(u"bt_103")
        self.bt_103.setMinimumSize(QSize(120, 30))
        self.bt_103.setMaximumSize(QSize(120, 40))

        self.verticalLayout_132.addWidget(self.bt_103)


        self.horizontalLayout_62.addWidget(self.frame_174, 0, Qt.AlignHCenter)


        self.verticalLayout_130.addWidget(self.frame_173)

        self.verticalLayout_130.setStretch(0, 8)
        self.verticalLayout_130.setStretch(1, 2)
        self.tabWidget_10.addTab(self.tab_41, "")
        self.tab_55 = QWidget()
        self.tab_55.setObjectName(u"tab_55")
        self.verticalLayout_159 = QVBoxLayout(self.tab_55)
        self.verticalLayout_159.setObjectName(u"verticalLayout_159")
        self.frame_201 = QFrame(self.tab_55)
        self.frame_201.setObjectName(u"frame_201")
        self.frame_201.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"	font: 9pt \"Rockwell\";\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 900 12pt \"Roboto Black\";\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(158, 158, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(170, 170, 0);\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_201.setFrameShape(QFrame.StyledPanel)
        self.frame_201.setFrameShadow(QFrame.Raised)
        self.lineEdit_30 = QLineEdit(self.frame_201)
        self.lineEdit_30.setObjectName(u"lineEdit_30")
        self.lineEdit_30.setGeometry(QRect(220, 260, 181, 51))
        self.label_169 = QLabel(self.frame_201)
        self.label_169.setObjectName(u"label_169")
        self.label_169.setGeometry(QRect(100, 280, 111, 20))
        self.label_170 = QLabel(self.frame_201)
        self.label_170.setObjectName(u"label_170")
        self.label_170.setGeometry(QRect(130, 350, 91, 20))
        self.lineEdit_39 = QLineEdit(self.frame_201)
        self.lineEdit_39.setObjectName(u"lineEdit_39")
        self.lineEdit_39.setGeometry(QRect(220, 330, 181, 51))
        self.comboBox_50 = QComboBox(self.frame_201)
        self.comboBox_50.addItem("")
        self.comboBox_50.addItem("")
        self.comboBox_50.addItem("")
        self.comboBox_50.setObjectName(u"comboBox_50")
        self.comboBox_50.setGeometry(QRect(230, 190, 171, 41))
        self.comboBox_50.setCursor(QCursor(Qt.OpenHandCursor))
        self.label_171 = QLabel(self.frame_201)
        self.label_171.setObjectName(u"label_171")
        self.label_171.setGeometry(QRect(100, 200, 121, 20))
        self.line_74 = QFrame(self.frame_201)
        self.line_74.setObjectName(u"line_74")
        self.line_74.setGeometry(QRect(450, 0, 20, 661))
        self.line_74.setFrameShape(QFrame.VLine)
        self.line_74.setFrameShadow(QFrame.Sunken)
        self.label_172 = QLabel(self.frame_201)
        self.label_172.setObjectName(u"label_172")
        self.label_172.setGeometry(QRect(490, 40, 121, 31))
        self.label_173 = QLabel(self.frame_201)
        self.label_173.setObjectName(u"label_173")
        self.label_173.setGeometry(QRect(640, 40, 211, 31))
        self.label_173.setStyleSheet(u"color: rgb(135, 68, 0);\n"
"background-color: rgb(185, 185, 185);\n"
"font: 900 12pt \"Roboto\";")
        self.label_173.setAlignment(Qt.AlignCenter)
        self.label_174 = QLabel(self.frame_201)
        self.label_174.setObjectName(u"label_174")
        self.label_174.setGeometry(QRect(640, 80, 211, 31))
        self.label_174.setStyleSheet(u"color: rgb(135, 68, 0);\n"
"background-color: rgb(185, 185, 185);\n"
"font: 900 12pt \"Roboto\";")
        self.label_174.setAlignment(Qt.AlignCenter)
        self.label_175 = QLabel(self.frame_201)
        self.label_175.setObjectName(u"label_175")
        self.label_175.setGeometry(QRect(490, 80, 121, 31))
        self.line_75 = QFrame(self.frame_201)
        self.line_75.setObjectName(u"line_75")
        self.line_75.setGeometry(QRect(457, 133, 411, 20))
        self.line_75.setFrameShape(QFrame.HLine)
        self.line_75.setFrameShadow(QFrame.Sunken)
        self.line_76 = QFrame(self.frame_201)
        self.line_76.setObjectName(u"line_76")
        self.line_76.setGeometry(QRect(680, 300, 21, 171))
        self.line_76.setFrameShape(QFrame.VLine)
        self.line_76.setFrameShadow(QFrame.Sunken)
        self.line_77 = QFrame(self.frame_201)
        self.line_77.setObjectName(u"line_77")
        self.line_77.setGeometry(QRect(457, 470, 401, 20))
        self.line_77.setFrameShape(QFrame.HLine)
        self.line_77.setFrameShadow(QFrame.Sunken)
        self.line_78 = QFrame(self.frame_201)
        self.line_78.setObjectName(u"line_78")
        self.line_78.setGeometry(QRect(553, 490, 20, 171))
        self.line_78.setFrameShape(QFrame.VLine)
        self.line_78.setFrameShadow(QFrame.Sunken)
        self.line_79 = QFrame(self.frame_201)
        self.line_79.setObjectName(u"line_79")
        self.line_79.setGeometry(QRect(560, 616, 301, 16))
        self.line_79.setFrameShape(QFrame.HLine)
        self.line_79.setFrameShadow(QFrame.Sunken)
        self.label_176 = QLabel(self.frame_201)
        self.label_176.setObjectName(u"label_176")
        self.label_176.setGeometry(QRect(490, 290, 161, 31))
        self.label_177 = QLabel(self.frame_201)
        self.label_177.setObjectName(u"label_177")
        self.label_177.setGeometry(QRect(490, 340, 161, 31))
        self.label_178 = QLabel(self.frame_201)
        self.label_178.setObjectName(u"label_178")
        self.label_178.setGeometry(QRect(490, 390, 161, 31))
        self.label_179 = QLabel(self.frame_201)
        self.label_179.setObjectName(u"label_179")
        self.label_179.setGeometry(QRect(490, 430, 161, 31))
        self.label_180 = QLabel(self.frame_201)
        self.label_180.setObjectName(u"label_180")
        self.label_180.setGeometry(QRect(490, 580, 51, 31))
        self.label_181 = QLabel(self.frame_201)
        self.label_181.setObjectName(u"label_181")
        self.label_181.setGeometry(QRect(580, 630, 91, 31))
        self.label_182 = QLabel(self.frame_201)
        self.label_182.setObjectName(u"label_182")
        self.label_182.setGeometry(QRect(570, 540, 111, 31))
        self.label_183 = QLabel(self.frame_201)
        self.label_183.setObjectName(u"label_183")
        self.label_183.setGeometry(QRect(570, 590, 101, 31))
        self.label_184 = QLabel(self.frame_201)
        self.label_184.setObjectName(u"label_184")
        self.label_184.setGeometry(QRect(570, 490, 101, 31))
        self.label_185 = QLabel(self.frame_201)
        self.label_185.setObjectName(u"label_185")
        self.label_185.setGeometry(QRect(720, 290, 161, 31))
        self.label_185.setStyleSheet(u"color: rgb(229, 153, 0);")
        self.label_185.setAlignment(Qt.AlignCenter)
        self.label_186 = QLabel(self.frame_201)
        self.label_186.setObjectName(u"label_186")
        self.label_186.setGeometry(QRect(720, 340, 161, 31))
        self.label_186.setStyleSheet(u"color: rgb(229, 153, 0);")
        self.label_186.setAlignment(Qt.AlignCenter)
        self.label_187 = QLabel(self.frame_201)
        self.label_187.setObjectName(u"label_187")
        self.label_187.setGeometry(QRect(720, 390, 161, 31))
        self.label_187.setStyleSheet(u"color: rgb(229, 153, 0);")
        self.label_187.setAlignment(Qt.AlignCenter)
        self.label_188 = QLabel(self.frame_201)
        self.label_188.setObjectName(u"label_188")
        self.label_188.setGeometry(QRect(700, 440, 201, 31))
        self.label_188.setStyleSheet(u"color: rgb(166, 166, 166);\n"
"background-color: rgb(170, 0, 0);\n"
"font: 900 12pt \"Roboto\";")
        self.label_188.setAlignment(Qt.AlignCenter)
        self.label_189 = QLabel(self.frame_201)
        self.label_189.setObjectName(u"label_189")
        self.label_189.setGeometry(QRect(690, 490, 211, 31))
        self.label_189.setStyleSheet(u"color: rgb(0, 170, 0);\n"
"font: 900 12pt \"Roboto\";")
        self.label_189.setAlignment(Qt.AlignCenter)
        self.label_190 = QLabel(self.frame_201)
        self.label_190.setObjectName(u"label_190")
        self.label_190.setGeometry(QRect(690, 540, 211, 31))
        self.label_190.setStyleSheet(u"color: rgb(0, 170, 0);\n"
"font: 900 12pt \"Roboto\";")
        self.label_190.setAlignment(Qt.AlignCenter)
        self.label_191 = QLabel(self.frame_201)
        self.label_191.setObjectName(u"label_191")
        self.label_191.setGeometry(QRect(690, 590, 211, 31))
        self.label_191.setStyleSheet(u"color: rgb(0, 170, 0);\n"
"font: 900 12pt \"Roboto\";")
        self.label_191.setAlignment(Qt.AlignCenter)
        self.label_192 = QLabel(self.frame_201)
        self.label_192.setObjectName(u"label_192")
        self.label_192.setGeometry(QRect(680, 630, 211, 31))
        self.label_192.setStyleSheet(u"background-color: rgb(156, 78, 0);\n"
"color: rgb(188, 188, 188);\n"
"font: 900 12pt \"Roboto\";")
        self.label_192.setAlignment(Qt.AlignCenter)
        self.line_80 = QFrame(self.frame_201)
        self.line_80.setObjectName(u"line_80")
        self.line_80.setGeometry(QRect(460, 420, 441, 16))
        self.line_80.setFrameShape(QFrame.HLine)
        self.line_80.setFrameShadow(QFrame.Sunken)
        self.line_81 = QFrame(self.frame_201)
        self.line_81.setObjectName(u"line_81")
        self.line_81.setGeometry(QRect(460, 370, 441, 16))
        self.line_81.setFrameShape(QFrame.HLine)
        self.line_81.setFrameShadow(QFrame.Sunken)
        self.line_82 = QFrame(self.frame_201)
        self.line_82.setObjectName(u"line_82")
        self.line_82.setGeometry(QRect(460, 320, 441, 16))
        self.line_82.setFrameShape(QFrame.HLine)
        self.line_82.setFrameShadow(QFrame.Sunken)
        self.label_193 = QLabel(self.frame_201)
        self.label_193.setObjectName(u"label_193")
        self.label_193.setGeometry(QRect(110, 20, 201, 61))
        self.label_193.setAlignment(Qt.AlignCenter)
        self.pushButton_26 = QPushButton(self.frame_201)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setGeometry(QRect(20, 470, 191, 61))
        self.pushButton_26.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_27 = QPushButton(self.frame_201)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setGeometry(QRect(240, 470, 191, 61))
        self.pushButton_27.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_28 = QPushButton(self.frame_201)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setGeometry(QRect(150, 560, 191, 61))
        self.pushButton_28.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_159.addWidget(self.frame_201)

        self.tabWidget_10.addTab(self.tab_55, "")

        self.verticalLayout_99.addWidget(self.tabWidget_10)


        self.horizontalLayout_44.addWidget(self.frame_123)

        self.horizontalLayout_44.setStretch(0, 2)
        self.horizontalLayout_44.setStretch(1, 8)

        self.horizontalLayout_43.addWidget(self.frame_120)

        self.tabWidget_9.addTab(self.tab_31, "")

        self.verticalLayout_93.addWidget(self.tabWidget_9)


        self.verticalLayout_133.addWidget(self.frame_117)

        self.tabWidget.addTab(self.tab_29, "")
        self.tab_42 = QWidget()
        self.tab_42.setObjectName(u"tab_42")
        self.verticalLayout_134 = QVBoxLayout(self.tab_42)
        self.verticalLayout_134.setSpacing(0)
        self.verticalLayout_134.setObjectName(u"verticalLayout_134")
        self.verticalLayout_134.setContentsMargins(0, 0, 0, 0)
        self.frame_176 = QFrame(self.tab_42)
        self.frame_176.setObjectName(u"frame_176")
        self.frame_176.setStyleSheet(u"background-color: rgb(108, 170, 144);")
        self.frame_176.setFrameShape(QFrame.StyledPanel)
        self.frame_176.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.frame_176)
        self.horizontalLayout_63.setSpacing(0)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.frame_175 = QFrame(self.frame_176)
        self.frame_175.setObjectName(u"frame_175")
        self.frame_175.setFrameShape(QFrame.StyledPanel)
        self.frame_175.setFrameShadow(QFrame.Raised)
        self.verticalLayout_135 = QVBoxLayout(self.frame_175)
        self.verticalLayout_135.setObjectName(u"verticalLayout_135")
        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_135.addItem(self.verticalSpacer_8)

        self.frame_178 = QFrame(self.frame_175)
        self.frame_178.setObjectName(u"frame_178")
        self.frame_178.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(163, 82, 0);\n"
"}\n"
"QPushButton {\n"
"	background-color: Transparent;\n"
"	border-top-left-radius: 15px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"	color: rgb(0, 140, 140);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.329, y2:1, stop:0 rgba(81, 127, 107, 255), stop:1 rgba(204, 204, 204, 248));\n"
"	border-bottom-left-radius: 8px;\n"
"	color: #dfe6ed;\n"
"}\n"
"")
        self.frame_178.setFrameShape(QFrame.StyledPanel)
        self.frame_178.setFrameShadow(QFrame.Raised)
        self.label_473 = QLabel(self.frame_178)
        self.label_473.setObjectName(u"label_473")
        self.label_473.setGeometry(QRect(40, 20, 191, 131))
        self.label_473.setPixmap(QPixmap(u"assets/imgs/myLogo.jpg"))
        self.label_473.setScaledContents(True)
        self.label_474 = QLabel(self.frame_178)
        self.label_474.setObjectName(u"label_474")
        self.label_474.setGeometry(QRect(100, 170, 71, 21))
        self.label_474.setStyleSheet(u"font: 700 11pt \"Roboto\";")
        self.label_475 = QLabel(self.frame_178)
        self.label_475.setObjectName(u"label_475")
        self.label_475.setGeometry(QRect(40, 190, 191, 21))
        self.label_475.setStyleSheet(u"font: 700 11pt \"Roboto\";")
        self.label_475.setAlignment(Qt.AlignCenter)
        self.label_476 = QLabel(self.frame_178)
        self.label_476.setObjectName(u"label_476")
        self.label_476.setGeometry(QRect(40, 220, 191, 21))
        self.label_476.setStyleSheet(u"font: 700 11pt \"Roboto\";")
        self.label_476.setAlignment(Qt.AlignCenter)
        self.label_477 = QLabel(self.frame_178)
        self.label_477.setObjectName(u"label_477")
        self.label_477.setGeometry(QRect(40, 250, 201, 21))
        self.label_477.setStyleSheet(u"font: 700 11pt \"Roboto\";")
        self.label_477.setAlignment(Qt.AlignCenter)
        self.label_478 = QLabel(self.frame_178)
        self.label_478.setObjectName(u"label_478")
        self.label_478.setGeometry(QRect(30, 280, 221, 21))
        self.label_478.setStyleSheet(u"font: 700 11pt \"Roboto\";")
        self.label_478.setAlignment(Qt.AlignCenter)
        self.bt_104 = QPushButton(self.frame_178)
        self.bt_104.setObjectName(u"bt_104")
        self.bt_104.setGeometry(QRect(90, 330, 91, 31))
        self.bt_104.setCursor(QCursor(Qt.PointingHandCursor))
        icon26 = QIcon()
        icon26.addFile(u":/icons/assets/buttons/play-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_104.setIcon(icon26)
        self.bt_104.setIconSize(QSize(28, 28))
        self.pushButton_13 = QPushButton(self.frame_178)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(94, 373, 81, 31))
        self.pushButton_13.setIcon(icon16)
        self.pushButton_13.setIconSize(QSize(28, 28))

        self.verticalLayout_135.addWidget(self.frame_178)

        self.verticalSpacer_7 = QSpacerItem(20, 219, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_135.addItem(self.verticalSpacer_7)

        self.verticalLayout_135.setStretch(1, 6)
        self.verticalLayout_135.setStretch(2, 3)

        self.horizontalLayout_63.addWidget(self.frame_175)

        self.frame_177 = QFrame(self.frame_176)
        self.frame_177.setObjectName(u"frame_177")
        self.frame_177.setStyleSheet(u"QPlainTextEdit{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border-radius: 15px;\n"
"}")
        self.frame_177.setFrameShape(QFrame.StyledPanel)
        self.frame_177.setFrameShadow(QFrame.Raised)
        self.verticalLayout_136 = QVBoxLayout(self.frame_177)
        self.verticalLayout_136.setObjectName(u"verticalLayout_136")
        self.plainTextEdit_4 = QPlainTextEdit(self.frame_177)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")

        self.verticalLayout_136.addWidget(self.plainTextEdit_4)


        self.horizontalLayout_63.addWidget(self.frame_177)

        self.horizontalLayout_63.setStretch(0, 3)
        self.horizontalLayout_63.setStretch(1, 8)

        self.verticalLayout_134.addWidget(self.frame_176)

        self.tabWidget.addTab(self.tab_42, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(4)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(1)
        self.tabWidget_4.setCurrentIndex(4)
        self.tabWidget_5.setCurrentIndex(4)
        self.tabWidget_6.setCurrentIndex(1)
        self.tabWidget_7.setCurrentIndex(2)
        self.tabWidget_8.setCurrentIndex(3)
        self.tabWidget_9.setCurrentIndex(1)
        self.tabWidget_10.setCurrentIndex(2)
        self.tabWidget_11.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Schools Management System", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"WELCOME", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Please Login to gain access", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"USER NAME", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"PASSWORD", None))
        self.bt_createAccount.setText(QCoreApplication.translate("MainWindow", u"Not Registed/Create New Account", None))
        self.bt_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_16.setText("")
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.login), QCoreApplication.translate("MainWindow", u"login", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"PLEASE FILL IN THE FROM", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"USER NAME", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"PASSWORD", None))
        self.bt_back_2.setText(QCoreApplication.translate("MainWindow", u"Already Have An Account/login", None))
        self.bt_signup.setText(QCoreApplication.translate("MainWindow", u"SignUp", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"FULL NAME", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"COMFIRM PASSWORD", None))
        self.label_22.setText("")
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.signup), QCoreApplication.translate("MainWindow", u"signup", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"login/signup", None))
        self.label_5.setText("")
        self.bt.setText(QCoreApplication.translate("MainWindow", u"GES", None))
        self.bt_1.setText(QCoreApplication.translate("MainWindow", u"CAMBRIDGE", None))
        self.bt_2.setText(QCoreApplication.translate("MainWindow", u"MONTESSORI", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"selection", None))
        self.label_4.setText("")
        self.bt_3.setText(QCoreApplication.translate("MainWindow", u"STUDENTS", None))
        self.bt_4.setText(QCoreApplication.translate("MainWindow", u"ADMIN/TEACHERS", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Student/Admin Selection", None))
        self.label_45.setText("")
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"WELCOME TO SCHOOL MANAGEMENT SYSTEM", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"PLEASE CLICK ", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"THE BUTTON BELOW TO GET STARTED", None))
        self.bt_113.setText(QCoreApplication.translate("MainWindow", u"Get Started", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_52), QCoreApplication.translate("MainWindow", u"Welcome", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Student Management System For GES Schools", None))
        self.label_2.setText("")
        self.bt_5.setText(QCoreApplication.translate("MainWindow", u"Get Started", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Welcome", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Total Number Of Students :", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"..", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Total School Fees :", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"..", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Total Feeding Fees :", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"..", None))
        self.bt_6.setText(QCoreApplication.translate("MainWindow", u"Add New Students", None))
        self.bt_7.setText(QCoreApplication.translate("MainWindow", u"Update Students", None))
        self.bt_8.setText(QCoreApplication.translate("MainWindow", u"Sudents Marks", None))
        self.bt_12.setText(QCoreApplication.translate("MainWindow", u"Attendances", None))
        self.bt_9.setText(QCoreApplication.translate("MainWindow", u"Students Reports", None))
        self.bt_11.setText(QCoreApplication.translate("MainWindow", u"Students Fees", None))
        self.bt_10.setText(QCoreApplication.translate("MainWindow", u"Send Email", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"Expenses", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Student's Details", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Registration Number :", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Date Of Birth :", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Class :", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Crache", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Nursery 1", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Nursery 2", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Kindergaten 1", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Kindergaten 2", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Class 1", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Class 2", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Class 3", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Class 4", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Class 5", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"Class 6", None))
        self.comboBox.setItemText(11, QCoreApplication.translate("MainWindow", u"JHS 1", None))
        self.comboBox.setItemText(12, QCoreApplication.translate("MainWindow", u"JHS 2", None))
        self.comboBox.setItemText(13, QCoreApplication.translate("MainWindow", u"JHS 3", None))

        self.comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"class .....", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Male", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Female", None))

        self.comboBox_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"gender.....", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Gender :", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Home Address :", None))
        self.textEdit.setPlaceholderText("")
        self.lineEdit_20.setPlaceholderText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Full Name :", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Parent's Details", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Phone Number :", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Parent Full Name :", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Email Address :", None))
        self.bt_13.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.bt_14.setText(QCoreApplication.translate("MainWindow", u"View", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Reg_No:-", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Full Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Date Of Birth", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Class", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Gender", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Home Address", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Parent Full Name", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Email Address", None));
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Add_student", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Student's Details", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Registration Number :", None))
        self.lineEdit_7.setInputMask("")
        self.lineEdit_7.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Full Name :", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Date Of Birth :", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Class :", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"Male", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"Female", None))

        self.comboBox_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"gender...", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Gender :", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Home Address :", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Crache", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Nursery 1", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Nursery 2", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"Kindergaten 1", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("MainWindow", u"Kindergaten 2", None))
        self.comboBox_3.setItemText(5, QCoreApplication.translate("MainWindow", u"Class 1", None))
        self.comboBox_3.setItemText(6, QCoreApplication.translate("MainWindow", u"Class 2", None))
        self.comboBox_3.setItemText(7, QCoreApplication.translate("MainWindow", u"Class 3", None))
        self.comboBox_3.setItemText(8, QCoreApplication.translate("MainWindow", u"Class 4", None))
        self.comboBox_3.setItemText(9, QCoreApplication.translate("MainWindow", u"Class 5", None))
        self.comboBox_3.setItemText(10, QCoreApplication.translate("MainWindow", u"Class 6", None))
        self.comboBox_3.setItemText(11, QCoreApplication.translate("MainWindow", u"JHS 1", None))
        self.comboBox_3.setItemText(12, QCoreApplication.translate("MainWindow", u"JHS 2", None))
        self.comboBox_3.setItemText(13, QCoreApplication.translate("MainWindow", u"JHS 3", None))

        self.comboBox_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"class .....", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Parent's Details", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Phone Number :", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Parent Full Name :", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Email Address :", None))
        self.bt_15.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.bt_17.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.bt_16.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.bt_29.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Reg_No:-", None));
        ___qtablewidgetitem10 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Full Name", None));
        ___qtablewidgetitem11 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Date Of Birth", None));
        ___qtablewidgetitem12 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Class", None));
        ___qtablewidgetitem13 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Gender", None));
        ___qtablewidgetitem14 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Home Address", None));
        ___qtablewidgetitem15 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Parent Full Name", None));
        ___qtablewidgetitem16 = self.tableWidget_2.horizontalHeaderItem(7)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None));
        ___qtablewidgetitem17 = self.tableWidget_2.horizontalHeaderItem(8)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Email Address", None));
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Update_student", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Student Marks", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Full Name :", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Class :", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"Crache", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("MainWindow", u"Nursery 1", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("MainWindow", u"Nursery 2", None))
        self.comboBox_5.setItemText(3, QCoreApplication.translate("MainWindow", u"Kindergaten 1", None))
        self.comboBox_5.setItemText(4, QCoreApplication.translate("MainWindow", u"Kindergaten 2", None))
        self.comboBox_5.setItemText(5, QCoreApplication.translate("MainWindow", u"Class 1", None))
        self.comboBox_5.setItemText(6, QCoreApplication.translate("MainWindow", u"Class 2", None))
        self.comboBox_5.setItemText(7, QCoreApplication.translate("MainWindow", u"Class 3", None))
        self.comboBox_5.setItemText(8, QCoreApplication.translate("MainWindow", u"Class 4", None))
        self.comboBox_5.setItemText(9, QCoreApplication.translate("MainWindow", u"Class 5", None))
        self.comboBox_5.setItemText(10, QCoreApplication.translate("MainWindow", u"Class 6", None))
        self.comboBox_5.setItemText(11, QCoreApplication.translate("MainWindow", u"JHS 1", None))
        self.comboBox_5.setItemText(12, QCoreApplication.translate("MainWindow", u"JHS 2", None))
        self.comboBox_5.setItemText(13, QCoreApplication.translate("MainWindow", u"JHS 3", None))

        self.comboBox_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"class .....", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Registration Number :", None))
        self.comboBox_6.setItemText(0, QCoreApplication.translate("MainWindow", u"English Language", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("MainWindow", u"Mathematics", None))
        self.comboBox_6.setItemText(2, QCoreApplication.translate("MainWindow", u"Intergrated Science", None))
        self.comboBox_6.setItemText(3, QCoreApplication.translate("MainWindow", u"Computing", None))
        self.comboBox_6.setItemText(4, QCoreApplication.translate("MainWindow", u"Social Studies", None))
        self.comboBox_6.setItemText(5, QCoreApplication.translate("MainWindow", u"History", None))
        self.comboBox_6.setItemText(6, QCoreApplication.translate("MainWindow", u"Creative Arts", None))
        self.comboBox_6.setItemText(7, QCoreApplication.translate("MainWindow", u"French", None))
        self.comboBox_6.setItemText(8, QCoreApplication.translate("MainWindow", u"Ghanaian Language", None))
        self.comboBox_6.setItemText(9, QCoreApplication.translate("MainWindow", u"Basic Design and Tech.", None))
        self.comboBox_6.setItemText(10, QCoreApplication.translate("MainWindow", u"Our World Our People", None))
        self.comboBox_6.setItemText(11, QCoreApplication.translate("MainWindow", u"Religious and Moral Education", None))
        self.comboBox_6.setItemText(12, QCoreApplication.translate("MainWindow", u"Language and Oral Literacy Skills", None))
        self.comboBox_6.setItemText(13, QCoreApplication.translate("MainWindow", u"Pre-Reading Skills", None))
        self.comboBox_6.setItemText(14, QCoreApplication.translate("MainWindow", u"Pre-Writing", None))
        self.comboBox_6.setItemText(15, QCoreApplication.translate("MainWindow", u"Numeracy", None))
        self.comboBox_6.setItemText(16, QCoreApplication.translate("MainWindow", u"Health and Environment Studies", None))
        self.comboBox_6.setItemText(17, QCoreApplication.translate("MainWindow", u"Psychosocial Skills", None))
        self.comboBox_6.setItemText(18, QCoreApplication.translate("MainWindow", u"Creative Skills", None))

        self.comboBox_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"subject...", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Subjects :", None))
        self.comboBox_7.setItemText(0, QCoreApplication.translate("MainWindow", u"Term 1", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("MainWindow", u"Term 2", None))
        self.comboBox_7.setItemText(2, QCoreApplication.translate("MainWindow", u"Term 3", None))

        self.comboBox_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"term ...", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Term :", None))
        self.comboBox_8.setItemText(0, QCoreApplication.translate("MainWindow", u"Exams", None))
        self.comboBox_8.setItemText(1, QCoreApplication.translate("MainWindow", u"Class Work", None))
        self.comboBox_8.setItemText(2, QCoreApplication.translate("MainWindow", u"Projects", None))

        self.comboBox_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"type...", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Marks Type :", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Grade :", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Marks :", None))
        self.comboBox_28.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_28.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_28.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_28.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_28.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_28.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_28.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_28.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_28.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))

        self.comboBox_28.setPlaceholderText(QCoreApplication.translate("MainWindow", u"type...", None))
        self.bt_18.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.bt_19.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.bt_20.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.bt_21.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.bt_30.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.lineEdit_16.setPlaceholderText(QCoreApplication.translate("MainWindow", u"search by name", None))
        ___qtablewidgetitem18 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Reg_No:-", None));
        ___qtablewidgetitem19 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Full Name", None));
        ___qtablewidgetitem20 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Class", None));
        ___qtablewidgetitem21 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Subjects", None));
        ___qtablewidgetitem22 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Term", None));
        ___qtablewidgetitem23 = self.tableWidget_3.horizontalHeaderItem(5)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Marks Type", None));
        ___qtablewidgetitem24 = self.tableWidget_3.horizontalHeaderItem(6)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem25 = self.tableWidget_3.horizontalHeaderItem(7)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Grade", None));
        ___qtablewidgetitem26 = self.tableWidget_3.horizontalHeaderItem(8)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Marks", None));
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"Student Marks", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Attendance", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Registration Number :", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Full Name :", None))
        self.comboBox_9.setItemText(0, QCoreApplication.translate("MainWindow", u"Crache", None))
        self.comboBox_9.setItemText(1, QCoreApplication.translate("MainWindow", u"Nursery 1", None))
        self.comboBox_9.setItemText(2, QCoreApplication.translate("MainWindow", u"Nursery 2", None))
        self.comboBox_9.setItemText(3, QCoreApplication.translate("MainWindow", u"Kindergaten 1", None))
        self.comboBox_9.setItemText(4, QCoreApplication.translate("MainWindow", u"Kindergaten 2", None))
        self.comboBox_9.setItemText(5, QCoreApplication.translate("MainWindow", u"Class 1", None))
        self.comboBox_9.setItemText(6, QCoreApplication.translate("MainWindow", u"Class 2", None))
        self.comboBox_9.setItemText(7, QCoreApplication.translate("MainWindow", u"Class 3", None))
        self.comboBox_9.setItemText(8, QCoreApplication.translate("MainWindow", u"Class 4", None))
        self.comboBox_9.setItemText(9, QCoreApplication.translate("MainWindow", u"Class 5", None))
        self.comboBox_9.setItemText(10, QCoreApplication.translate("MainWindow", u"Class 6", None))
        self.comboBox_9.setItemText(11, QCoreApplication.translate("MainWindow", u"JHS 1", None))
        self.comboBox_9.setItemText(12, QCoreApplication.translate("MainWindow", u"JHS 2", None))
        self.comboBox_9.setItemText(13, QCoreApplication.translate("MainWindow", u"JHS 3", None))

        self.comboBox_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"class .....", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Class :", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.bt_22.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.bt_24.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.bt_25.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.bt_23.setText(QCoreApplication.translate("MainWindow", u"View", None))
        ___qtablewidgetitem27 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Reg_No:-", None));
        ___qtablewidgetitem28 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Full Name", None));
        ___qtablewidgetitem29 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Class", None));
        ___qtablewidgetitem30 = self.tableWidget_4.horizontalHeaderItem(3)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"Attendance", None))
        self.bt_26.setText(QCoreApplication.translate("MainWindow", u"Crache/Nursery", None))
        self.bt_27.setText(QCoreApplication.translate("MainWindow", u"Kg/Primary", None))
        self.bt_28.setText(QCoreApplication.translate("MainWindow", u"JHS", None))
        self.groupBox_38.setTitle(QCoreApplication.translate("MainWindow", u"crache", None))
        self.label_258.setText(QCoreApplication.translate("MainWindow", u"Full Name :", None))
        self.comboBox_68.setItemText(0, QCoreApplication.translate("MainWindow", u"Term 1", None))
        self.comboBox_68.setItemText(1, QCoreApplication.translate("MainWindow", u"Term 2", None))
        self.comboBox_68.setItemText(2, QCoreApplication.translate("MainWindow", u"Term 3", None))

        self.comboBox_68.setPlaceholderText(QCoreApplication.translate("MainWindow", u"term ...", None))
        self.label_259.setText(QCoreApplication.translate("MainWindow", u"Term :", None))
        self.label_260.setText(QCoreApplication.translate("MainWindow", u"Class :", None))
        self.label_261.setText(QCoreApplication.translate("MainWindow", u"School Name :", None))
        self.label_262.setText(QCoreApplication.translate("MainWindow", u"School Address :", None))
        self.label_263.setText(QCoreApplication.translate("MainWindow", u"Phone Number :", None))
        self.label_549.setText(QCoreApplication.translate("MainWindow", u"Promoted To:", None))
        self.label_550.setText(QCoreApplication.translate("MainWindow", u"PLEASE FILL IN THE FROM TO PRINT THE REPORT", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.comboBox_10.setItemText(0, QCoreApplication.translate("MainWindow", u"Crache", None))
        self.comboBox_10.setItemText(1, QCoreApplication.translate("MainWindow", u"Nursery 1", None))
        self.comboBox_10.setItemText(2, QCoreApplication.translate("MainWindow", u"Nursery 2", None))
        self.comboBox_10.setItemText(3, QCoreApplication.translate("MainWindow", u"Kindergaten 1", None))
        self.comboBox_10.setItemText(4, QCoreApplication.translate("MainWindow", u"Kindergaten 2", None))
        self.comboBox_10.setItemText(5, QCoreApplication.translate("MainWindow", u"Class 1", None))
        self.comboBox_10.setItemText(6, QCoreApplication.translate("MainWindow", u"Class 2", None))
        self.comboBox_10.setItemText(7, QCoreApplication.translate("MainWindow", u"Class 3", None))
        self.comboBox_10.setItemText(8, QCoreApplication.translate("MainWindow", u"Class 4", None))
        self.comboBox_10.setItemText(9, QCoreApplication.translate("MainWindow", u"Class 5", None))
        self.comboBox_10.setItemText(10, QCoreApplication.translate("MainWindow", u"Class 6", None))
        self.comboBox_10.setItemText(11, QCoreApplication.translate("MainWindow", u"JHS 1", None))
        self.comboBox_10.setItemText(12, QCoreApplication.translate("MainWindow", u"JHS 2", None))
        self.comboBox_10.setItemText(13, QCoreApplication.translate("MainWindow", u"JHS 3", None))

        self.comboBox_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"class .....", None))
        self.comboBox_11.setItemText(0, QCoreApplication.translate("MainWindow", u"Crache", None))
        self.comboBox_11.setItemText(1, QCoreApplication.translate("MainWindow", u"Nursery 1", None))
        self.comboBox_11.setItemText(2, QCoreApplication.translate("MainWindow", u"Nursery 2", None))
        self.comboBox_11.setItemText(3, QCoreApplication.translate("MainWindow", u"Kindergaten 1", None))
        self.comboBox_11.setItemText(4, QCoreApplication.translate("MainWindow", u"Kindergaten 2", None))
        self.comboBox_11.setItemText(5, QCoreApplication.translate("MainWindow", u"Class 1", None))
        self.comboBox_11.setItemText(6, QCoreApplication.translate("MainWindow", u"Class 2", None))
        self.comboBox_11.setItemText(7, QCoreApplication.translate("MainWindow", u"Class 3", None))
        self.comboBox_11.setItemText(8, QCoreApplication.translate("MainWindow", u"Class 4", None))
        self.comboBox_11.setItemText(9, QCoreApplication.translate("MainWindow", u"Class 5", None))
        self.comboBox_11.setItemText(10, QCoreApplication.translate("MainWindow", u"Class 6", None))
        self.comboBox_11.setItemText(11, QCoreApplication.translate("MainWindow", u"JHS 1", None))
        self.comboBox_11.setItemText(12, QCoreApplication.translate("MainWindow", u"JHS 2", None))
        self.comboBox_11.setItemText(13, QCoreApplication.translate("MainWindow", u"JHS 3", None))

        self.comboBox_11.setPlaceholderText(QCoreApplication.translate("MainWindow", u"class .....", None))
        self.label_1322.setText(QCoreApplication.translate("MainWindow", u"Total Attendance :", None))
        self.label_1329.setText(QCoreApplication.translate("MainWindow", u"Term Ending :", None))
        self.label_1330.setText(QCoreApplication.translate("MainWindow", u"Next Term Begins :", None))
        self.label_1347.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.lineEdit_183.setPlaceholderText(QCoreApplication.translate("MainWindow", u"please enter today's date ...", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_11), QCoreApplication.translate("MainWindow", u"Crache", None))
        self.groupBox_37.setTitle(QCoreApplication.translate("MainWindow", u"kg/primary", None))
        self.label_252.setText(QCoreApplication.translate("MainWindow", u"Full Name :", None))
        self.comboBox_65.setItemText(0, QCoreApplication.translate("MainWindow", u"Term 1", None))
        self.comboBox_65.setItemText(1, QCoreApplication.translate("MainWindow", u"Term 2", None))
        self.comboBox_65.setItemText(2, QCoreApplication.translate("MainWindow", u"Term 3", None))

        self.comboBox_65.setPlaceholderText(QCoreApplication.translate("MainWindow", u"term ...", None))
        self.label_253.setText(QCoreApplication.translate("MainWindow", u"Term :", None))
        self.label_254.setText(QCoreApplication.translate("MainWindow", u"Class :", None))
        self.label_255.setText(QCoreApplication.translate("MainWindow", u"School Name :", None))
        self.label_256.setText(QCoreApplication.translate("MainWindow", u"School Address :", None))
        self.label_257.setText(QCoreApplication.translate("MainWindow", u"Phone Number :", None))
        self.label_547.setText(QCoreApplication.translate("MainWindow", u"Promoted To:", None))
        self.label_548.setText(QCoreApplication.translate("MainWindow", u"PLEASE FILL IN THE FROM TO PRINT THE REPORT", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.comboBox_12.setItemText(0, QCoreApplication.translate("MainWindow", u"Crache", None))
        self.comboBox_12.setItemText(1, QCoreApplication.translate("MainWindow", u"Nursery 1", None))
        self.comboBox_12.setItemText(2, QCoreApplication.translate("MainWindow", u"Nursery 2", None))
        self.comboBox_12.setItemText(3, QCoreApplication.translate("MainWindow", u"Kindergaten 1", None))
        self.comboBox_12.setItemText(4, QCoreApplication.translate("MainWindow", u"Kindergaten 2", None))
        self.comboBox_12.setItemText(5, QCoreApplication.translate("MainWindow", u"Class 1", None))
        self.comboBox_12.setItemText(6, QCoreApplication.translate("MainWindow", u"Class 2", None))
        self.comboBox_12.setItemText(7, QCoreApplication.translate("MainWindow", u"Class 3", None))
        self.comboBox_12.setItemText(8, QCoreApplication.translate("MainWindow", u"Class 4", None))
        self.comboBox_12.setItemText(9, QCoreApplication.translate("MainWindow", u"Class 5", None))
        self.comboBox_12.setItemText(10, QCoreApplication.translate("MainWindow", u"Class 6", None))
        self.comboBox_12.setItemText(11, QCoreApplication.translate("MainWindow", u"JHS 1", None))
        self.comboBox_12.setItemText(12, QCoreApplication.translate("MainWindow", u"JHS 2", None))
        self.comboBox_12.setItemText(13, QCoreApplication.translate("MainWindow", u"JHS 3", None))

        self.comboBox_12.setPlaceholderText(QCoreApplication.translate("MainWindow", u"class .....", None))
        self.comboBox_13.setItemText(0, QCoreApplication.translate("MainWindow", u"Crache", None))
        self.comboBox_13.setItemText(1, QCoreApplication.translate("MainWindow", u"Nursery 1", None))
        self.comboBox_13.setItemText(2, QCoreApplication.translate("MainWindow", u"Nursery 2", None))
        self.comboBox_13.setItemText(3, QCoreApplication.translate("MainWindow", u"Kindergaten 1", None))
        self.comboBox_13.setItemText(4, QCoreApplication.translate("MainWindow", u"Kindergaten 2", None))
        self.comboBox_13.setItemText(5, QCoreApplication.translate("MainWindow", u"Class 1", None))
        self.comboBox_13.setItemText(6, QCoreApplication.translate("MainWindow", u"Class 2", None))
        self.comboBox_13.setItemText(7, QCoreApplication.translate("MainWindow", u"Class 3", None))
        self.comboBox_13.setItemText(8, QCoreApplication.translate("MainWindow", u"Class 4", None))
        self.comboBox_13.setItemText(9, QCoreApplication.translate("MainWindow", u"Class 5", None))
        self.comboBox_13.setItemText(10, QCoreApplication.translate("MainWindow", u"Class 6", None))
        self.comboBox_13.setItemText(11, QCoreApplication.translate("MainWindow", u"JHS 1", None))
        self.comboBox_13.setItemText(12, QCoreApplication.translate("MainWindow", u"JHS 2", None))
        self.comboBox_13.setItemText(13, QCoreApplication.translate("MainWindow", u"JHS 3", None))

        self.comboBox_13.setPlaceholderText(QCoreApplication.translate("MainWindow", u"class .....", None))
        self.label_1319.setText(QCoreApplication.translate("MainWindow", u"Promoted To:", None))
        self.label_1320.setText(QCoreApplication.translate("MainWindow", u"Total Attendance :", None))
        self.label_1331.setText(QCoreApplication.translate("MainWindow", u"Term Ending :", None))
        self.label_1332.setText(QCoreApplication.translate("MainWindow", u"Next Term Begins :", None))
        self.label_1348.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.lineEdit_184.setPlaceholderText(QCoreApplication.translate("MainWindow", u"please enter today's date ...", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_12), QCoreApplication.translate("MainWindow", u"Kg/Primary", None))
        self.groupBox_36.setTitle(QCoreApplication.translate("MainWindow", u"jhs", None))
        self.label_246.setText(QCoreApplication.translate("MainWindow", u"Full Name :", None))
        self.comboBox_62.setItemText(0, QCoreApplication.translate("MainWindow", u"Term 1", None))
        self.comboBox_62.setItemText(1, QCoreApplication.translate("MainWindow", u"Term 2", None))
        self.comboBox_62.setItemText(2, QCoreApplication.translate("MainWindow", u"Term 3", None))

        self.comboBox_62.setPlaceholderText(QCoreApplication.translate("MainWindow", u"term ...", None))
        self.label_247.setText(QCoreApplication.translate("MainWindow", u"Term :", None))
        self.label_248.setText(QCoreApplication.translate("MainWindow", u"Class :", None))
        self.label_249.setText(QCoreApplication.translate("MainWindow", u"School Name :", None))
        self.label_250.setText(QCoreApplication.translate("MainWindow", u"School Address :", None))
        self.label_251.setText(QCoreApplication.translate("MainWindow", u"Phone Number :", None))
        self.label_545.setText(QCoreApplication.translate("MainWindow", u"Promoted To:", None))
        self.label_546.setText(QCoreApplication.translate("MainWindow", u"PLEASE FILL IN THE FROM TO PRINT THE REPORT", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.comboBox_14.setItemText(0, QCoreApplication.translate("MainWindow", u"Crache", None))
        self.comboBox_14.setItemText(1, QCoreApplication.translate("MainWindow", u"Nursery 1", None))
        self.comboBox_14.setItemText(2, QCoreApplication.translate("MainWindow", u"Nursery 2", None))
        self.comboBox_14.setItemText(3, QCoreApplication.translate("MainWindow", u"Kindergaten 1", None))
        self.comboBox_14.setItemText(4, QCoreApplication.translate("MainWindow", u"Kindergaten 2", None))
        self.comboBox_14.setItemText(5, QCoreApplication.translate("MainWindow", u"Class 1", None))
        self.comboBox_14.setItemText(6, QCoreApplication.translate("MainWindow", u"Class 2", None))
        self.comboBox_14.setItemText(7, QCoreApplication.translate("MainWindow", u"Class 3", None))
        self.comboBox_14.setItemText(8, QCoreApplication.translate("MainWindow", u"Class 4", None))
        self.comboBox_14.setItemText(9, QCoreApplication.translate("MainWindow", u"Class 5", None))
        self.comboBox_14.setItemText(10, QCoreApplication.translate("MainWindow", u"Class 6", None))
        self.comboBox_14.setItemText(11, QCoreApplication.translate("MainWindow", u"JHS 1", None))
        self.comboBox_14.setItemText(12, QCoreApplication.translate("MainWindow", u"JHS 2", None))
        self.comboBox_14.setItemText(13, QCoreApplication.translate("MainWindow", u"JHS 3", None))

        self.comboBox_14.setPlaceholderText(QCoreApplication.translate("MainWindow", u"class .....", None))
        self.comboBox_15.setItemText(0, QCoreApplication.translate("MainWindow", u"Crache", None))
        self.comboBox_15.setItemText(1, QCoreApplication.translate("MainWindow", u"Nursery 1", None))
        self.comboBox_15.setItemText(2, QCoreApplication.translate("MainWindow", u"Nursery 2", None))
        self.comboBox_15.setItemText(3, QCoreApplication.translate("MainWindow", u"Kindergaten 1", None))
        self.comboBox_15.setItemText(4, QCoreApplication.translate("MainWindow", u"Kindergaten 2", None))
        self.comboBox_15.setItemText(5, QCoreApplication.translate("MainWindow", u"Class 1", None))
        self.comboBox_15.setItemText(6, QCoreApplication.translate("MainWindow", u"Class 2", None))
        self.comboBox_15.setItemText(7, QCoreApplication.translate("MainWindow", u"Class 3", None))
        self.comboBox_15.setItemText(8, QCoreApplication.translate("MainWindow", u"Class 4", None))
        self.comboBox_15.setItemText(9, QCoreApplication.translate("MainWindow", u"Class 5", None))
        self.comboBox_15.setItemText(10, QCoreApplication.translate("MainWindow", u"Class 6", None))
        self.comboBox_15.setItemText(11, QCoreApplication.translate("MainWindow", u"JHS 1", None))
        self.comboBox_15.setItemText(12, QCoreApplication.translate("MainWindow", u"JHS 2", None))
        self.comboBox_15.setItemText(13, QCoreApplication.translate("MainWindow", u"JHS 3", None))

        self.comboBox_15.setPlaceholderText(QCoreApplication.translate("MainWindow", u"class .....", None))
        self.label_1321.setText(QCoreApplication.translate("MainWindow", u"Total Attendance :", None))
        self.label_1333.setText(QCoreApplication.translate("MainWindow", u"Term Ending :", None))
        self.label_1334.setText(QCoreApplication.translate("MainWindow", u"Next Term Begins :", None))
        self.label_1349.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.lineEdit_185.setPlaceholderText(QCoreApplication.translate("MainWindow", u"please enter today's date ...", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_13), QCoreApplication.translate("MainWindow", u"JHS", None))
        self.label_659.setText(QCoreApplication.translate("MainWindow", u"...............................................................................", None))
        self.label_660.setText(QCoreApplication.translate("MainWindow", u"...................", None))
        self.label_661.setText(QCoreApplication.translate("MainWindow", u"................", None))
        self.label_662.setText(QCoreApplication.translate("MainWindow", u"PUPILS TERMINAL PROGRESS REPORT", None))
        self.label_663.setText(QCoreApplication.translate("MainWindow", u"ID No_:", None))
        self.label_664.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_665.setText(QCoreApplication.translate("MainWindow", u"Name :", None))
        self.label_666.setText(QCoreApplication.translate("MainWindow", u"..................................", None))
        self.label_667.setText(QCoreApplication.translate("MainWindow", u"Term Endding :", None))
        self.label_668.setText(QCoreApplication.translate("MainWindow", u".............................", None))
        self.label_669.setText(QCoreApplication.translate("MainWindow", u"Next Term Begins :", None))
        self.label_670.setText(QCoreApplication.translate("MainWindow", u".............................", None))
        self.label_671.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.label_672.setText(QCoreApplication.translate("MainWindow", u"............................", None))
        self.label_673.setText(QCoreApplication.translate("MainWindow", u"Class :", None))
        self.label_674.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_675.setText(QCoreApplication.translate("MainWindow", u"SUJECTS", None))
        self.label_676.setText(QCoreApplication.translate("MainWindow", u"CLASS SCORE", None))
        self.label_677.setText(QCoreApplication.translate("MainWindow", u"50%", None))
        self.label_678.setText(QCoreApplication.translate("MainWindow", u"GRADE", None))
        self.label_679.setText(QCoreApplication.translate("MainWindow", u"REMARKS", None))
        self.label_680.setText(QCoreApplication.translate("MainWindow", u"English Language", None))
        self.label_681.setText(QCoreApplication.translate("MainWindow", u"Vocabulary Develop.", None))
        self.label_682.setText(QCoreApplication.translate("MainWindow", u"Mathematics", None))
        self.label_683.setText(QCoreApplication.translate("MainWindow", u"Natural Science", None))
        self.label_684.setText(QCoreApplication.translate("MainWindow", u"R. M. E", None))
        self.label_685.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.label_686.setText(QCoreApplication.translate("MainWindow", u"Computing", None))
        self.label_687.setText(QCoreApplication.translate("MainWindow", u"Creative Arts", None))
        self.label_688.setText(QCoreApplication.translate("MainWindow", u"OWOP", None))
        self.label_689.setText(QCoreApplication.translate("MainWindow", u"Attendances:", None))
        self.label_690.setText(QCoreApplication.translate("MainWindow", u"..............", None))
        self.label_691.setText(QCoreApplication.translate("MainWindow", u"Out of:", None))
        self.label_692.setText(QCoreApplication.translate("MainWindow", u"..............", None))
        self.label_693.setText(QCoreApplication.translate("MainWindow", u"Promoted To :", None))
        self.label_694.setText(QCoreApplication.translate("MainWindow", u"..............", None))
        self.label_695.setText(QCoreApplication.translate("MainWindow", u"...........................................................", None))
        self.label_696.setText(QCoreApplication.translate("MainWindow", u"Conduct:", None))
        self.label_697.setText(QCoreApplication.translate("MainWindow", u"Interest:", None))
        self.label_698.setText(QCoreApplication.translate("MainWindow", u"............................................................", None))
        self.label_699.setText(QCoreApplication.translate("MainWindow", u"Class Teacher's Remarks:", None))
        self.label_700.setText(QCoreApplication.translate("MainWindow", u"...........................................................", None))
        self.label_701.setText(QCoreApplication.translate("MainWindow", u".........................", None))
        self.label_702.setText(QCoreApplication.translate("MainWindow", u"Signature:", None))
        self.label_703.setText(QCoreApplication.translate("MainWindow", u"Principals Remarks:", None))
        self.label_704.setText(QCoreApplication.translate("MainWindow", u"...........................................................", None))
        self.label_705.setText(QCoreApplication.translate("MainWindow", u".........................", None))
        self.label_706.setText(QCoreApplication.translate("MainWindow", u"Signature:", None))
        self.label_707.setText(QCoreApplication.translate("MainWindow", u"EXAM SCORE", None))
        self.label_708.setText(QCoreApplication.translate("MainWindow", u"50%", None))
        self.label_709.setText(QCoreApplication.translate("MainWindow", u"TOTAL SCORE", None))
        self.label_710.setText(QCoreApplication.translate("MainWindow", u"100%", None))
        self.label_711.setText(QCoreApplication.translate("MainWindow", u"Tel :", None))
        self.label_712.setText(QCoreApplication.translate("MainWindow", u"Address :", None))
        self.bt_109.setText(QCoreApplication.translate("MainWindow", u"PRINT", None))
        self.label_713.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_714.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_715.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_716.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_717.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_718.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_719.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_720.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_721.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_722.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_723.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_724.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_725.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_726.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_727.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_728.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_729.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_730.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_731.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_732.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_733.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_734.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_735.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_736.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_737.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_738.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_739.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_740.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_741.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_742.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_743.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_744.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_745.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_746.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_747.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_748.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_749.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_750.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_751.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_752.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_753.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_754.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_755.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_756.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_757.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_46), QCoreApplication.translate("MainWindow", u"crache print", None))
        self.label_605.setText(QCoreApplication.translate("MainWindow", u"...............................................................................", None))
        self.label_606.setText(QCoreApplication.translate("MainWindow", u"...................", None))
        self.label_607.setText(QCoreApplication.translate("MainWindow", u"................", None))
        self.label_608.setText(QCoreApplication.translate("MainWindow", u"PUPILS TERMINAL PROGRESS REPORT", None))
        self.label_609.setText(QCoreApplication.translate("MainWindow", u"ID No_:", None))
        self.label_610.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_611.setText(QCoreApplication.translate("MainWindow", u"Name :", None))
        self.label_612.setText(QCoreApplication.translate("MainWindow", u"..................................", None))
        self.label_613.setText(QCoreApplication.translate("MainWindow", u"Term Endding :", None))
        self.label_614.setText(QCoreApplication.translate("MainWindow", u".............................", None))
        self.label_615.setText(QCoreApplication.translate("MainWindow", u"Next Term Begins :", None))
        self.label_616.setText(QCoreApplication.translate("MainWindow", u".............................", None))
        self.label_617.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.label_618.setText(QCoreApplication.translate("MainWindow", u"............................", None))
        self.label_619.setText(QCoreApplication.translate("MainWindow", u"Class :", None))
        self.label_620.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_621.setText(QCoreApplication.translate("MainWindow", u"SUJECTS", None))
        self.label_622.setText(QCoreApplication.translate("MainWindow", u"CLASS SCORE", None))
        self.label_623.setText(QCoreApplication.translate("MainWindow", u"50%", None))
        self.label_624.setText(QCoreApplication.translate("MainWindow", u"GRADE", None))
        self.label_625.setText(QCoreApplication.translate("MainWindow", u"REMARKS", None))
        self.label_626.setText(QCoreApplication.translate("MainWindow", u"English Language", None))
        self.label_627.setText(QCoreApplication.translate("MainWindow", u"Ghanaian Language", None))
        self.label_628.setText(QCoreApplication.translate("MainWindow", u"Mathematics", None))
        self.label_629.setText(QCoreApplication.translate("MainWindow", u"Intergrated Science", None))
        self.label_630.setText(QCoreApplication.translate("MainWindow", u"R. M. E", None))
        self.label_631.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.label_632.setText(QCoreApplication.translate("MainWindow", u"Computing", None))
        self.label_633.setText(QCoreApplication.translate("MainWindow", u"Creative Arts", None))
        self.label_634.setText(QCoreApplication.translate("MainWindow", u"OWOP", None))
        self.label_635.setText(QCoreApplication.translate("MainWindow", u"Attendances:", None))
        self.label_636.setText(QCoreApplication.translate("MainWindow", u"..............", None))
        self.label_637.setText(QCoreApplication.translate("MainWindow", u"Out of:", None))
        self.label_638.setText(QCoreApplication.translate("MainWindow", u"..............", None))
        self.label_639.setText(QCoreApplication.translate("MainWindow", u"Promoted To :", None))
        self.label_640.setText(QCoreApplication.translate("MainWindow", u"..............", None))
        self.label_641.setText(QCoreApplication.translate("MainWindow", u"...........................................................", None))
        self.label_642.setText(QCoreApplication.translate("MainWindow", u"Conduct:", None))
        self.label_643.setText(QCoreApplication.translate("MainWindow", u"Interest:", None))
        self.label_644.setText(QCoreApplication.translate("MainWindow", u"............................................................", None))
        self.label_645.setText(QCoreApplication.translate("MainWindow", u"Class Teacher's Remarks:", None))
        self.label_646.setText(QCoreApplication.translate("MainWindow", u"...........................................................", None))
        self.label_647.setText(QCoreApplication.translate("MainWindow", u".........................", None))
        self.label_648.setText(QCoreApplication.translate("MainWindow", u"Signature:", None))
        self.label_649.setText(QCoreApplication.translate("MainWindow", u"Principals Remarks:", None))
        self.label_650.setText(QCoreApplication.translate("MainWindow", u"...........................................................", None))
        self.label_651.setText(QCoreApplication.translate("MainWindow", u".........................", None))
        self.label_652.setText(QCoreApplication.translate("MainWindow", u"Signature:", None))
        self.label_653.setText(QCoreApplication.translate("MainWindow", u"EXAM SCORE", None))
        self.label_654.setText(QCoreApplication.translate("MainWindow", u"50%", None))
        self.label_655.setText(QCoreApplication.translate("MainWindow", u"TOTAL SCORE", None))
        self.label_656.setText(QCoreApplication.translate("MainWindow", u"100%", None))
        self.label_657.setText(QCoreApplication.translate("MainWindow", u"Tel :", None))
        self.label_658.setText(QCoreApplication.translate("MainWindow", u"Address :", None))
        self.bt_108.setText(QCoreApplication.translate("MainWindow", u"PRINT", None))
        self.label_758.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_759.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_760.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_761.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_762.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_763.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_764.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_765.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_766.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_767.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_768.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_769.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_770.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_771.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_772.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_773.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_774.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_775.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_776.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_777.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_778.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_779.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_780.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_781.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_782.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_783.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_784.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_785.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_786.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_787.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_788.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_789.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_790.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_791.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_792.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_793.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_794.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_795.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_796.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_797.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_798.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_799.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_800.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_801.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_802.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_47), QCoreApplication.translate("MainWindow", u"kg/primary print", None))
        self.label_551.setText(QCoreApplication.translate("MainWindow", u"...............................................................................", None))
        self.label_552.setText(QCoreApplication.translate("MainWindow", u"...................", None))
        self.label_553.setText(QCoreApplication.translate("MainWindow", u"................", None))
        self.label_554.setText(QCoreApplication.translate("MainWindow", u"PUPILS TERMINAL PROGRESS REPORT", None))
        self.label_555.setText(QCoreApplication.translate("MainWindow", u"ID No_:", None))
        self.label_556.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_557.setText(QCoreApplication.translate("MainWindow", u"Name :", None))
        self.label_558.setText(QCoreApplication.translate("MainWindow", u"..................................", None))
        self.label_559.setText(QCoreApplication.translate("MainWindow", u"Term Endding :", None))
        self.label_560.setText(QCoreApplication.translate("MainWindow", u".............................", None))
        self.label_561.setText(QCoreApplication.translate("MainWindow", u"Next Term Begins :", None))
        self.label_562.setText(QCoreApplication.translate("MainWindow", u".............................", None))
        self.label_563.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.label_564.setText(QCoreApplication.translate("MainWindow", u"............................", None))
        self.label_565.setText(QCoreApplication.translate("MainWindow", u"Class :", None))
        self.label_566.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_567.setText(QCoreApplication.translate("MainWindow", u"SUJECTS", None))
        self.label_568.setText(QCoreApplication.translate("MainWindow", u"CLASS SCORE", None))
        self.label_569.setText(QCoreApplication.translate("MainWindow", u"50%", None))
        self.label_570.setText(QCoreApplication.translate("MainWindow", u"GRADE", None))
        self.label_571.setText(QCoreApplication.translate("MainWindow", u"REMARKS", None))
        self.label_572.setText(QCoreApplication.translate("MainWindow", u"English Language", None))
        self.label_573.setText(QCoreApplication.translate("MainWindow", u"Ghanaian Language", None))
        self.label_574.setText(QCoreApplication.translate("MainWindow", u"Mathematics", None))
        self.label_575.setText(QCoreApplication.translate("MainWindow", u"Intergrated Science", None))
        self.label_576.setText(QCoreApplication.translate("MainWindow", u"R. M. E", None))
        self.label_577.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.label_578.setText(QCoreApplication.translate("MainWindow", u"Computing", None))
        self.label_579.setText(QCoreApplication.translate("MainWindow", u"Basic Design and Tech", None))
        self.label_580.setText(QCoreApplication.translate("MainWindow", u"OWOP", None))
        self.label_581.setText(QCoreApplication.translate("MainWindow", u"Attendances:", None))
        self.label_582.setText(QCoreApplication.translate("MainWindow", u"..............", None))
        self.label_583.setText(QCoreApplication.translate("MainWindow", u"Out of:", None))
        self.label_584.setText(QCoreApplication.translate("MainWindow", u"..............", None))
        self.label_585.setText(QCoreApplication.translate("MainWindow", u"Promoted To :", None))
        self.label_586.setText(QCoreApplication.translate("MainWindow", u"..............", None))
        self.label_587.setText(QCoreApplication.translate("MainWindow", u"...........................................................", None))
        self.label_588.setText(QCoreApplication.translate("MainWindow", u"Conduct:", None))
        self.label_589.setText(QCoreApplication.translate("MainWindow", u"Interest:", None))
        self.label_590.setText(QCoreApplication.translate("MainWindow", u"............................................................", None))
        self.label_591.setText(QCoreApplication.translate("MainWindow", u"Class Teacher's Remarks:", None))
        self.label_592.setText(QCoreApplication.translate("MainWindow", u"...........................................................", None))
        self.label_593.setText(QCoreApplication.translate("MainWindow", u".........................", None))
        self.label_594.setText(QCoreApplication.translate("MainWindow", u"Signature:", None))
        self.label_595.setText(QCoreApplication.translate("MainWindow", u"Principals Remarks:", None))
        self.label_596.setText(QCoreApplication.translate("MainWindow", u"...........................................................", None))
        self.label_597.setText(QCoreApplication.translate("MainWindow", u".........................", None))
        self.label_598.setText(QCoreApplication.translate("MainWindow", u"Signature:", None))
        self.label_599.setText(QCoreApplication.translate("MainWindow", u"EXAM SCORE", None))
        self.label_600.setText(QCoreApplication.translate("MainWindow", u"50%", None))
        self.label_601.setText(QCoreApplication.translate("MainWindow", u"TOTAL SCORE", None))
        self.label_602.setText(QCoreApplication.translate("MainWindow", u"100%", None))
        self.label_603.setText(QCoreApplication.translate("MainWindow", u"Tel :", None))
        self.label_604.setText(QCoreApplication.translate("MainWindow", u"Address :", None))
        self.bt_107.setText(QCoreApplication.translate("MainWindow", u"PRINT", None))
        self.label_803.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_804.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_805.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_806.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_807.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_808.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_809.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_810.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_811.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_812.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_813.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_814.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_815.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_816.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_817.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_818.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_819.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_820.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_821.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_822.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_823.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_824.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_825.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_826.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_827.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_828.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_829.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_830.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_831.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_832.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_833.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_834.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_835.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_836.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_837.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_838.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_839.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_840.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_841.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_842.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_843.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_844.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_845.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_846.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_847.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_48), QCoreApplication.translate("MainWindow", u"jhs print", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"Student Report", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"School Fees", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.comboBox_16.setItemText(0, QCoreApplication.translate("MainWindow", u"Crache", None))
        self.comboBox_16.setItemText(1, QCoreApplication.translate("MainWindow", u"Nursery 1", None))
        self.comboBox_16.setItemText(2, QCoreApplication.translate("MainWindow", u"Nursery 2", None))
        self.comboBox_16.setItemText(3, QCoreApplication.translate("MainWindow", u"Kindergaten 1", None))
        self.comboBox_16.setItemText(4, QCoreApplication.translate("MainWindow", u"Kindergaten 2", None))
        self.comboBox_16.setItemText(5, QCoreApplication.translate("MainWindow", u"Class 1", None))
        self.comboBox_16.setItemText(6, QCoreApplication.translate("MainWindow", u"Class 2", None))
        self.comboBox_16.setItemText(7, QCoreApplication.translate("MainWindow", u"Class 3", None))
        self.comboBox_16.setItemText(8, QCoreApplication.translate("MainWindow", u"Class 4", None))
        self.comboBox_16.setItemText(9, QCoreApplication.translate("MainWindow", u"Class 5", None))
        self.comboBox_16.setItemText(10, QCoreApplication.translate("MainWindow", u"Class 6", None))
        self.comboBox_16.setItemText(11, QCoreApplication.translate("MainWindow", u"JHS 1", None))
        self.comboBox_16.setItemText(12, QCoreApplication.translate("MainWindow", u"JHS 2", None))
        self.comboBox_16.setItemText(13, QCoreApplication.translate("MainWindow", u"JHS 3", None))

        self.comboBox_16.setPlaceholderText(QCoreApplication.translate("MainWindow", u"class .....", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"Full Name :", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"Paid By :", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"Amount Paid :", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"Term :", None))
        self.comboBox_17.setItemText(0, QCoreApplication.translate("MainWindow", u"Term 1", None))
        self.comboBox_17.setItemText(1, QCoreApplication.translate("MainWindow", u"Term 2", None))
        self.comboBox_17.setItemText(2, QCoreApplication.translate("MainWindow", u"Term 3", None))

        self.comboBox_17.setPlaceholderText(QCoreApplication.translate("MainWindow", u"term ...", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"Class :", None))
        self.bt_33.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.bt_32.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.bt_31.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.bt_115.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Feeding Fees/Studies Fees", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"Class :", None))
        self.comboBox_18.setItemText(0, QCoreApplication.translate("MainWindow", u"Crache", None))
        self.comboBox_18.setItemText(1, QCoreApplication.translate("MainWindow", u"Nursery 1", None))
        self.comboBox_18.setItemText(2, QCoreApplication.translate("MainWindow", u"Nursery 2", None))
        self.comboBox_18.setItemText(3, QCoreApplication.translate("MainWindow", u"Kindergaten 1", None))
        self.comboBox_18.setItemText(4, QCoreApplication.translate("MainWindow", u"Kindergaten 2", None))
        self.comboBox_18.setItemText(5, QCoreApplication.translate("MainWindow", u"Class 1", None))
        self.comboBox_18.setItemText(6, QCoreApplication.translate("MainWindow", u"Class 2", None))
        self.comboBox_18.setItemText(7, QCoreApplication.translate("MainWindow", u"Class 3", None))
        self.comboBox_18.setItemText(8, QCoreApplication.translate("MainWindow", u"Class 4", None))
        self.comboBox_18.setItemText(9, QCoreApplication.translate("MainWindow", u"Class 5", None))
        self.comboBox_18.setItemText(10, QCoreApplication.translate("MainWindow", u"Class 6", None))
        self.comboBox_18.setItemText(11, QCoreApplication.translate("MainWindow", u"JHS 1", None))
        self.comboBox_18.setItemText(12, QCoreApplication.translate("MainWindow", u"JHS 2", None))
        self.comboBox_18.setItemText(13, QCoreApplication.translate("MainWindow", u"JHS 3", None))

        self.comboBox_18.setPlaceholderText(QCoreApplication.translate("MainWindow", u"class .....", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"Amount Paid :", None))
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"Full Name :", None))
        self.comboBox_31.setItemText(0, QCoreApplication.translate("MainWindow", u"Feeding Fees", None))
        self.comboBox_31.setItemText(1, QCoreApplication.translate("MainWindow", u"Studies Fees", None))

        self.comboBox_31.setPlaceholderText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_126.setText(QCoreApplication.translate("MainWindow", u"Type of Fees :", None))
        self.bt_114.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.bt_118.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.bt_34.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.bt_35.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.bt_36.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        ___qtablewidgetitem31 = self.tableWidget_5.horizontalHeaderItem(0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Full Name", None));
        ___qtablewidgetitem32 = self.tableWidget_5.horizontalHeaderItem(1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Class", None));
        ___qtablewidgetitem33 = self.tableWidget_5.horizontalHeaderItem(2)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Term", None));
        ___qtablewidgetitem34 = self.tableWidget_5.horizontalHeaderItem(3)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Amount Paid", None));
        ___qtablewidgetitem35 = self.tableWidget_5.horizontalHeaderItem(4)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Paid By", None));
        ___qtablewidgetitem36 = self.tableWidget_5.horizontalHeaderItem(5)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem37 = self.tableWidget_6.horizontalHeaderItem(0)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Full Name", None));
        ___qtablewidgetitem38 = self.tableWidget_6.horizontalHeaderItem(1)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Class", None));
        ___qtablewidgetitem39 = self.tableWidget_6.horizontalHeaderItem(2)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Type Of Fees", None));
        ___qtablewidgetitem40 = self.tableWidget_6.horizontalHeaderItem(3)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Amount Paid", None));
        ___qtablewidgetitem41 = self.tableWidget_6.horizontalHeaderItem(4)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_14), QCoreApplication.translate("MainWindow", u"Student Fees", None))
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"Message Subject :", None))
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"To :", None))
        self.bt_37.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_15), QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Expenses For :", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Amout :", None))
        self.comboBox_30.setItemText(0, QCoreApplication.translate("MainWindow", u"School Fees", None))
        self.comboBox_30.setItemText(1, QCoreApplication.translate("MainWindow", u"Feeding Fees", None))
        self.comboBox_30.setItemText(2, QCoreApplication.translate("MainWindow", u"Studies Fees", None))

        self.comboBox_30.setPlaceholderText("")
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Expenses From :", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"School Fees :", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Feeding Fees :", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"From School Fees :", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"From Feeding Fees :", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"From Studies Fees :", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Expenses :", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Balances :", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Feeding Fees :", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"Studies Fees :", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"School Fees :", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"..", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400; text-decoration: underline;\">Adding Expenses Used</span></p></body></html>", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u" School Fees", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"Feeding Fees", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"Studies Fees", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_53), QCoreApplication.translate("MainWindow", u"Exepenses", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Management", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"GES", None))
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"Student Management System For Montessori Schools", None))
        self.label_124.setText("")
        self.bt_38.setText(QCoreApplication.translate("MainWindow", u"Get Started", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_17), QCoreApplication.translate("MainWindow", u"Welcome", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Total Number Of Students :", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"..", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"..", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Total School Fees :", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Total Feeding Fees :", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"..", None))
        self.bt_39.setText(QCoreApplication.translate("MainWindow", u"Add New Students", None))
        self.bt_40.setText(QCoreApplication.translate("MainWindow", u"Update Students", None))
        self.bt_41.setText(QCoreApplication.translate("MainWindow", u"Sudents Marks", None))
        self.bt_42.setText(QCoreApplication.translate("MainWindow", u"Attendances", None))
        self.bt_43.setText(QCoreApplication.translate("MainWindow", u"Students Reports", None))
        self.bt_44.setText(QCoreApplication.translate("MainWindow", u"Students Fees", None))
        self.bt_45.setText(QCoreApplication.translate("MainWindow", u"Send Email", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"Expenses", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"Student's Details", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"Registration Number :", None))
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"Date Of Birth :", None))
        self.label_129.setText(QCoreApplication.translate("MainWindow", u"Class :", None))
        self.comboBox_19.setItemText(0, QCoreApplication.translate("MainWindow", u"Crache", None))
        self.comboBox_19.setItemText(1, QCoreApplication.translate("MainWindow", u"Nursery 1", None))
        self.comboBox_19.setItemText(2, QCoreApplication.translate("MainWindow", u"Nursery 2", None))
        self.comboBox_19.setItemText(3, QCoreApplication.translate("MainWindow", u"Kindergaten 1", None))
        self.comboBox_19.setItemText(4, QCoreApplication.translate("MainWindow", u"Kindergaten 2", None))
        self.comboBox_19.setItemText(5, QCoreApplication.translate("MainWindow", u"Class 1", None))
        self.comboBox_19.setItemText(6, QCoreApplication.translate("MainWindow", u"Class 2", None))
        self.comboBox_19.setItemText(7, QCoreApplication.translate("MainWindow", u"Class 3", None))
        self.comboBox_19.setItemText(8, QCoreApplication.translate("MainWindow", u"Class 4", None))
        self.comboBox_19.setItemText(9, QCoreApplication.translate("MainWindow", u"Class 5", None))
        self.comboBox_19.setItemText(10, QCoreApplication.translate("MainWindow", u"Class 6", None))
        self.comboBox_19.setItemText(11, QCoreApplication.translate("MainWindow", u"JHS 1", None))
        self.comboBox_19.setItemText(12, QCoreApplication.translate("MainWindow", u"JHS 2", None))
        self.comboBox_19.setItemText(13, QCoreApplication.translate("MainWindow", u"JHS 3", None))

        self.comboBox_19.setPlaceholderText(QCoreApplication.translate("MainWindow", u"class .....", None))
        self.comboBox_20.setItemText(0, QCoreApplication.translate("MainWindow", u"Male", None))
        self.comboBox_20.setItemText(1, QCoreApplication.translate("MainWindow", u"Female", None))

        self.comboBox_20.setPlaceholderText(QCoreApplication.translate("MainWindow", u"gender.....", None))
        self.label_130.setText(QCoreApplication.translate("MainWindow", u"Gender :", None))
        self.label_131.setText(QCoreApplication.translate("MainWindow", u"Home Address :", None))
        self.textEdit_3.setPlaceholderText("")
        self.lineEdit_60.setPlaceholderText("")
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Full Name :", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"Parent's Details", None))
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"Phone Number :", None))
        self.label_133.setText(QCoreApplication.translate("MainWindow", u"Parent Full Name :", None))
        self.label_134.setText(QCoreApplication.translate("MainWindow", u"Email Address :", None))
        self.bt_46.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.bt_47.setText(QCoreApplication.translate("MainWindow", u"View", None))
        ___qtablewidgetitem42 = self.tableWidget_7.horizontalHeaderItem(0)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Reg_No:-", None));
        ___qtablewidgetitem43 = self.tableWidget_7.horizontalHeaderItem(1)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Full Name", None));
        ___qtablewidgetitem44 = self.tableWidget_7.horizontalHeaderItem(2)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Date Of Birth", None));
        ___qtablewidgetitem45 = self.tableWidget_7.horizontalHeaderItem(3)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Class", None));
        ___qtablewidgetitem46 = self.tableWidget_7.horizontalHeaderItem(4)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Gender", None));
        ___qtablewidgetitem47 = self.tableWidget_7.horizontalHeaderItem(5)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Home Address", None));
        ___qtablewidgetitem48 = self.tableWidget_7.horizontalHeaderItem(6)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"Parent Full Name", None));
        ___qtablewidgetitem49 = self.tableWidget_7.horizontalHeaderItem(7)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None));
        ___qtablewidgetitem50 = self.tableWidget_7.horizontalHeaderItem(8)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"Email Address", None));
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_19), QCoreApplication.translate("MainWindow", u"Add_student", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"Student's Details", None))
        self.label_135.setText(QCoreApplication.translate("MainWindow", u"Registration Number :", None))
        self.lineEdit_44.setInputMask("")
        self.lineEdit_44.setText("")
        self.label_138.setText(QCoreApplication.translate("MainWindow", u"Date Of Birth :", None))
        self.label_139.setText(QCoreApplication.translate("MainWindow", u"Class :", None))
        self.comboBox_21.setItemText(0, QCoreApplication.translate("MainWindow", u"Male", None))
        self.comboBox_21.setItemText(1, QCoreApplication.translate("MainWindow", u"Female", None))

        self.comboBox_21.setPlaceholderText(QCoreApplication.translate("MainWindow", u"gender...", None))
        self.label_140.setText(QCoreApplication.translate("MainWindow", u"Gender :", None))
        self.label_141.setText(QCoreApplication.translate("MainWindow", u"Home Address :", None))
        self.comboBox_22.setItemText(0, QCoreApplication.translate("MainWindow", u"Grade 1", None))
        self.comboBox_22.setItemText(1, QCoreApplication.translate("MainWindow", u"Grade 2", None))
        self.comboBox_22.setItemText(2, QCoreApplication.translate("MainWindow", u"Grade 3", None))
        self.comboBox_22.setItemText(3, QCoreApplication.translate("MainWindow", u"Grade 4", None))
        self.comboBox_22.setItemText(4, QCoreApplication.translate("MainWindow", u"Grade 5", None))
        self.comboBox_22.setItemText(5, QCoreApplication.translate("MainWindow", u"Grade 6", None))
        self.comboBox_22.setItemText(6, QCoreApplication.translate("MainWindow", u"Grade 7", None))
        self.comboBox_22.setItemText(7, QCoreApplication.translate("MainWindow", u"Grade 8", None))
        self.comboBox_22.setItemText(8, QCoreApplication.translate("MainWindow", u"Grade 9", None))

        self.comboBox_22.setPlaceholderText(QCoreApplication.translate("MainWindow", u"class .....", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Full Name :", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", u"Parent's Details", None))
        self.label_142.setText(QCoreApplication.translate("MainWindow", u"Phone Number :", None))
        self.label_143.setText(QCoreApplication.translate("MainWindow", u"Parent Full Name :", None))
        self.label_144.setText(QCoreApplication.translate("MainWindow", u"Email Address :", None))
        self.bt_48.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.bt_49.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.bt_50.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.bt_51.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        ___qtablewidgetitem51 = self.tableWidget_8.horizontalHeaderItem(0)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"Reg_No:-", None));
        ___qtablewidgetitem52 = self.tableWidget_8.horizontalHeaderItem(1)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"Full Name", None));
        ___qtablewidgetitem53 = self.tableWidget_8.horizontalHeaderItem(2)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"Date Of Birth", None));
        ___qtablewidgetitem54 = self.tableWidget_8.horizontalHeaderItem(3)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"Class", None));
        ___qtablewidgetitem55 = self.tableWidget_8.horizontalHeaderItem(4)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"Gender", None));
        ___qtablewidgetitem56 = self.tableWidget_8.horizontalHeaderItem(5)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"Home Address", None));
        ___qtablewidgetitem57 = self.tableWidget_8.horizontalHeaderItem(6)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"Parent Full Name", None));
        ___qtablewidgetitem58 = self.tableWidget_8.horizontalHeaderItem(7)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None));
        ___qtablewidgetitem59 = self.tableWidget_8.horizontalHeaderItem(8)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"Email Address", None));
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_20), QCoreApplication.translate("MainWindow", u"Update_student", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("MainWindow", u"Student Marks", None))
        self.label_145.setText(QCoreApplication.translate("MainWindow", u"Full Name :", None))
        self.label_146.setText(QCoreApplication.translate("MainWindow", u"Class :", None))
        self.label_147.setText(QCoreApplication.translate("MainWindow", u"Registration Number :", None))
        self.comboBox_24.setItemText(0, QCoreApplication.translate("MainWindow", u"English Language", None))
        self.comboBox_24.setItemText(1, QCoreApplication.translate("MainWindow", u"Vocabulary Development", None))
        self.comboBox_24.setItemText(2, QCoreApplication.translate("MainWindow", u"Mathematics", None))
        self.comboBox_24.setItemText(3, QCoreApplication.translate("MainWindow", u"Computing", None))
        self.comboBox_24.setItemText(4, QCoreApplication.translate("MainWindow", u"Natural Science", None))
        self.comboBox_24.setItemText(5, QCoreApplication.translate("MainWindow", u"Religious and Moral Education", None))
        self.comboBox_24.setItemText(6, QCoreApplication.translate("MainWindow", u"History", None))
        self.comboBox_24.setItemText(7, QCoreApplication.translate("MainWindow", u"Creative Arts", None))
        self.comboBox_24.setItemText(8, QCoreApplication.translate("MainWindow", u"Our World Our People", None))

        self.comboBox_24.setPlaceholderText(QCoreApplication.translate("MainWindow", u"subject...", None))
        self.label_148.setText(QCoreApplication.translate("MainWindow", u"Subjects :", None))
        self.comboBox_25.setItemText(0, QCoreApplication.translate("MainWindow", u"Term 1", None))
        self.comboBox_25.setItemText(1, QCoreApplication.translate("MainWindow", u"Term 2", None))
        self.comboBox_25.setItemText(2, QCoreApplication.translate("MainWindow", u"Term 3", None))

        self.comboBox_25.setPlaceholderText(QCoreApplication.translate("MainWindow", u"term ...", None))
        self.label_149.setText(QCoreApplication.translate("MainWindow", u"Term :", None))
        self.comboBox_26.setItemText(0, QCoreApplication.translate("MainWindow", u"Exams", None))
        self.comboBox_26.setItemText(1, QCoreApplication.translate("MainWindow", u"Class Work", None))
        self.comboBox_26.setItemText(2, QCoreApplication.translate("MainWindow", u"Projects", None))

        self.comboBox_26.setPlaceholderText(QCoreApplication.translate("MainWindow", u"type...", None))
        self.label_150.setText(QCoreApplication.translate("MainWindow", u"Marks Type :", None))
        self.label_151.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.comboBox_23.setItemText(0, QCoreApplication.translate("MainWindow", u"Grade 1", None))
        self.comboBox_23.setItemText(1, QCoreApplication.translate("MainWindow", u"Grade 2", None))
        self.comboBox_23.setItemText(2, QCoreApplication.translate("MainWindow", u"Grade 3", None))
        self.comboBox_23.setItemText(3, QCoreApplication.translate("MainWindow", u"Grade 4", None))
        self.comboBox_23.setItemText(4, QCoreApplication.translate("MainWindow", u"Grade 5", None))
        self.comboBox_23.setItemText(5, QCoreApplication.translate("MainWindow", u"Grade 6", None))
        self.comboBox_23.setItemText(6, QCoreApplication.translate("MainWindow", u"Grade 7", None))
        self.comboBox_23.setItemText(7, QCoreApplication.translate("MainWindow", u"Grade 8", None))
        self.comboBox_23.setItemText(8, QCoreApplication.translate("MainWindow", u"Grade 9", None))

        self.comboBox_23.setPlaceholderText(QCoreApplication.translate("MainWindow", u"class .....", None))
        self.label_156.setText(QCoreApplication.translate("MainWindow", u"Marks :", None))
        self.label_157.setText(QCoreApplication.translate("MainWindow", u"Grade :", None))
        self.comboBox_29.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_29.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_29.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_29.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_29.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_29.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_29.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_29.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_29.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))

        self.comboBox_29.setPlaceholderText(QCoreApplication.translate("MainWindow", u"type...", None))
        self.bt_52.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.bt_53.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.bt_54.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.bt_55.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.bt_56.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.lineEdit_53.setPlaceholderText(QCoreApplication.translate("MainWindow", u"search by name", None))
        ___qtablewidgetitem60 = self.tableWidget_9.horizontalHeaderItem(0)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"Reg_No:-", None));
        ___qtablewidgetitem61 = self.tableWidget_9.horizontalHeaderItem(1)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"Full Name", None));
        ___qtablewidgetitem62 = self.tableWidget_9.horizontalHeaderItem(2)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"Class", None));
        ___qtablewidgetitem63 = self.tableWidget_9.horizontalHeaderItem(3)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"Subjects", None));
        ___qtablewidgetitem64 = self.tableWidget_9.horizontalHeaderItem(4)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"Term", None));
        ___qtablewidgetitem65 = self.tableWidget_9.horizontalHeaderItem(5)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"Marks Type", None));
        ___qtablewidgetitem66 = self.tableWidget_9.horizontalHeaderItem(6)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem67 = self.tableWidget_9.horizontalHeaderItem(7)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem68 = self.tableWidget_9.horizontalHeaderItem(8)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"Marks", None));
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_21), QCoreApplication.translate("MainWindow", u"Student Marks", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("MainWindow", u"Attendance", None))
        self.label_152.setText(QCoreApplication.translate("MainWindow", u"Registration Number :", None))
        self.label_153.setText(QCoreApplication.translate("MainWindow", u"Full Name :", None))
        self.label_154.setText(QCoreApplication.translate("MainWindow", u"Class :", None))
        self.label_155.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.comboBox_27.setItemText(0, QCoreApplication.translate("MainWindow", u"Grade 1", None))
        self.comboBox_27.setItemText(1, QCoreApplication.translate("MainWindow", u"Grade 2", None))
        self.comboBox_27.setItemText(2, QCoreApplication.translate("MainWindow", u"Grade 3", None))
        self.comboBox_27.setItemText(3, QCoreApplication.translate("MainWindow", u"Grade 4", None))
        self.comboBox_27.setItemText(4, QCoreApplication.translate("MainWindow", u"Grade 5", None))
        self.comboBox_27.setItemText(5, QCoreApplication.translate("MainWindow", u"Grade 6", None))
        self.comboBox_27.setItemText(6, QCoreApplication.translate("MainWindow", u"Grade 7", None))
        self.comboBox_27.setItemText(7, QCoreApplication.translate("MainWindow", u"Grade 8", None))
        self.comboBox_27.setItemText(8, QCoreApplication.translate("MainWindow", u"Grade 9", None))

        self.comboBox_27.setPlaceholderText(QCoreApplication.translate("MainWindow", u"class .....", None))
        self.bt_57.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.bt_58.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.bt_59.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.bt_60.setText(QCoreApplication.translate("MainWindow", u"View", None))
        ___qtablewidgetitem69 = self.tableWidget_10.horizontalHeaderItem(0)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"Reg_No:-", None));
        ___qtablewidgetitem70 = self.tableWidget_10.horizontalHeaderItem(1)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"Full Name", None));
        ___qtablewidgetitem71 = self.tableWidget_10.horizontalHeaderItem(2)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"Class", None));
        ___qtablewidgetitem72 = self.tableWidget_10.horizontalHeaderItem(3)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_22), QCoreApplication.translate("MainWindow", u"Attendance", None))
        self.bt_61.setText(QCoreApplication.translate("MainWindow", u"Crache/Nursery", None))
        self.bt_62.setText(QCoreApplication.translate("MainWindow", u"Grade 1 - 6", None))
        self.bt_63.setText(QCoreApplication.translate("MainWindow", u"Grade 7 - 9", None))
        self.groupBox_35.setTitle(QCoreApplication.translate("MainWindow", u"Crache", None))
        self.label_240.setText(QCoreApplication.translate("MainWindow", u"Full Name :", None))
        self.comboBox_59.setItemText(0, QCoreApplication.translate("MainWindow", u"Term 1", None))
        self.comboBox_59.setItemText(1, QCoreApplication.translate("MainWindow", u"Term 2", None))
        self.comboBox_59.setItemText(2, QCoreApplication.translate("MainWindow", u"Term 3", None))

        self.comboBox_59.setPlaceholderText(QCoreApplication.translate("MainWindow", u"term ...", None))
        self.label_241.setText(QCoreApplication.translate("MainWindow", u"Term :", None))
        self.label_242.setText(QCoreApplication.translate("MainWindow", u"Class :", None))
        self.label_243.setText(QCoreApplication.translate("MainWindow", u"School Name :", None))
        self.label_244.setText(QCoreApplication.translate("MainWindow", u"School Address :", None))
        self.label_245.setText(QCoreApplication.translate("MainWindow", u"Phone Number :", None))
        self.comboBox_60.setItemText(0, QCoreApplication.translate("MainWindow", u"Grade 1", None))
        self.comboBox_60.setItemText(1, QCoreApplication.translate("MainWindow", u"Grade 2", None))
        self.comboBox_60.setItemText(2, QCoreApplication.translate("MainWindow", u"Grade 3", None))
        self.comboBox_60.setItemText(3, QCoreApplication.translate("MainWindow", u"Grade 4", None))
        self.comboBox_60.setItemText(4, QCoreApplication.translate("MainWindow", u"Grade 5", None))
        self.comboBox_60.setItemText(5, QCoreApplication.translate("MainWindow", u"Grade 6", None))
        self.comboBox_60.setItemText(6, QCoreApplication.translate("MainWindow", u"Grade 7", None))
        self.comboBox_60.setItemText(7, QCoreApplication.translate("MainWindow", u"Grade 8", None))
        self.comboBox_60.setItemText(8, QCoreApplication.translate("MainWindow", u"Grade 9", None))

        self.comboBox_60.setPlaceholderText(QCoreApplication.translate("MainWindow", u"class .....", None))
        self.label_543.setText(QCoreApplication.translate("MainWindow", u"Promoted To:", None))
        self.comboBox_61.setItemText(0, QCoreApplication.translate("MainWindow", u"Grade 1", None))
        self.comboBox_61.setItemText(1, QCoreApplication.translate("MainWindow", u"Grade 2", None))
        self.comboBox_61.setItemText(2, QCoreApplication.translate("MainWindow", u"Grade 3", None))
        self.comboBox_61.setItemText(3, QCoreApplication.translate("MainWindow", u"Grade 4", None))
        self.comboBox_61.setItemText(4, QCoreApplication.translate("MainWindow", u"Grade 5", None))
        self.comboBox_61.setItemText(5, QCoreApplication.translate("MainWindow", u"Grade 6", None))
        self.comboBox_61.setItemText(6, QCoreApplication.translate("MainWindow", u"Grade 7", None))
        self.comboBox_61.setItemText(7, QCoreApplication.translate("MainWindow", u"Grade 8", None))
        self.comboBox_61.setItemText(8, QCoreApplication.translate("MainWindow", u"Grade 9", None))

        self.comboBox_61.setPlaceholderText(QCoreApplication.translate("MainWindow", u"class .....", None))
        self.label_544.setText(QCoreApplication.translate("MainWindow", u"PLEASE FILL IN THE FROM TO PRINT THE REPORT", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.label_1323.setText(QCoreApplication.translate("MainWindow", u"Total Attendance :", None))
        self.label_1335.setText(QCoreApplication.translate("MainWindow", u"Term Ending :", None))
        self.label_1336.setText(QCoreApplication.translate("MainWindow", u"Next Term Begins :", None))
        self.label_1350.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.lineEdit_186.setPlaceholderText(QCoreApplication.translate("MainWindow", u"please enter today's date ...", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_24), QCoreApplication.translate("MainWindow", u"Crache", None))
        self.groupBox_34.setTitle(QCoreApplication.translate("MainWindow", u"Grade 1 -6", None))
        self.label_234.setText(QCoreApplication.translate("MainWindow", u"Full Name :", None))
        self.comboBox_56.setItemText(0, QCoreApplication.translate("MainWindow", u"Term 1", None))
        self.comboBox_56.setItemText(1, QCoreApplication.translate("MainWindow", u"Term 2", None))
        self.comboBox_56.setItemText(2, QCoreApplication.translate("MainWindow", u"Term 3", None))

        self.comboBox_56.setPlaceholderText(QCoreApplication.translate("MainWindow", u"term ...", None))
        self.label_235.setText(QCoreApplication.translate("MainWindow", u"Term :", None))
        self.label_236.setText(QCoreApplication.translate("MainWindow", u"Class :", None))
        self.label_237.setText(QCoreApplication.translate("MainWindow", u"School Name :", None))
        self.label_238.setText(QCoreApplication.translate("MainWindow", u"School Address :", None))
        self.label_239.setText(QCoreApplication.translate("MainWindow", u"Phone Number :", None))
        self.comboBox_57.setItemText(0, QCoreApplication.translate("MainWindow", u"Grade 1", None))
        self.comboBox_57.setItemText(1, QCoreApplication.translate("MainWindow", u"Grade 2", None))
        self.comboBox_57.setItemText(2, QCoreApplication.translate("MainWindow", u"Grade 3", None))
        self.comboBox_57.setItemText(3, QCoreApplication.translate("MainWindow", u"Grade 4", None))
        self.comboBox_57.setItemText(4, QCoreApplication.translate("MainWindow", u"Grade 5", None))
        self.comboBox_57.setItemText(5, QCoreApplication.translate("MainWindow", u"Grade 6", None))
        self.comboBox_57.setItemText(6, QCoreApplication.translate("MainWindow", u"Grade 7", None))
        self.comboBox_57.setItemText(7, QCoreApplication.translate("MainWindow", u"Grade 8", None))
        self.comboBox_57.setItemText(8, QCoreApplication.translate("MainWindow", u"Grade 9", None))

        self.comboBox_57.setPlaceholderText(QCoreApplication.translate("MainWindow", u"class .....", None))
        self.label_541.setText(QCoreApplication.translate("MainWindow", u"Promoted To:", None))
        self.comboBox_58.setItemText(0, QCoreApplication.translate("MainWindow", u"Grade 1", None))
        self.comboBox_58.setItemText(1, QCoreApplication.translate("MainWindow", u"Grade 2", None))
        self.comboBox_58.setItemText(2, QCoreApplication.translate("MainWindow", u"Grade 3", None))
        self.comboBox_58.setItemText(3, QCoreApplication.translate("MainWindow", u"Grade 4", None))
        self.comboBox_58.setItemText(4, QCoreApplication.translate("MainWindow", u"Grade 5", None))
        self.comboBox_58.setItemText(5, QCoreApplication.translate("MainWindow", u"Grade 6", None))
        self.comboBox_58.setItemText(6, QCoreApplication.translate("MainWindow", u"Grade 7", None))
        self.comboBox_58.setItemText(7, QCoreApplication.translate("MainWindow", u"Grade 8", None))
        self.comboBox_58.setItemText(8, QCoreApplication.translate("MainWindow", u"Grade 9", None))

        self.comboBox_58.setPlaceholderText(QCoreApplication.translate("MainWindow", u"class .....", None))
        self.label_542.setText(QCoreApplication.translate("MainWindow", u"PLEASE FILL IN THE FROM TO PRINT THE REPORT", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.label_1324.setText(QCoreApplication.translate("MainWindow", u"Total Attendance :", None))
        self.label_1337.setText(QCoreApplication.translate("MainWindow", u"Term Ending :", None))
        self.label_1338.setText(QCoreApplication.translate("MainWindow", u"Next Term Begins :", None))
        self.label_1351.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.lineEdit_187.setPlaceholderText(QCoreApplication.translate("MainWindow", u"please enter today's date ...", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_25), QCoreApplication.translate("MainWindow", u"Grade 1-6", None))
        self.groupBox_20.setTitle(QCoreApplication.translate("MainWindow", u"Grade 7 -9", None))
        self.label_216.setText(QCoreApplication.translate("MainWindow", u"Full Name :", None))
        self.comboBox_32.setItemText(0, QCoreApplication.translate("MainWindow", u"Term 1", None))
        self.comboBox_32.setItemText(1, QCoreApplication.translate("MainWindow", u"Term 2", None))
        self.comboBox_32.setItemText(2, QCoreApplication.translate("MainWindow", u"Term 3", None))

        self.comboBox_32.setPlaceholderText(QCoreApplication.translate("MainWindow", u"term ...", None))
        self.label_217.setText(QCoreApplication.translate("MainWindow", u"Term :", None))
        self.label_218.setText(QCoreApplication.translate("MainWindow", u"Class :", None))
        self.label_219.setText(QCoreApplication.translate("MainWindow", u"School Name :", None))
        self.label_220.setText(QCoreApplication.translate("MainWindow", u"School Address :", None))
        self.label_221.setText(QCoreApplication.translate("MainWindow", u"Phone Number :", None))
        self.comboBox_33.setItemText(0, QCoreApplication.translate("MainWindow", u"Grade 1", None))
        self.comboBox_33.setItemText(1, QCoreApplication.translate("MainWindow", u"Grade 2", None))
        self.comboBox_33.setItemText(2, QCoreApplication.translate("MainWindow", u"Grade 3", None))
        self.comboBox_33.setItemText(3, QCoreApplication.translate("MainWindow", u"Grade 4", None))
        self.comboBox_33.setItemText(4, QCoreApplication.translate("MainWindow", u"Grade 5", None))
        self.comboBox_33.setItemText(5, QCoreApplication.translate("MainWindow", u"Grade 6", None))
        self.comboBox_33.setItemText(6, QCoreApplication.translate("MainWindow", u"Grade 7", None))
        self.comboBox_33.setItemText(7, QCoreApplication.translate("MainWindow", u"Grade 8", None))
        self.comboBox_33.setItemText(8, QCoreApplication.translate("MainWindow", u"Grade 9", None))

        self.comboBox_33.setPlaceholderText(QCoreApplication.translate("MainWindow", u"class .....", None))
        self.label_485.setText(QCoreApplication.translate("MainWindow", u"Promoted To:", None))
        self.comboBox_55.setItemText(0, QCoreApplication.translate("MainWindow", u"Grade 1", None))
        self.comboBox_55.setItemText(1, QCoreApplication.translate("MainWindow", u"Grade 2", None))
        self.comboBox_55.setItemText(2, QCoreApplication.translate("MainWindow", u"Grade 3", None))
        self.comboBox_55.setItemText(3, QCoreApplication.translate("MainWindow", u"Grade 4", None))
        self.comboBox_55.setItemText(4, QCoreApplication.translate("MainWindow", u"Grade 5", None))
        self.comboBox_55.setItemText(5, QCoreApplication.translate("MainWindow", u"Grade 6", None))
        self.comboBox_55.setItemText(6, QCoreApplication.translate("MainWindow", u"Grade 7", None))
        self.comboBox_55.setItemText(7, QCoreApplication.translate("MainWindow", u"Grade 8", None))
        self.comboBox_55.setItemText(8, QCoreApplication.translate("MainWindow", u"Grade 9", None))

        self.comboBox_55.setPlaceholderText(QCoreApplication.translate("MainWindow", u"class .....", None))
        self.label_486.setText(QCoreApplication.translate("MainWindow", u"PLEASE FILL IN THE FROM TO PRINT THE REPORT", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.label_1325.setText(QCoreApplication.translate("MainWindow", u"Total Attendance :", None))
        self.label_1339.setText(QCoreApplication.translate("MainWindow", u"Term Ending :", None))
        self.label_1340.setText(QCoreApplication.translate("MainWindow", u"Next Term Begins :", None))
        self.label_1352.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.lineEdit_188.setPlaceholderText(QCoreApplication.translate("MainWindow", u"please enter today's date ...", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_26), QCoreApplication.translate("MainWindow", u"Grade 7-9", None))
        self.label_200.setText(QCoreApplication.translate("MainWindow", u"...............................................................................", None))
        self.label_201.setText(QCoreApplication.translate("MainWindow", u"...................", None))
        self.label_202.setText(QCoreApplication.translate("MainWindow", u"................", None))
        self.label_203.setText(QCoreApplication.translate("MainWindow", u"PUPILS TERMINAL PROGRESS REPORT", None))
        self.label_204.setText(QCoreApplication.translate("MainWindow", u"ID No_:", None))
        self.label_205.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_206.setText(QCoreApplication.translate("MainWindow", u"Name :", None))
        self.label_207.setText(QCoreApplication.translate("MainWindow", u"..................................", None))
        self.label_208.setText(QCoreApplication.translate("MainWindow", u"Term Endding :", None))
        self.label_209.setText(QCoreApplication.translate("MainWindow", u".............................", None))
        self.label_210.setText(QCoreApplication.translate("MainWindow", u"Next Term Begins :", None))
        self.label_211.setText(QCoreApplication.translate("MainWindow", u".............................", None))
        self.label_212.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.label_213.setText(QCoreApplication.translate("MainWindow", u"............................", None))
        self.label_214.setText(QCoreApplication.translate("MainWindow", u"Class :", None))
        self.label_215.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_266.setText(QCoreApplication.translate("MainWindow", u"SUJECTS", None))
        self.label_267.setText(QCoreApplication.translate("MainWindow", u"CLASS SCORE", None))
        self.label_268.setText(QCoreApplication.translate("MainWindow", u"50%", None))
        self.label_269.setText(QCoreApplication.translate("MainWindow", u"GRADE", None))
        self.label_270.setText(QCoreApplication.translate("MainWindow", u"REMARKS", None))
        self.label_271.setText(QCoreApplication.translate("MainWindow", u"English Language", None))
        self.label_272.setText(QCoreApplication.translate("MainWindow", u"Vocabulary Develop.", None))
        self.label_273.setText(QCoreApplication.translate("MainWindow", u"Mathematics", None))
        self.label_274.setText(QCoreApplication.translate("MainWindow", u"Natural Science", None))
        self.label_275.setText(QCoreApplication.translate("MainWindow", u"R. M. E", None))
        self.label_276.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.label_277.setText(QCoreApplication.translate("MainWindow", u"Computing", None))
        self.label_278.setText(QCoreApplication.translate("MainWindow", u"Creative Arts", None))
        self.label_279.setText(QCoreApplication.translate("MainWindow", u"OWOP", None))
        self.label_280.setText(QCoreApplication.translate("MainWindow", u"Attendances:", None))
        self.label_281.setText(QCoreApplication.translate("MainWindow", u"..............", None))
        self.label_282.setText(QCoreApplication.translate("MainWindow", u"Out of:", None))
        self.label_283.setText(QCoreApplication.translate("MainWindow", u"..............", None))
        self.label_284.setText(QCoreApplication.translate("MainWindow", u"Promoted To :", None))
        self.label_285.setText(QCoreApplication.translate("MainWindow", u"..............", None))
        self.label_286.setText(QCoreApplication.translate("MainWindow", u"...........................................................", None))
        self.label_287.setText(QCoreApplication.translate("MainWindow", u"Conduct:", None))
        self.label_288.setText(QCoreApplication.translate("MainWindow", u"Interest:", None))
        self.label_289.setText(QCoreApplication.translate("MainWindow", u"............................................................", None))
        self.label_290.setText(QCoreApplication.translate("MainWindow", u"Class Teacher's Remarks:", None))
        self.label_291.setText(QCoreApplication.translate("MainWindow", u"...........................................................", None))
        self.label_292.setText(QCoreApplication.translate("MainWindow", u".........................", None))
        self.label_293.setText(QCoreApplication.translate("MainWindow", u"Signature:", None))
        self.label_294.setText(QCoreApplication.translate("MainWindow", u"Principals Remarks:", None))
        self.label_295.setText(QCoreApplication.translate("MainWindow", u"...........................................................", None))
        self.label_296.setText(QCoreApplication.translate("MainWindow", u".........................", None))
        self.label_297.setText(QCoreApplication.translate("MainWindow", u"Signature:", None))
        self.label_479.setText(QCoreApplication.translate("MainWindow", u"EXAM SCORE", None))
        self.label_480.setText(QCoreApplication.translate("MainWindow", u"50%", None))
        self.label_481.setText(QCoreApplication.translate("MainWindow", u"TOTAL SCORE", None))
        self.label_482.setText(QCoreApplication.translate("MainWindow", u"100%", None))
        self.label_483.setText(QCoreApplication.translate("MainWindow", u"Tel :", None))
        self.label_484.setText(QCoreApplication.translate("MainWindow", u"Address :", None))
        self.bt_105.setText(QCoreApplication.translate("MainWindow", u"PRINT", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_43), QCoreApplication.translate("MainWindow", u"grade 1 -6 print", None))
        self.label_487.setText(QCoreApplication.translate("MainWindow", u"...............................................................................", None))
        self.label_488.setText(QCoreApplication.translate("MainWindow", u"...................", None))
        self.label_489.setText(QCoreApplication.translate("MainWindow", u"................", None))
        self.label_490.setText(QCoreApplication.translate("MainWindow", u"PUPILS TERMINAL PROGRESS REPORT", None))
        self.label_491.setText(QCoreApplication.translate("MainWindow", u"ID No_:", None))
        self.label_492.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_493.setText(QCoreApplication.translate("MainWindow", u"Name :", None))
        self.label_494.setText(QCoreApplication.translate("MainWindow", u"..................................", None))
        self.label_495.setText(QCoreApplication.translate("MainWindow", u"Term Endding :", None))
        self.label_496.setText(QCoreApplication.translate("MainWindow", u".............................", None))
        self.label_497.setText(QCoreApplication.translate("MainWindow", u"Next Term Begins :", None))
        self.label_498.setText(QCoreApplication.translate("MainWindow", u".............................", None))
        self.label_499.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.label_500.setText(QCoreApplication.translate("MainWindow", u"............................", None))
        self.label_501.setText(QCoreApplication.translate("MainWindow", u"Class :", None))
        self.label_502.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_503.setText(QCoreApplication.translate("MainWindow", u"SUJECTS", None))
        self.label_504.setText(QCoreApplication.translate("MainWindow", u"CLASS SCORE", None))
        self.label_505.setText(QCoreApplication.translate("MainWindow", u"50%", None))
        self.label_506.setText(QCoreApplication.translate("MainWindow", u"GRADE", None))
        self.label_507.setText(QCoreApplication.translate("MainWindow", u"REMARKS", None))
        self.label_508.setText(QCoreApplication.translate("MainWindow", u"English Language", None))
        self.label_509.setText(QCoreApplication.translate("MainWindow", u"Vocabulary Develop.", None))
        self.label_510.setText(QCoreApplication.translate("MainWindow", u"Mathematics", None))
        self.label_511.setText(QCoreApplication.translate("MainWindow", u"Natural Science", None))
        self.label_512.setText(QCoreApplication.translate("MainWindow", u"R. M. E", None))
        self.label_513.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.label_514.setText(QCoreApplication.translate("MainWindow", u"Computing", None))
        self.label_515.setText(QCoreApplication.translate("MainWindow", u"Creative Arts", None))
        self.label_516.setText(QCoreApplication.translate("MainWindow", u"OWOP", None))
        self.label_517.setText(QCoreApplication.translate("MainWindow", u"Attendances:", None))
        self.label_518.setText(QCoreApplication.translate("MainWindow", u"..............", None))
        self.label_519.setText(QCoreApplication.translate("MainWindow", u"Out of:", None))
        self.label_520.setText(QCoreApplication.translate("MainWindow", u"..............", None))
        self.label_521.setText(QCoreApplication.translate("MainWindow", u"Promoted To :", None))
        self.label_522.setText(QCoreApplication.translate("MainWindow", u"..............", None))
        self.label_523.setText(QCoreApplication.translate("MainWindow", u"...........................................................", None))
        self.label_524.setText(QCoreApplication.translate("MainWindow", u"Conduct:", None))
        self.label_525.setText(QCoreApplication.translate("MainWindow", u"Interest:", None))
        self.label_526.setText(QCoreApplication.translate("MainWindow", u"............................................................", None))
        self.label_527.setText(QCoreApplication.translate("MainWindow", u"Class Teacher's Remarks:", None))
        self.label_528.setText(QCoreApplication.translate("MainWindow", u"...........................................................", None))
        self.label_529.setText(QCoreApplication.translate("MainWindow", u".........................", None))
        self.label_530.setText(QCoreApplication.translate("MainWindow", u"Signature:", None))
        self.label_531.setText(QCoreApplication.translate("MainWindow", u"Principals Remarks:", None))
        self.label_532.setText(QCoreApplication.translate("MainWindow", u"...........................................................", None))
        self.label_533.setText(QCoreApplication.translate("MainWindow", u".........................", None))
        self.label_534.setText(QCoreApplication.translate("MainWindow", u"Signature:", None))
        self.label_535.setText(QCoreApplication.translate("MainWindow", u"EXAM SCORE", None))
        self.label_536.setText(QCoreApplication.translate("MainWindow", u"50%", None))
        self.label_537.setText(QCoreApplication.translate("MainWindow", u"TOTAL SCORE", None))
        self.label_538.setText(QCoreApplication.translate("MainWindow", u"100%", None))
        self.label_539.setText(QCoreApplication.translate("MainWindow", u"Tel :", None))
        self.label_540.setText(QCoreApplication.translate("MainWindow", u"Address :", None))
        self.bt_106.setText(QCoreApplication.translate("MainWindow", u"PRINT", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_44), QCoreApplication.translate("MainWindow", u"grade 7 - 9 print", None))
        self.label_1016.setText(QCoreApplication.translate("MainWindow", u"...............................................................................", None))
        self.label_1117.setText(QCoreApplication.translate("MainWindow", u"...................", None))
        self.label_1118.setText(QCoreApplication.translate("MainWindow", u"................", None))
        self.label_1119.setText(QCoreApplication.translate("MainWindow", u"PUPILS TERMINAL PROGRESS REPORT", None))
        self.label_1120.setText(QCoreApplication.translate("MainWindow", u"ID No_:", None))
        self.label_1121.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_1122.setText(QCoreApplication.translate("MainWindow", u"Name :", None))
        self.label_1123.setText(QCoreApplication.translate("MainWindow", u"..................................", None))
        self.label_1124.setText(QCoreApplication.translate("MainWindow", u"Term Endding :", None))
        self.label_1125.setText(QCoreApplication.translate("MainWindow", u".............................", None))
        self.label_1126.setText(QCoreApplication.translate("MainWindow", u"Next Term Begins :", None))
        self.label_1127.setText(QCoreApplication.translate("MainWindow", u".............................", None))
        self.label_1128.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.label_1129.setText(QCoreApplication.translate("MainWindow", u"............................", None))
        self.label_1130.setText(QCoreApplication.translate("MainWindow", u"Class :", None))
        self.label_1131.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_1132.setText(QCoreApplication.translate("MainWindow", u"SUJECTS", None))
        self.label_1133.setText(QCoreApplication.translate("MainWindow", u"CLASS SCORE", None))
        self.label_1134.setText(QCoreApplication.translate("MainWindow", u"50%", None))
        self.label_1135.setText(QCoreApplication.translate("MainWindow", u"GRADE", None))
        self.label_1136.setText(QCoreApplication.translate("MainWindow", u"REMARKS", None))
        self.label_1137.setText(QCoreApplication.translate("MainWindow", u"English Language", None))
        self.label_1138.setText(QCoreApplication.translate("MainWindow", u"Vocabulary Develop.", None))
        self.label_1139.setText(QCoreApplication.translate("MainWindow", u"Mathematics", None))
        self.label_1140.setText(QCoreApplication.translate("MainWindow", u"Natural Science", None))
        self.label_1141.setText(QCoreApplication.translate("MainWindow", u"R. M. E", None))
        self.label_1142.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.label_1143.setText(QCoreApplication.translate("MainWindow", u"Computing", None))
        self.label_1144.setText(QCoreApplication.translate("MainWindow", u"Creative Arts", None))
        self.label_1145.setText(QCoreApplication.translate("MainWindow", u"OWOP", None))
        self.label_1146.setText(QCoreApplication.translate("MainWindow", u"Attendances:", None))
        self.label_1147.setText(QCoreApplication.translate("MainWindow", u"..............", None))
        self.label_1148.setText(QCoreApplication.translate("MainWindow", u"Out of:", None))
        self.label_1149.setText(QCoreApplication.translate("MainWindow", u"..............", None))
        self.label_1150.setText(QCoreApplication.translate("MainWindow", u"Promoted To :", None))
        self.label_1151.setText(QCoreApplication.translate("MainWindow", u"..............", None))
        self.label_1152.setText(QCoreApplication.translate("MainWindow", u"...........................................................", None))
        self.label_1153.setText(QCoreApplication.translate("MainWindow", u"Conduct:", None))
        self.label_1154.setText(QCoreApplication.translate("MainWindow", u"Interest:", None))
        self.label_1155.setText(QCoreApplication.translate("MainWindow", u"............................................................", None))
        self.label_1156.setText(QCoreApplication.translate("MainWindow", u"Class Teacher's Remarks:", None))
        self.label_1157.setText(QCoreApplication.translate("MainWindow", u"...........................................................", None))
        self.label_1158.setText(QCoreApplication.translate("MainWindow", u".........................", None))
        self.label_1159.setText(QCoreApplication.translate("MainWindow", u"Signature:", None))
        self.label_1160.setText(QCoreApplication.translate("MainWindow", u"Principals Remarks:", None))
        self.label_1161.setText(QCoreApplication.translate("MainWindow", u"...........................................................", None))
        self.label_1162.setText(QCoreApplication.translate("MainWindow", u".........................", None))
        self.label_1163.setText(QCoreApplication.translate("MainWindow", u"Signature:", None))
        self.label_1164.setText(QCoreApplication.translate("MainWindow", u"EXAM SCORE", None))
        self.label_1165.setText(QCoreApplication.translate("MainWindow", u"50%", None))
        self.label_1166.setText(QCoreApplication.translate("MainWindow", u"TOTAL SCORE", None))
        self.label_1167.setText(QCoreApplication.translate("MainWindow", u"100%", None))
        self.label_1168.setText(QCoreApplication.translate("MainWindow", u"Tel :", None))
        self.label_1169.setText(QCoreApplication.translate("MainWindow", u"Address :", None))
        self.bt_124.setText(QCoreApplication.translate("MainWindow", u"PRINT", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_45), QCoreApplication.translate("MainWindow", u"crache print", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_23), QCoreApplication.translate("MainWindow", u"Student Report", None))
        self.groupBox_21.setTitle(QCoreApplication.translate("MainWindow", u"School Fees", None))
        self.label_222.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.label_223.setText(QCoreApplication.translate("MainWindow", u"Full Name :", None))
        self.label_224.setText(QCoreApplication.translate("MainWindow", u"Paid By :", None))
        self.label_225.setText(QCoreApplication.translate("MainWindow", u"Amount Paid :", None))
        self.label_226.setText(QCoreApplication.translate("MainWindow", u"Term :", None))
        self.comboBox_35.setItemText(0, QCoreApplication.translate("MainWindow", u"Term 1", None))
        self.comboBox_35.setItemText(1, QCoreApplication.translate("MainWindow", u"Term 2", None))
        self.comboBox_35.setItemText(2, QCoreApplication.translate("MainWindow", u"Term 3", None))

        self.comboBox_35.setPlaceholderText(QCoreApplication.translate("MainWindow", u"term ...", None))
        self.label_227.setText(QCoreApplication.translate("MainWindow", u"Class :", None))
        self.comboBox_34.setItemText(0, QCoreApplication.translate("MainWindow", u"Grade 1", None))
        self.comboBox_34.setItemText(1, QCoreApplication.translate("MainWindow", u"Grade 2", None))
        self.comboBox_34.setItemText(2, QCoreApplication.translate("MainWindow", u"Grade 3", None))
        self.comboBox_34.setItemText(3, QCoreApplication.translate("MainWindow", u"Grade 4", None))
        self.comboBox_34.setItemText(4, QCoreApplication.translate("MainWindow", u"Grade 5", None))
        self.comboBox_34.setItemText(5, QCoreApplication.translate("MainWindow", u"Grade 6", None))
        self.comboBox_34.setItemText(6, QCoreApplication.translate("MainWindow", u"Grade 7", None))
        self.comboBox_34.setItemText(7, QCoreApplication.translate("MainWindow", u"Grade 8", None))
        self.comboBox_34.setItemText(8, QCoreApplication.translate("MainWindow", u"Grade 9", None))

        self.comboBox_34.setPlaceholderText(QCoreApplication.translate("MainWindow", u"class .....", None))
        self.bt_64.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.bt_65.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.bt_66.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.bt_119.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.groupBox_22.setTitle(QCoreApplication.translate("MainWindow", u"Feeding Fees/Studies Fees", None))
        self.label_228.setText(QCoreApplication.translate("MainWindow", u"Class :", None))
        self.label_229.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.label_230.setText(QCoreApplication.translate("MainWindow", u"Amount Paid :", None))
        self.label_231.setText(QCoreApplication.translate("MainWindow", u"Full Name :", None))
        self.comboBox_36.setItemText(0, QCoreApplication.translate("MainWindow", u"Grade 1", None))
        self.comboBox_36.setItemText(1, QCoreApplication.translate("MainWindow", u"Grade 2", None))
        self.comboBox_36.setItemText(2, QCoreApplication.translate("MainWindow", u"Grade 3", None))
        self.comboBox_36.setItemText(3, QCoreApplication.translate("MainWindow", u"Grade 4", None))
        self.comboBox_36.setItemText(4, QCoreApplication.translate("MainWindow", u"Grade 5", None))
        self.comboBox_36.setItemText(5, QCoreApplication.translate("MainWindow", u"Grade 6", None))
        self.comboBox_36.setItemText(6, QCoreApplication.translate("MainWindow", u"Grade 7", None))
        self.comboBox_36.setItemText(7, QCoreApplication.translate("MainWindow", u"Grade 8", None))
        self.comboBox_36.setItemText(8, QCoreApplication.translate("MainWindow", u"Grade 9", None))

        self.comboBox_36.setPlaceholderText(QCoreApplication.translate("MainWindow", u"class .....", None))
        self.comboBox_47.setItemText(0, QCoreApplication.translate("MainWindow", u"Feeding Fees", None))
        self.comboBox_47.setItemText(1, QCoreApplication.translate("MainWindow", u"Studies Fees", None))

        self.comboBox_47.setPlaceholderText(QCoreApplication.translate("MainWindow", u" .....", None))
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"Type of Fees :", None))
        self.bt_116.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.bt_120.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.bt_67.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.bt_68.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.bt_69.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        ___qtablewidgetitem73 = self.tableWidget_11.horizontalHeaderItem(0)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"Full Name", None));
        ___qtablewidgetitem74 = self.tableWidget_11.horizontalHeaderItem(1)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"Class", None));
        ___qtablewidgetitem75 = self.tableWidget_11.horizontalHeaderItem(2)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"Term", None));
        ___qtablewidgetitem76 = self.tableWidget_11.horizontalHeaderItem(3)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"Amount Paid", None));
        ___qtablewidgetitem77 = self.tableWidget_11.horizontalHeaderItem(4)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"Paid By", None));
        ___qtablewidgetitem78 = self.tableWidget_11.horizontalHeaderItem(5)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem79 = self.tableWidget_12.horizontalHeaderItem(0)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"Full Name", None));
        ___qtablewidgetitem80 = self.tableWidget_12.horizontalHeaderItem(1)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"Class", None));
        ___qtablewidgetitem81 = self.tableWidget_12.horizontalHeaderItem(2)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"Type Of Fees", None));
        ___qtablewidgetitem82 = self.tableWidget_12.horizontalHeaderItem(3)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"Amount Paid", None));
        ___qtablewidgetitem83 = self.tableWidget_12.horizontalHeaderItem(4)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_27), QCoreApplication.translate("MainWindow", u"Student Fees", None))
        self.label_232.setText(QCoreApplication.translate("MainWindow", u"Message Subject :", None))
        self.label_233.setText(QCoreApplication.translate("MainWindow", u"To :", None))
        self.bt_70.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_28), QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"Expenses For :", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"Amout :", None))
        self.comboBox_49.setItemText(0, QCoreApplication.translate("MainWindow", u"School Fees", None))
        self.comboBox_49.setItemText(1, QCoreApplication.translate("MainWindow", u"Feeding Fees", None))
        self.comboBox_49.setItemText(2, QCoreApplication.translate("MainWindow", u"Studies Fees", None))

        self.comboBox_49.setPlaceholderText("")
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"Expenses From :", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"School Fees :", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"Feeding Fees :", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"From School Fees :", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"From Feeding Fees :", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"From Studies Fees :", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"Expenses :", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"Balances :", None))
        self.label_137.setText(QCoreApplication.translate("MainWindow", u"Feeding Fees :", None))
        self.label_158.setText(QCoreApplication.translate("MainWindow", u"Studies Fees :", None))
        self.label_159.setText(QCoreApplication.translate("MainWindow", u"School Fees :", None))
        self.label_160.setText(QCoreApplication.translate("MainWindow", u"..", None))
        self.label_161.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_162.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_163.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_164.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_165.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_166.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_167.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_168.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400; text-decoration: underline;\">Adding Expenses Used</span></p></body></html>", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u" School Fees", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"Feeding Fees", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"Studies Fees", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_54), QCoreApplication.translate("MainWindow", u"Expenses", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_18), QCoreApplication.translate("MainWindow", u"Management", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_16), QCoreApplication.translate("MainWindow", u"MONTESSORI", None))
        self.label_298.setText(QCoreApplication.translate("MainWindow", u"Student Management System For Cambridge Schools", None))
        self.label_299.setText("")
        self.bt_71.setText(QCoreApplication.translate("MainWindow", u"Get Started", None))
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.tab_30), QCoreApplication.translate("MainWindow", u"Welcome", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Total Number Of Students :", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"..", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Total School Fees :", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"..", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Total Feeding Fees :", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"..", None))
        self.bt_72.setText(QCoreApplication.translate("MainWindow", u"Add New Students", None))
        self.bt_73.setText(QCoreApplication.translate("MainWindow", u"Update Students", None))
        self.bt_74.setText(QCoreApplication.translate("MainWindow", u"Sudents Marks", None))
        self.bt_75.setText(QCoreApplication.translate("MainWindow", u"Attendances", None))
        self.bt_76.setText(QCoreApplication.translate("MainWindow", u"Students Reports", None))
        self.bt_77.setText(QCoreApplication.translate("MainWindow", u"Students Fees", None))
        self.bt_78.setText(QCoreApplication.translate("MainWindow", u"Send Email", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"Expenses", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.groupBox_23.setTitle(QCoreApplication.translate("MainWindow", u"Student's Details", None))
        self.label_300.setText(QCoreApplication.translate("MainWindow", u"Registration Number :", None))
        self.label_303.setText(QCoreApplication.translate("MainWindow", u"Date Of Birth :", None))
        self.label_304.setText(QCoreApplication.translate("MainWindow", u"Class :", None))
        self.comboBox_37.setItemText(0, QCoreApplication.translate("MainWindow", u"Crache", None))
        self.comboBox_37.setItemText(1, QCoreApplication.translate("MainWindow", u"Nursery 1", None))
        self.comboBox_37.setItemText(2, QCoreApplication.translate("MainWindow", u"Nursery 2", None))
        self.comboBox_37.setItemText(3, QCoreApplication.translate("MainWindow", u"Kindergaten 1", None))
        self.comboBox_37.setItemText(4, QCoreApplication.translate("MainWindow", u"Kindergaten 2", None))
        self.comboBox_37.setItemText(5, QCoreApplication.translate("MainWindow", u"Class 1", None))
        self.comboBox_37.setItemText(6, QCoreApplication.translate("MainWindow", u"Class 2", None))
        self.comboBox_37.setItemText(7, QCoreApplication.translate("MainWindow", u"Class 3", None))
        self.comboBox_37.setItemText(8, QCoreApplication.translate("MainWindow", u"Class 4", None))
        self.comboBox_37.setItemText(9, QCoreApplication.translate("MainWindow", u"Class 5", None))
        self.comboBox_37.setItemText(10, QCoreApplication.translate("MainWindow", u"Class 6", None))
        self.comboBox_37.setItemText(11, QCoreApplication.translate("MainWindow", u"JHS 1", None))
        self.comboBox_37.setItemText(12, QCoreApplication.translate("MainWindow", u"JHS 2", None))
        self.comboBox_37.setItemText(13, QCoreApplication.translate("MainWindow", u"JHS 3", None))

        self.comboBox_37.setPlaceholderText(QCoreApplication.translate("MainWindow", u"class .....", None))
        self.comboBox_38.setItemText(0, QCoreApplication.translate("MainWindow", u"Male", None))
        self.comboBox_38.setItemText(1, QCoreApplication.translate("MainWindow", u"Female", None))

        self.comboBox_38.setPlaceholderText(QCoreApplication.translate("MainWindow", u"gender.....", None))
        self.label_305.setText(QCoreApplication.translate("MainWindow", u"Gender :", None))
        self.label_306.setText(QCoreApplication.translate("MainWindow", u"Home Address :", None))
        self.textEdit_5.setPlaceholderText("")
        self.lineEdit_95.setPlaceholderText("")
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Full Name :", None))
        self.groupBox_24.setTitle(QCoreApplication.translate("MainWindow", u"Parent's Details", None))
        self.label_307.setText(QCoreApplication.translate("MainWindow", u"Phone Number :", None))
        self.label_308.setText(QCoreApplication.translate("MainWindow", u"Parent Full Name :", None))
        self.label_309.setText(QCoreApplication.translate("MainWindow", u"Email Address :", None))
        self.bt_79.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.bt_80.setText(QCoreApplication.translate("MainWindow", u"View", None))
        ___qtablewidgetitem84 = self.tableWidget_13.horizontalHeaderItem(0)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"Reg_No:-", None));
        ___qtablewidgetitem85 = self.tableWidget_13.horizontalHeaderItem(1)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("MainWindow", u"Full Name", None));
        ___qtablewidgetitem86 = self.tableWidget_13.horizontalHeaderItem(2)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("MainWindow", u"Date Of Birth", None));
        ___qtablewidgetitem87 = self.tableWidget_13.horizontalHeaderItem(3)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("MainWindow", u"Class", None));
        ___qtablewidgetitem88 = self.tableWidget_13.horizontalHeaderItem(4)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("MainWindow", u"Gender", None));
        ___qtablewidgetitem89 = self.tableWidget_13.horizontalHeaderItem(5)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("MainWindow", u"Home Address", None));
        ___qtablewidgetitem90 = self.tableWidget_13.horizontalHeaderItem(6)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("MainWindow", u"Parent Full Name", None));
        ___qtablewidgetitem91 = self.tableWidget_13.horizontalHeaderItem(7)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None));
        ___qtablewidgetitem92 = self.tableWidget_13.horizontalHeaderItem(8)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("MainWindow", u"Email Address", None));
        self.tabWidget_10.setTabText(self.tabWidget_10.indexOf(self.tab_32), QCoreApplication.translate("MainWindow", u"Add_student", None))
        self.groupBox_25.setTitle(QCoreApplication.translate("MainWindow", u"Student's Details", None))
        self.label_310.setText(QCoreApplication.translate("MainWindow", u"Registration Number :", None))
        self.lineEdit_81.setInputMask("")
        self.lineEdit_81.setText("")
        self.label_313.setText(QCoreApplication.translate("MainWindow", u"Date Of Birth :", None))
        self.label_314.setText(QCoreApplication.translate("MainWindow", u"Class :", None))
        self.comboBox_39.setItemText(0, QCoreApplication.translate("MainWindow", u"Male", None))
        self.comboBox_39.setItemText(1, QCoreApplication.translate("MainWindow", u"Female", None))

        self.comboBox_39.setPlaceholderText(QCoreApplication.translate("MainWindow", u"gender...", None))
        self.label_315.setText(QCoreApplication.translate("MainWindow", u"Gender :", None))
        self.label_316.setText(QCoreApplication.translate("MainWindow", u"Home Address :", None))
        self.comboBox_40.setItemText(0, QCoreApplication.translate("MainWindow", u"Grade 1", None))
        self.comboBox_40.setItemText(1, QCoreApplication.translate("MainWindow", u"Grade 2", None))
        self.comboBox_40.setItemText(2, QCoreApplication.translate("MainWindow", u"Grade 3", None))
        self.comboBox_40.setItemText(3, QCoreApplication.translate("MainWindow", u"Grade 4", None))
        self.comboBox_40.setItemText(4, QCoreApplication.translate("MainWindow", u"Grade 5", None))
        self.comboBox_40.setItemText(5, QCoreApplication.translate("MainWindow", u"Grade 6", None))
        self.comboBox_40.setItemText(6, QCoreApplication.translate("MainWindow", u"Grade 7", None))
        self.comboBox_40.setItemText(7, QCoreApplication.translate("MainWindow", u"Grade 8", None))
        self.comboBox_40.setItemText(8, QCoreApplication.translate("MainWindow", u"Grade 9", None))

        self.comboBox_40.setPlaceholderText(QCoreApplication.translate("MainWindow", u"class .....", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Full Name :", None))
        self.groupBox_26.setTitle(QCoreApplication.translate("MainWindow", u"Parent's Details", None))
        self.label_317.setText(QCoreApplication.translate("MainWindow", u"Phone Number :", None))
        self.label_318.setText(QCoreApplication.translate("MainWindow", u"Parent Full Name :", None))
        self.label_319.setText(QCoreApplication.translate("MainWindow", u"Email Address :", None))
        self.bt_81.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.bt_82.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.bt_83.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.bt_84.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        ___qtablewidgetitem93 = self.tableWidget_14.horizontalHeaderItem(0)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("MainWindow", u"Reg_No:-", None));
        ___qtablewidgetitem94 = self.tableWidget_14.horizontalHeaderItem(1)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("MainWindow", u"Full Name", None));
        ___qtablewidgetitem95 = self.tableWidget_14.horizontalHeaderItem(2)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("MainWindow", u"Date Of Birth", None));
        ___qtablewidgetitem96 = self.tableWidget_14.horizontalHeaderItem(3)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("MainWindow", u"Class", None));
        ___qtablewidgetitem97 = self.tableWidget_14.horizontalHeaderItem(4)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("MainWindow", u"Gender", None));
        ___qtablewidgetitem98 = self.tableWidget_14.horizontalHeaderItem(5)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("MainWindow", u"Home Address", None));
        ___qtablewidgetitem99 = self.tableWidget_14.horizontalHeaderItem(6)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("MainWindow", u"Parent Full Name", None));
        ___qtablewidgetitem100 = self.tableWidget_14.horizontalHeaderItem(7)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None));
        ___qtablewidgetitem101 = self.tableWidget_14.horizontalHeaderItem(8)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("MainWindow", u"Email Address", None));
        self.tabWidget_10.setTabText(self.tabWidget_10.indexOf(self.tab_33), QCoreApplication.translate("MainWindow", u"Update_student", None))
        self.groupBox_27.setTitle(QCoreApplication.translate("MainWindow", u"Student Marks", None))
        self.label_320.setText(QCoreApplication.translate("MainWindow", u"Full Name :", None))
        self.label_321.setText(QCoreApplication.translate("MainWindow", u"Class :", None))
        self.label_322.setText(QCoreApplication.translate("MainWindow", u"Registration Number :", None))
        self.comboBox_41.setItemText(0, QCoreApplication.translate("MainWindow", u"English Language", None))
        self.comboBox_41.setItemText(1, QCoreApplication.translate("MainWindow", u"Vocabulary Development", None))
        self.comboBox_41.setItemText(2, QCoreApplication.translate("MainWindow", u"Mathematics", None))
        self.comboBox_41.setItemText(3, QCoreApplication.translate("MainWindow", u"Computing", None))
        self.comboBox_41.setItemText(4, QCoreApplication.translate("MainWindow", u"Natural Science", None))
        self.comboBox_41.setItemText(5, QCoreApplication.translate("MainWindow", u"Religious and Moral Education", None))
        self.comboBox_41.setItemText(6, QCoreApplication.translate("MainWindow", u"History", None))
        self.comboBox_41.setItemText(7, QCoreApplication.translate("MainWindow", u"Creative Arts", None))
        self.comboBox_41.setItemText(8, QCoreApplication.translate("MainWindow", u"Our World Our People", None))

        self.comboBox_41.setPlaceholderText(QCoreApplication.translate("MainWindow", u"subject...", None))
        self.label_323.setText(QCoreApplication.translate("MainWindow", u"Subjects :", None))
        self.comboBox_42.setItemText(0, QCoreApplication.translate("MainWindow", u"Term 1", None))
        self.comboBox_42.setItemText(1, QCoreApplication.translate("MainWindow", u"Term 2", None))
        self.comboBox_42.setItemText(2, QCoreApplication.translate("MainWindow", u"Term 3", None))

        self.comboBox_42.setPlaceholderText(QCoreApplication.translate("MainWindow", u"term ...", None))
        self.label_324.setText(QCoreApplication.translate("MainWindow", u"Term :", None))
        self.comboBox_43.setItemText(0, QCoreApplication.translate("MainWindow", u"Exams", None))
        self.comboBox_43.setItemText(1, QCoreApplication.translate("MainWindow", u"Class Work", None))
        self.comboBox_43.setItemText(2, QCoreApplication.translate("MainWindow", u"Projects", None))

        self.comboBox_43.setPlaceholderText(QCoreApplication.translate("MainWindow", u"type...", None))
        self.label_325.setText(QCoreApplication.translate("MainWindow", u"Marks Type :", None))
        self.label_326.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.comboBox_44.setItemText(0, QCoreApplication.translate("MainWindow", u"Grade 1", None))
        self.comboBox_44.setItemText(1, QCoreApplication.translate("MainWindow", u"Grade 2", None))
        self.comboBox_44.setItemText(2, QCoreApplication.translate("MainWindow", u"Grade 3", None))
        self.comboBox_44.setItemText(3, QCoreApplication.translate("MainWindow", u"Grade 4", None))
        self.comboBox_44.setItemText(4, QCoreApplication.translate("MainWindow", u"Grade 5", None))
        self.comboBox_44.setItemText(5, QCoreApplication.translate("MainWindow", u"Grade 6", None))
        self.comboBox_44.setItemText(6, QCoreApplication.translate("MainWindow", u"Grade 7", None))
        self.comboBox_44.setItemText(7, QCoreApplication.translate("MainWindow", u"Grade 8", None))
        self.comboBox_44.setItemText(8, QCoreApplication.translate("MainWindow", u"Grade 9", None))

        self.comboBox_44.setPlaceholderText(QCoreApplication.translate("MainWindow", u"class .....", None))
        self.label_347.setText(QCoreApplication.translate("MainWindow", u"Grade :", None))
        self.label_348.setText(QCoreApplication.translate("MainWindow", u"Marks :", None))
        self.comboBox_46.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_46.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_46.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_46.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_46.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_46.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_46.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_46.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_46.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))

        self.comboBox_46.setPlaceholderText(QCoreApplication.translate("MainWindow", u"type...", None))
        self.bt_85.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.bt_86.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.bt_87.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.bt_88.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.bt_89.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.lineEdit_90.setPlaceholderText(QCoreApplication.translate("MainWindow", u"search by name", None))
        ___qtablewidgetitem102 = self.tableWidget_15.horizontalHeaderItem(0)
        ___qtablewidgetitem102.setText(QCoreApplication.translate("MainWindow", u"Reg_No:-", None));
        ___qtablewidgetitem103 = self.tableWidget_15.horizontalHeaderItem(1)
        ___qtablewidgetitem103.setText(QCoreApplication.translate("MainWindow", u"Full Name", None));
        ___qtablewidgetitem104 = self.tableWidget_15.horizontalHeaderItem(2)
        ___qtablewidgetitem104.setText(QCoreApplication.translate("MainWindow", u"Class", None));
        ___qtablewidgetitem105 = self.tableWidget_15.horizontalHeaderItem(3)
        ___qtablewidgetitem105.setText(QCoreApplication.translate("MainWindow", u"Subjects", None));
        ___qtablewidgetitem106 = self.tableWidget_15.horizontalHeaderItem(4)
        ___qtablewidgetitem106.setText(QCoreApplication.translate("MainWindow", u"Term", None));
        ___qtablewidgetitem107 = self.tableWidget_15.horizontalHeaderItem(5)
        ___qtablewidgetitem107.setText(QCoreApplication.translate("MainWindow", u"Marks Type", None));
        ___qtablewidgetitem108 = self.tableWidget_15.horizontalHeaderItem(6)
        ___qtablewidgetitem108.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem109 = self.tableWidget_15.horizontalHeaderItem(7)
        ___qtablewidgetitem109.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem110 = self.tableWidget_15.horizontalHeaderItem(8)
        ___qtablewidgetitem110.setText(QCoreApplication.translate("MainWindow", u"Marks", None));
        self.tabWidget_10.setTabText(self.tabWidget_10.indexOf(self.tab_34), QCoreApplication.translate("MainWindow", u"Student Marks", None))
        self.groupBox_28.setTitle(QCoreApplication.translate("MainWindow", u"Attendance", None))
        self.label_327.setText(QCoreApplication.translate("MainWindow", u"Registration Number :", None))
        self.label_328.setText(QCoreApplication.translate("MainWindow", u"Full Name :", None))
        self.label_329.setText(QCoreApplication.translate("MainWindow", u"Class :", None))
        self.label_330.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.comboBox_45.setItemText(0, QCoreApplication.translate("MainWindow", u"Grade 1", None))
        self.comboBox_45.setItemText(1, QCoreApplication.translate("MainWindow", u"Grade 2", None))
        self.comboBox_45.setItemText(2, QCoreApplication.translate("MainWindow", u"Grade 3", None))
        self.comboBox_45.setItemText(3, QCoreApplication.translate("MainWindow", u"Grade 4", None))
        self.comboBox_45.setItemText(4, QCoreApplication.translate("MainWindow", u"Grade 5", None))
        self.comboBox_45.setItemText(5, QCoreApplication.translate("MainWindow", u"Grade 6", None))
        self.comboBox_45.setItemText(6, QCoreApplication.translate("MainWindow", u"Grade 7", None))
        self.comboBox_45.setItemText(7, QCoreApplication.translate("MainWindow", u"Grade 8", None))
        self.comboBox_45.setItemText(8, QCoreApplication.translate("MainWindow", u"Grade 9", None))

        self.comboBox_45.setPlaceholderText(QCoreApplication.translate("MainWindow", u"class .....", None))
        self.bt_90.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.bt_91.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.bt_92.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.bt_93.setText(QCoreApplication.translate("MainWindow", u"View", None))
        ___qtablewidgetitem111 = self.tableWidget_16.horizontalHeaderItem(0)
        ___qtablewidgetitem111.setText(QCoreApplication.translate("MainWindow", u"Reg_No:-", None));
        ___qtablewidgetitem112 = self.tableWidget_16.horizontalHeaderItem(1)
        ___qtablewidgetitem112.setText(QCoreApplication.translate("MainWindow", u"Full Name", None));
        ___qtablewidgetitem113 = self.tableWidget_16.horizontalHeaderItem(2)
        ___qtablewidgetitem113.setText(QCoreApplication.translate("MainWindow", u"Class", None));
        ___qtablewidgetitem114 = self.tableWidget_16.horizontalHeaderItem(3)
        ___qtablewidgetitem114.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        self.tabWidget_10.setTabText(self.tabWidget_10.indexOf(self.tab_35), QCoreApplication.translate("MainWindow", u"Attendance", None))
        self.bt_94.setText(QCoreApplication.translate("MainWindow", u"Crache/Nursery", None))
        self.bt_95.setText(QCoreApplication.translate("MainWindow", u"Grade 1 - 6", None))
        self.bt_96.setText(QCoreApplication.translate("MainWindow", u"Grade 7 - 9", None))
        self.groupBox_39.setTitle("")
        self.label_264.setText(QCoreApplication.translate("MainWindow", u"Full Name :", None))
        self.comboBox_63.setItemText(0, QCoreApplication.translate("MainWindow", u"Term 1", None))
        self.comboBox_63.setItemText(1, QCoreApplication.translate("MainWindow", u"Term 2", None))
        self.comboBox_63.setItemText(2, QCoreApplication.translate("MainWindow", u"Term 3", None))

        self.comboBox_63.setPlaceholderText(QCoreApplication.translate("MainWindow", u"term ...", None))
        self.label_265.setText(QCoreApplication.translate("MainWindow", u"Term :", None))
        self.label_331.setText(QCoreApplication.translate("MainWindow", u"Class :", None))
        self.label_332.setText(QCoreApplication.translate("MainWindow", u"School Name :", None))
        self.label_333.setText(QCoreApplication.translate("MainWindow", u"School Address :", None))
        self.label_334.setText(QCoreApplication.translate("MainWindow", u"Phone Number :", None))
        self.comboBox_64.setItemText(0, QCoreApplication.translate("MainWindow", u"Grade 1", None))
        self.comboBox_64.setItemText(1, QCoreApplication.translate("MainWindow", u"Grade 2", None))
        self.comboBox_64.setItemText(2, QCoreApplication.translate("MainWindow", u"Grade 3", None))
        self.comboBox_64.setItemText(3, QCoreApplication.translate("MainWindow", u"Grade 4", None))
        self.comboBox_64.setItemText(4, QCoreApplication.translate("MainWindow", u"Grade 5", None))
        self.comboBox_64.setItemText(5, QCoreApplication.translate("MainWindow", u"Grade 6", None))
        self.comboBox_64.setItemText(6, QCoreApplication.translate("MainWindow", u"Grade 7", None))
        self.comboBox_64.setItemText(7, QCoreApplication.translate("MainWindow", u"Grade 8", None))
        self.comboBox_64.setItemText(8, QCoreApplication.translate("MainWindow", u"Grade 9", None))

        self.comboBox_64.setPlaceholderText(QCoreApplication.translate("MainWindow", u"class .....", None))
        self.label_848.setText(QCoreApplication.translate("MainWindow", u"Promoted To:", None))
        self.comboBox_66.setItemText(0, QCoreApplication.translate("MainWindow", u"Grade 1", None))
        self.comboBox_66.setItemText(1, QCoreApplication.translate("MainWindow", u"Grade 2", None))
        self.comboBox_66.setItemText(2, QCoreApplication.translate("MainWindow", u"Grade 3", None))
        self.comboBox_66.setItemText(3, QCoreApplication.translate("MainWindow", u"Grade 4", None))
        self.comboBox_66.setItemText(4, QCoreApplication.translate("MainWindow", u"Grade 5", None))
        self.comboBox_66.setItemText(5, QCoreApplication.translate("MainWindow", u"Grade 6", None))
        self.comboBox_66.setItemText(6, QCoreApplication.translate("MainWindow", u"Grade 7", None))
        self.comboBox_66.setItemText(7, QCoreApplication.translate("MainWindow", u"Grade 8", None))
        self.comboBox_66.setItemText(8, QCoreApplication.translate("MainWindow", u"Grade 9", None))

        self.comboBox_66.setPlaceholderText(QCoreApplication.translate("MainWindow", u"class .....", None))
        self.label_849.setText(QCoreApplication.translate("MainWindow", u"PLEASE FILL IN THE FROM TO PRINT THE REPORT", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.label_1326.setText(QCoreApplication.translate("MainWindow", u"Total Attendance :", None))
        self.label_1341.setText(QCoreApplication.translate("MainWindow", u"Term Ending :", None))
        self.label_1342.setText(QCoreApplication.translate("MainWindow", u"Next Term Begins :", None))
        self.label_1355.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.lineEdit_191.setPlaceholderText(QCoreApplication.translate("MainWindow", u"please enter today's date ...", None))
        self.tabWidget_11.setTabText(self.tabWidget_11.indexOf(self.tab_37), QCoreApplication.translate("MainWindow", u"Crache", None))
        self.groupBox_40.setTitle(QCoreApplication.translate("MainWindow", u"Grade 1 - 6", None))
        self.label_335.setText(QCoreApplication.translate("MainWindow", u"Full Name :", None))
        self.comboBox_67.setItemText(0, QCoreApplication.translate("MainWindow", u"Term 1", None))
        self.comboBox_67.setItemText(1, QCoreApplication.translate("MainWindow", u"Term 2", None))
        self.comboBox_67.setItemText(2, QCoreApplication.translate("MainWindow", u"Term 3", None))

        self.comboBox_67.setPlaceholderText(QCoreApplication.translate("MainWindow", u"term ...", None))
        self.label_336.setText(QCoreApplication.translate("MainWindow", u"Term :", None))
        self.label_337.setText(QCoreApplication.translate("MainWindow", u"Class :", None))
        self.label_338.setText(QCoreApplication.translate("MainWindow", u"School Name :", None))
        self.label_339.setText(QCoreApplication.translate("MainWindow", u"School Address :", None))
        self.label_340.setText(QCoreApplication.translate("MainWindow", u"Phone Number :", None))
        self.comboBox_69.setItemText(0, QCoreApplication.translate("MainWindow", u"Grade 1", None))
        self.comboBox_69.setItemText(1, QCoreApplication.translate("MainWindow", u"Grade 2", None))
        self.comboBox_69.setItemText(2, QCoreApplication.translate("MainWindow", u"Grade 3", None))
        self.comboBox_69.setItemText(3, QCoreApplication.translate("MainWindow", u"Grade 4", None))
        self.comboBox_69.setItemText(4, QCoreApplication.translate("MainWindow", u"Grade 5", None))
        self.comboBox_69.setItemText(5, QCoreApplication.translate("MainWindow", u"Grade 6", None))
        self.comboBox_69.setItemText(6, QCoreApplication.translate("MainWindow", u"Grade 7", None))
        self.comboBox_69.setItemText(7, QCoreApplication.translate("MainWindow", u"Grade 8", None))
        self.comboBox_69.setItemText(8, QCoreApplication.translate("MainWindow", u"Grade 9", None))

        self.comboBox_69.setPlaceholderText(QCoreApplication.translate("MainWindow", u"class .....", None))
        self.label_850.setText(QCoreApplication.translate("MainWindow", u"Promoted To:", None))
        self.comboBox_70.setItemText(0, QCoreApplication.translate("MainWindow", u"Grade 1", None))
        self.comboBox_70.setItemText(1, QCoreApplication.translate("MainWindow", u"Grade 2", None))
        self.comboBox_70.setItemText(2, QCoreApplication.translate("MainWindow", u"Grade 3", None))
        self.comboBox_70.setItemText(3, QCoreApplication.translate("MainWindow", u"Grade 4", None))
        self.comboBox_70.setItemText(4, QCoreApplication.translate("MainWindow", u"Grade 5", None))
        self.comboBox_70.setItemText(5, QCoreApplication.translate("MainWindow", u"Grade 6", None))
        self.comboBox_70.setItemText(6, QCoreApplication.translate("MainWindow", u"Grade 7", None))
        self.comboBox_70.setItemText(7, QCoreApplication.translate("MainWindow", u"Grade 8", None))
        self.comboBox_70.setItemText(8, QCoreApplication.translate("MainWindow", u"Grade 9", None))

        self.comboBox_70.setPlaceholderText(QCoreApplication.translate("MainWindow", u"class .....", None))
        self.label_851.setText(QCoreApplication.translate("MainWindow", u"PLEASE FILL IN THE FROM TO PRINT THE REPORT", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.label_1327.setText(QCoreApplication.translate("MainWindow", u"Total Attendance :", None))
        self.label_1343.setText(QCoreApplication.translate("MainWindow", u"Term Ending :", None))
        self.label_1344.setText(QCoreApplication.translate("MainWindow", u"Next Term Begins :", None))
        self.label_1354.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.lineEdit_190.setPlaceholderText(QCoreApplication.translate("MainWindow", u"please enter today's date ...", None))
        self.tabWidget_11.setTabText(self.tabWidget_11.indexOf(self.tab_38), QCoreApplication.translate("MainWindow", u"Grade 1-6", None))
        self.groupBox_41.setTitle(QCoreApplication.translate("MainWindow", u"Grade 7 -9", None))
        self.label_341.setText(QCoreApplication.translate("MainWindow", u"Full Name :", None))
        self.comboBox_71.setItemText(0, QCoreApplication.translate("MainWindow", u"Term 1", None))
        self.comboBox_71.setItemText(1, QCoreApplication.translate("MainWindow", u"Term 2", None))
        self.comboBox_71.setItemText(2, QCoreApplication.translate("MainWindow", u"Term 3", None))

        self.comboBox_71.setPlaceholderText(QCoreApplication.translate("MainWindow", u"term ...", None))
        self.label_342.setText(QCoreApplication.translate("MainWindow", u"Term :", None))
        self.label_343.setText(QCoreApplication.translate("MainWindow", u"Class :", None))
        self.label_344.setText(QCoreApplication.translate("MainWindow", u"School Name :", None))
        self.label_345.setText(QCoreApplication.translate("MainWindow", u"School Address :", None))
        self.label_346.setText(QCoreApplication.translate("MainWindow", u"Phone Number :", None))
        self.comboBox_72.setItemText(0, QCoreApplication.translate("MainWindow", u"Grade 1", None))
        self.comboBox_72.setItemText(1, QCoreApplication.translate("MainWindow", u"Grade 2", None))
        self.comboBox_72.setItemText(2, QCoreApplication.translate("MainWindow", u"Grade 3", None))
        self.comboBox_72.setItemText(3, QCoreApplication.translate("MainWindow", u"Grade 4", None))
        self.comboBox_72.setItemText(4, QCoreApplication.translate("MainWindow", u"Grade 5", None))
        self.comboBox_72.setItemText(5, QCoreApplication.translate("MainWindow", u"Grade 6", None))
        self.comboBox_72.setItemText(6, QCoreApplication.translate("MainWindow", u"Grade 7", None))
        self.comboBox_72.setItemText(7, QCoreApplication.translate("MainWindow", u"Grade 8", None))
        self.comboBox_72.setItemText(8, QCoreApplication.translate("MainWindow", u"Grade 9", None))

        self.comboBox_72.setPlaceholderText(QCoreApplication.translate("MainWindow", u"class .....", None))
        self.label_852.setText(QCoreApplication.translate("MainWindow", u"Promoted To:", None))
        self.comboBox_73.setItemText(0, QCoreApplication.translate("MainWindow", u"Grade 1", None))
        self.comboBox_73.setItemText(1, QCoreApplication.translate("MainWindow", u"Grade 2", None))
        self.comboBox_73.setItemText(2, QCoreApplication.translate("MainWindow", u"Grade 3", None))
        self.comboBox_73.setItemText(3, QCoreApplication.translate("MainWindow", u"Grade 4", None))
        self.comboBox_73.setItemText(4, QCoreApplication.translate("MainWindow", u"Grade 5", None))
        self.comboBox_73.setItemText(5, QCoreApplication.translate("MainWindow", u"Grade 6", None))
        self.comboBox_73.setItemText(6, QCoreApplication.translate("MainWindow", u"Grade 7", None))
        self.comboBox_73.setItemText(7, QCoreApplication.translate("MainWindow", u"Grade 8", None))
        self.comboBox_73.setItemText(8, QCoreApplication.translate("MainWindow", u"Grade 9", None))

        self.comboBox_73.setPlaceholderText(QCoreApplication.translate("MainWindow", u"class .....", None))
        self.label_853.setText(QCoreApplication.translate("MainWindow", u"PLEASE FILL IN THE FROM TO PRINT THE REPORT", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.label_1328.setText(QCoreApplication.translate("MainWindow", u"Total Attendance :", None))
        self.label_1345.setText(QCoreApplication.translate("MainWindow", u"Term Ending :", None))
        self.label_1346.setText(QCoreApplication.translate("MainWindow", u"Next Term Begins :", None))
        self.label_1353.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.lineEdit_189.setPlaceholderText(QCoreApplication.translate("MainWindow", u"please enter today's date ...", None))
        self.tabWidget_11.setTabText(self.tabWidget_11.indexOf(self.tab_39), QCoreApplication.translate("MainWindow", u"Grade 7-9", None))
        self.label_962.setText(QCoreApplication.translate("MainWindow", u"...............................................................................", None))
        self.label_963.setText(QCoreApplication.translate("MainWindow", u"...................", None))
        self.label_964.setText(QCoreApplication.translate("MainWindow", u"................", None))
        self.label_965.setText(QCoreApplication.translate("MainWindow", u"PUPILS TERMINAL PROGRESS REPORT", None))
        self.label_966.setText(QCoreApplication.translate("MainWindow", u"ID No_:", None))
        self.label_967.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_968.setText(QCoreApplication.translate("MainWindow", u"Name :", None))
        self.label_969.setText(QCoreApplication.translate("MainWindow", u"..................................", None))
        self.label_970.setText(QCoreApplication.translate("MainWindow", u"Term Endding :", None))
        self.label_971.setText(QCoreApplication.translate("MainWindow", u".............................", None))
        self.label_972.setText(QCoreApplication.translate("MainWindow", u"Next Term Begins :", None))
        self.label_973.setText(QCoreApplication.translate("MainWindow", u".............................", None))
        self.label_974.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.label_975.setText(QCoreApplication.translate("MainWindow", u"............................", None))
        self.label_976.setText(QCoreApplication.translate("MainWindow", u"Class :", None))
        self.label_977.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_978.setText(QCoreApplication.translate("MainWindow", u"SUJECTS", None))
        self.label_979.setText(QCoreApplication.translate("MainWindow", u"CLASS SCORE", None))
        self.label_980.setText(QCoreApplication.translate("MainWindow", u"50%", None))
        self.label_981.setText(QCoreApplication.translate("MainWindow", u"GRADE", None))
        self.label_982.setText(QCoreApplication.translate("MainWindow", u"REMARKS", None))
        self.label_983.setText(QCoreApplication.translate("MainWindow", u"English Language", None))
        self.label_984.setText(QCoreApplication.translate("MainWindow", u"Vocabulary Develop.", None))
        self.label_985.setText(QCoreApplication.translate("MainWindow", u"Mathematics", None))
        self.label_986.setText(QCoreApplication.translate("MainWindow", u"Natural Science", None))
        self.label_987.setText(QCoreApplication.translate("MainWindow", u"R. M. E", None))
        self.label_988.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.label_989.setText(QCoreApplication.translate("MainWindow", u"Computing", None))
        self.label_990.setText(QCoreApplication.translate("MainWindow", u"Creative Arts", None))
        self.label_991.setText(QCoreApplication.translate("MainWindow", u"OWOP", None))
        self.label_992.setText(QCoreApplication.translate("MainWindow", u"Attendances:", None))
        self.label_993.setText(QCoreApplication.translate("MainWindow", u"..............", None))
        self.label_994.setText(QCoreApplication.translate("MainWindow", u"Out of:", None))
        self.label_995.setText(QCoreApplication.translate("MainWindow", u"..............", None))
        self.label_996.setText(QCoreApplication.translate("MainWindow", u"Promoted To :", None))
        self.label_997.setText(QCoreApplication.translate("MainWindow", u"..............", None))
        self.label_998.setText(QCoreApplication.translate("MainWindow", u"...........................................................", None))
        self.label_999.setText(QCoreApplication.translate("MainWindow", u"Conduct:", None))
        self.label_1000.setText(QCoreApplication.translate("MainWindow", u"Interest:", None))
        self.label_1001.setText(QCoreApplication.translate("MainWindow", u"............................................................", None))
        self.label_1002.setText(QCoreApplication.translate("MainWindow", u"Class Teacher's Remarks:", None))
        self.label_1003.setText(QCoreApplication.translate("MainWindow", u"...........................................................", None))
        self.label_1004.setText(QCoreApplication.translate("MainWindow", u".........................", None))
        self.label_1005.setText(QCoreApplication.translate("MainWindow", u"Signature:", None))
        self.label_1006.setText(QCoreApplication.translate("MainWindow", u"Principals Remarks:", None))
        self.label_1007.setText(QCoreApplication.translate("MainWindow", u"...........................................................", None))
        self.label_1008.setText(QCoreApplication.translate("MainWindow", u".........................", None))
        self.label_1009.setText(QCoreApplication.translate("MainWindow", u"Signature:", None))
        self.label_1010.setText(QCoreApplication.translate("MainWindow", u"EXAM SCORE", None))
        self.label_1011.setText(QCoreApplication.translate("MainWindow", u"50%", None))
        self.label_1012.setText(QCoreApplication.translate("MainWindow", u"TOTAL SCORE", None))
        self.label_1013.setText(QCoreApplication.translate("MainWindow", u"100%", None))
        self.label_1014.setText(QCoreApplication.translate("MainWindow", u"Tel :", None))
        self.label_1015.setText(QCoreApplication.translate("MainWindow", u"Address :", None))
        self.bt_112.setText(QCoreApplication.translate("MainWindow", u"PRINT", None))
        self.tabWidget_11.setTabText(self.tabWidget_11.indexOf(self.tab_49), QCoreApplication.translate("MainWindow", u"crache print", None))
        self.label_908.setText(QCoreApplication.translate("MainWindow", u"...............................................................................", None))
        self.label_909.setText(QCoreApplication.translate("MainWindow", u"...................", None))
        self.label_910.setText(QCoreApplication.translate("MainWindow", u"................", None))
        self.label_911.setText(QCoreApplication.translate("MainWindow", u"PUPILS TERMINAL PROGRESS REPORT", None))
        self.label_912.setText(QCoreApplication.translate("MainWindow", u"ID No_:", None))
        self.label_913.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_914.setText(QCoreApplication.translate("MainWindow", u"Name :", None))
        self.label_915.setText(QCoreApplication.translate("MainWindow", u"..................................", None))
        self.label_916.setText(QCoreApplication.translate("MainWindow", u"Term Endding :", None))
        self.label_917.setText(QCoreApplication.translate("MainWindow", u".............................", None))
        self.label_918.setText(QCoreApplication.translate("MainWindow", u"Next Term Begins :", None))
        self.label_919.setText(QCoreApplication.translate("MainWindow", u".............................", None))
        self.label_920.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.label_921.setText(QCoreApplication.translate("MainWindow", u"............................", None))
        self.label_922.setText(QCoreApplication.translate("MainWindow", u"Class :", None))
        self.label_923.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_924.setText(QCoreApplication.translate("MainWindow", u"SUJECTS", None))
        self.label_925.setText(QCoreApplication.translate("MainWindow", u"CLASS SCORE", None))
        self.label_926.setText(QCoreApplication.translate("MainWindow", u"50%", None))
        self.label_927.setText(QCoreApplication.translate("MainWindow", u"GRADE", None))
        self.label_928.setText(QCoreApplication.translate("MainWindow", u"REMARKS", None))
        self.label_929.setText(QCoreApplication.translate("MainWindow", u"English Language", None))
        self.label_930.setText(QCoreApplication.translate("MainWindow", u"Vocabulary Develop.", None))
        self.label_931.setText(QCoreApplication.translate("MainWindow", u"Mathematics", None))
        self.label_932.setText(QCoreApplication.translate("MainWindow", u"Natural Science", None))
        self.label_933.setText(QCoreApplication.translate("MainWindow", u"R. M. E", None))
        self.label_934.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.label_935.setText(QCoreApplication.translate("MainWindow", u"Computing", None))
        self.label_936.setText(QCoreApplication.translate("MainWindow", u"Creative Arts", None))
        self.label_937.setText(QCoreApplication.translate("MainWindow", u"OWOP", None))
        self.label_938.setText(QCoreApplication.translate("MainWindow", u"Attendances:", None))
        self.label_939.setText(QCoreApplication.translate("MainWindow", u"..............", None))
        self.label_940.setText(QCoreApplication.translate("MainWindow", u"Out of:", None))
        self.label_941.setText(QCoreApplication.translate("MainWindow", u"..............", None))
        self.label_942.setText(QCoreApplication.translate("MainWindow", u"Promoted To :", None))
        self.label_943.setText(QCoreApplication.translate("MainWindow", u"..............", None))
        self.label_944.setText(QCoreApplication.translate("MainWindow", u"...........................................................", None))
        self.label_945.setText(QCoreApplication.translate("MainWindow", u"Conduct:", None))
        self.label_946.setText(QCoreApplication.translate("MainWindow", u"Interest:", None))
        self.label_947.setText(QCoreApplication.translate("MainWindow", u"............................................................", None))
        self.label_948.setText(QCoreApplication.translate("MainWindow", u"Class Teacher's Remarks:", None))
        self.label_949.setText(QCoreApplication.translate("MainWindow", u"...........................................................", None))
        self.label_950.setText(QCoreApplication.translate("MainWindow", u".........................", None))
        self.label_951.setText(QCoreApplication.translate("MainWindow", u"Signature:", None))
        self.label_952.setText(QCoreApplication.translate("MainWindow", u"Principals Remarks:", None))
        self.label_953.setText(QCoreApplication.translate("MainWindow", u"...........................................................", None))
        self.label_954.setText(QCoreApplication.translate("MainWindow", u".........................", None))
        self.label_955.setText(QCoreApplication.translate("MainWindow", u"Signature:", None))
        self.label_956.setText(QCoreApplication.translate("MainWindow", u"EXAM SCORE", None))
        self.label_957.setText(QCoreApplication.translate("MainWindow", u"50%", None))
        self.label_958.setText(QCoreApplication.translate("MainWindow", u"TOTAL SCORE", None))
        self.label_959.setText(QCoreApplication.translate("MainWindow", u"100%", None))
        self.label_960.setText(QCoreApplication.translate("MainWindow", u"Tel :", None))
        self.label_961.setText(QCoreApplication.translate("MainWindow", u"Address :", None))
        self.bt_111.setText(QCoreApplication.translate("MainWindow", u"PRINT", None))
        self.tabWidget_11.setTabText(self.tabWidget_11.indexOf(self.tab_50), QCoreApplication.translate("MainWindow", u"grade 1 - 6 print", None))
        self.label_854.setText(QCoreApplication.translate("MainWindow", u"...............................................................................", None))
        self.label_855.setText(QCoreApplication.translate("MainWindow", u"...................", None))
        self.label_856.setText(QCoreApplication.translate("MainWindow", u"................", None))
        self.label_857.setText(QCoreApplication.translate("MainWindow", u"PUPILS TERMINAL PROGRESS REPORT", None))
        self.label_858.setText(QCoreApplication.translate("MainWindow", u"ID No_:", None))
        self.label_859.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_860.setText(QCoreApplication.translate("MainWindow", u"Name :", None))
        self.label_861.setText(QCoreApplication.translate("MainWindow", u"..................................", None))
        self.label_862.setText(QCoreApplication.translate("MainWindow", u"Term Endding :", None))
        self.label_863.setText(QCoreApplication.translate("MainWindow", u".............................", None))
        self.label_864.setText(QCoreApplication.translate("MainWindow", u"Next Term Begins :", None))
        self.label_865.setText(QCoreApplication.translate("MainWindow", u".............................", None))
        self.label_866.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.label_867.setText(QCoreApplication.translate("MainWindow", u"............................", None))
        self.label_868.setText(QCoreApplication.translate("MainWindow", u"Class :", None))
        self.label_869.setText(QCoreApplication.translate("MainWindow", u"..................", None))
        self.label_870.setText(QCoreApplication.translate("MainWindow", u"SUJECTS", None))
        self.label_871.setText(QCoreApplication.translate("MainWindow", u"CLASS SCORE", None))
        self.label_872.setText(QCoreApplication.translate("MainWindow", u"50%", None))
        self.label_873.setText(QCoreApplication.translate("MainWindow", u"GRADE", None))
        self.label_874.setText(QCoreApplication.translate("MainWindow", u"REMARKS", None))
        self.label_875.setText(QCoreApplication.translate("MainWindow", u"English Language", None))
        self.label_876.setText(QCoreApplication.translate("MainWindow", u"Vocabulary Develop.", None))
        self.label_877.setText(QCoreApplication.translate("MainWindow", u"Mathematics", None))
        self.label_878.setText(QCoreApplication.translate("MainWindow", u"Natural Science", None))
        self.label_879.setText(QCoreApplication.translate("MainWindow", u"R. M. E", None))
        self.label_880.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.label_881.setText(QCoreApplication.translate("MainWindow", u"Computing", None))
        self.label_882.setText(QCoreApplication.translate("MainWindow", u"Creative Arts", None))
        self.label_883.setText(QCoreApplication.translate("MainWindow", u"OWOP", None))
        self.label_884.setText(QCoreApplication.translate("MainWindow", u"Attendances:", None))
        self.label_885.setText(QCoreApplication.translate("MainWindow", u"..............", None))
        self.label_886.setText(QCoreApplication.translate("MainWindow", u"Out of:", None))
        self.label_887.setText(QCoreApplication.translate("MainWindow", u"..............", None))
        self.label_888.setText(QCoreApplication.translate("MainWindow", u"Promoted To :", None))
        self.label_889.setText(QCoreApplication.translate("MainWindow", u"..............", None))
        self.label_890.setText(QCoreApplication.translate("MainWindow", u"...........................................................", None))
        self.label_891.setText(QCoreApplication.translate("MainWindow", u"Conduct:", None))
        self.label_892.setText(QCoreApplication.translate("MainWindow", u"Interest:", None))
        self.label_893.setText(QCoreApplication.translate("MainWindow", u"............................................................", None))
        self.label_894.setText(QCoreApplication.translate("MainWindow", u"Class Teacher's Remarks:", None))
        self.label_895.setText(QCoreApplication.translate("MainWindow", u"...........................................................", None))
        self.label_896.setText(QCoreApplication.translate("MainWindow", u".........................", None))
        self.label_897.setText(QCoreApplication.translate("MainWindow", u"Signature:", None))
        self.label_898.setText(QCoreApplication.translate("MainWindow", u"Principals Remarks:", None))
        self.label_899.setText(QCoreApplication.translate("MainWindow", u"...........................................................", None))
        self.label_900.setText(QCoreApplication.translate("MainWindow", u".........................", None))
        self.label_901.setText(QCoreApplication.translate("MainWindow", u"Signature:", None))
        self.label_902.setText(QCoreApplication.translate("MainWindow", u"EXAM SCORE", None))
        self.label_903.setText(QCoreApplication.translate("MainWindow", u"50%", None))
        self.label_904.setText(QCoreApplication.translate("MainWindow", u"TOTAL SCORE", None))
        self.label_905.setText(QCoreApplication.translate("MainWindow", u"100%", None))
        self.label_906.setText(QCoreApplication.translate("MainWindow", u"Tel :", None))
        self.label_907.setText(QCoreApplication.translate("MainWindow", u"Address :", None))
        self.bt_110.setText(QCoreApplication.translate("MainWindow", u"PRINT", None))
        self.tabWidget_11.setTabText(self.tabWidget_11.indexOf(self.tab_51), QCoreApplication.translate("MainWindow", u"grade 7 -9 print", None))
        self.tabWidget_10.setTabText(self.tabWidget_10.indexOf(self.tab_36), QCoreApplication.translate("MainWindow", u"Student Report", None))
        self.groupBox_32.setTitle(QCoreApplication.translate("MainWindow", u"School Fees", None))
        self.label_461.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.label_462.setText(QCoreApplication.translate("MainWindow", u"Full Name :", None))
        self.label_463.setText(QCoreApplication.translate("MainWindow", u"Paid By :", None))
        self.label_464.setText(QCoreApplication.translate("MainWindow", u"Amount Paid :", None))
        self.label_465.setText(QCoreApplication.translate("MainWindow", u"Term :", None))
        self.comboBox_52.setItemText(0, QCoreApplication.translate("MainWindow", u"Term 1", None))
        self.comboBox_52.setItemText(1, QCoreApplication.translate("MainWindow", u"Term 2", None))
        self.comboBox_52.setItemText(2, QCoreApplication.translate("MainWindow", u"Term 3", None))

        self.comboBox_52.setPlaceholderText(QCoreApplication.translate("MainWindow", u"term ...", None))
        self.label_466.setText(QCoreApplication.translate("MainWindow", u"Class :", None))
        self.comboBox_53.setItemText(0, QCoreApplication.translate("MainWindow", u"Grade 1", None))
        self.comboBox_53.setItemText(1, QCoreApplication.translate("MainWindow", u"Grade 2", None))
        self.comboBox_53.setItemText(2, QCoreApplication.translate("MainWindow", u"Grade 3", None))
        self.comboBox_53.setItemText(3, QCoreApplication.translate("MainWindow", u"Grade 4", None))
        self.comboBox_53.setItemText(4, QCoreApplication.translate("MainWindow", u"Grade 5", None))
        self.comboBox_53.setItemText(5, QCoreApplication.translate("MainWindow", u"Grade 6", None))
        self.comboBox_53.setItemText(6, QCoreApplication.translate("MainWindow", u"Grade 7", None))
        self.comboBox_53.setItemText(7, QCoreApplication.translate("MainWindow", u"Grade 8", None))
        self.comboBox_53.setItemText(8, QCoreApplication.translate("MainWindow", u"Grade 9", None))

        self.comboBox_53.setPlaceholderText(QCoreApplication.translate("MainWindow", u"class .....", None))
        self.bt_97.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.bt_98.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.bt_99.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.bt_121.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.groupBox_33.setTitle(QCoreApplication.translate("MainWindow", u"Feeding Fees/Studies Fees", None))
        self.label_467.setText(QCoreApplication.translate("MainWindow", u"Class :", None))
        self.label_468.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.label_469.setText(QCoreApplication.translate("MainWindow", u"Amount Paid :", None))
        self.label_470.setText(QCoreApplication.translate("MainWindow", u"Full Name :", None))
        self.comboBox_54.setItemText(0, QCoreApplication.translate("MainWindow", u"Grade 1", None))
        self.comboBox_54.setItemText(1, QCoreApplication.translate("MainWindow", u"Grade 2", None))
        self.comboBox_54.setItemText(2, QCoreApplication.translate("MainWindow", u"Grade 3", None))
        self.comboBox_54.setItemText(3, QCoreApplication.translate("MainWindow", u"Grade 4", None))
        self.comboBox_54.setItemText(4, QCoreApplication.translate("MainWindow", u"Grade 5", None))
        self.comboBox_54.setItemText(5, QCoreApplication.translate("MainWindow", u"Grade 6", None))
        self.comboBox_54.setItemText(6, QCoreApplication.translate("MainWindow", u"Grade 7", None))
        self.comboBox_54.setItemText(7, QCoreApplication.translate("MainWindow", u"Grade 8", None))
        self.comboBox_54.setItemText(8, QCoreApplication.translate("MainWindow", u"Grade 9", None))

        self.comboBox_54.setPlaceholderText(QCoreApplication.translate("MainWindow", u"class .....", None))
        self.comboBox_48.setItemText(0, QCoreApplication.translate("MainWindow", u"Feeding Fees", None))
        self.comboBox_48.setItemText(1, QCoreApplication.translate("MainWindow", u"Studies Fees", None))

        self.comboBox_48.setPlaceholderText(QCoreApplication.translate("MainWindow", u" .....", None))
        self.label_136.setText(QCoreApplication.translate("MainWindow", u"Type of Fees :", None))
        self.bt_117.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.bt_122.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.bt_100.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.bt_101.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.bt_102.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        ___qtablewidgetitem115 = self.tableWidget_17.horizontalHeaderItem(0)
        ___qtablewidgetitem115.setText(QCoreApplication.translate("MainWindow", u"Full Name", None));
        ___qtablewidgetitem116 = self.tableWidget_17.horizontalHeaderItem(1)
        ___qtablewidgetitem116.setText(QCoreApplication.translate("MainWindow", u"Class", None));
        ___qtablewidgetitem117 = self.tableWidget_17.horizontalHeaderItem(2)
        ___qtablewidgetitem117.setText(QCoreApplication.translate("MainWindow", u"Term", None));
        ___qtablewidgetitem118 = self.tableWidget_17.horizontalHeaderItem(3)
        ___qtablewidgetitem118.setText(QCoreApplication.translate("MainWindow", u"Amount Paid", None));
        ___qtablewidgetitem119 = self.tableWidget_17.horizontalHeaderItem(4)
        ___qtablewidgetitem119.setText(QCoreApplication.translate("MainWindow", u"Paid By", None));
        ___qtablewidgetitem120 = self.tableWidget_17.horizontalHeaderItem(5)
        ___qtablewidgetitem120.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem121 = self.tableWidget_18.horizontalHeaderItem(0)
        ___qtablewidgetitem121.setText(QCoreApplication.translate("MainWindow", u"Full Name", None));
        ___qtablewidgetitem122 = self.tableWidget_18.horizontalHeaderItem(1)
        ___qtablewidgetitem122.setText(QCoreApplication.translate("MainWindow", u"Class", None));
        ___qtablewidgetitem123 = self.tableWidget_18.horizontalHeaderItem(2)
        ___qtablewidgetitem123.setText(QCoreApplication.translate("MainWindow", u"Type Of Fees", None));
        ___qtablewidgetitem124 = self.tableWidget_18.horizontalHeaderItem(3)
        ___qtablewidgetitem124.setText(QCoreApplication.translate("MainWindow", u"Amount Paid", None));
        ___qtablewidgetitem125 = self.tableWidget_18.horizontalHeaderItem(4)
        ___qtablewidgetitem125.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.tabWidget_10.setTabText(self.tabWidget_10.indexOf(self.tab_40), QCoreApplication.translate("MainWindow", u"Student Fees", None))
        self.label_471.setText(QCoreApplication.translate("MainWindow", u"Message Subject :", None))
        self.label_472.setText(QCoreApplication.translate("MainWindow", u"To :", None))
        self.bt_103.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.tabWidget_10.setTabText(self.tabWidget_10.indexOf(self.tab_41), QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_169.setText(QCoreApplication.translate("MainWindow", u"Expenses For :", None))
        self.label_170.setText(QCoreApplication.translate("MainWindow", u"Amout :", None))
        self.comboBox_50.setItemText(0, QCoreApplication.translate("MainWindow", u"School Fees", None))
        self.comboBox_50.setItemText(1, QCoreApplication.translate("MainWindow", u"Feeding Fees", None))
        self.comboBox_50.setItemText(2, QCoreApplication.translate("MainWindow", u"Studies Fees", None))

        self.comboBox_50.setPlaceholderText("")
        self.label_171.setText(QCoreApplication.translate("MainWindow", u"Expenses From :", None))
        self.label_172.setText(QCoreApplication.translate("MainWindow", u"School Fees :", None))
        self.label_173.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_174.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_175.setText(QCoreApplication.translate("MainWindow", u"Feeding Fees :", None))
        self.label_176.setText(QCoreApplication.translate("MainWindow", u"From School Fees :", None))
        self.label_177.setText(QCoreApplication.translate("MainWindow", u"From Feeding Fees :", None))
        self.label_178.setText(QCoreApplication.translate("MainWindow", u"From Studies Fees :", None))
        self.label_179.setText(QCoreApplication.translate("MainWindow", u"Expenses :", None))
        self.label_180.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.label_181.setText(QCoreApplication.translate("MainWindow", u"Balances :", None))
        self.label_182.setText(QCoreApplication.translate("MainWindow", u"Feeding Fees :", None))
        self.label_183.setText(QCoreApplication.translate("MainWindow", u"Studies Fees :", None))
        self.label_184.setText(QCoreApplication.translate("MainWindow", u"School Fees :", None))
        self.label_185.setText(QCoreApplication.translate("MainWindow", u"..", None))
        self.label_186.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_187.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_188.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_189.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_190.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_191.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_192.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_193.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400; text-decoration: underline;\">Adding Expenses Used</span></p></body></html>", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u" School Fees", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"Feeding Fees", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"Studies Fees", None))
        self.tabWidget_10.setTabText(self.tabWidget_10.indexOf(self.tab_55), QCoreApplication.translate("MainWindow", u"Expenses", None))
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.tab_31), QCoreApplication.translate("MainWindow", u"Management", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_29), QCoreApplication.translate("MainWindow", u"CAMBRIDGE", None))
        self.label_473.setText("")
        self.label_474.setText(QCoreApplication.translate("MainWindow", u"Welcome", None))
        self.label_475.setText(QCoreApplication.translate("MainWindow", u"To Research Portal", None))
        self.label_476.setText(QCoreApplication.translate("MainWindow", u"To use this from Kindlly", None))
        self.label_477.setText(QCoreApplication.translate("MainWindow", u"Clicked on the button Below", None))
        self.label_478.setText(QCoreApplication.translate("MainWindow", u"To activate an Assistant", None))
        self.bt_104.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_42), QCoreApplication.translate("MainWindow", u"Student Lib", None))
    # retranslateUi

