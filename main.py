import random
import datetime
import sys
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QCommandLinkButton, QDateEdit,
    QFrame, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget, QMessageBox)

from PySide6 import QtGui, QtCore, QtPrintSupport, QtWidgets

from ui_SMS import *
import mysql.connector

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        for row in range(self.tableWidget_5.rowCount()):
            for col in range(self.tableWidget_5.columnCount()):
                item = QtWidgets.QTableWidgetItem('(%d, %d)' % (row, col))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget_5.setItem(row, col, item)

        # Setting up tabs
        self.tabWidget.tabBar().setVisible(False)
        self.tabWidget_2.tabBar().setVisible(False)
        self.tabWidget_3.tabBar().setVisible(False)
        self.tabWidget_4.tabBar().setVisible(False)
        self.tabWidget_5.tabBar().setVisible(False)
        self.tabWidget_6.tabBar().setVisible(False)
        self.tabWidget_7.tabBar().setVisible(False)
        self.tabWidget_8.tabBar().setVisible(False)
        self.tabWidget_9.tabBar().setVisible(False)
        self.tabWidget_10.tabBar().setVisible(False)
        self.tabWidget_11.tabBar().setVisible(False)
        self.tabWidget.setCurrentIndex(3)
        self.frame.setVisible(False)

        # Button Handler
        self.bt_113.clicked.connect(self.welcome)
        self.bt_createAccount.clicked.connect(self.create_info)
        self.bt_signup.clicked.connect(self.creatAccount)
        self.bt_back_2.clicked.connect(self.login_info)
        self.bt_login.clicked.connect(self.loginUser)
        self.bt.clicked.connect(self.gotoGES)
        self.bt_1.clicked.connect(self.gotoCAMBRIDGE)
        self.bt_2.clicked.connect(self.gotoMONTESSORI)
        self.bt_3.clicked.connect(self.areStudent)
        self.bt_4.clicked.connect(self.areAdmin)
        self.bt_5.clicked.connect(self.dashboardGES)
        self.bt_6.clicked.connect(self.set_addStudent_tab)
        self.bt_13.clicked.connect(self.addStudent)
        self.bt_14.clicked.connect(self.display1)
        self.bt_7.clicked.connect(self.set_updateTab)
        self.bt_15.clicked.connect(self.updateStudents)
        self.bt_16.clicked.connect(self.display2)
        self.bt_29.clicked.connect(self.displaySearch)
        self.bt_17.clicked.connect(self.deleteStudent)
        self.bt_8.clicked.connect(self.Student_marks_tab)
        self.bt_18.clicked.connect(self.addStudent_mark)
        self.bt_21.clicked.connect(self.display3)
        self.bt_30.clicked.connect(self.displaySearch1)
        self.bt_20.clicked.connect(self.deleteMarks)
        self.bt_19.clicked.connect(self.updateMarks)
        self.bt_22.clicked.connect(self.addAttendance)
        self.bt_24.clicked.connect(self.updateAttendance)
        self.bt_25.clicked.connect(self.deleteAttendance)
        self.bt_23.clicked.connect(self.displayAttendance1)
        self.bt_12.clicked.connect(self.studentAttendance)
        self.bt_11.clicked.connect(self.studentFees)
        self.bt_31.clicked.connect(self.addSchoolFees)
        self.bt_32.clicked.connect(self.updateSchoolFees)
        self.bt_33.clicked.connect(self.deleteSchoolFees)
        self.pushButton.clicked.connect(self.resetButton)
        self.bt_115.clicked.connect(self.searchSchool_fees)
        self.bt_34.clicked.connect(self.addFeeding_Fees)
        self.bt_35.clicked.connect(self.updateFees)
        self.bt_36.clicked.connect(self.deleteFees)
        self.bt_118.clicked.connect(self.searchFees)
        self.bt_9.clicked.connect(self.reportsTab)
        self.bt_26.clicked.connect(self.crache_inputTab)
        self.bt_27.clicked.connect(self.primary_inputTab)
        self.bt_28.clicked.connect(self.jhs_inputTab)
        self.pushButton_9.clicked.connect(self.crache_printTab)
        #self.bt_114.clicked.connect(self.handlePrint)

    def welcome(self):
        self.tabWidget.setCurrentIndex(0)

# Login And Account Creating
    def Db_Connect(self):
        self.mydb = mysql.connector.connect(
		            host = "localhost",
		            user = "root",
		            passwd = "",
		            db = "school_db"
		        )
        self.cur = self.mydb.cursor()
    
    def create_info(self):
        self.tabWidget_2.setCurrentIndex(1)

    def creatAccount(self):
        try:
            full_name = self.signup_fullname_2.text()
            user_name = self.signup_username_2.text()
            password = self.signup_password_2.text()
            confirm_password = self.signup_comfirmpassword_2.text()

            if len(user_name) == 0 or len(password) == 0 or len(confirm_password) == 0:
                QMessageBox.Retry(self, "Invalid", "Please fill in all input")
                

            elif password != confirm_password:
                QMessageBox.warning(self, "Invalid", "Password do not match.")
                
            else:
                mydb = mysql.connector.connect(
                    host = "localhost",
                    user = "root",
                    passwd = "",
                    db = "school_db"
                )
                cur = mydb.cursor()
                user_info = [user_name, full_name, password, confirm_password]
                qry = ('''
                    INSERT INTO login_info (username, fullname, password, confirm_password)
                    VALUES(%s,%s,%s,%s)
                ''')
                cur.execute(qry, user_info)
                mydb.commit()
                mydb.close()
                QMessageBox.information(self, "Successfully", "Account created successfully!, please login now")
                self.tabWidget_2.setCurrentIndex(0)
                
        
        except Exception as DatabaseError:
            QMessageBox.warning(self, "Error", "Account details already exist")
    
    def login_info(self):
        self.tabWidget_2.setCurrentIndex(0)
    
    def loginUser(self):
        try:
            user_name = self.login_username_2.text()
            password = self.login_password_2.text()

            
            if len(user_name) == 0 or len(password) == 0:
                    QMessageBox.warning(self, "Login Form", "Please Fill All ")
                    self.login_username_2.clear()
                    self.login_password_2.clear()

            else:
                mydb = mysql.connector.connect(
                    host = "localhost",
                    user = "root",
                    passwd = "",
                    db = "school_db"
                )
                cur = mydb.cursor()
                query = 'SELECT password FROM login_info WHERE username =\'' + user_name + "\'"
                cur.execute(query)
                result_pass = cur.fetchone()[0]
                if result_pass == password:
                    self.tabWidget.setCurrentIndex(2)
                    self.frame.setVisible(True)
                    self.login_username_2.clear()
                    self.login_password_2.clear()

                else:
                    QMessageBox.warning(self, "login info", "Invalid username or password")
        
        except Exception as DatabaseError:
             QMessageBox.warning(self, "Error", "user or password not found")


