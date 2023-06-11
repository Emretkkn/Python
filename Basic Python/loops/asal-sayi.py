sayi = int(input("Lütfen Asal Kontrolü Yapmak İstediğiniz Sayıyı Giriniz : "))
kontrol = True
while True:
    if sayi == 1:
        kontrol = False
    for i in range(2,sayi):
        if sayi % i == 0:
            kontrol = False
            break
    if kontrol:
        print(f"{sayi} sayısı asaldır.")
        break
    else:
        print(f"{sayi} sayısı asal değildir.")
        break
    