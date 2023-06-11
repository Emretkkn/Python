import random
print("Her soru 20 puandır")
rastgele1 = random.randint(1,100)
hak1 = int(input("Lütfen kullanacağınız hak sayısını giriniz : " ))
# Soru 1
for i in range(hak1):
    tahmin = int(input("Lütfen tahmin yapınız : "))
    if tahmin == rastgele1:
        denemesayi1 = i + 1
        puan1 = int(20/denemesayi1)
        print(f"Sayıyı {denemesayi1} denemede buldunuz ve puanınız {puan1}")
        print("2.Soru")
        break
    elif tahmin < rastgele1:
        print("Yukarı")
    elif tahmin > rastgele1:
        print("Aşağı")
if tahmin != rastgele1:
    print(f"Sayıyı bulamadınız ve 1. sorunun cevabı {rastgele1}")
    print("2.Soru")
    puan1 = 0


rastgele2 = random.randint(1,100)
hak2 = int(input("Lütfen kullanacağınız hak sayısını giriniz : " ))
# Soru 2
for i in range(hak2):
    tahmin2 = int(input("Lütfen tahmin yapınız : "))
    if tahmin2 == rastgele2:
        denemesayi2 = i + 1
        puan2 = int(20/denemesayi2)
        toplam_puan = puan1 + puan2
        print(f"Sayıyı {denemesayi2} denemede buldunuz ve puanınız {puan2}")
        break
    elif tahmin2 < rastgele2:
        print("Yukarı")
    elif tahmin2 > rastgele2:
        print("Aşağı")

if tahmin2 != rastgele2:
    puan2 = 0
    toplam_puan = puan1 + puan2
    print(f"Sayıyı bulamadınız ve 2. sorunun cevabı {rastgele2}")


rastgele3 = random.randint(1,100)
hak3 = int(input("Lütfen kullanacağınız hak sayısını giriniz : " ))
# Soru 2
for i in range(hak3):
    tahmin3 = int(input("Lütfen tahmin yapınız : "))
    if tahmin3 == rastgele3:
        denemesayi3 = i + 1
        puan3 = int(20/denemesayi3)
        toplam_puan = puan1 + puan2 + puan3
        print(f"Sayıyı {denemesayi3} denemede buldunuz ve puanınız {puan3}")
        break
    elif tahmin3 < rastgele3:
        print("Yukarı")
    elif tahmin3 > rastgele3:
        print("Aşağı")

if tahmin3 != rastgele3:
    puan3 = 0
    toplam_puan = puan1 + puan2 + puan3
    print(f"Sayıyı bulamadınız ve 3. sorunun cevabı {rastgele3}")



rastgele4 = random.randint(1,100)
hak4 = int(input("Lütfen kullanacağınız hak sayısını giriniz : " ))
# Soru 2
for i in range(hak4):
    tahmin4 = int(input("Lütfen tahmin yapınız : "))
    if tahmin4 == rastgele4:
        denemesayi4 = i + 1
        puan4 = int(20/denemesayi4)
        toplam_puan = puan1 + puan2 + puan3 + puan4
        print(f"Sayıyı {denemesayi4} denemede buldunuz ve puanınız {puan4}")
        break
    elif tahmin4 < rastgele4:
        print("Yukarı")
    elif tahmin4 > rastgele4:
        print("Aşağı")

if tahmin4 != rastgele4:
    puan4 = 0
    toplam_puan = puan1 + puan2 + puan3 + puan4
    print(f"Sayıyı bulamadınız ve 4. sorunun cevabı {rastgele4}")



rastgele5 = random.randint(1,100)
hak5 = int(input("Lütfen kullanacağınız hak sayısını giriniz : " ))
# Soru 2
for i in range(hak5):
    tahmin5 = int(input("Lütfen tahmin yapınız : "))
    if tahmin5 == rastgele5:
        denemesayi5 = i + 1
        puan5 = int(20/denemesayi5)
        toplam_puan = puan1 + puan2 + puan3 + puan4 + puan5
        print(f"Sayıyı {denemesayi5} denemede buldunuz ve\nToplam puanınız {toplam_puan}")
        break
    elif tahmin5 < rastgele5:
        print("Yukarı")
    elif tahmin5 > rastgele5:
        print("Aşağı")

if tahmin5 != rastgele5:
    puan5 = 0
    toplam_puan = puan1 + puan2 + puan3 + puan4 + puan5
    print(f"Sayıyı bulamadınız ve 5. sorunun cevabı {rastgele5}\nToplam puanınız {toplam_puan}")


