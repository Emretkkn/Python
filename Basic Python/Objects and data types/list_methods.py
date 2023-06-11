# # Soru 1
# brands = ["BMW","Opel","Mercedes","Mazda"]
# # Soru 2
# # print(len(brands))
# # Soru 3
# # print(brands[0],brands[-1])
# # Soru 4
# brands = list(map(lambda x: x.replace("Mazda","Toyota"),brands))
# # print(brands)
# # Soru 5
# sonuc = "Mercedes" in brands
# # print(sonuc)
# # Soru 6
# b = brands[-2]
# # print(b)
# # Soru 7
# c = brands[0:3]
# # print(c)
# # Soru 8
# brands[-2:] = ["Renault","Toyota"]
# # Soru 9
# brands = brands + ["Audi","Nissan"]
# # Soru 10
# del brands[-1]
# # print(brands)
# # Soru 11
# reversebrand = brands[::-1]
# print(reversebrand)

# studentA = ["Yiğit","Bilgi",2002,[56,78,84]]
# studentB = ["Zeynep","Sena",2001,[99,99,100]]
# studentC = ["Emre","Tekin",2001,[75,22,90]]

# fstring = f"{studentB[0]} {studentB[2]} {(2023-2001)} yaşında ve not ortalaması {(studentB[3][0] + studentB[3][1] + studentB[3][2])/3} ve onu çok seviyordum hala seviyor muyum bilmiyorum seviyorum galiba."
# print(fstring)

# numbers = [1,2,3,4,5,16,7,7,7,8,9,10]
# letters = ["a","b","c","d","e","n"]

# val = min(numbers)
# val = max(numbers)
# val = numbers[2:8]
# numbers.append(27)
# numbers.insert(8,99)
# numbers.insert(-1,19)
# numbers.pop(0)
# numbers.remove(19)
# numbers.sort()
# letters.sort()
# numbers.reverse()
# letters.reverse()
# print(numbers.count(7))
# print(letters.count("a"))
# numbers.clear()
# print(numbers)