# file = open("newfile.txt","r",encoding="utf-8")
# content = file.read()
# print(content)
# file.close()

with open("newfile.txt","r",encoding="utf-8") as file: # with kod bloğunun sonuna gelindiğinde açılmış olan dosyayı otomatik kapatır.
    content = file.read(10)
    print(content)
    file.seek(25) # İçine girilen index'e cursoru yönlendirir. 
    print(file.tell()) # O anki cursor'un konumunu söyler. İşaretçinin
    content2 = file.read()
    print(content2)