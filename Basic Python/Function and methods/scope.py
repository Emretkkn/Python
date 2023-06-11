# isim = "Emre" # Global Scope
# def fonksiyon():
#     isim = "Ali" # Local Scope
#     if isim == "Ali":
#         print(isim)
# fonksiyon()
# print(isim)

# brand = "Mercedes"
# def changeBrand():
#     # brand = "BMW"
#     def goodbye():
#         # brand = "Renault"
#         print("Bye " + brand)
#     goodbye()
# changeBrand()
x = 30
def test():        # global ifadesi fonksiyon dışında tanımlanan değerin de değiştirilmesini sağlar.
    global x
    print(f"x : {x}")
    x = 80
    print(f"x {x}'e değiştirildi.")
        
test()
print(x)