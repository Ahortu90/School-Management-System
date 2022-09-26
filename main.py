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

from ui_SMS import *
import mysql.connector

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

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

    # Getting Data from the DATABASE

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
            qry = ("SELECT registration_number FROM students WHERE full_name = '{}'").format(search_by_name)
            cur.execute(qry)
            data = cur.fetchone()

            #self.lineEdit_7.setDisabled(True)
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
        if date != '':
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
        QMessageBox.information(self, "Update Button", "Please you cann't use the update button\nPlease delete the details to add \n new one")

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


if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())