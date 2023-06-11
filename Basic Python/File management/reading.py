# file = open("newfile.txt","a",encoding="utf-8")
# file.write("Emre Tekin\nElif Tekin\nTuğba Aktaş\nZehra Akçay")
# file.close()
# try:
#     file = open("newfile2.txt","r")
#     print(file)
# except FileNotFoundError:
#     print("Dosya Okunamadı")
# finally:
#     file.close()

# for döngüsü ile okuma yapılabilir.
# for i in file:
#     print(i, end="")
# file.close()

# read() fonksiyonu*****
# file = open("newfile.txt","r",encoding="utf-8")
# icerik = file.read(5)

# print(icerik)


# readline() fonksiyonu**********************
# file = open("newfile.txt","r",encoding="utf-8")
# print(file.readline(), end="") 
# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline(), end="")


# readlines() fonksiyonu ***************************
file = open("newfile.txt","r",encoding="utf-8")
array = file.readlines()
print(array[0],end="")
print(array[1],end="")
print(array[2],end="")