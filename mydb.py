import mysql.connector

dataBase= mysql.connector.connect(
    host='localhost',
    user='sleepingfox',
    passwd='1234'
)

#prepare a cursor

cursorObject= dataBase.cursor()

#create a database

cursorObject.execute("CREATE DATABASE lufi")

print("All Done!")