# Selection

    def areStudent(self):
        self.tabWidget.setCurrentIndex(7)
    
    def areAdmin(self):
        self.tabWidget.setCurrentIndex(1)
 # Educational system selection
 #        
    def gotoGES(self):
        self.tabWidget.setCurrentIndex(4)
        self.tabWidget_3.setCurrentIndex(0)
        self.set_addStudent_tab()
    
    def gotoCAMBRIDGE(self):
        self.tabWidget.setCurrentIndex(6)
        self.tabWidget_9.setCurrentIndex(0)

    def gotoMONTESSORI(self):
        self.tabWidget.setCurrentIndex(5)
        self.tabWidget_6.setCurrentIndex(0)

    #def buttonActive(self):


# GES Dashboard
    def dashboardGES(self):
        self.tabWidget_3.setCurrentIndex(1)

    # Registrating Student

    def set_addStudent_tab(self):
        self.tabWidget_4.setCurrentIndex(0)
        self.fill_next_reg_number()
    
    def fill_next_reg_number(self):
        self.lineEdit.setDisabled(True)
        rand_ref = random.randint(10000, 20000)
        conv_ref = ('REG-' + str(rand_ref))
        self.lineEdit.setText(conv_ref)

    def addStudent(self):
        #try:
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            db = "school_db"
        )
        cur = mydb.cursor()

        reg_number = self.lineEdit.text()
        full_name = self.lineEdit_9.text()
        date_of_birth = self.lineEdit_20.text()
        Class = self.comboBox.currentText()
        gender = self.comboBox_2.currentText()
        address = self.textEdit.toPlainText()
        parent_fullName = self.lineEdit_4.text()
        phone_number = self.lineEdit_5.text()
        email_address = self.lineEdit_6.text()

        if full_name != '' and Class != '' and parent_fullName != '':
            qry = ('''
                INSERT INTO students (registration_number, full_name, date_of_birth, Class,
                gender, home_address, parent_full_name, phone_number, email_address)
                VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)
            ''').format(reg_number, full_name, date_of_birth, Class, gender, address, parent_fullName, phone_number, email_address)
            value = (reg_number, full_name, date_of_birth, Class, gender, address, parent_fullName, phone_number, email_address)
            cur.execute(qry, value)
            mydb.commit()
            cur.close()

            QMessageBox.information(self, "success", "Saved Successfully")

            self.fill_next_reg_number()
            self.lineEdit_9.clear()
            self.lineEdit_4.clear()
            self.lineEdit_5.clear()
            self.lineEdit_6.clear()
            self.display1()

        else:
            QMessageBox.warning(self, "warning", "fill the empty field!!")
        
        #except Exception as DatabaseError:
           # QMessageBox.warning(self, "Error", "Crendentail already exist")

    # Getting Registed Student Data from the DATABASE

    def display1(self):
        self.tableWidget.setRowCount(0)
        self.tableWidget.insertRow(0)

        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            db = "school_db"
        )
        cur = mydb.cursor()

        cur.execute("SELECT * FROM students")

        data = cur.fetchall()

        for row , form in enumerate(data):
            for col , item in enumerate(form):
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(item)))
                col +=1

                row_position = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_position)

