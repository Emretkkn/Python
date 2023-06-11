from datetime import datetime,timedelta
import os
result = dir(os)
result = os.name # İşletim sistemi ismini değer alır.
result = os.getcwd() # Dosyanın hangi klasör içinde bulunduğunu gösterir.

# os.chdir("C://Users//") # Changeing directory
# os.chdir("..//..") # iki kere üst klasöre geçiş işlemi yapar

# os.makedirs("newdirectory/yeniklasor") # Birden fazla klasör oluşturmak için kullanılır.
result = os.getcwd()
result = os.listdir() # Directory'deki dosyaları listeler.
result = os.listdir("C://Users")
# os.mkdir("Yeni_klasor")
# os.rename("Yeni_klasor","Servet_sayar")
# os.mkdir("Yeni_klasor") # Klasör oluşturma
# os.rmdir("Servet_sayar") # Alt dizini olmayan klasörleri silmek için kullanılır.
# os.makedirs("Yeni_klasor/emret/imamhatiplerkapatilsin")
# os.removedirs("Yeni_klasor/emret/imamhatiplerkapatilsin") # Alt dizini olan klasörleri silmek için kullanılır.
# print(result)
# for dosya in os.listdir():
#     if dosya.endswith(".py"):
#         print(dosya)

durum = os.stat("bankamatik.py") # Dosya durumu hakkında bilgi verir.
sonuc = durum.st_size/1024 # Byte to kilobyte
tarih = durum.st_ctime # Dosya oluşturulma zamanı
tarih = durum.st_atime # Son erişilme tarihi
tarih = durum.st_mtime # Son düzenlenme tarihi
# cevir = datetime.fromtimestamp(tarih) # Timestamp to Tarih
                    # OR
cevir = datetime.fromtimestamp(durum.st_atime) 
# print(cevir)

# os.system("notepad.exe") # Dosya açmak için

# PATH dosya uzantisiyla ilgili işlemler için kullanılır.
result = os.path.abspath("_os.py")
dosyayolu = os.path.dirname("C:/wamp64/python/_os.py") # Tam dosya yolu verir.
result = os.path.dirname(os.path.abspath("bankamatik.py")) # Tek satırda uygulanış şekli        
# print(result)

# varmi = os.path.exists("errors.py") # Dosya sorgulamak için 
# varmi2 = os.path.exists("C:/wamp64/www/python") # Dizin sorgulamak için
# if varmi2 == True:
#     print("Dosya belirtilen konumda var")
# else:
#     print("Dosya belirtilen konumda yok.")

# Belirtilen yolun klasör olup olmadığını sorgulamak için
# klasormu = os.path.isdir("C:/wamp64")
# klasormu = os.path.isdir("C:/wamp64/python/dictionary.py")
# if klasormu == True:
#     print("Klasör")
# else:
#     print("Dosya")

# Belirtilen yolun dosya olup olmadığını sorgulamak için
# dosyami = os.path.isfile("C:/wamp64/python/bankamatik.py")
# if dosyami == True:
#     print("Dosya")
# else:
#     print("Klasör")

# Dosya yollarını birleştirmek için
birlestir = os.path.join("C:/","wamp64/","www/","python/")
# print(birlestir)
# Dosya yollarını bölmek için
bolme = os.path.split("C:/wamp64") # Tuple listesi oluşturur.
# print(bolme)
# Dosya adını "dosya adı" ve "uzantısı" şeklinde bolmek icin
isimbol = os.path.splitext("bankamatik.py")
print(isimbol)