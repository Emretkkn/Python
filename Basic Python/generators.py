# def cube():
#     sonuc = []
#     for i in range(10):
#         sonuc.append(i**3)
#     return sonuc

# print(cube())
def square():
    for i in range(10):
        yield i**2

generator = square()
# while True:
#     try:
#         deger = next(generator)
#         print(deger)
#     except:
#         raise StopIteration
# for i in generator: # Generator kullanımı
#     print(i)
liste = [i**3 for i in range(5)] # Bellekte yer tutar
# print(liste)
generator = (i**2 for i in range(5)) # Bellekte yer tutmaz
for i in generator:
    print(i)
