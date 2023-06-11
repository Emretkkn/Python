# Inheritance (Kalıtım) : Miras Alma

# Person => name, lastname ,age, eat(), run(), drink() eg.

class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
        # print("Person Created.")
    def who_am_i(self):
        print("Ben Superhero'yum")
    def eat(self):
        print("I'm Eating")





class Student(Person):
    def __init__(self,fname,lname,number,grade):
        Person.__init__(self,fname,lname)
        self.studentNumber = number
        self.studentGrade = grade
        # print("Student Created.")

    # Overwritting    
    def who_am_i(self):
        print("I am a student.")

    def cagirBeni(self):
        print("Çağırdın Geldim.")
p1 = Person("Emre","Tekin")
s1 = Student("Servet","Sayar",2019469062,3)
# print(f"Merhaba {p1.firstname} {p1.lastname} ")
# print(f"Merhaba {s1.firstname} {s1.lastname} {s1.studentNumber} numaralı öğrencimiz {s1.studentGrade} sınıfta öğrenim görmektesiniz.")
# s1.who_am_i()

# s1.cagirBeni()

class Teacher(Person):
    def __init__(self, fname, lname,branch,acadegree):
        super().__init__(fname,lname)
        self.branch = branch
        self.degree = acadegree

    def who_am_i(self):
        print(f"I'm a {self.branch} Teacher.")

t1 = Teacher("Çiğdem","Tarhan","Veritabanı","Doçent")
# print(f"Ben {t1.firstname} {t1.lastname} Branşım {t1.branch} Derecem {t1.degree}")
t1.who_am_i()