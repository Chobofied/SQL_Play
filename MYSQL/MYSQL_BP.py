#https://realpython.com/python-sql-libraries/#creating-tables


import mysql.connector
from mysql.connector import Error
import os

#Gets Environmental Variables
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
  def execute_read_query(self, query,data=None):
    #self.cursor = self.connection.cursor()
    result = None
    try:
        self.cursor.execute(query,data)
        result = self.cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

  def user_entry(self, insert_stmt,data):
    try:
      self.cursor.execute(insert_stmt, data)
      self.connection.commit()
      x=4
    except Error as e:
        print(f"The error '{e}' occurred")
  

def Create_New_Account(MYSQL_DB,Acc_ID,Name,Balances,Address):
  
  ## Creates a new account
  Account_Creation=("INSERT INTO `Accounts` (`name`,`address`) "
    "VALUES (%s, %s)"
  )

  MYSQL_DB.user_entry(Account_Creation,(Name,Address))
  
  
  initial_deposit = (
    "INSERT INTO `Transactions` (`Acc_ID`,CURDATE(),`Changes`,`Comment`,`Balances`) "
    "VALUES (%s, %s, %s,%s)"
  )
  insert_data=(Acc_ID,Balances,'Initial Deposit',Balances)
  MYSQL_DB.user_entry(initial_deposit,insert_data)

def New_Transaction(MYSQL_DB,Acc_ID,change,comment):

  # Finds the latest balance and makes account changes to it and assings it to @bal. 
  MYSQL_DB.user_entry("""SET @bal =(SELECT Balances FROM transactions 
                        Where Acc_id=%s 
                        ORDER BY Trans_ID desc LIMIT 1)+%s;
                        """,(Acc_ID,change))

 # Inserts that new balance into the transaction table
  MYSQL_DB.user_entry("""
                        INSERT INTO `Transactions` (`Acc_ID`,`TimeStamp`,`Changes`,`Comment`,`Balances`)  
                        VALUES (%s, CURDATE(), %s, %s,@bal)""",(Acc_ID,change,comment))
  


### EXAMPLE CONNECTION AND SELECTING DATA
if __name__ == '__main__':

  # Get Environmental variables. Password is saved in .env file
  MYSQL_PASSWORD=os.environ.get('MYSQL_PASSWORD')

  #Establish Connection to MYSQL
  test_MYSQL=MYSQL_db("localhost", "root", MYSQL_PASSWORD,"sm_app")


  ## MAKE A TABLE EXAMPLE
  create_users_table = """
  CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT, 
    name varchar(255) NOT NULL, 
    age INT, 
    gender TEXT, 
    nationality TEXT,
    UNIQUE (name),
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

  create_accounts_table="""
  CREATE TABLE IF NOT EXISTS Accounts (
    Acc_ID INT AUTO_INCREMENT,
    Name varchar(255) NOT NULL,
    address varchar(255),
    UNIQUE(Name),
    PRIMARY KEY (Acc_ID)
); """

  create_transaction_table="""
  CREATE TABLE IF NOT EXISTS Transactions (
  Trans_ID INT AUTO_INCREMENT,
  Acc_ID INT NOT NULL,
  TimeStamp varchar(255) NOT NULL,
  Changes FLOAT,
  Comment TEXT,
  Balances FLOAT,
  PRIMARY KEY (Trans_ID),
  FOREIGN KEY (Acc_ID) REFERENCES Accounts(Acc_ID)
);
  """

  test_MYSQL.execute_query(create_users_table)
  test_MYSQL.execute_query(create_persons_table)

  test_MYSQL.execute_query(create_accounts_table)
  test_MYSQL.execute_query(create_transaction_table)

  ## INSERTING RECORDS EXAMPLE

  #This replaces the data if it is already there (if someone has that name, the rest of the values are updated rather than duplicated)
  create_users = """
  REPLACE INTO
    `users` (`name`, `age`, `gender`, `nationality`)
  VALUES
    ('James', 1010, 'male', 'USA'),
    ('Leila', 32, 'female', 'France'),
    ('Brigitte', 35, 'female', 'England'),
    ('Mike', 40, 'male', 'Denmark'),
    ('Elizabeth', 21, 'female', 'Canada');

  """

  create_Accounts = """
  INSERT INTO
    `Accounts` (`name`,`address`)
  VALUES
    ('Zach','Portland'),
    ('Annie','NewYork'),
    ('Taylor','Everett');
  """

  create_Transactions = """
  INSERT INTO
    `Transactions` (`Acc_ID`,`TimeStamp`,`Changes`,`Comment`,`Balances`)
  VALUES
    ('1','10/21','50','init_depot1','50'),
    ('1','10/22','-40','Diablo2 Pur','10'),
    ('1','10/23','10','BDay$','20'),
    ('3','10/24','-20','Horse','-20'),
    ('2','10/25','20','Payday$','20');
  """



#There is a Unique last name, so if a duplicate last name appears, it ignores it and chugs on
  create_persons = """
  INSERT INTO
    `persons` (`ID`, `LastName`, `FirstName`, `Age`)
  VALUES
    (1, 'Taylor', 'Joe', 31),
    (2, 'Taylor2', 'Joe', 33),
    (3, 'Taylor3', 'Joe', 33);
  """


  test_MYSQL.execute_query(create_users)
  test_MYSQL.execute_query(create_persons)

  test_MYSQL.execute_query(create_Accounts)
  test_MYSQL.execute_query(create_Transactions)


  ## INNER JOIN

  inner_join="""SELECT 
  transactions.Trans_ID,accounts.Name 
  FROM transactions 
  INNER JOIN accounts ON 
  transactions.Acc_ID=Accounts.Acc_ID"""

  innjoin=test_MYSQL.execute_read_query(inner_join)


  ## SELECTING RECORDS EXAMPLE


  select_users = "SELECT * FROM users"
  users = test_MYSQL.execute_read_query(select_users)

  for user in users:
      print(user)

  ## UPDATING RECORDS
  update_user_name= """
  UPDATE 
    users 
  SET 
    name='Update Name Success' 
  WHERE 
    id=2;
  """
  test_MYSQL.execute_query(update_user_name)

  ## DELETE RECORD

  Delete_Person="""
  DELETE FROM persons 
  WHERE LastName in ('Taylor2')"""

  test_MYSQL.execute_query(Delete_Person)


  ## SAFE USER ENTRY EXAMPLE

  insert_stmt = (
    "INSERT INTO `persons` (`ID`, `LastName`, `FirstName`,`Age`) "
    "VALUES (%s, %s, %s, %s)"
  )

  data = (3, 'Taylor23', 'Joe3', 34)


 ##  New Account Creation 
  Create_New_Account(test_MYSQL,'4','ZOSU',100,'Bungie')

  ## Transactions Made for new account
  New_Transaction(test_MYSQL,'4',-40,'D2R')
  New_Transaction(test_MYSQL,'4',80,'PayCheck')
  New_Transaction(test_MYSQL,'4',-15,'Taco-Bell')

  #Get Account Data for selected User
  Account='ZOSU'
  Statement = test_MYSQL.execute_read_query("""SELECT * FROM transactions 
                      Where Acc_ID=(SELECT Acc_ID FROM accounts Where Name=%s) 
                      ORDER BY Trans_ID desc LIMIT 100""",(Account,))

  print(Statement)
  x=4