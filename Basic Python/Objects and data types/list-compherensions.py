# List compherensions

# numbers = [x for x in range(15)] # List compherension yapısı
# print(numbers)

# sayilar = []
# for i in range(15): # For döngüsü ile yapılma şekli
#     sayilar.append(i)
# print(sayilar)

# karesi = [x**2 for x in range(8)] # List compherension yapısı
# print(karesi)

# karesi2 = []
# for i in range(8): # For döngüsü ile yapılışı
#     karesi2.append(i**2)
# print(karesi2)

# karesi3 = [x*x for x in range(10) if x % 2 == 0] # Sadece çift sayılar ekrana basılır.
# print(karesi3)

# string = "Dokuz Eylül Üniversitesi"
# newlist = [x for x in string if x == "ü" or x == "Ü"] # Başka bir örnek
# print(newlist)

# yillar = [1983,1977,2001,2004,1998]
# yaslar = [2023-i for i in yillar]
# print(yaslar)

# sayilar = [x if x % 2 == 1 else "Çift Sayı" for x in range(1,100)]
# print(sayilar)

# result = []    # For döngüsü ile yapılış
# for x in range(3):
#     for y in range(3):
#         result.append((x,y))
# print(result)

# result = [(x,y) for x in range(4) for y in range(4)] # List-compherension yapısı ile:
# print(result)
