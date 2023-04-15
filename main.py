import mysql.connector
connection = mysql.connector.connect(user = 'root',database='bankingproject',password='TheFinisher518!')
cursor = connection.cursor()
def check(ID):
    Query = ("SELECT accountBalance FROM accounts Where accountID = " + ID + "")
    cursor.execute(Query)
    for item in cursor:
        print(item)
check('6');
connection.commit()
cursor.close()
connection.close()