# Updating Student info:

    def set_updateTab(self):
        self.tabWidget_4.setCurrentIndex(1)

    # Getting Student Registration Number from DataBase and Displaying it:
    #   
    def getReg_number(self):
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            db = "school_db"
        )
        cur = mydb.cursor()

        search_by_name = self.lineEdit_13.text()
        if search_by_name != '':  
            qry = ("SELECT (registration_number) FROM students WHERE full_name = '{}'").format(search_by_name)
            cur.execute(qry)
            data = cur.fetchall()[0][0]

            self.lineEdit_7.setDisabled(True)
            self.lineEdit_7.setText(str(data))
         
    def displaySearch(self):
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.insertRow(0)

        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            db = "school_db"
        )
        cur = mydb.cursor()

        search_by_name = self.lineEdit_13.text()
        if search_by_name != '':
            qry = ("SELECT * FROM students WHERE full_name = '{}'").format(search_by_name)
            cur.execute(qry)
            data = cur.fetchall()

            for row , form in enumerate(data):
                for col , item in enumerate(form):
                    self.tableWidget_2.setItem(row, col, QTableWidgetItem(str(item)))
                    col +=1

                    row_position = self.tableWidget_2.rowCount()
                    self.tableWidget_2.insertRow(row_position)
                    self.getReg_number()
        
        else:
            QMessageBox.information(self, " ", "Please enter the full name\n of the student to search")
    
    def display2(self):
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.insertRow(0)

        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            db = "school_db"
        )
        cur = mydb.cursor()

        cur.execute("SELECT * FROM students")

        data = cur.fetchall()

        for row , form in enumerate(data):
            for col , item in enumerate(form):
                self.tableWidget_2.setItem(row, col, QTableWidgetItem(str(item)))
                col +=1

                row_position = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(row_position)

    def updateStudents(self):
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            db = "school_db"
        )
        cur = mydb.cursor()
        
        reg_number = self.lineEdit_7.text()
        full_name = self.lineEdit_8.text()
        date_of_birth = self.lineEdit_19.text()
        Class = self.comboBox_3.currentText()
        gender = self.comboBox_4.currentText()
        address = self.textEdit_2.toPlainText()
        parent_fullName = self.lineEdit_10.text()
        phone_number = self.lineEdit_11.text()
        email_address = self.lineEdit_12.text()

        if reg_number != '' and email_address != '' and phone_number != '':
            qry =("UPDATE students SET email_address = '{}', phone_number ='{}' WHERE registration_number = '{}'" ).format(email_address, phone_number, reg_number)
            cur.execute(qry)
            mydb.commit()
            cur.close()

            QMessageBox.information(self, "success", "Updated Email Address and Phone number Successfully")

            self.display2()
            self.lineEdit_8.clear()
            self.lineEdit_10.clear()
            self.lineEdit_11.clear()
            self.lineEdit_12.clear()
        
        elif reg_number != '' and full_name != '':
            qry =("UPDATE students SET full_name = '{}' WHERE registration_number = '{}'" ).format(full_name, reg_number)
            cur.execute(qry)
            mydb.commit()
            cur.close()
            QMessageBox.information(self, "success", "Full name updated Successfully")
            self.display2()
            
        elif reg_number != '' and date_of_birth != '':
            qry =("UPDATE students SET date_of_birth = '{}' WHERE registration_number = '{}'" ).format(date_of_birth, reg_number)
            cur.execute(qry)
            mydb.commit()
            cur.close()
            QMessageBox.information(self, "success", "Date of Birth updated Successfully")
            self.display2()

        elif reg_number != '' and Class != '':
            qry =("UPDATE students SET Class = '{}' WHERE registration_number = '{}'" ).format(Class, reg_number)
            cur.execute(qry)
            mydb.commit()
            cur.close()
            QMessageBox.information(self, "success", "Class updated Successfully")
            self.display2()
        
        elif reg_number != '' and email_address != '':
            qry =("UPDATE students SET email_address = '{}' WHERE registration_number = '{}'" ).format(email_address, reg_number)
            cur.execute(qry)
            mydb.commit()
            cur.close()
            QMessageBox.information(self, "success", "Email Address updated Successfully")
            self.display2()
        
        else:
            if reg_number != '' and full_name!= '' and date_of_birth!= '' and Class!= '' and gender!='' and address != '' and parent_fullName!= '' and phone_number!= '' and email_address !='':
                qry = ('''
                    UPDATE students SET full_name = '{}', date_of_birth = '{}', Class = '{}',
                    gender = '{}', home_address = '{}', parent_full_name = '{}', phone_number ='{}', email_address = '{}'
                    WHERE registration_number = '{}'
                ''').format(full_name, date_of_birth, Class, gender, address, parent_fullName, phone_number, email_address, reg_number)
                cur.execute(qry)
                mydb.commit()
                cur.close()

                QMessageBox.information(self, "success", "Updated all Successfully")

                self.display2()
                self.lineEdit_8.clear()
                self.lineEdit_10.clear()
                self.lineEdit_11.clear()
                self.lineEdit_12.clear()

# Delete Student

    def deleteStudent(self):
        full_name = self.lineEdit_8.text()

        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            db = "school_db"
        )
        cur = mydb.cursor()

        delete_message = QMessageBox.warning(self ," " , "Do you want to Delete ?",QMessageBox.Yes | QMessageBox.No )

        if full_name != '':
            if delete_message == QMessageBox.Yes :
                qry = "DELETE  FROM students WHERE full_name = '{}'".format(full_name)
                cur.execute(qry)
                mydb.commit()
                cur.close()
                QMessageBox.information(self, " ", "Deleted successfully")
                self.display2()
        else:
            QMessageBox.information(self, " ", "Please Enter a valid name to delete")

