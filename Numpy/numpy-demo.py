import numpy as np
# 1- (10,15,30,45,60) değerlerine sahip numpy dizisi oluşturunuz.
np_array = np.array([10,15,30,45,60])
# 2- (5-15) arasındaki sayılarla numpy dizisi oluşturunuz.
np_array = np.arange(5,15)
# 3- (50-100) arasında 5'er 5'er artarak numpy dizisi oluşturunuz.
np_array = np.arange(50,100,5)
# 4- 10 elemanlı sıfırlardan oluşan bir dizi oluşturunuz.
np_array = np.zeros(10)
# 5- 10 elemanlı birlerden oluşan bir dizi oluşturunuz.
np_array = np.ones(10)
# 6- (0-100) arasında eşit aralıklı 5 sayı üretin.
np_array = np.linspace(0,100,5)
# 7- (10-30) arasında rastgele 5 tane tamsayı üretin.
np_array = np.random.randint(0,30,5)
# 8- (-1 ile 1) arasında 10 tane sayı üretin.
np_array = np.random.rand(10)
# 9- (3x5) boyutlarında (10-50) arasında rastgele bir matris oluşturunuz.
np_array = np.random.randint(10,50,15).reshape(3,5)
# 10- Üretilen matrisin satır ve sütun sayıları toplamını hesaplayınız.
matris = np.random.randint(10,50,15).reshape(3,5)
# rowTotal = matris.sum(axis=1)
# colTotal = matris.sum(axis=0)
# print(np_array)
# print(rowTotal,colTotal)
# 11- Üretilen matrisin en küçük en büyük ve ortalaması nedir ?
result = matris.min()
result = matris.max()
result = matris.mean()
# 12- Üretilen matrisin en büyük değerinin indexi kaçtır ?
result = matris.argmax()
result = matris.argmin() # en küçük değerin indexi
# print(matris)
# print(result)
# 13- (10-20) arasındaki sayıları içeren dizinin ilk 3 elemanını seçiniz.
array = np.arange(10,20)
array[:3]
# 14- Üretilen dizinin elemanlarını tersten yazdırın.
# print(array[::-1])
# 15- Üretilen matrisin ilk satırını seçiniz.
result = matris[0]
# print(matris)
# print(result)
# 16- Üretilen matrisin 2.satır 3.sütunundaki elemanı hangisidir ?
# print(matris[1][2])
# 17- Üretilen matrisin tüm satırlardaki ilk elemanını seçiniz.
# print(matris[:,0])
# 18- Üretilen matrisin her bir elemanının karesini alınız.
# print(np.power(matris,2))
#print(matris ** 2)
# 19- Üretilen matris elemanlarından hangisi pozitif çift sayıdır
# Aralığı (-50,+50) arasında yapınız.
matris = np.random.randint(-50,50,15).reshape(3,5)
positive = matris[matris % 2 == 0]
result = positive[positive > 0]
print(matris)
print(result)
