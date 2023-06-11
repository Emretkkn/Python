import mysql.connector
def aggregate():
    connection = mysql.connector.connect(host="localhost",user="root",password="",database="python")
    cursor = connection.cursor()
    sql = "SELECT MAX(product.price) FROM product"
    sql = "SELECT COUNT(*) FROM product"
    sql = "SELECT AVG(product.price) FROM product"
    sql = "SELECT product.name, product.price FROM product WHERE product.price=(SELECT MAX(product.price) FROM product)"
    
    cursor.execute(sql)
    # result = cursor.fetchone()
    # print(result[0])
    result = cursor.fetchall()
    for i in result:
        print(f"Name: {i[0]} Price: {i[1]}")
aggregate()