# Students Marks {Adding, Deleting, Updating}

    def Student_marks_tab(self):
        self.tabWidget_4.setCurrentIndex(2)
    
    def addStudent_mark(self):
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            db = "school_db"
        )
        cur = mydb.cursor()
        
        reg_number = self.lineEdit_15.text()
        full_name = self.lineEdit_14.text()
        Class = self.comboBox_5.currentText()
        subjects = self.comboBox_6.currentText()
        term = self.comboBox_7.currentText()
        marks_type = self.comboBox_8.currentText()
        date = self.lineEdit_26.text()
        grade = self.comboBox_28.currentText()
        marks = self.lineEdit_28.text()

        if reg_number != '' and full_name != '' and Class != '' and subjects != '' and term != '' and marks_type != '':
            qry = ("""INSERT INTO mark (registration_number, full_name, Class, subjects, term, mark_type, date, grade, marks) 
            VALUE(%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """).format(reg_number,full_name, Class, subjects, term, marks_type, date, grade, marks)
            value = (reg_number,full_name, Class, subjects, term, marks_type, date, grade, marks)
            cur.execute(qry, value)
            mydb.commit()
            cur.close
            QMessageBox.information(self, " ", "Marks added successfully")
            self.display3()
        
        else:
            QMessageBox.warning(self, "Warning", "Student Detail Already Exist")
    
    def display3(self):
        self.tableWidget_3.setRowCount(0)
        self.tableWidget_3.insertRow(0)
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            db = "school_db"
        )
        cur = mydb.cursor()

        cur.execute("SELECT * FROM mark")

        data = cur.fetchall()

        for row , form in enumerate(data):
            for col , item in enumerate(form):
                self.tableWidget_3.setItem(row, col, QTableWidgetItem(str(item)))
                col +=1

                row_position = self.tableWidget_3.rowCount()
                self.tableWidget_3.insertRow(row_position)

    def displaySearch1(self):
        self.tableWidget_3.setRowCount(0)
        self.tableWidget_3.insertRow(0)

        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            db = "school_db"
        )
        cur = mydb.cursor()

        search_by_name = self.lineEdit_16.text()
        if search_by_name != '':
            qry = ("SELECT * FROM mark WHERE full_name = '{}'").format(search_by_name)
            cur.execute(qry)
            data = cur.fetchall()

            for row , form in enumerate(data):
                for col , item in enumerate(form):
                    self.tableWidget_3.setItem(row, col, QTableWidgetItem(str(item)))
                    col +=1

                    row_position = self.tableWidget_3.rowCount()
                    self.tableWidget_3.insertRow(row_position)
                    self.getReg_number()
        
        else:
            QMessageBox.information(self, " ", "Please enter the <storng>full name</strong>\n of the student to search")

    def deleteMarks(self):
        full_name = self.lineEdit_14.text()

        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            db = "school_db"
        )
        cur = mydb.cursor()

        delete_message = QMessageBox.warning(self ,"COMFIRMATION" , "Do you want to Delete ?",QMessageBox.Yes | QMessageBox.No )

        if full_name != '':
            if delete_message == QMessageBox.Yes :
                qry = "DELETE FROM mark WHERE full_name  = '{}'".format(full_name )
                cur.execute(qry)
                mydb.commit()
                cur.close()
                QMessageBox.information(self, " ", "Deleted successfully")
                self.display3()
        else:
            QMessageBox.warning(self, " ", "Marks not found in DATABASE")

    def updateMarks(self):
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            db = "school_db"
        )
        cur = mydb.cursor()

        reg_number = self.lineEdit_15.text()
        full_name = self.lineEdit_14.text()
        Class = self.comboBox_5.currentText()
        subjects = self.comboBox_6.currentText()
        term = self.comboBox_7.currentText()
        marks_type = self.comboBox_8.currentText()
        date = self.lineEdit_26.text()
        grade = self.comboBox_28.currentText()
        marks = self.lineEdit_28.text()

        if reg_number != '' and full_name != '' and Class != '' and term !='' and date != ''and marks != '':
            mydb = mysql.connector.connect(
                    host = "localhost",
                    user = "root",
                    passwd = "",
                    db = "school_db"
                )
            cur = mydb.cursor()
            qry = ('''
                    UPDATE mark SET full_name = '{}', Class = '{}',
                    subjects = '{}', term = '{}', mark_type = '{}', date ='{}', grade ='{}', marks ='{}'
                    WHERE registration_number = '{}'
                ''').format(full_name, Class, subjects, term, marks_type, date, grade, marks, reg_number)
            cur.execute(qry)
            mydb.commit()
            cur.close()

            QMessageBox.information(self, " ", "Updated all Successfully")
            self.display3()
            self.lineEdit_14.clear()

            
        else:
            QMessageBox.information(self, " ", "<strong>Please Fill in all inputs</strong>")

# Students Attendance

    def studentAttendance(self):
        self.tabWidget_4.setCurrentIndex(3)
    
    def displayAttendance1(self):
        self.tableWidget_4.setRowCount(0)
        self.tableWidget_4.insertRow(0)
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            db = "school_db"
        )
        cur = mydb.cursor()

        cur.execute("SELECT * FROM attendance")

        data = cur.fetchall()

        for row , form in enumerate(data):
            for col , item in enumerate(form):
                self.tableWidget_4.setItem(row, col, QTableWidgetItem(str(item)))
                col +=1

                row_position = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_position)

    def addAttendance(self):

        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            db = "school_db"
        )
        cur = mydb.cursor()
        
        reg_number = self.lineEdit_17.text()
        full_name = self.lineEdit_18.text()
        Class = self.comboBox_9.currentText()
        date = self.lineEdit_21.text()

        if reg_number != '' and full_name != '' and Class != '':
            qry = ("""INSERT INTO attendance (registration_number, full_name, Class, date) 
            VALUE(%s,%s,%s,%s)
            """).format(reg_number,full_name, Class, date)
            value = (reg_number,full_name, Class, date)
            cur.execute(qry, value)
            mydb.commit()
            cur.close()
            QMessageBox.information(self, " ", "Added successfully")
            self.displayAttendance1()
        
        else:
            QMessageBox.warning(self, "Warning", "Please Fill All inputs")

    def updateAttendance(self):
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            db = "school_db"
        )
        cur = mydb.cursor()

        reg_number = self.lineEdit_17.text()
        full_name = self.lineEdit_18.text()
        Class = self.comboBox_9.currentText()
        date = self.lineEdit_21.text()

        if reg_number != '' and full_name != '' and Class != '' and date != '':
            qry = "UPDATE attendance SET registration_number = '{}', full_name = '{}', Class = '{}' WHERE date = '{}'".format(reg_number, full_name, Class, date)
            cur.execute(qry)
            mydb.commit()
            cur.close()
            QMessageBox.information(self, "", "Updated Successfully!!")
            self.displayAttendance1()
        else:
            QMessageBox.warning(self, "", "Please fill all inputs")

    def deleteAttendance(self):
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            db = "school_db"
        )
        cur = mydb.cursor()

        full_name = self.lineEdit_18.text()
        if full_name != '':
            qry = "DELETE FROM attendance WHERE fullname ='{}'".format(full_name)
            cur.execute(qry)
            mydb.commit()
            cur.close()
            QMessageBox.information(self, "", "Deleted Successfully!!")
            self.displayAttendance1()
        else:
            QMessageBox.warning(self, "", "Please enter the date to delete")

