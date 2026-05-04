import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="studentdb"
)

if conn.is_connected():
    print("Connected to MySQL Database")

cursor = conn.cursor()


cursor.execute("USE studentdb")


sql_multi = "DELETE FROM studentss"
values_multi =cursor.execute(sql_multi )



conn.commit()






cursor.close()

conn.close()



