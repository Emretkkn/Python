# Soru 1
students = {}
# students[st_number] = {
#     "Name" : st_name,
#     "Surname" : st_surname,
#     "Phone" : st_phone
# }
# 2. Yol
st_number = int(input("Lütfen öğrenci numarası giriniz : "))
st_name = str(input("Lütfen öğrenci adını yazınız : "))
st_surname = str(input("Lütfen öğrenci soyadını yazınız : "))
st_phone = int(input("Lütfen öğrencinin telefon numarasını yazınız : "))

students.update({
    st_number : {
        "Name" : st_name,
        "Surname" : st_surname,
        "Phone" : st_phone
    }
})
# Soru 2
print("*"*50)
ogr_no = int(input("Lütfen Aramak İstediğiniz Öğrenci Numarası Giriniz : "))
ogrencibul = students[ogr_no]
print(f'{ogr_no} numaralı öğrencinin:/n Adı : {students["Name"]}')
