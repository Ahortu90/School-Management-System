import mysql.connector

mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            db = "school_db"
            )
cur = mydb.cursor()