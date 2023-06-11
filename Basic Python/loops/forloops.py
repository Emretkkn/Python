sifir = 0
sayilar = [1,3,5,7,9,12,19,21]
# Soru 1
# for i in sayilar:
#     if i % 3 == 0:
#         print(i, end=" ")
# Soru 2
# for i in sayilar:
#     a += i
# print(a)
# Soru 3
# for i in sayilar:
#     if i % 2 != 0:
#         print(i**2, end=" ")
# Soru 4
# sehirler = ["Kocaeli","İstanbul","Ankara","İzmir","Rize"]
# for i in sehirler:
#     a = len(i)
#     if a <= 5:
#         print(i, end=" ")
# Soru 5
urunler = [
    {"name":"samsung S6", "price":"3000"},
    {"name":"samsung S7", "price":"4000"},
    {"name":"samsung S8", "price":"5000"},
    {"name":"samsung S9", "price":"6000"},
    {"name":"samsung S10", "price":"7000"}
]
# for i in urunler:
#     for b,c in i.items():
#         if b == "price":
#             sifir = sifir + int(c)
# print(sifir)
# Soru 6
for i in urunler:
    if (int(i["price"]) <= 5000):
        print(i["name"])


            

            


            


        

