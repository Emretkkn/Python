import mysql.connector
def insertProduct(name,price,imageUrl,description):
    connection = mysql.connector.connect(host="localhost",user="root",password="",database="python")
    cursor = connection.cursor()
    sql = "INSERT INTO product(name,price,imageurl,description) VALUES(%s,%s,%s,%s)"
    # values = ("Nike Air Force",2900,"nike.jpeg","This shoes was made in Croatia")
    values = (name,price,imageUrl,description)
    cursor.execute(sql,values)
    
    try:
        connection.commit()
        print("Kayıt Başarıyla Eklendi.")
        print(f"{cursor.rowcount} tane kayıt eklendi")
        print(f"Son eklenen ürünün id'si: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("Hata: ",err)
    finally:
        connection.close()
        print("Database bağlantısı kapandı.")

def insertProducts(list):
    connection = mysql.connector.connect(host="localhost",user="root",password="",database="python")
    cursor = connection.cursor()
    sql = "INSERT INTO product(name,price,imageurl,description) VALUES(%s,%s,%s,%s)"
    values = list
    cursor.executemany(sql,values)
    try:
        connection.commit()
        print(f"Kayıtlar Başarıyla eklendi.\nSon eklenen ürünün id numarası {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("BağlantI Hatası",err)
    finally:
        connection.close()
liste = []
while True:
    choose = int(input("1-Tek Kayıt Ekle\n2-Çoklu Kayıt Ekle\n3-Çıkış\nLütfen yapmak istediğiniz işlemin numarasını tuşlayınız: "))
    if choose == 1:
        name = input("Ürün ismini yazınız: ").strip()
        price = int(input("Ürünün fiyatını yazınız: "))
        imageUrl = input("Ürün fotoğraf adını yazınız: ")
        description = input("Ürün hakkında açıklama yazınız: ")
        try:
            insertProduct(name=name,price=price,imageUrl=imageUrl,description=description)
        except mysql.connector.Error as err:
            print("Kayıt Eklenemedi: ",err)
    elif choose == 2:
        kayit_sayi = int(input("Kaç adet kayıt eklemek istiyor sunuz ?: "))
        for i in range(kayit_sayi):
            name = input("Ürün ismini yazınız: ").strip()
            price = int(input("Ürünün fiyatını yazınız: "))
            imageUrl = input("Ürün fotoğraf adını yazınız: ")
            description = input("Ürün hakkında açıklama yazınız: ")
            liste.append((name,price,imageUrl,description))
        try:
            insertProducts(liste)
        except mysql.connector.Error as err:
            print("Kayıt Eklenemedi",err)
    elif choose == 3:
        break
    else:
        print("Lütfen geçerli bir değer giriniz.")