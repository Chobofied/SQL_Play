#https://realpython.com/python-sql-libraries/#creating-tables


import SQL_Querie
import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")



def main_routine():
  ##Call from Shell Command
  #python
  #from sqllite_create import main_routine
  #main_routine
  path="C://Users//Taylo//OneDrive//Python//Functions//SQL//SQLLite//sqllite_test.db"

  ## CREATES Connection / Empty Database
  connection=create_connection(path)

  ## Connects to Database and Creates a Table if it does not exist (User)


  #SQL_Querie.Create.create_users_table
  execute_query(connection, SQL_Querie.Create.create_users_table)
  
def Create_Tables():
  execute_query(connection, SQL_Querie.Create.create_users_table)
  execute_query(connection, SQL_Querie.Create.create_posts_table) 
  execute_query(connection, SQL_Querie.Create.create_comments_table)  
  execute_query(connection, SQL_Querie.Create.create_likes_table) 

def Fill_Tables():
  execute_query(connection, SQL_Querie.Create.create_users)
  execute_query(connection, SQL_Querie.Create.create_posts)
  execute_query(connection, SQL_Querie.Create.create_comments)
  execute_query(connection, SQL_Querie.Create.create_likes)  

def Show_Data(Data):
  Results=execute_read_query(connection, Data)

  for result in Results:
        print(result)


if __name__ == '__main__':

    main_routine()
    path="C://Users//Taylo//OneDrive//Python//Functions//SQL//SQLLite//sqllite_test.db"

    ## CREATES Connection / Empty Database
    connection=create_connection(path)

    ## Connects to Database and Creates a Table if it does not exist (User)


    #SQL_Querie.Create.create_users_table
    Create_Tables()
    Fill_Tables()
    Show_Data(SQL_Querie.Select.select_users_posts)

    """
    execute_query(connection, SQL_Querie.Create.create_users_table)
    execute_query(connection, SQL_Querie.Create.create_posts_table) 
    execute_query(connection, SQL_Querie.Create.create_comments_table)  
    execute_query(connection, SQL_Querie.Create.create_likes_table)  
    
    
    """
  

    ## Inserts Records Into Table (User)


    User_Append = """
    INSERT INTO
      users (name, age, gender, nationality)
    VALUES
      ('Taylor', 30, 'male', 'USA');
    """



    execute_query(connection, User_Append)







    ## See https://docs.python.org/3/library/sqlite3.html
    # Set up for users to input data

    The_Name='RealSlimShady'

    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name, age, gender, nationality) VALUES (?,?,?,?)",(The_Name, 21, "female", "Canada"))
    connection.commit()
    #execute_query(connection, create_users)

    #Delete Example
    delete_comment = "DELETE FROM users WHERE id = 5"
    execute_query(connection, delete_comment)

    delete_comment = "DELETE FROM users WHERE name = 'Taylor'"
    execute_query(connection, delete_comment)


    #User Delete Example

    Delete_Name='Brigitte'
    cursor.execute("DELETE FROM users WHERE name = (?)",(Delete_Name,))
    connection.commit()









 