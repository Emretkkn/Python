import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "python"
)
cursor = mydb.cursor()
# cursor.execute("CREATE DATABASE python")
# cursor.execute("DROP DATABASE python")
# cursor.execute("SHOW DATABASES")
# for x in cursor:
#     print(x)
# cursor.execute("SELECT * FROM model")
# for i in cursor:
#     print(i)
cursor.execute("CREATE TABLE arabalar (id INT(11), name VARCHAR(255), year DATE)")