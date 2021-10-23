import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user="root",
    password = "",
    database = "clothweb"

)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM cloth ORDER BY name ASC")

myresult = mycursor.fetchall()

for row in myresult:
    print(row)