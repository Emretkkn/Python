def toplama(a,b):
    return a+b
def cikartma(a,b):
    return a-b
def carpim(a,b):
    return a*b
def bolme(a,b):
    return a/b

def islem(f1,f2,f3,f4,islem_adi):
    if islem_adi == "Toplama":
        return f1(10,21)
    elif islem_adi == "Çıkartma":
        return f2(10,21)
    elif islem_adi == "Çarpma":
        return f3(10,21)
    elif islem_adi == "Bölme":
        return f4(10,21)
    else:
        print("Geçersiz Değerler.")

print(islem(toplama,cikartma,carpim,bolme,"Çıkartma"))
print(islem(toplama,cikartma,carpim,bolme,"Toplama"))
print(islem(toplama,cikartma,carpim,bolme,"Çarpma"))
print(islem(toplama,cikartma,carpim,bolme,"Bölme"))
