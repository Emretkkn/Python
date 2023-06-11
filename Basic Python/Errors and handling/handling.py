# Error handling -> Hata Yönetimi
# try:
#     x = int(input("1.sayıyı giriniz : "))
#     y = int(input("2.sayıyı giriniz : "))
#     print(x/y)
# except ZeroDivisionError:
#     print("Y için sıfır girilemez.")
# except ValueError:
#     print("X ve Y için sayısal ifadeler girmelisiniz.")
# except (ZeroDivisionError,ValueError) as a:
#     print("Yanlış Değer girdiniz.")
#     print(a)
while True:
    try:
        x = int(input("1.sayıyı giriniz : "))
        y = int(input("2.sayıyı giriniz : "))
        print(x/y)
    except Exception as e: # Objeye ulaşılamadığı için hata tanımlaması yapılamaz.
        print("Hatalı değer girdiniz.",e)
    else:
        break
    finally: # Try except hangisi çalışırsa çalışsın her zaman çalışır
        print("Try except is ended.")