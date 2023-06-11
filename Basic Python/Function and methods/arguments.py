# def changeName(n): # Fonksiyon değeri değiştiremedi.
#     n = "Emre"
# name = "Ali"
# changeName(name)
# print(name)

# def change(n):
#     n[0] = "Balıkesir"

# sehirler = ["Ankara","  İzmir"]
# change(sehirler[:])
# print(sehirler)

# def add(*hepsi):  # * işareti o fonksiyonda istenildiği kadar parametre tanımlanabileceği anlamına gelir.
#     return sum((hepsi))


# print(add(10,25))
# print(add(10,25,45))
# print(add(10,25,45,50,60,70))

# def kullanici(**params): # ** ile fonksiyonun içine dictionary gireceği belirtilir.
#     print(type(params))
#     for key,value in params.items():
#         print("{} is {}".format(key,value))


# kullanici(name = "Emre", age = 22, city = "İzmir")
# kullanici(name = "Elif", age = 26, city = "İzmir", phone = "011038192")
# kullanici(name = "Tuğba", age = 21, city = "İzmir", email = "tugba@outlook.com")

# def myFunction(a,b,c,*args,**kwargs):
#     print(a)
#     print(b)
#     print(c)
#     print(args)
#     print(kwargs)

# myFunction(1,4,8,7,5,"Emre","Ali", key1 = "Value1", key2 = "Value2")