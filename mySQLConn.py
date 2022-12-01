import mysql.connector
from LiteratureWork import Work
def connect():
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        database = "BTLPython"
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM lworks")

    result = cursor.fetchall()
    list = []
    for x in result:
        list.append(Work(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8]))
    return list

