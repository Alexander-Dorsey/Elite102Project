import mysql.connector
connection = mysql.connector.connect(user = 'root',database='bankingproject',password='TheFinisher518!')
cursor = connection.cursor()
cursor.execute("INSERT INTO accounts(accountName,AccountBalance,AccountCredit) VALUES('Joe','5432.81','740')")
testQuery = "SELECT * FROM accounts"
cursor.execute(testQuery)
for item in cursor:
    print(item)
cursor.close()
connection.close()
