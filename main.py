import mysql.connector
connection = mysql.connector.connect(user = 'root',database='bankingproject',password='TheFinisher518!')
cursor = connection.cursor()
def check(ID):
    ID = str(ID)
    Query = ("SELECT accountBalance FROM accounts Where accountID = " + ID + "")
    cursor.execute(Query)
    for item in cursor:
        print(item)
def info(ID):
    ID = str(ID)
    Query = ("SELECT * FROM accounts Where accountID = " + ID + "")
    cursor.execute(Query)
    for item in cursor:
        print(item)
def create(name,balance,cred,password):
    addData = ("INSERT INTO accounts(accountName,accountBalance,credit,password) VALUES('" + name + "'," + balance + "," + cred + ",'" + password + "')")
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
    elif(data[0].upper() == "P"):
        change = ("UPDATE accounts SET password = " + value + " WHERE accountID = " + str(ID))
    else:
        print("Not valid imput")
        return
    cursor.execute(change)
    connection.commit()
def login(): 
     n = input("Enter the name for your account\n")
     n = str(n)
     p = input("Enter the password of your account\n")
     p = str(p)
     Query = ("SELECT * FROM accounts WHERE accountName = '" + n + "' AND password = '" + p + "'")
     cursor.execute(Query)
     count = 0
     for item in cursor:
         count = count + 1
         print(item)
     if(count != 1):
         print("Account with provided info does not exist please try again")
         login()
     for item in cursor:
        print(item)
     global identifier
     q = ("SELECT accountID FROM accounts WHERE password = '" + p + "'")
     cursor.execute(q)
     for item in cursor:
        ident = item
     identifier = ident[0]
"""
cond = True
while(cond == True):
    act = input("Welcome to the banking app.\nWould you like to create an account or login\n")
    if(act[0].upper() == 'L'):
            login()
            cond = False
    elif(act[0].upper() == 'C'):
        con = False
        while(con == False):
            n = input("Set the name for your account\n")
            m = input("Set the starting balance of your account\n")
            c = input("Set the credit of your account\n")
            p = input("Set the password of your account\n")
            Query = ("SELECT * FROM accounts Where password = '" + p  + "'")
            cursor.execute(Query)
            count = 0
            for item in cursor:
                count = count + 1
            if(count == 0):
                create(n,m,c,p)
                con = True
            else:
                print("Account with password already exists")
    else:
        print("Invalid Input")
run = True
while(run):
    uIn = input("What would you like to do\nThe Options are:\nCheck Balance\nSee Info\nAdd Money\nWithdraw\nModify account info\nDelete Accout\nQuit\n")
    if(uIn[0].upper() == 'C'):
        check(identifier)
    elif(uIn[0].upper() == 'A'):
        depo = input("How much would you like to input?\n")
        add(identifier,depo)
    elif(uIn[0].upper() == 'W'):
        loss = input("How much would you like to withdraw\n")
        withdraw(identifier,loss)
    elif(uIn[0].upper() == 'M'):
        change = input("What would you like to change\nYou can change your accounts name password or credit\n")
        v = input("What would you like to change it to\n")
        modify(identifier,change,v)
    elif(uIn[0].upper() == 'D'):
        confirm = input("Are you sure you would like to delete your account\n")
        if(confirm[0].upper() == "Y"):
            delete(identifier)
            run = False 
        else:
            print("Account not deleted")
    elif(uIn[0].upper() == 'Q'):
        confirm = input("Are you sure you would like to quit\n")
        if(confirm[0].upper() == "Y"):
            run = False
    elif(uIn[0].upper() == 'S'):
        info(identifier)
"""
connection.close()
