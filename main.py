import mysql.connector
connection = mysql.connector.connect(user = 'root',database='bankingproject',password='TheFinisher518!')
cursor = connection.cursor()
def check(ID):
    Query = ("SELECT accountBalance FROM accounts Where accountID = " + ID + "")
    cursor.execute(Query)
    for item in cursor:
        print(item)
def create(name,balance,cred):
    addData = ("INSERT INTO accounts(accountName,accountBalance,credit) VALUES('" + name + "'," + balance + "," + cred + ")")
    cursor.execute(addData)
    connection.commit()
def show():
    testQuery = ("SELECT * FROM accounts")
    cursor.execute(testQuery)
    for item in cursor:
        print(item)
def add(ID,amount):
    ID = str(ID)
    Query = ("(SELECT accountBalance FROM accounts Where accountID = " + ID + ")")
    amount = float(amount)
    cursor.execute(Query)
    for item in cursor:
        temp = str(item[0])
        break
    amount += float(temp)
    amount = str(amount)
    addM = ("UPDATE accounts SET accountBalance =" + amount + " Where accountID = " + ID + "")
    cursor.execute(addM)
    connection.commit()
def withdraw(ID,amount):
    ID = str(ID)
    Query = ("(SELECT accountBalance FROM accounts Where accountID = " + ID + ")")
    amount = float(amount)
    cursor.execute(Query)
    for item in cursor:
        temp = str(item[0])
        break
    temp = float(temp)
    temp -= amount
    temp = str(temp)
    addM = ("UPDATE accounts SET accountBalance =" + temp + " Where accountID = " + ID + "")
    cursor.execute(addM)
    connection.commit()
def trunc():
    truncateData = ("TRUNCATE accounts")
    cursor.execute(truncateData)
    connection.commit()
def delete(ID):
    ID = str(ID)
    delete = ("DELETE FROM accounts WHERE accountID = " + ID)
    cursor.execute(delete)
    connection.commit()
def modify(ID,data,value):
    ID = str(ID)
    data = str(data)
    value = str(value)
    if (data[0].upper() == "N"):
        change = ("UPDATE accounts SET accountName = \"" + value + "\" WHERE accountID = " + str(ID))
    elif(data[0].upper() == "C"):
        change = ("UPDATE accounts SET credit = " + value + " WHERE accountID = " + str(ID))
    cursor.execute(change)
    connection.commit()
##trunc()
##create("John","54832.8","650")
##add(1,500.00)
##withdraw(1,500.00)
##modify(1,"name","Smith")
##delete(1)
show()
connection.close()
