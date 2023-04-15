import mysql.connector
connection = mysql.connector.connect(user = 'root',database='bankingproject',password='TheFinisher518!')
cursor = connection.cursor()
def check(ID):
    Query = ("SELECT accountBalance FROM accounts Where accountID = " + ID + "")
    cursor.execute(Query)
    for item in cursor:
        print(item)
def create(name,balance,cred):
    addData = ("INSERT INTO accounts(accountName,accountBalance,credit) VALUES(" + name + "," + balance + "," + cred + ")")
    cursor.execute(addData)
    connection.commit
def show():
    testQuery = ("SELECT * FROM accounts")
    cursor.execute(testQuery)
create('John','6900','450')
show()
connection.commit()
cursor.close()
connection.close()
