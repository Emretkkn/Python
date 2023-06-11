import re
result = dir(re)
str = "Python Kursu: Python Programlama Rehberiniz | 40 saat"
result = re.findall("Python",str) # Girilen pattern'dan kaç tane geçiyorsa tamamını listeler.
result = re.split(" ",str) # Girilen parametreye göre stringi böler.
result = re.sub(" ","-",str) # İlk parametredeki değeri ikinci ile değiştirir.
result = re.sub("\s","-",str) # \s regular expressions için boşluk karakteri yerine geçer.
ara = re.search("Programlama",str) # İçine girilen stringin İLK bulunduğu konumu match objesi olarak döndürür.
result = ara.span() # Başlangıç ve bitişi birlikte döndürür.
result = ara.start() # Sadece başlangıç değerini döndürür.
result = ara.end() # Sadece bitiş değerini döndürür.
result = ara.group() # Bulduğu ifadeyi döndürür.    
result = ara.string # Arama işleminin nerede yapıldığını gösterir.

# Regular expressions
'''
Köşeli Parantezler [] arasına yazılan tüm karakterleri aranır.
    [abc] gibi                 [^abc] -> abc dışındaki karekterler
    [a-e] [a,b,c,d,e]          [^0-9] -> rakam olmayan karakterler.
    [1-9] [1,2,3,4,5,6,7,8,9]

. - Herhangi bir tek karakteri temsil eder
    re.findall(".",str)
    
^ - Belirtilen string  (tamamı) karakterle başlayıp başlamadığını kontrol eder.     
    re.findall("^a",str)

$ - Belirtilen string (tamamı) karakterle bitiyor mu ?
    re.findall(t$,str)

    
* - Bir karakterin sıfır ya da daha fazla sayıda olup olmamasını kontrol eder.
        em*e => eme : one match
                emme : one match
                emmmmmmme: one match
                emte : No match (m'nin arkasından e gelmiyor.)

+ - Bir karakterin bir ya da daha fazla sayıda olmasını kontrol eder                
        ma+n => man: One match
                maaan : One match
                main : No match a'nın arkasından n gelmiyor.

                
? - Bir karakterin sıfır ya da bir kez olup olmadığını kontrol eder (daha fazlası yok)
        ma?n = > man: One match
                 mn: One match
                 maaaaan: No match
{} - Karakter sayısını kontrol eder.
        al{2} => a karakterinin arkasındaki l iki defa tekrarlamalı.
        al{2,3} => a karakterinin arkasındaki l en az 2 en fazla 3 defa tekrarlamalı.
        [0-9]{2,4} => en az 2 en fazla 4 basamaklı sayılar. 

| - ifadesi alternatif seçeneklerden en az birinin gerçekleşmesi anlamına gelir.        


() - ifadesi grıplama yapmak için kullanılır.
        (a|b|c)xz => a,b,c karakterlerinin en az birinin arkasından xz gelmeli

\ - ifadesi özel karakterleri aramamızı sağlar.
        \$a $ karakterinin arkasında a karakteri arar.
            Regular exp. engine tarafından yorumlanmaz.

        \A belirtilen karakter stringin başındamı
            \Athe => The stringin başındamı        
        
        \Z belirtilen karakter stringin sonundamı.
            \Zthe => The stringin sonundamı   

\b - ifadesi belirtilen karakter kelimenin başında ya da sonunda mı ?
        \bthe => the kelimenin başında mı
        the\b => the kelimenin sonunda mı

\d - [0-9] ifadesi ile aynı anlama gelir rakam olanları arar.                
        \D => 123abCD567
        

\D - [^0-9] ifadesi ile aynı anlama gelir rakam olmayanları arar.                
        \D => 123abCD567

        
        \s boşluk karakterlerini arar.
        \S boşluk karakterleri dışındakileri arar.
        \w alfabetik karakterler, rakamlar ve alt çizgi karakteri
        \W \w nün tam tersi.        
'''
new_Str = "Emmmre Tekin"
numberstr = "290 4500 12 336 55861"
str2 = "Balıkesir"
email = "emretekin_35@outlook.com"

result = re.findall("[abc]",str)
result = re.findall("[a-z]",str) # a-z arasındaki tüm harfler
result = re.findall("[0-9]",str) # tüm rakamlar
result = re.findall("[^a-z]",str) # alfabetik olmayan değerler.
result = re.findall("[^0-9]",str) # Rakam dışındaki değerler.
result = re.findall("....",str) # yazılan nokta kadar karakterleri gruplar.
result = re.findall("^Py",str) # Belirtilen string  (tamamı) karakterle başlayıp başlamadığını kontrol eder.
result = re.findall("t$",str) # Belirtilen string (tamamı) karakterle bitiyor mu ?
result = re.findall("Em*e",new_Str) # 0 ya da daha fazla sayıda olup olmadığını kontrol eder.
result = re.findall("Em+e",new_Str) # 1 ya da daha fazla sayıda olup olmadığını kontrol eder.
result = re.findall("Em?r",new_Str) # 0 ya da 1 kez olup olmadığını kontrol eder.
result = re.findall("m{2}",new_Str) # {} içine girilen değer kadar olup olmadığını kontrol eder.
result = re.findall("[0-9]{4}",numberstr)
result = re.findall("a|i",str2) # Or anlamına gelir
result = re.findall("(A|B|C)alı",str2) # Gruplama yapar
result = re.findall("\@o",email) # Özel karakter
result = re.findall("\ABalk",str2) # belirtilen ifadeyle başlayıp başlamadığını kontrol eder.
result = re.findall("sir\Z",str2) # belirtilen ifadeyle bitip bitmediğini kontrol eder.
result = re.findall("at\Z",str)
v2 = re.findall("\bBalı",new_Str)
v1 = re.findall("\d",str)
result = re.findall("\w",str)
result = re.findall("\W",str)
print(result)
