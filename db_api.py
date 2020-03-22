import MySQLdb
import base64
import socket

DataBaseName = input("Please Enter Your Database Name Here: ")
TableName = input("Please Enter your Table Name Here: ")
HostName = socket.gethostname()
mySQLUsername = input("Please enter your MySQL Username here: ")
mySQLPassword = input("Please enter your MySQL Password here: ")

base64.b64encode(mySQLUsername)
base64.b64encode(mySQLPassword)

if mySQLPassword == True :
    base64.b64decode(encryptUsername)
    base64.b64decode(encryptPassword)
    mySQLConnection = MySQLdb.connect('DataBaseName', 'HostName', user=mySQLUsername, password=mySQLPassword)
else :
    print("Please retype your password and try again.")
    break

def testCommit:
    try:
        mySQLQuery_INSERT = """INSERT INTO """ + TableName + """(TestData)
                    VALUES
                    (Transceiver Tested Successfully.) """
        mySQLCursor = mySQLConnection.cursor()
        mySQLCursor.execute(mySQLQuery_INSERT)
        mySQLConnection.commit()
        mySQLQuery_GET = """SELECT TestData FROM """ + mySQLTableName
        mysSQLCursor.execute(mySQLQuery_GET)
        mySQLConnection.commit()
        mySQLCursor.close()
    except mysql.connector.Error as error:
        print("System failed to retreive data. Please try again.")
        break
    finally:
        if (mySQLConnection.is_connected()):
            mySQLConnection.close()
testCommit()
