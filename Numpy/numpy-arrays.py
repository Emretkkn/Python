import numpy as np
# result = np.array([2,4,6,8,10])
# result = np.arange(1,11)
# result = np.arange(0,101,4)
# result = np.zeros(5)
# result = np.ones(5) # Her eleman float döner
# result = np.linspace(0,100,5) # Başlangıç ve bitiş değerini eşit aralıklarla böler.
# result = np.random.randint(0,10) # Belirtilen değerler arasında rastgele bir sayı döndürür bitiş değeri dahil değill.
# result = np.random.randint(0,10,4)
# result = np.random.rand(5) # 0 ile 1 arasında girilen değer kadar sayı döndürür.
# result = np.random.randn(5) # negatif değerler de dahil olur.
# np_array = np.arange(40)
# np_multi = np_array.reshape(4,10)
# print(np_multi.sum(axis=1)) # Satırların toplamını verir.
# print(np_multi.sum(axis=0)) # Sütunların toplamını verir.
rnd_numbers = np.random.randint(1,100,10)
print(rnd_numbers)
# result = rnd_numbers.max() # Sayıların en büyüğünü döndürür.
# result = rnd_numbers.mean() # Ortalama alır.
result = rnd_numbers.argmax() # En büyük sayının index numarasını verir.
result = rnd_numbers.argmin() # En küçük sayının index numarasını verir.
print(result)