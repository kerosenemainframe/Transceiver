#Imports
from flask import Flask
import MySQLdb
import base64
from socket import gethostname, socket
from zlib import compress, decompress
from time import sleep
from sys import getsizeof
from json import dumps

#Database Values
def dataGather():
    DataBaseName = input("Please Enter The Name Of Your Database Here: ")
    TableName = input("Please Enter The Name Of Your Table Here: ")
    HostName = gethostname()
    mySQLUsername = input("Please enter your MySQL Username here: ")
    mySQLPassword = input("Please enter your MySQL Password here: ")
dataGather()

#API Values
API_app = Flask(__name__)
def flaskHomeScreen():
    return "<h1>Welcome to the Transceiver API System.</h1>"

#Base64 Encoding
base64.b64encode(mySQLUsername)
base64.b64encode(mySQLPassword)

#Base64 Decrypting
while mySQLPassword == True :
    base64.b64decode(encryptUsername)
    base64.b64decode(encryptPassword)
    mySQLConnection = MySQLdb.connect(db='DataBaseName', host='HostName', user=mySQLUsername, password=mySQLPassword)
    break
else :
    print("Please retype your password and try again.")
    dataGather()

#MySQL Testing
def testCommit():
    try:
        mySQLQuery_TEST_INSERT = """INSERT INTO """ + TableName + """(TestData)
                    VALUES
                    (Transceiver Tested Successfully.) """
        mySQLCursor = mySQLConnection.cursor()
        mySQLCursor.execute(mySQLQuery_TEST_INSERT)
        mySQLConnection.commit()
        mySQLQuery_TEST_GET = """SELECT TestData FROM """ + TableName
        mySQLCursor.execute(mySQLQuery_TEST_GET)
        mySQLConnection.commit()
        mySQLQuery_TEST_DELETE = """DELETE FROM `""" + TableName + """` WHERE `TestData` = Transceiver Tested Syccessfully."""
        mySQLCursor.execute(mySQLQuery_TEST_DELETE)
        mySQLConnection.commit()
        mySQLCursor.close()
    except mysql.connector.Error as error:
        print("System failed to retreive data. Please try again.")
        return
    finally:
        if (mySQLConnection.is_connected()):
            mySQLConnection.close()

testCommit()

#API Setup
@API_app.route('/uplink', methods=['POST'])

#API GET Data Sourcing
def dataSourcing_GET_INITIAL():
    mySQLQuery_API_INIT_GET = """SELECT * FROM """ + TableName
    mySQLCursor.execute(mySQLQuery_API_INIT_GET)
    fetchInitialData = mySQLConnection.fetchmany(size=1)
    fetchInitialData()
def dataSourcing_GET_REPEAT():
    mySQLQuery_API_REPEAT_GET = """SELECT * FROM """ + TableName
    mySQLCursor.execute(mySQLQuery_API_REPEAT_GET)
    fetchData = mySQLConnection.fetchmany(size=1)
    fetchData()
def dataSourcing_COMPRESS():
    zlib.compress(resultSet, -1)
def dataSourcing_ENCRYPT():
    base64.b64encode(resultSet)
def dataSourcing_CONVERT():
    flask.jsonify(resultSet)
dataSourcing_GET_INITIAL()
dataSourcing_CONVERT() #Encryption and compression may cause issues with this method. A direct upload to Flask may be easier.
dataSourcing_COMPRESS() #A decompression script may be needed
dataSourcing_ENCRYPT()
API_app.run()
dataSourcing_GET_REPEAT()
GET_Memory_Buffer = getsizeof(resultSet)
if (fetchData != fetchInitialData):
    fetchInitialData = 0
    fetchInitialData = fetchData
    dataSourcing_GET_REPEAT()
    dataSourcing_CONVERT()
    dataSourcing_COMPRESS()
    dataSourcing_ENCRYPT()
    API_app.run(port=5001)
elif GET_Memory_Buffer > 2147483648:
    print("This file is too large to upload in one part.")
    oversizeBufferResponse = input("Would you like a multipart upload (Y/n)")
    while oversizeBufferResponse == Y:
        print("Starting Multipart Upload...")
        sliceMultiPart = slice(1, 2147483649, 2147483648)
        mySQLCursor.execute("""SELECT * FROM""" + TableName)
        mySQLConnection.fetchmany(size=1)
    while oversizeBufferResponse == n:
        break
    while oversizeBufferResponse != 'Y' || 'n':
        print("An incorrect value was given. Please try again and close this program.")
else:
    time.sleep(5)
    dataSourcing_GET()

#API Entry Request Sourcing
def dataSourcing_INITIAL_INSERT():
    """INSERT INTO """ + TableName + """VALUES (initialDataStream)"""
def socketListener_INITIAL():
    socketConnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        socketConnection.bind((HostName, 5001))
    except socket.error as msg:
        print("API Communication Failed. Please try again.")
        return
    print("Entry request sub-API connected.")
    socketConnection.listen(6)
    conn, addr = socketConnection.accept()
    initialDataStream = conn.recv(1024)
def sysDump():
    json.dumps(initialDataStream)
    mySQLCursor.execute(dataSourcing_INITIAL_INSERT)
    mySQLConnection.commit()
socketListener_INITIAL()
sysDump()
def repeatDataStream(): conn.recv(1024)
if repeatDataStream != initialDataStream :
    initialDataStream = 0
    initialDataStream = repeatDataStream
    time.sleep(5)
    repeatDataStream()
else:
    time.sleep(5)
    repeatDataStream()
