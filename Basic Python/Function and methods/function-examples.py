# Soru 1
# kelime = input("Lütfen kelimeyi yazınız : ")
# kelime.strip()
# shownumber = int(input("Lütfen gösterme sayısını yazınız : "))
# def kelimegoster():
#     for i in range(shownumber):
#         print(f"{kelime}")

# kelimegoster()

# Soru 2
def listeyap(*param):
    liste = []
    for i in param:
        liste.append(i)
    return liste
result = listeyap(10,20,40,"SayHello", 6000)
# print(result)


# Soru 3
# sayi1 = int(input("1. Sayıyı Giriniz : "))
# sayi2 = int(input("2. Sayıyı Giriniz : "))
# if sayi1 < 0 or sayi2 < 0:
#      print("Lüfen pozitif değerler giriniz")

# def asalsayilaribul(sayi1,sayi2):
#     for x in range(sayi1,sayi2+1):
#         if x > 1:
#             for i in range(2,x):
#                 if (x % i == 0):
#                     break
#             else:
#                 print(x)
# asalsayilaribul(sayi1,sayi2)

# Soru 4
# sayi = int(input("Sayı gir: "))
# if sayi >= 1:
#     def tambolen(x):
#         liste = []
#         for i in range(1,x+1):
#             if x % i == float:
#                 break
#             else:
#                 liste.append(i)
#         print(liste)

#     tambolen(sayi)
# else:
#     print("Lütfen 0'dan büyük değerler giriniz.")

# Soru 5
# def tambolen(x):
#     bosliste = []
#     for i in range(1,x+1):
#         if (x % i == 0):
#             bosliste.append(i)
#     return bosliste

# print(tambolen(30))

