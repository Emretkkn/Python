# def usalma(number):
#     def inner(power):
#         return number ** power
#     return inner
# four = usalma(4)
# five = usalma(5)
# print(four(3))
# print(five(2))

# def yetki_sorgula(page):
#     def inner(role):
#         if role == "Admin":
#             return "{0} rolü {1} sayfasına ulaşabilir".format(role,page)
#         else:
#             return "{0} rolü {1} sayfasına ulaşamaz.".format(role,page)
#     return inner

# kullanici1 = yetki_sorgula("Dashboard")
# print(kullanici1("Admin"))

# def islem(islem_adi):
#     def toplama(*args):
#         toplam = 0
#         for i in args:
#             toplam += i
#         return toplam
    
#     def carpma(*args):
#         carpim = 1
#         for i in args:
#             carpim *= i
#         return carpim
    
#     if islem_adi == "Toplama":
#         return toplama
#     elif islem_adi == "Çarpma":
#         return carpma
    
# toplama = islem("Toplama")
# carpma = islem("Çarpma")
# print(toplama(1,2,3,4,5,6))
# print(carpma(1,2,3,4,5,6))
