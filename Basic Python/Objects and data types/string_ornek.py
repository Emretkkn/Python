website = "https://www.google.com"
course = "Python Kursumuzu Sadık Turan programcısı veriyor."
uzunluk = len(website)
uzunluk2 = len(course)
# 1.Soru
soru1 = website[8:11]
# print(soru1)
# 2. Soru
soru2 = website[uzunluk-3:uzunluk]
#print(soru2)
# 3.Soru
soru3 = course[:15] + course[-15:]
# print(soru3)
# 4.Soru
soru4 = course[::-1]
# print(soru4)
# 5.Soru
name, surname, age, job = "Emre", "Tekin", 22, "Öğrenci"
text = "Benim adım {0} {1}, Yaşım {2} ve mesleğim {3}".format(name,surname,age,job)
# print(text)
# 6.Soru
yazi = "Hello world"
a = yazi[:6] + "W" + yazi[-4:]
#print(a)
# 2.Yöntem
yazi = yazi.replace('w','W')
#print(yazi)
# 8.Soru
string = "abc"
print(string * 3)
