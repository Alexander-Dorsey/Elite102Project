import mysql.connector
connection = mysql.connector.connect(user = 'root',database='bankingproject',password='TheFinisher518!')
cursor = connection.cursor()
addData =("INSERT INTO accounts(accountName,accountBalance,credit) VALUES('Joe',5432.81,740)")
cursor.execute(addData)
testQuery = ("SELECT * FROM accounts")
cursor.execute(testQuery)
for item in cursor:
    print(item)
connection.commit()
cursor.close()
connection.close()
