# def cube(x): return x ** 3
# liste = [3,5,7,9,10,12,16,4,2]
#sonuc = list(map(cube, liste))
# print(sonuc)
# newlist = []
# for i in liste:
#     a = i ** 3
#       newlist.append(a)
# print(newlist)

# square = lambda x: x**2 
# sonuc = list(map(square,liste)) # Lambda expression
# sonuc = square(4)  
# print(sonuc)

# def ciftsec(x): return x % 2 == 0
# sonuc = list(filter(lambda x: x % 2 == 0,liste)) # lambda expression kullanımı
# teksayi = lambda x: x % 2 == 1
# sonuc = list(filter(teksayi,liste))
# sonuc1 = teksayi(liste[3])
# print(sonuc1)