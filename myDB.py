import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Benoseno89@@',
    )

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE crmDB")

print("Done")