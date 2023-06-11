import mysql.connector
def ordering():
    connection = mysql.connector.connect(host="localhost",user="root",password="",database="python")
    mycursor = connection.cursor()
    mycursor.execute("SELECT * FROM product ORDER BY product.id DESC")
    try:
        result = mycursor.fetchall()
        for i in result:
            print(f"Ürün adı: {i[0]}, fiyatı: {i[1]}, açıklaması: {i[2]}")
    except mysql.connector.Error as err:
        print("Sorgu Hatası",err)
    finally:
        connection.close()
        print("Veritabanı bağlantısı kapandı.")

ordering()