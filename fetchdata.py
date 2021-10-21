import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user="root",
    password = "",
    database = "clothweb"

)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM cloth")

myresult = mycursor.fetchall()

for row in myresult:
    print(row)