# class
# class Person:
    # class attributes
    # address =   "No information"
    # constructor (yapıcı metod)
    # def __init__(self, name, year):
    #     self.name = name
    #     self.birthyear = year

        # print("İnit metodu çalıştı")
    # object attributes
    # instance methods
    # def intro(self):
    #     print(f"Say Hello I'm {self.name}")
    # def calculateAge(self):
    #     return 2023 - self.birthyear
# object(instance)
# p1 = Person(name = "Emre", year = 2001)
# p2 = Person(name = "Elif", year = 1999)
# print(f"Merhaba ismim {p1.name} Yaşım {p1.calculateAge()}")
# Updating
# p1.name = "Rümeysa"
# p2.name = "Nilay"
# Accessing object attributes
# print(f"İsim : {p1.name}, Doğumyılı : {p1.birthyear} Adres : {p1.address}")
# print(f"İsim : {p2.name}, Doğumyılı : {p2.birthyear} Adres : {p2.address}")

#print(p1,p2)
# print(type (p1),type(p2))


# class Circle:
#     # Class object attribute
#     pi = 3.14
#     def __init__(self, yaricap = 1):
#         self.yaricap = yaricap

#     # Methods 
#     def cevrehesapla(self):
#         return 2 * self.pi * self.yaricap
    
#     def alanhesapla(self):
#         return self.pi * (self.yaricap**2)
    
# c1 = Circle() # Yaricap belirtilmedigi icin 1'e eşitlenecek
# c2 = Circle(5)
# c3 = Circle(6)
# c4 = Circle(2)
# c5 = Circle(7)

# print(f"Yarıçapı 5 olan dairenin\nçevresi: {c2.cevrehesapla()}\n alanı: {c2.alanhesapla()}")
# print(f"Yarıçapı 1 olan dairenin\nçevresi: {c1.cevrehesapla()}\n alanı: {c1.alanhesapla()}")
# print(f"Yarıçapı 6 olan dairenin\nçevresi: {c3.cevrehesapla()}\n alanı: {c3.alanhesapla()}")
# print(f"Yarıçapı 7 olan dairenin\nçevresi: {c5.cevrehesapla()}\n alanı: {c5.alanhesapla()}")
