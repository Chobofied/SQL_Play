#https://realpython.com/python-sql-libraries/#creating-tables


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


if __name__ == '__main__':
    path="C://Users//Taylo//OneDrive//Python//Functions//SQL//SQLLite//sqllite_test.db"


    
    ## CREATES Connection / Empty Database
    connection=create_connection(path)

    ## Connects to Database and Creates a Table if it does not exist (User)

    create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  age INTEGER,
  gender TEXT,
  nationality TEXT
);
"""

create_posts_table = """
CREATE TABLE IF NOT EXISTS posts(
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  title TEXT NOT NULL, 
  description TEXT NOT NULL, 
  user_id INTEGER NOT NULL, 
  FOREIGN KEY (user_id) REFERENCES users (id)
);
"""

create_comments_table = """
CREATE TABLE IF NOT EXISTS comments (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  text TEXT NOT NULL, 
  user_id INTEGER NOT NULL, 
  post_id INTEGER NOT NULL, 
  FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
);
"""

create_likes_table = """
CREATE TABLE IF NOT EXISTS likes (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  user_id INTEGER NOT NULL, 
  post_id integer NOT NULL, 
  FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
);
"""


execute_query(connection, create_users_table)
execute_query(connection, create_posts_table) 
execute_query(connection, create_comments_table)  
execute_query(connection, create_likes_table)  

## Inserts Records Into Table (User)

create_users = """
INSERT INTO
  users (name, age, gender, nationality)
VALUES
  ('James', 25, 'male', 'USA'),
  ('Leila', 32, 'female', 'France'),
  ('Brigitte', 35, 'female', 'England'),
  ('Mike', 40, 'male', 'Denmark'),
  ('Elizabeth', 21, 'female', 'Canada');
"""
create_posts = """
INSERT INTO
  posts (title, description, user_id)
VALUES
  ("Happy", "I am feeling very happy today", 1),
  ("Hot Weather", "The weather is very hot today", 2),
  ("Help", "I need some help with my work", 2),
  ("Great News", "I am getting married", 1),
  ("Interesting Game", "It was a fantastic game of tennis", 5),
  ("Party", "Anyone up for a late-night party today?", 3);
"""

create_comments = """
INSERT INTO
  comments (text, user_id, post_id)
VALUES
  ('Count me in', 1, 6),
  ('What sort of help?', 5, 3),
  ('Congrats buddy', 2, 4),
  ('I was rooting for Nadal though', 4, 5),
  ('Help with your thesis?', 2, 3),
  ('Many congratulations', 5, 4);
"""

create_likes = """
INSERT INTO
  likes (user_id, post_id)
VALUES
  (1, 6),
  (2, 3),
  (1, 5),
  (5, 4),
  (2, 4),
  (4, 2),
  (3, 6);
"""

User_Append = """
INSERT INTO
  users (name, age, gender, nationality)
VALUES
  ('Taylor', 30, 'male', 'USA');
"""


execute_query(connection, create_users)
execute_query(connection, create_posts)
execute_query(connection, create_comments)
execute_query(connection, create_likes)  

execute_query(connection, User_Append)

select_users_posts = """
SELECT
  users.id,
  users.name,
  users.age,
  posts.description
FROM
  posts
  INNER JOIN users ON users.id = posts.user_id
"""



users_posts = execute_read_query(connection, select_users_posts)

for users_post in users_posts:
    print(users_post)





## See https://docs.python.org/3/library/sqlite3.html
# Set up for users to input data

The_Name='RealSlimShady'

cursor = connection.cursor()
cursor.execute("INSERT INTO users (name, age, gender, nationality) VALUES (?,?,?,?)",(The_Name, 21, "female", "Canada"))
connection.commit()
execute_query(connection, create_users)

#Delete Example
delete_comment = "DELETE FROM users WHERE id = 5"
execute_query(connection, delete_comment)

delete_comment = "DELETE FROM users WHERE name = 'Taylor'"
execute_query(connection, delete_comment)


#User Delete Example

Delete_Name='Brigitte'
cursor.execute("DELETE FROM users WHERE name = (?)",(Delete_Name,))
connection.commit()
execute_query(connection, delete_comment)








 