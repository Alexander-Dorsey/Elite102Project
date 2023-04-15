import mysql.connector
connection = mysql.connector.connect(user = 'root',database='bankingproject',password='TheFinisher518!')
cursor = connection.cursor
test = "SELECT * FROM accounts"
cursor.execute(test)
for item in cursor:
    print(item)
cursor.close()
connection.close()
