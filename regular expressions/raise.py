# x = int(input("Lütfen bir değer giriniz : "))
# if x < 5:
#     raise Exception("Lütfen 5'ten büyük değerler giriniz.")

# def check_password(psw):
#     import re
#     if len(psw) < 8:
#         raise Exception("Parola en az 8 karakterden oluşmalıdır.")
#     elif not re.search("[a-z]",psw):
#         raise Exception("Parola küçük harf içermelidir.")
#     elif not re.search("[A-Z]",psw):
#         raise Exception("Parola büyük harf içermelidir.")
#     elif not re.search("[0-9]",psw):
#         raise Exception("Parola rakam içermelidir.")
#     elif not re.search("[_@$]",psw):
#         raise Exception("Parola alpha numeric değerler içermelidir.")
#     elif re.search("\s",psw):
#         raise Exception("Parola boşluk karakteri içermemelidir.")        
    
# password = "12345678 "
# try:
#     check_password(password)
# except Exception as hata:
#     print(hata)
# else:
#     print("Geçerli Parola.")
# finally:
#     print("Validation was completed.")

class Person:
    def __init__(self,name,year):
        if len(name) > 10:
            raise Exception("İsim uzunluğu 10 karakteri geçmemelidir")
        else:
            self.name = name

p1 = Person("Emre",2001)
