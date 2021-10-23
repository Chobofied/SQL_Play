#https://realpython.com/python-sql-libraries/#creating-tables


import mysql.connector
from mysql.connector import Error
import os


from dotenv import load_dotenv
load_dotenv()



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
  def execute_query(self, query):
    self.cursor = self.connection.cursor()
    try:
        self.cursor.execute(query)
        self.connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

  # Reads (Fetches) Data from the database
  def execute_read_query(self, query):
    self.cursor = self.connection.cursor()
    result = None
    try:
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

  def user_entry(self, insert_stmt,data):
      self.cursor.execute(insert_stmt, data)
      self.connection.commit()
      x=4



### EXAMPLE CONNECTION AND SELECTING DATA

# Get Environmental variables
MYSQL_PASSWORD=os.environ.get('MYSQL_PASSWORD')
test_MYSQL=MYSQL_db("localhost", "root", MYSQL_PASSWORD,"sm_app")

## MAKE A TABLE EXAMPLE

create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT, 
  name TEXT NOT NULL, 
  age INT, 
  gender TEXT, 
  nationality TEXT,
  PRIMARY KEY (id)
) ENGINE = InnoDB
"""

create_persons_table="""CREATE TABLE IF NOT EXISTS Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    UNIQUE (LastName)
);"""

test_MYSQL.execute_query(create_users_table)
test_MYSQL.execute_query(create_persons_table)

## INSERTING RECORDS EXAMPLE

create_users = """
INSERT INTO
  `users` (`name`, `age`, `gender`, `nationality`)
VALUES
  ('James', 101, 'male', 'USA'),
  ('Leila', 32, 'female', 'France'),
  ('Brigitte', 35, 'female', 'England'),
  ('Mike', 40, 'male', 'Denmark'),
  ('Elizabeth', 21, 'female', 'Canada');
"""



create_persons = """
INSERT INTO
  `persons` (`ID`, `LastName`, `FirstName`, `Age`)
VALUES
  (1, 'Taylor', 'Joe', 31),
  (2, 'Taylor2', 'Joe', 33);
"""

#"INSERT INTO `persons` (`ID`, `LastName`, `FirstName`,`Age`) VALUES (3, 'Taylor23', 'Joe3', 34)"

test_MYSQL.execute_query(create_users)
test_MYSQL.execute_query(create_persons)


## SELECTING RECORDS EXAMPLE


select_users = "SELECT * FROM users"
users = test_MYSQL.execute_read_query(select_users)

for user in users:
    print(user)

## DELETE RECORD

Delete_Person="""
 DELETE FROM persons 
 WHERE LastName in ('Taylor2')"""

test_MYSQL.execute_query(Delete_Person)

x=5

## SAFE ENTRY

insert_stmt = (
  "INSERT INTO `persons` (`ID`, `LastName`, `FirstName`,`Age`) "
  "VALUES (%s, %s, %s, %s)"
)
data = (3, 'Taylor23', 'Joe3', 34)
test_MYSQL.user_entry(insert_stmt, data)