from dbmanager import DbManager
from datetime import datetime
from student import Student
class App:
    def __init__(self):
        self.db = DbManager()

    def addStudent(self):
        self.displayClasses()
        classid = int(input("Hangi sınıfa öğrenci eklemek istiyorsunuz ?: "))
        studentnumber = input("Eklemek İstediğiniz Öğrencinin Numarasını Giriniz: ")
        name = input("Eklemek İstediğiniz Öğrencinin Adını Giriniz: ")
        surname = input("Eklemek İstediğiniz Öğrencinin Soyadını Giriniz: ")
        year = input("Yıl: ")
        month = input("Ay: ")
        day = input("Gün: ")
        birthdate = datetime(int(year),int(month),int(day))
        gender = input("Eklemek İstediğiniz Öğrencinin Cinsiyetini Giriniz (E/K): ")
        student = Student(None,studentnumber,name,surname,birthdate,gender,classid)
        self.db.addStudent(student)

    def editStudent(self):
        classid = self.displayStudents()
        studentid = int(input("Düzenlemek istediğiniz öğrenci id giriniz: "))
        student = self.db.getStudentById(studentid)
        student[0].studentNumber = input("Yeni Öğrencinin Numarasını Giriniz: ") or student[0].studentNumber
        student[0].name = input("Yeni Öğrencinin Adını Giriniz: ") or student[0].name
        student[0].surname = input("Yeni Öğrencinin Soyadını Giriniz: ") or student[0].surname
        student[0].gender = input("Yeni Öğrencinin Cinsiyetini Giriniz: ") or student[0].gender
        student[0].classid = input("Yeni Öğrencinin Sınıfını Giriniz: ") or student[0].classid
        year = int(input("Doğum Yılı: "))
        month = int(input("Doğum Ayı: "))
        day = int(input("Doğum Günü: "))
        student[0].birthdate = datetime(year,month,day)
        self.db.editStudent(student[0])


    def displayClasses(self):
        classlist = self.db.getClassList()
        for x in classlist:
            print(f"{x.id}: {x.name}")
    
    def displayStudents(self):
        self.displayClasses()
        classid = int(input("Hangi sınıftaki öğrencileri listelemek istiyorsunuz ?: "))
        students = self.db.getStudentsByClassId(classid)
        for st in students:
            print(f"{st.id}- {st.studentNumber} {st.name} {st.surname} {st.gender}")
        return classid
    
    
    def initApp(self):
        msg = "**************"
        menu = "\n1-Öğrenci Listesi\n2-Öğrenci Ekle\n3-Öğrenci Güncelle\n4-Öğrenci Sil\n5-Öğretmen Ekle\n6-Sınıflara göre dersler\n7-Çıkış"
        while True:
            print(msg+menu)
            secim = input("Lütfen Seçim Yapınız: ")
            if secim == "1":
                self.displayStudents()
            elif secim == "2":
                self.addStudent()
            elif secim == "3":
                self.editStudent()
            elif secim == "4":
                pass
            elif secim == "5":
                pass
            elif secim == "6":
                pass
            elif secim == "7":
                break
            else:
                print("Yanlış Tercih Yaptınız.")

app = App()
app.initApp()