# School Fees And Feeding Fees

    def studentFees(self):
        self.tabWidget_4.setCurrentIndex(5)

    def addSchoolFees(self):
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            db = "school_db"
        )
        cur = mydb.cursor()

        full_name = self.lineEdit_33.text()
        Class = self.comboBox_16.currentText()
        term = self.comboBox_17.currentText()
        amount_paid = self.lineEdit_32.text()
        paid_by = self.lineEdit_31.text()
        date = self.lineEdit_56.text()

        if full_name != '' and term != '' and amount_paid !='':
            qry = """INSERT INTO school_fees(full_name, Class, term, amount_paid, paid_by, date)
                VALUE(%s,%s,%s,%s,%s,%s)""".format(full_name, Class, term, amount_paid, paid_by, date)
            value = (full_name, Class, term, amount_paid, paid_by, date)
            cur.execute(qry, value)
            mydb.commit()
            cur.close()
            QMessageBox.information(self, "", "Added Successfully!!")
            self.displaySchoolFees1()
        else:
            QMessageBox.warning(self, "", "Please fill all inputs")

    def updateSchoolFees(self):
        full_name = self.lineEdit_33.text()
        Class = self.comboBox_16.currentText()
        term = self.comboBox_17.currentText()
        amount_paid = self.lineEdit_32.text()
        paid_by = self.lineEdit_31.text()
        date = self.lineEdit_56.text()

        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            db = "school_db"
        )
        cur = mydb.cursor()
        if full_name != '{}':
            qry = """UPDATE school_fees SET Class = '{}', term = '{}', amount_paid = '{}',
             paid_by = '{}', date = '{}' WHERE full_name = '{}'""".format(Class, term, amount_paid, paid_by, date, full_name)
            cur.execute(qry)
            mydb.commit()
            cur.close()
            QMessageBox.information(self, " ", "Updated Successfully")
            self.displaySchoolFees1()
        else:
            QMessageBox.warning(self, "Error", "Please fill the right details to updated")

    def searchSchool_fees(self):
        Class = self.comboBox_16.currentText()
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            db = "school_db"
        )
        cur = mydb.cursor()
        if Class != '{}':
            qry = "SELECT * FROM school_fees WHERE Class ='{}'".format(Class)
            cur.execute(qry)
            data = cur.fetchall()

            for row , form in enumerate(data):
                for col , item in enumerate(form):
                    self.tableWidget_5.setItem(row, col, QTableWidgetItem(str(item)))
                    col +=1

                    row_position = self.tableWidget_5.rowCount()
                    self.tableWidget_5.insertRow(row_position)
            QMessageBox.information(self, "","Data fetch successfully")
        else:
            QMessageBox.warning(self, "Error", "Please select a class to search")


    def deleteSchoolFees(self):
        full_name = self.lineEdit_33.text()
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            db = "school_db"
        )
        cur = mydb.cursor()

        delete_message = QMessageBox.warning(self ,"COMFIRMATION" , "Do you want to Delete ?",QMessageBox.Yes | QMessageBox.No )

        if full_name != '':
            if delete_message == QMessageBox.Yes :
                qry = "DELETE FROM school_fees WHERE full_name  = '{}'".format(full_name )
                cur.execute(qry)
                mydb.commit()
                cur.close()
                QMessageBox.information(self, " ", "Deleted successfully")
                self.displaySchoolFees1()
        else:
            QMessageBox.warning(self, " ", "Student's School Fees\n not found in DATABASE")

    def displaySchoolFees1(self):
        self.tableWidget_5.setRowCount(0)
        self.tableWidget_5.insertRow(0)
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            db = "school_db"
        )
        cur = mydb.cursor()

        qry = "SELECT * FROM school_fees"
        cur.execute(qry)
        data = cur.fetchall()

        for row , form in enumerate(data):
            for col , item in enumerate(form):
                self.tableWidget_5.setItem(row, col, QTableWidgetItem(str(item)))
                col +=1

                row_position = self.tableWidget_5.rowCount()
                self.tableWidget_5.insertRow(row_position)
        QMessageBox.information(self, "","Data fetch successfully")


    def resetButton(self):
        self.lineEdit_33.clear()
        self.lineEdit_32.clear()
        self.lineEdit_31.clear()
        self.lineEdit_56.clear()

