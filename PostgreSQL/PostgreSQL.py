#https://realpython.com/python-sql-libraries/#creating-tables


import psycopg2
from psycopg2 import Error

try:
    # Connect to an existing database
    connection = psycopg2.connect(user="postgres",
                                  password="pynative@#29",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres_db")

    # Create a cursor to perform database operations
    cursor = connection.cursor()
    # Print PostgreSQL details
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")
    # Executing a SQL query
    cursor.execute("SELECT version();")
    # Fetch result
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")



class PostgreSQL_db():

  #Establishes a connection to the SQLite DB
  def __init__(self,db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

  # Reads (Fetches) Data from the database
  def execute_read_query(self, query):
    result = None
    try:
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

def example_routine_POST():
  connection = PostgreSQL_db(
    "postgres", "postgres", "abc123", "127.0.0.1", "5432"
)

def example_routine():
  '''
  Example Routine that creates an SQLlite Database, 
  posts, reads, appends, deletes data with user inputs allowed
  
  Call from Shell Command below
  python
  from sqllite_create import example_routine
  example_routine
  '''
 
  path="C://Users//Taylo//OneDrive//Python//Functions//SQL//SQLLite//sqllite_test.db"

  #Creates an instance of the SQLlite Database
  test_sql=sqllite_db(path)

  #Creates lists of the Tables and Data to added to the SQLlite Database
  Tables=(SQL_Querie.Create.create_users_table,
          SQL_Querie.Create.create_posts_table,
          SQL_Querie.Create.create_comments_table,
          SQL_Querie.Create.create_likes_table)

  Tables_Data=(SQL_Querie.Create.create_users,
              SQL_Querie.Create.create_posts,
              SQL_Querie.Create.create_comments,
              SQL_Querie.Create.create_likes)

  #Creates the Tables and fills them with data
  for Table in Tables:
    test_sql.execute_query(Table)

  for Table_Data in Tables_Data:
    test_sql.execute_query(Table_Data)


  #Reads Specific Data from the Database and printes them
  results=test_sql.execute_read_query(SQL_Querie.Select.select_users_posts)

  for result in results:
        print(result)


  #Inserts Records Into Table (User)
  User_Append = """
  INSERT INTO
    users (name, age, gender, nationality)
  VALUES
    ('Taylor', 30, 'male', 'USA');
  """

  test_sql.execute_query(User_Append)
  #test_sql.execute_query(SQL_Querie.Create.create_users_table)


  #User Input Data, SQL injection protection

  # See https://docs.python.org/3/library/sqlite3.html
  # Set up for users to input data

  The_Name='RealSlimShady'
  test_sql.cursor.execute("INSERT INTO users (name, age, gender, nationality) VALUES (?,?,?,?)",(The_Name, 21, "female", "Canada"))
  test_sql.connection.commit()

  #Delete Example
  delete_comment = "DELETE FROM users WHERE id = 5"
  test_sql.execute_query(delete_comment)

  delete_comment = "DELETE FROM users WHERE name = 'Taylor'"
  test_sql.execute_query(delete_comment)

  #User Delete Example

  Delete_Name='Brigitte'
  test_sql.cursor.execute("DELETE FROM users WHERE name = (?)",(Delete_Name,))
  test_sql.connection.commit()


if __name__ == '__main__':
  x=3
    #connection = create_connection(
    #"postgres", "postgres", "abc123", "127.0.0.1", "5432"
#)
    #example_routine_POST()
    
