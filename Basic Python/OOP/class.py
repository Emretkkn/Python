# class
class Person:
    pass
    # class attributes
    address =   "No information"
    # constructor (yapıcı metod)
    def __init__(self, name, year):
        self.name = name
        self.birthyear = year
        print("İnit metodu çalıştı")
    # object attributes

    # methods

# object(instance)
p1 = Person("Emre", 2001)
p2 = Person("Elif", 1999)
# Updating
p1.name = "Rümeysa"
p2.name = "Nilay"
# Accessing object attributes
print(f"İsim : {p1.name}, Doğumyılı : {p1.birthyear} Adres : {p1.address}")
print(f"İsim : {p2.name}, Doğumyılı : {p2.birthyear} Adres : {p2.address}")

#print(p1,p2)
# print(type (p1),type(p2))