#Feeding Fess & Studies Fees
    def addFeeding_Fees(self):
        is_studies = "Studies Fees"
        is_feeding = "Feeding Fees"

        ans = self.comboBox_31.currentText()
        full_name = self.lineEdit_34.text()
        Class = self.comboBox_18.currentText()
        amount_paid = self.lineEdit_35.text()
        date = self.lineEdit_57.text()

        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            db = "school_db"
        )
        cur = mydb.cursor()

        if ans == is_feeding and full_name != '{}' and amount_paid != '{}':
            qry = """INSERT INTO feeding_fees (full_name, Class, type_of_fees, amount_paid, date)
                VALUES(%s,%s,%s,%s,%s)""".format(full_name, Class, ans, amount_paid, date)
            value = (full_name, Class, ans, amount_paid, date)
            cur.execute(qry, value)
            mydb.commit()
            QMessageBox.information(self, " ", "Feeding Fees Added Successfully")
            #self.displayFees1()

        elif ans == is_studies and full_name != '{}' and amount_paid != '{}':
            qry = """INSERT INTO studies_fees (full_name, Class, type_of_fees, amount_paid, date)
                VALUES(%s,%s,%s,%s,%s)""".format(full_name, Class, ans, amount_paid, date)
            value = (full_name, Class, ans, amount_paid, date)
            cur.execute(qry, value)
            mydb.commit()
            QMessageBox.information(self, " ", "Studies Fees Added Successfully")
           #self.displayFees2()
        else:
            QMessageBox.warning(self, "Error", "Please fill all flied to add up!")

    def displayFees1(self):
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            db = "school_db"
        )
        cur = mydb.cursor()
        qry = "SELECT * FROM feeding_fees"
        cur.execute(qry)
        data = cur.fetchall()

        for row , form in enumerate(data):
            for col , item in enumerate(form):
                self.tableWidget_6.setItem(row, col, QTableWidgetItem(str(item)))
                col +=1

                row_position = self.tableWidget_6.rowCount()
                self.tableWidget_6.insertRow(row_position)
        QMessageBox.information(self, "","Data fetch successfully")

    def displayFees2(self):
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            db = "school_db"
        )
        cur = mydb.cursor()
        qry = "SELECT * FROM studies_fees"
        cur.execute(qry)
        data = cur.fetchall()

        for row , form in enumerate(data):
            for col , item in enumerate(form):
                self.tableWidget_6.setItem(row, col, QTableWidgetItem(str(item)))
                col +=1

                row_position = self.tableWidget_6.rowCount()
                self.tableWidget_6.insertRow(row_position)
        QMessageBox.information(self, "","Data fetch successfully")

    def updateFees(self):
        is_studies = "Studies Fees"
        is_feeding = "Feeding Fees"

        ans = self.comboBox_31.currentText()
        full_name = self.lineEdit_34.text()
        Class = self.comboBox_18.currentText()
        amount_paid = self.lineEdit_35.text()
        date = self.lineEdit_57.text()

        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            db = "school_db"
        )
        cur = mydb.cursor()

        if ans == is_feeding and full_name != '{}' and amount_paid != '{}':

            qry = """UPDATE feeding_fees SET Class = '{}',type_of_fees = '{}', amount_paid = '{}',  date = '{}',
              WHERE full_name = '{}'""".format(Class, ans, amount_paid, date, full_name)
            cur.execute(qry)
            mydb.commit()
            cur.close()
            QMessageBox.information(self, " ", "Updated Successfully")
            self.displayFees1()

        elif ans == is_studies and full_name != '{}' and amount_paid != '{}':

            qry = """UPDATE studies_fees SET Class = '{}',type_of_fees = '{}', amount_paid = '{}',  date = '{}',
              WHERE full_name = '{}'""".format(Class, ans, amount_paid, date, full_name)
            cur.execute(qry)
            mydb.commit()
            cur.close()
            QMessageBox.information(self, " ", "Updated Successfully")
            self.displayFees2()
        else:
            QMessageBox.warning(self, "Error", "Please fill the right details to updated")

    def searchFees(self):
        is_studies = "Studies Fees"
        is_feeding = "Feeding Fees"

        ans = self.comboBox_31.currentText()
        full_name = self.lineEdit_34.text()
        Class = self.comboBox_18.currentText()
        amount_paid = self.lineEdit_35.text()
        date = self.lineEdit_57.text()

        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            db = "school_db"
        )
        cur = mydb.cursor()
        if ans == is_feeding and full_name != '{}':
            QMessageBox.information(self, "Searching", "Search student Feeding Fees by Name")
            qry = "SELECT  FROM feeding_fees WHERE full_name ='{}'AND Class ='{}' AND date = '{}'".format(full_name, Class, date)
            cur.execute(qry)
            data = cur.fetchall()

            for row , form in enumerate(data):
                for col , item in enumerate(form):
                    self.tableWidget_6.setItem(row, col, QTableWidgetItem(str(item)))
                    col +=1

                    row_position = self.tableWidget_6.rowCount()
                    self.tableWidget_6.insertRow(row_position)
            QMessageBox.information(self, "","Data fetch successfully")

        elif ans == is_studies and full_name != '{}':
            QMessageBox.information(self, "Searching", "Search student Studies Fees by Name")
            qry = "SELECT * FROM studies_fees WHERE full_name ='{}'AND Class ='{}' AND date = '{}'".format(full_name, Class, date)
            cur.execute(qry)
            data = cur.fetchall()

            for row , form in enumerate(data):
                for col , item in enumerate(form):
                    self.tableWidget_6.setItem(row, col, QTableWidgetItem(str(item)))
                    col +=1

                    row_position = self.tableWidget_6.rowCount()
                    self.tableWidget_6.insertRow(row_position)
            QMessageBox.information(self, "","Data fetch successfully")

        else:
            QMessageBox.warning(self, "Error", "Please select a class to search")


    def deleteFees(self):
        is_studies = "Studies Fees"
        is_feeding = "Feeding Fees"

        ans = self.comboBox_31.currentText()
        full_name = self.lineEdit_34.text()
        Class = self.comboBox_18.currentText()

        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            db = "school_db"
        )
        cur = mydb.cursor()

        delete_message = QMessageBox.warning(self ,"COMFIRMATION" , "Do you want to Delete ?",QMessageBox.Yes | QMessageBox.No )
        QMessageBox.information(self, "Deleting", "Please select the Student's name and Class to delete")
        if ans == is_feeding and full_name != '':
            if delete_message == QMessageBox.Yes :
                qry = "DELETE * FROM feeding_fees WHERE full_name  = '{}' AND Class = '{}'".format(full_name, Class)
                cur.execute(qry)
                mydb.commit()
                cur.close()
                QMessageBox.information(self, " ", "Deleted successfully")
                self.displayFees1()

        elif ans == is_studies and full_name != '':
            if delete_message == QMessageBox.Yes :
                qry = "DELETE * FROM studies_fees WHERE full_name  = '{}' AND Class = '{}'".format(full_name, Class)
                cur.execute(qry)
                mydb.commit()
                cur.close()
                QMessageBox.information(self, " ", "Deleted successfully")
                self.displayFees2()
        else:
            QMessageBox.warning(self, " ", "Student's School Fees\n not found in DATABASE")
#self.tableWidget_5
# Printing Table

