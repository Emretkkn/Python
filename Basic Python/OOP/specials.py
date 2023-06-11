myList = [1,2,3,4,5]
myString = "Dokuz Eylül Üniversitesi"

class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print("Object Created")


    def __str__(self):
        return f"{self.title} adlı filmin yönetmeni {self.director}"
    
    def __len__(self):
        return self.duration

    def __del__(self):
        print("Movie was deleted.")

m1 = Movie("Alacakaranlık","David Slade",120)
print(str(m1))
# del m1 # Del keyword'ü tanımlanan objeyi siler.

# print(str(m1))
# print(len(m1))
# print((myList))
# print((myString))
