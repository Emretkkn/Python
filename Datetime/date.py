
from datetime import timedelta
from datetime import datetime
# import datetime
# sonuc = dir(datetime)
# print(sonuc)
simdi = datetime.now() # birbirleri yerine kullanılabilir.
simdi = datetime.today()
yil = simdi.year
ay = simdi.month
gun = simdi.day
saat = simdi.hour
dakika = simdi.minute
detayli = datetime.ctime(simdi)
slicing = datetime.strftime(simdi,"%Y") # yil
slicing = datetime.strftime(simdi,"%B") # ay
slicing = datetime.strftime(simdi,"%X") # saat
slicing = datetime.strftime(simdi,"%d") # int gün
slicing = datetime.strftime(simdi,"%A") # str gün
slicing = datetime.strftime(simdi,"%B") # str ay  
slicing = datetime.strftime(simdi,"%Y %M %A")

time = "22 July 2001 hour 09:05:21"
sonuc = datetime.strptime(time,"%d %B %Y hour %H:%M:%S")
result = sonuc.year
result = sonuc.month
# result = sonuc.minute
# print(result)
# print(yil,ay,gun)
# print(slicing)

myBirthday = datetime(2001,7,22,14,30,55)
result = datetime.timestamp(myBirthday) # Saniye
result = datetime.fromtimestamp(result) # Saniye to Datetime
# print(myBirthday)

result = datetime.fromtimestamp(0) # Bilgisayarlar için milat
fark = simdi - myBirthday # Obje döndürür.
kacgungecmis = fark.days
kacsaniye = fark.seconds
# print(kacsaniye)

# Tarih ekleme işlemleri
gunekle = simdi + timedelta(days=10) # 10 gün ekleme
saniyeekle = simdi + timedelta(seconds=5000) # 5000 saniye ekleme
# print(saniyeekle)

# Tarih fark alma işlemleri
farkal = simdi - timedelta(days=730)
print(f"{simdi}\n{farkal}")