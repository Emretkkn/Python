# with open("newfile.txt","r+",encoding="utf-8") as file:
#     file.seek(10)
#     file.write("Sadi Tekin\n")

# with open("newfile.txt","r+",encoding="utf-8") as file:
#     print(file.read())

# ************** Sayfa sonunda güncelleme *********************

# with open("newfile.txt","a",encoding="utf-8") as file:
#     file.write("\nHanife Yanar")

#  ****************** Sayfa başında güncelleme ****************
# with open("newfile.txt","r+",encoding="utf-8") as file:
#     icerik = file.read()
#     icerik = "Zeynep Akçay\n" + icerik
#     file.seek(0)
#     file.write(icerik)
#     print(icerik)

# with open("newfile.txt","r+",encoding="utf-8") as file:
#     liste = file.readlines()
#     liste.insert(0,"\nİsmail Akçay\n")
#     # print(liste)
#     for i in liste:
#         file.write(i)

# with open("newfile.txt","r",encoding="utf-8") as file:
#     print(file.read())

# ****************** Sayfa ortasında güncelleme *********************
with open("newfile.txt","r+",encoding="utf-8") as file:
    liste = file.readlines()
    liste.insert(0,"Kemal Kılıçdaroğlu\n")
    file.seek(0)
    file.writelines(liste)

with open("newfile.txt","r",encoding="utf-8") as file:
    print(file.read())
