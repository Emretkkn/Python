# Bankamatik Uygulaması
emreHesap = {
    "ad": "Emre Tekin",
    "il" : "İzmir",
    "sifre": 220799,
    "hesapNo" : "2148148812",
    "bakiye" : 4500,
    "ekHesap" : 6000
}

elifHesap = {
    "ad": "Elif Tekin",
    "il" : "İzmir",
    "sifre" : 12345,
    "hesapNo" : "4233252812",
    "bakiye" : 14500,
    "ekHesap" : 66000
}

zehraHesap = {
    "ad" : "Zehra Nur Akçay",
    "il" : "Kocaeli",
    "sifre" : 1234,
    "hesapNo" : "1248712471247",
    "bakiye" : 50000,
    "ekHesap" : 10000
}

rumeysaHesap = {
    "ad" : "Rümeysa Koyun",
    "il" : "Balıkesir",
    "sifre" : 3456,
    "hesapNo" : "12784712848",
    "bakiye" : 1500,
    "ekHesap": 20000
}   




def paraCek(hesap, miktar):
    print(f'Merhaba {hesap["ad"]}')
    if hesap["bakiye"] >= miktar:
        hesap["bakiye"] = hesap["bakiye"] - miktar
        print(f"Paranızı Alabilirsiniz\n{hesap['hesapNo']}'lu hesabınızda kalan tutar {hesap['bakiye']}")
    else:
        if hesap["ekHesap"] >= miktar:
            sor = input(f"Hesabınızdaki para miktarı: {hesap['bakiye']} ve ek hesap bakiyeniz {hesap['ekHesap']} kullanmak istermisiniz (Evet/Hayır) ? ")
            sor.strip()
            if sor == "Evet":
                hesap["ekHesap"] = hesap["ekHesap"] - miktar
                print(f"Paranızı Alabilirsiniz.\nHesabınızdaki para miktarı: {hesap['bakiye']} ve ek hesap bakiyeniz {hesap['ekHesap']}")
            else:
                print("Kartınızı Alabilirsiniz.")
        else:
            print(f"İki hesabınızda da yeterli miktar yok kartınızı alabilirsiniz.\nHesap bakiyeniz: {hesap['bakiye']}\n Ek hesap bakiyeniz: {hesap['ekHesap']}")
    
isim = input("Lütfen isminizi soyisminizi arada bir boşluk olacak şekilde giriniz : ")
isim.strip()
sifre = int(input("Lütfen Şifrenizi giriniz : "))

if isim == "Emre Tekin" and sifre == 220799:
    hesap = emreHesap
    miktar = int(input("Lütfen çekmek istediğiniz tutarı giriniz : "))
    paraCek(hesap,miktar)
elif isim == "Elif Tekin" and sifre == 12345:
    hesap = elifHesap
    miktar = int(input("Lütfen çekmek istediğiniz tutarı giriniz : "))
    paraCek(hesap,miktar)
elif isim == "Zehra Nur Akçay" and sifre == 1234:
    hesap = zehraHesap
    miktar = int(input("Lütfen çekmek istediğiniz tutarı giriniz : "))
    paraCek(hesap,miktar)
elif isim == "Rümeysa Koyun" and sifre == 3456:
    hesap = rumeysaHesap
    miktar = int(input("Lütfen Çekmek İstediğiniz Tutarı Giriniz : "))
    paraCek(hesap,miktar)
else:
    print("İsminizi veya şifrenizi lütfen kontrol edin.")
