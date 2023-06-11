# x = 1
# y = 2
# z = 3

x,y,z = (4,5,6)
x,z = y,x
# print(x,y,z)
x += 10 # x = x+10 ile aynı şey
x -= 4 # x = x-4 ile aynı şey
x *= 10 # x = x*10 ile aynı şey
x /= 8 # x = x/8 ile aynı şey
x % 5 # x = x%5 ile aynı şey
x //= 4 # x'i tam böler sadece virgülden önceki kısmı alır 
x **= 7 # x = x**2 ile aynı şey
print(x)
values = (1,2,3,4,5,6,7)
a,b,*c = values # Eğer eleman sayıları eşleşmez ise hata alınır fakat elemanlardan birinin önüne yıldız işareti eklenirse kalan tüm elemanlar o listeye aktarılır.
print(a,b,c[2])
