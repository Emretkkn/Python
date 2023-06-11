def ortalama_hesapla():
    isim = input("Lütfen ortalaması hesaplanacak öğrencinin adını giriniz: ")
    isim.strip()
    soyisim = input("Lütfen ortalaması hesaplanacak öğrencinin soyisimini giriniz: ")
    soyisim.strip()
    with open("notlar.txt","r",encoding="utf-8") as file:
        for satir in file:
            toplam = 0
            liste = satir.split(": ")
            isimsoyisim = liste[0]
            aa = isimsoyisim.split(" ")
            name = aa[0]
            surname = aa[1]
            notlar = liste[1]
            nottlar = notlar.split(",")
            for i in nottlar:
                try:
                    i = int(i)
                except:
                    continue
                toplam += i
            ortalama = (toplam/len(nottlar))
            if isim == name and soyisim == surname:
                print(ortalama)

            

def not_gir():
    ad = input("Lütfen Adınızı giriniz: ") 
    ad.strip()
    soyad = input("Lütfen Soyadınızı giriniz: ") 
    soyad.strip()
    notliste = []
    try:
        notadet = int(input("Lütfen girmek istediğiniz not adedini yaziniz: "))
    except Exception as ex:
        print("Lütfen girdiğiniz değerleri kontrol ediniz", ex)
    for i in range(notadet):
        try:
            nott = int(input("Lütfen öğrencinin aldığı notu yazınız: "))
        except Exception as ex:
            print("Lütfen sayısal bir değer giriniz", ex)
        notliste.append(nott)
    with open("notlar.txt","a",encoding="utf-8") as file:
        uzunluk = file.write(f"{ad} {soyad}: ")
        for i in notliste:
            file.write(f"{i},")
        file.write("\n")

def notlari_oku():
    import re
    isim = input("Lütfen notunu öğrenmek istediğiniz öğrencinin ismini yazınız: ")
    soyisim = input("Lütfen notunu öğrenmek istediğiniz öğrencinin ismini yazınız: ")
    isim.strip()
    soyisim.strip()
    with open("notlar.txt","r",encoding="utf-8") as file:
        for satir in file:
            boslist = satir.split(": ")
            isimsoyisim = boslist[0]
            names = isimsoyisim.split(" ")
            name = names[0]
            surname = names[1]
            if isim == name and soyisim == surname:
                print(satir, end="")


while True:
    islem = input("1-Notları Oku\n2-Not Gir\n3-Ortalama hesapla\n4-Çıkış\nLütfen yapmak istediğiniz işlemin numarasını yazınız: ")
    if islem == "1":
        notlari_oku()
    elif islem == "2":
        not_gir()
    elif islem == "3":
        ortalama_hesapla() 
    else:
        break