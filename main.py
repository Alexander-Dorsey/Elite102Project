import mysql.connector
connection = mysql.connector.connect(user = 'root',database='bankingproject',password='TheFinisher518!')
cursor = connection.cursor()
addData =("INSERT INTO accounts(accountName,accountBalance,credit VALUES('Joe',5432.81,740)")
cursor.execute(addData)
connection.commit()
cursor.close()
connection.close()
