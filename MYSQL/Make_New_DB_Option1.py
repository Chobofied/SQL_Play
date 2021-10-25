from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user="root",
        password="1Gloomy10",
    ) as connection:
        create_db_query = "CREATE DATABASE online_movie_rating2"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
        print(connection)
except Error as e:
    print(e)