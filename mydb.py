import mysql.connector

# connect to mysql
dataBase = mysql.connector.connect(
    host='localhost',
    user='admin',
    passwd='admin'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create DB
cursorObject.execute("CREATE DATABASE elderco")

print("Database has been created!")
