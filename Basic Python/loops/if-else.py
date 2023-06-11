# Soru 1
# isim = input("İsminiz: ")
# yas = int(input("Yaşınız: "))
# egitim_durum = input("Eğitim durumunuz: ")

# if yas >= 18:
#     if egitim_durum == "Lisans":
#         print("Ehliyet alabilirsiniz")
#     elif egitim_durum == "Lise":
#         print("Ehliyet alabilirsiniz.")
#     else:
#         print("Ehliyet alabilmek için Lise ya da Lisans mezunu olmanız gerekir.")
# else:
#     print("Ehliyet alabilmek için yaşınızın 18'den büyük olması gerekir.")

# Soru 2
# yazili1 = int(input("1. Yazılı notunu giriniz : "))
# yazili2 = int(input("2. Yazılı notunu giriniz : "))
# sozlu = int(input("Sözlü notunu giriniz : "))

# ortalama = (((yazili1 + yazili2)/2) * 0.8 + (sozlu * 0.2))
# if ortalama < 25:
#     print(f"Ortalamanız {ortalama} Not : 0")
# elif ortalama >= 25 and ortalama < 45:
#     print(f"Ortalamanız {ortalama} Not : 1")
# elif ortalama >= 45 and ortalama < 55:
#     print(f"Ortalamanız {ortalama} Not : 2")
# elif ortalama >= 55 and ortalama < 70:
#     print(f"Ortalamanız {ortalama} Not : 3")
# elif ortalama >= 70 and ortalama < 85:
#     print(f"Ortalamanız {ortalama} Not : 4")
# else:
#     print(f"Ortalamanız {ortalama} Not : 5")

# Soru 3
# import datetime
# tarih = input("Lütfen aracınızın trafiğe çıkış tarihini giriniz : ")
# bolunmus_tarih = tarih.split("/")
# bolunmus_tarih = tarih.split("-")
# yil = bolunmus_tarih[0]
# ay = bolunmus_tarih[1]
# gun = bolunmus_tarih[2]
# cikistarihi = datetime.datetime(int(yil),int(ay),int(gun))
# simdi = datetime.datetime.now()
# fark = simdi - cikistarihi
# gun_farki = fark.days
# print(gun_farki)
# if gun_farki < 365:
#     print(f"1. Bakım yılı ve geçen gün {gun_farki}")
# elif gun_farki >= 365 and gun_farki < 365*2:
#     print(f"2. Bakım yılı ve geçen gün {gun_farki}")
# elif gun_farki >= 365*2 and gun_farki < 365*3:
#     print(f"3. Bakım yılı ve geçen gün {gun_farki}")
# else:
#     print(f"Tanımlanamayan bakım yılı ve geçen gün {gun_farki}") 

