from MYSQL_BP import MYSQL_db

def Establish_Connection(MYSQL_PASSWORD):
  Bank_MYSQL=MYSQL_db("localhost", "root", MYSQL_PASSWORD,"bank_sim")
  return Bank_MYSQL

def Create_Accounts_Table():

  create_accounts_table="""
  CREATE TABLE IF NOT EXISTS Accounts (
    Acc_ID INT AUTO_INCREMENT,
    Name varchar(255) NOT NULL,
    address varchar(255),
    UNIQUE(Name),
    PRIMARY KEY (Acc_ID)
); """


  Bank_MYSQL.execute_query(create_accounts_table)
  

def Create_Transaction_Table():

  create_transaction_table="""
  CREATE TABLE IF NOT EXISTS Transactions (
  Trans_ID INT AUTO_INCREMENT,
  Acc_ID INT NOT NULL,
  Date varchar(255) NOT NULL,
  TimeStamp varchar(255) NOT NULL,
  Changes FLOAT,
  Comment TEXT,
  Balances FLOAT,
  PRIMARY KEY (Trans_ID),
  FOREIGN KEY (Acc_ID) REFERENCES Accounts(Acc_ID)
);
  """

  Bank_MYSQL.execute_query(create_transaction_table)

def Create_New_Account(MYSQL_DB,Name,Balances,Address):
  
  ## Creates a new account
  Account_Creation=("INSERT INTO `Accounts` (`name`,`address`) "
    "VALUES (%s, %s)"
  )

  MYSQL_DB.execute_query(Account_Creation,(Name,Address))

  #Look up Account ID from Name
  MYSQL_DB.execute_query("""SET @ID =(SELECT Acc_ID FROM accounts Where Name=%s)""",(Name,))

  #Creates an initial Transaction for Bank Account  
  MYSQL_DB.execute_query("""
                        INSERT INTO `Transactions` (`Acc_ID`,`Date`,`TimeStamp`,`Changes`,`Comment`,`Balances`)  
                        VALUES (@ID, CURDATE(),NOW(), %s,%s,%s)""",(Balances,'Initial Deposit',Balances))

  #MYSQL_DB.user_entry(initial_deposit,insert_data)

def New_Transaction(MYSQL_DB,Account_Name,change,comment):

   #Look up Account ID from Name
  MYSQL_DB.execute_query("""SET @ID =(SELECT Acc_ID FROM accounts Where Name=%s)""",(Account_Name,))

  # Finds the latest balance and makes account changes to it and assings it to @bal. 
  MYSQL_DB.execute_query("""SET @bal =(SELECT Balances FROM transactions 
                        Where Acc_id=@ID 
                        ORDER BY Trans_ID desc LIMIT 1)+%s;
                        """,(change,))

 # Inserts that new balance into the transaction table
  MYSQL_DB.execute_query("""
                        INSERT INTO `Transactions` (`Acc_ID`,`Date`,`TimeStamp`,`Changes`,`Comment`,`Balances`)  
                        VALUES (@ID, CURDATE(),NOW(), %s, %s,@bal)""",(change,comment))


### EXAMPLE CONNECTION AND SELECTING DATA
if __name__ == '__main__':

  #Gets Environmental Variables
  import os
  from dotenv import load_dotenv
  load_dotenv()

  # Get Environmental variables. Password is saved in .env file
  MYSQL_PASSWORD=os.environ.get('MYSQL_PASSWORD')

  #Establish Connection to MYSQL
  Bank_MYSQL=Establish_Connection(MYSQL_PASSWORD)
  Create_Accounts_Table()
  Create_Transaction_Table()


  Create_New_Account(Bank_MYSQL,'ZOSU',100,'Bungie')

  ## Transactions Made for new account
  New_Transaction(Bank_MYSQL,'ZOSU',-40,'D2R')
  New_Transaction(Bank_MYSQL,'ZOSU',80,'PayCheck')
  New_Transaction(Bank_MYSQL,'ZOSU',-15,'Taco-Bell')
  

  Create_New_Account(Bank_MYSQL,'Taylor',200,'Everett')
  New_Transaction(Bank_MYSQL,'Taylor',-57,'Destiny2 Purchase')