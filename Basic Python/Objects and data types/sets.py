# Sets are immutable
boslist = []
brands = {"BMW","Mercedes","Renault"}
# adc = brands[0]
# for i in brands:
#     boslist.append(i)
# Setlere eleman eklemek için 
brands.add("Honda")
brands.update(["Suzuki","Toyota","Pagani"])
print(brands)
# Setin içindeki her bir değer unique'dir aynı veri sadece bir kez yazılabilir.
mylist = [1,2,2,3,5,5,4,6,7]
print(set(mylist))
# Setin içinden bir değer silmek için
brands.remove("Suzuki") # ya da
# brands.discard("Suzuki")
# Setlerde pop metodu listlerde olduğu gibi en son elemanı silmez, herhangi bir eleman silinebilir.
brands.pop() # Burda pagani silindi
# Tüm elemanları temizlemek için
brands.clear()
print(brands)
