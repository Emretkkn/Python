import mysql.connector
connection = mysql.connector.connect(host="localhost",user="root",password="",database="python")
class Product:
    connection = connection
    mycursor = connection.cursor()
    def __init__(self,name,price,imageurl,description):
        self.name = name
        self.price=price
        self.imageurl=imageurl
        self.description=description
    @staticmethod
    def saveProducts(Plist):
        sql = "INSERT INTO product(name,price,imageurl,description) VALUES(%s,%s,%s,%s)"
        values = Plist
        Product.mycursor.executemany(sql,values)
        try:
            Product.connection.commit()
            print(f"{Product.mycursor.rowcount} tane kayıt eklendi.")
            print(f"Son Eklenen ürünün id numarası {Product.mycursor.lastrowid}")
        except mysql.connector.Error as err:
            print("Kayıtlar Eklenemedi.",err)
        finally:
            Product.connection.close()     

    def getProducts():
        sql = "SELECT product.name, product.price FROM product"
        Product.mycursor.execute(sql)
        product = Product.mycursor.fetchone()
        print(f"Ürün adı :{product[0]} Ürün fiyatı: {product[1]}")
        # products = Product.mycursor.fetchall()
        # for product in products:
        #     print(f"Ürün adı :{product[0]} Ürün fiyatı: {product[1]}")
        Product.connection.close()
    @staticmethod
    def getProductById(id):
        sql = "SELECT * FROM product WHERE product.id=%s"
        params = (id,)
        Product.mycursor.execute(sql,params)
        result = Product.mycursor.fetchone()
        print(f"name: {result[0]}, price: {result[1]} imageurl: {result[2]}")
    @staticmethod
    def updateProductprice(name,price):
        sql = "UPDATE product SET product.price = %s WHERE product.name = %s"
        values = (price,name)
        Product.mycursor.execute(sql,values)
        try:
            Product.connection.commit()
            print(f"{name} isimli ürün fiyatı {price} güncellendi.")
        except mysql.connector.Error as err:
            price("Kayıt güncellenemedi",err)
        finally:
            Product.connection.close()
    @staticmethod
    def deleteProduct(name):
        sql = "DELETE FROM product WHERE product.name = %s"
        value = (name,)
        Product.mycursor.execute(sql,value)
        try:
            Product.connection.commit()
            print(f"{name} adlı ürün ürün silindi.")
        except mysql.connector.Error as err:
            print("Kayıt silinemedi",err)
        finally:
            Product.connection.close()
            print("Veritabanı bağlantısı kapandı.")

ProductList = [
    ("Adidas",300,"adidas.jpeg","Ayakkabı"),
    ("Nike",500,"nike.jpeg","Ayakkabı"),
    ("Puma",600,"Puma.jpeg","Ayakkabı"),
    ("Lotto",800,"Lotto.jpeg","Ayakkabı"),
    ("Gucci",1200,"Gucci.jpeg","Ayakkabı")
]

# Product.saveProducts(ProductList)
# Product.getProducts()
# Product.getProductById(2)
# Product.updateProductprice("Nike",1700)
Product.deleteProduct("Gucci")