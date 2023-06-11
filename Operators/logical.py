# Soru 1
# x = float(input("Lütfen bir sayı giriniz : "))
# if x > 0 and x < 100:
#     print("Girdiğiniz sayı 0 ile 100 arasındadır.")
# else:
#     print("Girdiğiniz sayı 0 ile 100 arasında değildir.") 
# Soru 2
# x = float(input("Lütfen bir sayı giriniz : "))
# if (x > 0) and (x % 2 == 0):
#     print("Girilen sayı bir pozitif çift sayıdır.")
# else:
#     print("Girilen sayı pozitif çift sayı değildir.")
# Soru 3
# eposta = "emretekin_35@outlook.com"
# sifre = "1234abcd"
# email = input("E postanızı yazınız : ")
# email = email.strip()
# password = input("Şifrenizi yazınız : ")

# if email == eposta and password == sifre:
#     print("Sisteme başarıyla giriş yaptınız.")
# else:
#     print("Lütfen e-postanızı veya şifrenizi kontrol ediniz.")
# Soru 4
# sayi1 = float(input("Lütfen 1. sayıyı giriniz."))
# sayi2 = float(input("Lütfen 2. sayıyı giriniz."))
# sayi3 = float(input("Lütfen 3. sayıyı giriniz."))

# if (sayi1 > sayi2) and (sayi1 > sayi3):
#     print(f"En büyük sayı {sayi1}")
# elif (sayi2 > sayi1) and (sayi2 > sayi3):
#     print(f"En büyük sayı {sayi2}")
# elif (sayi3 > sayi2) and (sayi3 > sayi1):
#     print(f"En büyük sayı {sayi3}")
# Soru 5
# vize1 = int(input("1. Vize notunu giriniz : "))
# vize2 = int(input("2. Vize notunu giriniz : "))
# final = int(input("Final notunu giriniz : "))
# ortalama = (((vize1 + vize2)/2) * 0.6) + (final * 0.4)
# gecme_notu = 50
# can = 70
# if ortalama > gecme_notu and final >= gecme_notu:
#     print(f"Ders başarılı ortalama : {ortalama}")
# elif ortalama > gecme_notu and final < gecme_notu:
#     print(f"Finalde 50'den düşük bir not aldığınız için kaldınız. ortalama {ortalama}")
# elif final > can:
#     print(f"Finalde 70'den yüksek bir not aldığınız için dersten başarıyla geçtiniz ortalama {ortalama}")
# else:
#     print(f"Dersten kaldınız ortalama {ortalama}")
# Soru 6
# isim = input("Adınız ve soyadınız : ")
# kilo = float(input("Kilonuzu yazınız : "))
# boy = float(input("Boyunuzu yazınız : "))
# vki = kilo / ((boy / 100)**2)
# if vki > 0 and vki < 18.5:
#     print("Zayıf")
# elif vki >= 18.5 and vki < 25:
#     print("Normal")
# elif vki >= 25 and vki < 30:
#     print("Fazla Kilolu")
# elif vki >= 30:
#     print("Obez")
# else:
#     print("Tanımlamayan kitle endeksi")

