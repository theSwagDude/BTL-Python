import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = ""
)

print(db)

cursor = db.cursor()
