import pyodbc

def read(conn):
    print("Readind...")
    cursor = conn.cursor()
    cursor.execute("select * from dummy")
    for row in cursor:
        print(f'row = {row}')

conn = pyodbc.connect(
    "Driver = {ODBC Driver 17 for SQL Server};\
    Server=;\
    Database=;\
    Trusted_Connection=Yes;"
)

read(conn)


conn.close()

# print(pyodbc.drivers())