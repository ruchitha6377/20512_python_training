import mysql.connector

def conect_mysql():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="root",
      database="case_study"
    )
    return mydb