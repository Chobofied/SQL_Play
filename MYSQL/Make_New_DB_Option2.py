import mysql.connector
from mysql.connector import Error
import os


from dotenv import load_dotenv
load_dotenv()

MYSQL_PASSWORD=os.environ.get('MYSQL_PASSWORD')

def create_connection(host_name, user_name, MYSQL_PASSWORD):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=MYSQL_PASSWORD
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection("localhost", "root", MYSQL_PASSWORD)

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

create_database_query = "CREATE DATABASE Bank_Sim"
create_database(connection, create_database_query)