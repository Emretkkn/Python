import random
value1 = random.randrange(1,200) # 1-200 arasında rastgele sayı üretir.
value1 = random.random() # 0.0 - 1.0 arasında rastgele sayı üretir.
value1 = random.randint(1,50) # Girilen iki değer atrasında rastgele integer sayı üretir.
value1 = random.uniform(1,20) # Girilen iki değer arasında rastgele ondalıklı sayı üretir.
# print(value1)
# result = dir(random)
# print(value1)

college = "Dokuz Eylül Üniversitesi"
names = ["Emre","Ali","Tuğba","Ali","Yağmur"]
sonuc = names[random.randint(0,len(names)-1)] # choice metodu kullanmadan yapılış şekli
sonuc = random.choice(names) # choice metodu kullanımı
sonuc = random.choice(college)


liste = list(range(15)) # 15 elemanlı sıralı bir liste
random.shuffle(liste) # Elemanları karıştırılmış bir liste

liste = range(200)
sonuc = random.sample(liste,5)
sonuc = random.sample(names,2)
print(sonuc)
# print(liste)