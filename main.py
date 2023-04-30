import mysql.connector
connection = mysql.connector.connect(user = 'root',database='bankingproject',password='TheFinisher518!')
cursor = connection.cursor()
def check(ID):
    Query = ("SELECT accountBalance FROM accounts Where accountID = " + ID + "")
    cursor.execute(Query)
    for item in cursor:
        print(item)
def create(name,balance,cred,password):
    balance = float(balance)
    cred = int(cred)
    addData = ("INSERT INTO accounts(accountName,accountBalance,credit,password) VALUES('" + name + "'," + balance + "," + cred + "," + password + ")")
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
    elif(data[0].upper() == "C"):
        change = ("UPDATE accounts SET password = " + value + " WHERE accountID = " + str(ID))
    else:
        print("Not valid imput")
        return
    cursor.execute(change)
    connection.commit()
def login(): 
    print()
while(True):
    act = input("Welcome to the banking app.\nWould you like to create an account or login\n")
    if(act[0].upper == "L"):
        if(login()):
            break
    elif(act[0].upper == "C"):
        n = input("Set the name for your account")
        m = input("Set the starting balance of your account")
        c = input("Set the credit of your account")
        p = input("Set the password of your account")
        create(n,m,c,p)
    else:
        print("Invalid Input")
connection.close()
