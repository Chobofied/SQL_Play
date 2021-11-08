#https://realpython.com/python-sql-libraries/#creating-tables

import mysql.connector
from mysql.connector import Error


class MYSQL_db():

  #Establishes a connection to the SQLite DB
  def __init__(self,host_name, user_name, MYSQL_PASSWORD, db_name):
    self.connection = None
    try:
        self.connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=MYSQL_PASSWORD,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
  
  # Posts data to the Database
  def execute_query(self, query,data=None):
    self.cursor = self.connection.cursor()
    try:
        self.cursor.execute(query,data)
        self.connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

  # Reads (Fetches) Data from the database
  def execute_read_query(self, query,data=None):
    #self.cursor = self.connection.cursor()
    result = None
    try:
        self.cursor.execute(query,data)
        result = self.cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")