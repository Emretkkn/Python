liste = ["1","2","5a","10b","abc","10","50"]
# Soru 1
# for i in liste:
#     try:
#         sonuc =int(i)
#         print(sonuc)
#     except ValueError:
#         continue

# Soru 2
# while True:
#     sayi = input("sayi : ")
#     if sayi == "q":
#         break
#     try:
#         result = float(sayi)
#         print("Girdiğiniz sayı",result)
#         break
#     except ValueError:
#         print("Geçersiz sayı")
#         continue

# Soru 3
# def check_pass(password):
#     turkce_karakterler = "şçİöğüı"
#     for i in password:
#         if i in turkce_karakterler:
#             raise TypeError("Lütfen Türkçe Karakter Kullanmayınız.")
#         else:
#             pass
#     print("Geçerli Parola")
        
# password = input("Şifre giriniz : ")
# try:
#     check_pass(password)
# except TypeError as err:
#     print(err)

def faktoriyel(x):
    x = int(x)
    if x < 0:
        raise ValueError("Negatif Değer")
    result = 1
    for i in range(1,x+1):
        result *= i
    return result

liste = [1,2,3,-8,"10a"]
for i in liste:
    try:
        y = faktoriyel(i)
    except ValueError as err:
        print(err)
        continue
    print(y)