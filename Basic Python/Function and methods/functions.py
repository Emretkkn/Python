def fonksiyon(name = "Ali"):
    return "Hello " + name
msg = fonksiyon("Emre")
# print(msg)

def toplam(x,y):  # Fonksiyon Örnekleri
    return x + y
sonuc = toplam(5,6)
# print(sonuc)

def yashesapla(x):
    return 2023 - x
ageEmre = yashesapla(2001)
ageTugba = yashesapla(2000)
ageElif = yashesapla(1997)
ageNermin = yashesapla(1977)

# print(ageEmre,ageElif,ageTugba,ageNermin)

def emekliligekacyilkaldi(dogumYili,isim):
    '''
    DOCSTRING: Doğum yiliniza göre emekliliğe kaç yil kaldı
    INPUT : Doğum yili, İsim
    OUTPUT : Hesaplanan yil bilgisi

    '''
    yas = yashesapla(dogumYili)
    emeklilik = 65
    kacyilkaldi = emeklilik - yas
    if kacyilkaldi > 0:
        print(f"Emekliliğinize {kacyilkaldi} yıl kaldı, Sayın {isim}")
    else:
        print(f"Zaten emeklisiniz sayın {isim}")
emekliligekacyilkaldi(1954,"Emre")
print(help(emekliligekacyilkaldi))