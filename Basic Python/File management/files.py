# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosya_adi,dosya_erişme_modu)
# dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.

# "w": (Write) Yazma modu. Dosyayı konumda oluşturur.
    # ** Dosyayı konumda oluşturur
    # *** Dosya içeriğini siler ve yeniden ekleme yapar.
# file = open("newfile.txt","w",encoding="utf-8")
# file = open("C:/users/emret/newfile.txt")
# file.write("Emre Tekin")
# file.close()
# "a": (Append) ekleme. Dosyayı konumda oluşturur.
# file = open("newfile.txt","a",encoding="utf-8")
# file.write("FENER AĞLAMA")
# file.close()
# "x": (Create) oluşturma Dosya zaten varsa hata verir.
file = open("newfile2.txt","x",encoding="utf-8")


# "r": (Read) okuma varsayılan. Dosya konumda yoksa hata verir.

# print(file)