#  Student Reports Butoon Handling
    def reportsTab(self):
        self.tabWidget_4.setCurrentIndex(4)
        self.tabWidget_5.setCurrentIndex(0)
    def crache_inputTab(self):
        self.tabWidget_5.setCurrentIndex(0)
    def primary_inputTab(self):
        self.tabWidget_5.setCurrentIndex(1)
    def jhs_inputTab(self):
        self.tabWidget_5.setCurrentIndex(2)
    
    def crache_printTab(self):
        self.tabWidget_5.setCurrentIndex(3)
        
    
    #
    def primary_printTab(self):
        self.tabWidget_5.setCurrentIndex(4)

        ##Seting Up
        school_name = self.lineEdit_125.text()
        school_address = self.lineEdit_126.text()
        phone_number = self.lineEdit_127.text()
        school_term = self.comboBox_65.currentText()
        student_name = self.lineEdit_124.text()
        student_class = self.comboBox_12.currentText()
        promoted_to = self.comboBox_13.currentText()
        total_attendance = self.lineEdit_156.text()
        term_begins = self.lineEdit_168.text()
        term_end = self.lineEdit_167.text()
        school_date = self.lineEdit_184.text()

        if school_name != '{}' and school_address != '{}' and phone_number != '{}' and school_term != '{}':
            self.label_605.setText(school_name)
            self.label_606.setText(phone_number)
            self.label_607.setText(school_address)
            
            mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            db = "school_db"
            )
            cur = mydb.cursor()
            qry = "SELECT (registration_number) FROM students WHERE full_name = '{}'".format(student_name)
            cur.execute(qry)
            data = cur.fetchall()[0][0]

            self.label_610.setText(str(data))
            self.label_612.setText(student_name)
            self.label_618.setText(school_date)
            self.label_620.setText(student_class)
            self.label_616.setText(term_begins)
            self.label_614.setText(term_end)
            self.label_638.setText(total_attendance)

# Making qurey for subjects --------- Exams And Class Work-----------------------
    # English Language (Exams & Class Work)
            english = "English Language"
            marksType = "Exams"
            marksType1 = "Class Work"

            qry = """SELECT (marks) FROM mark WHERE full_name = '{}' AND Class = '{}' AND term = '{}'
             AND subjects = '{}' AND mark_type = '{}'""".format(student_name, student_class, school_term, english, marksType)
            cur.execute(qry)
            data1 = cur.fetchall()[0][0]
            if data1 == None:
                 self.label_759.setText("")
            else:
                ans = float(data1)
                result = ans / 2
                self.label_759.setText(str(result))


            qry = """SELECT (marks) FROM mark WHERE full_name = '{}' AND Class = '{}' AND term = '{}'
             AND subjects = '{}' AND mark_type = '{}'""".format(student_name, student_class, school_term, english, marksType1)
            cur.execute(qry)
            data2 = cur.fetchall()[0][0]
            if data2 == None:
                self.label_758.setText("")
            else:
                ans1 = float(data2)
                result2 = ans1 / 2
                self.label_758.setText(str(result2))

    # ghanaian Language (Exams & Class Work)
            ghana_lang = "Ghanaian Language"
            marksType2 = "Exams"
            marksType3 = "Class Work"

            qry = """SELECT (marks) FROM mark WHERE full_name = '{}' AND Class = '{}' AND term = '{}'
             AND subjects = '{}' AND mark_type = '{}'""".format(student_name, student_class, school_term, ghana_lang, marksType2)
            cur.execute(qry)
            data3 = cur.fetchall()[0][0]
            if data3 == None:
                 self.label_766.setText("")
            else:
                ans2 = float(data3)
                result3 = ans2 / 2
                self.label_766.setText(str(result3))


            qry = """SELECT (marks) FROM mark WHERE full_name = '{}' AND Class = '{}' AND term = '{}'
             AND subjects = '{}' AND mark_type = '{}'""".format(student_name, student_class, school_term, ghana_lang, marksType3)
            cur.execute(qry)
            data4 = cur.fetchall()[0][0]
            if data4 == None:
                self.label_765.setText("")
            else:
                ans3 = float(data4)
                result4 = ans3 / 2
                self.label_765.setText(str(result4))

    # Maths (Exams & Class Work)
            Maths = "Mathematics"
            marksType4 = "Exams"
            marksType5 = "Class Work"

            qry = """SELECT (marks) FROM mark WHERE full_name = '{}' AND Class = '{}' AND term = '{}'
             AND subjects = '{}' AND mark_type = '{}'""".format(student_name, student_class, school_term, ghana_lang, marksType4)
            cur.execute(qry)
            data5 = cur.fetchall()[0][0]
            if data5 == None:
                self.label_769.setText("")
            else:
                ans4 = float(data5)
                result5 = ans4 / 2
                self.label_769.setText(str(result5))


            qry = """SELECT (marks) FROM mark WHERE full_name = '{}' AND Class = '{}' AND term = '{}'
             AND subjects = '{}' AND mark_type = '{}'""".format(student_name, student_class, school_term, ghana_lang, marksType5)
            cur.execute(qry)
            data6 = cur.fetchall()[0][0]
            if data6 == None:
                self.label_768.setText("")
            else:
                ans5 = float(data6)
                result6 = ans5 / 2
                self.label_768.setText(str(result6))

    # Intergrated Science (Exams & Class Work)
            Science = "Intergrated Science"
            marksType4 = "Exams"
            marksType5 = "Class Work"

            qry = """SELECT (marks) FROM mark WHERE full_name = '{}' AND Class = '{}' AND term = '{}'
             AND subjects = '{}' AND mark_type = '{}'""".format(student_name, student_class, school_term, Science, marksType4)
            cur.execute(qry)
            data7 = cur.fetchall()[0][0]
            if data7 == None:
                self.label_777.setText("")
            else:
                ans6 = float(data7)
                result7 = ans6 / 2
                self.label_777.setText(str(result7))


            qry = """SELECT (marks) FROM mark WHERE full_name = '{}' AND Class = '{}' AND term = '{}'
             AND subjects = '{}' AND mark_type = '{}'""".format(student_name, student_class, school_term, Science, marksType5)
            cur.execute(qry)
            data8 = cur.fetchall()[0][0]
            if data8 == None:
                self.label_776.setText("")
            else:
                ans7 = float(data8)
                result8 = ans7 / 2
                self.label_776.setText(str(result8))

    # Religious and Moral Education (Exams & Class Work)
            r_m_e = "Religious and Moral Education"
            marksType6 = "Exams"
            marksType7 = "Class Work"

            qry = """SELECT (marks) FROM mark WHERE full_name = '{}' AND Class = '{}' AND term = '{}'
             AND subjects = '{}' AND mark_type = '{}'""".format(student_name, student_class, school_term, r_m_e, marksType6)
            cur.execute(qry)
            data9 = cur.fetchall()[0][0]
            if data9 == None:
                self.label_782.setText("")
            else:
                ans8 = float(data9)
                result9 = ans8 / 2
                self.label_782.setText(str(result9))


            qry = """SELECT (marks) FROM mark WHERE full_name = '{}' AND Class = '{}' AND term = '{}'
             AND subjects = '{}' AND mark_type = '{}'""".format(student_name, student_class, school_term, r_m_e, marksType7)
            cur.execute(qry)
            data10 = cur.fetchall()[0][0]
            if data10 == None:
                self.label_781.setText("")
            else:
                ans9 = float(data10)
                result10 = ans9 / 2
                self.label_781.setText(str(result10))

    # History (Exams & Class Work)
            History = "History"
            marksType8 = "Exams"
            marksType9 = "Class Work"

            qry = """SELECT (marks) FROM mark WHERE full_name = '{}' AND Class = '{}' AND term = '{}'
             AND subjects = '{}' AND mark_type = '{}'""".format(student_name, student_class, school_term, History, marksType8)
            cur.execute(qry)
            data11 = cur.fetchall()[0][0]
            if data11 == None:
                self.label_787.setText
            else:
                ans10 = float(data11)
                result11 = ans10 / 2
                self.label_787.setText(str(result11))


            qry = """SELECT (marks) FROM mark WHERE full_name = '{}' AND Class = '{}' AND term = '{}'
             AND subjects = '{}' AND mark_type = '{}'""".format(student_name, student_class, school_term, History, marksType9)
            cur.execute(qry)
            data12 = cur.fetchall()[0][0]
            if data12 == None:
                self.label_786.setText("")
            else:
                ans11 = float(data12)
                result12 = ans11 / 2
                self.label_786.setText(str(result12))

    # Computing (Exams & Class Work)
            Computing = "Computing"
            marksType10 = "Exams"
            marksType11 = "Class Work"

            qry = """SELECT (marks) FROM mark WHERE full_name = '{}' AND Class = '{}' AND term = '{}'
             AND subjects = '{}' AND mark_type = '{}'""".format(student_name, student_class, school_term, Computing, marksType10)
            cur.execute(qry)
            data13 = cur.fetchall()[0][0]
            if data13 == None:
                self.label_792.setText("")
            else:
                ans12 = float(data13)
                result13 = ans12 / 2
                self.label_792.setText(str(result13))


            qry = """SELECT (marks) FROM mark WHERE full_name = '{}' AND Class = '{}' AND term = '{}'
             AND subjects = '{}' AND mark_type = '{}'""".format(student_name, student_class, school_term, Computing, marksType11)
            cur.execute(qry)
            data14 = cur.fetchall()[0][0]
            if data14 == None:
                 self.label_791.setText("")
            else:
                ans13 = float(data14)
                result14 = ans13 / 2
                self.label_791.setText(str(result14))

    # Creative Arts (Exams & Class Work)
            Creative_Arts = "Creative Arts"
            marksType12 = "Exams"
            marksType13 = "Class Work"

            qry = """SELECT (marks) FROM mark WHERE full_name = '{}' AND Class = '{}' AND term = '{}'
             AND subjects = '{}' AND mark_type = '{}'""".format(student_name, student_class, school_term, Creative_Arts, marksType12)
            cur.execute(qry)
            data15 = cur.fetchall()[0][0]
            if data15 == None:
                self.label_797.setText("")
            else:
                ans14 = float(data15)
                result15 = ans14 / 2
                self.label_797.setText(str(result15))


            qry = """SELECT (marks) FROM mark WHERE full_name = '{}' AND Class = '{}' AND term = '{}'
             AND subjects = '{}' AND mark_type = '{}'""".format(student_name, student_class, school_term, Creative_Arts, marksType13)
            cur.execute(qry)
            data16 = cur.fetchall()[0][0]
            if data16 == None:
                self.label_796.setText("")
            else:
                ans15 = float(data16)
                result16 = ans15 / 2
                self.label_796.setText(str(result16))

    # OWOP(Exams & Class Work)
            OWOP= "Our World Our People"
            marksType14 = "Exams"
            marksType15 = "Class Work"

            qry = """SELECT (marks) FROM mark WHERE full_name = '{}' AND Class = '{}' AND term = '{}'
             AND subjects = '{}' AND mark_type = '{}'""".format(student_name, student_class, school_term, OWOP, marksType14)
            cur.execute(qry)
            data17 = cur.fetchall()[0][0]
            if data17 == None:
                self.label_802.setText("")
            else:
                ans16 = float(data17)
                result17 = ans16 / 2
                self.label_802.setText(str(result17))


            qry = """SELECT (marks) FROM mark WHERE full_name = '{}' AND Class = '{}' AND term = '{}'
             AND subjects = '{}' AND mark_type = '{}'""".format(student_name, student_class, school_term, OWOP, marksType15)
            cur.execute(qry)
            data18 = cur.fetchall()[0][0]
            if data18 == None:
                self.label_801.setText("")
            else:
                ans17 = float(data18)
                result18 = ans17 / 2
                self.label_801.setText(str(result18))

    # Calculating Sum Total of Exams & Class Work ---------------(Exams + Class Work)
        
            sumTotal = result + result2
            self.label_760.setText(str(sumTotal))

            sumTotal2 = result3 + result4
            self.label_764.setText(str(sumTotal2))

            sumTotal3 = result5 + result6
            self.label_771.setText(str(sumTotal3))

    def jhs_printTab(self):
        self.tabWidget_5.setCurrentIndex(5)

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())