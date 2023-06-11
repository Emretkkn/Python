import mysql.connector
import datetime
baglanti = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "schooldb"
)
# mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "",
#     # database = "SchoolDB"
# )
# cursor = mydb.cursor()
# cursor.execute("CREATE DATABASE SchoolDB")
# cursor.execute("CREATE TABLE Student (id int(11),student_number int(11), name VARCHAR(255), surname VARCHAR(255), birthdate DATE, gender VARCHAR(50))")
# cursor.execute("SHOW DATABASES")
# for i in cursor:
#     print(i)

# connection = mysql.connector.connect(host="localhost",user="root",password="")
# cursor = connection.cursor()
# cursor.execute("DROP DATABASE python")
# cursor.execute("DROP DATABASE schooldb")
# cursor.execute("SHOW DATABASES")
# for x in cursor:
#     print(x)
# cursor.execute("CREATE DATABASE Python")


# connection = mysql.connector.connect(host="localhost",user="root",password="",database="schooldb")
# cursor = connection.cursor()
# sql = "INSERT INTO student(id,name,surname,birthdate,gender) VALUES(%s,%s,%s,%s,%s)"
# values = [("101","Ahmet","Tazegül",datetime.datetime(2001,5,18),"E"),
#           ("102","Emre","Tekin",datetime.datetime(2001,7,2),"E"),
#           ("103","Zeynep","Ferzan",datetime.datetime(2001,8,14),"K"),
#           ("104","Alperen","Yüksel",datetime.datetime(2001,6,30),"E"),
#           ("105","Can","Pınar",datetime.datetime(2002,3,11),"E"),
#           ("106","Oktay","Özcan",datetime.datetime(2004,8,9),"E")]
# cursor.executemany(sql,values)
# connection.commit()
# connection.close()


class Student:
    connection = baglanti
    cursor = connection.cursor()

    def __init__(self,id,name,surname,birthdate,gender):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender

    def saveStudent(self):
        sql = "INSERT INTO student(name,surname,birthdate,gender) VALUES(%s,%s,%s,%s)"
        value = (self.name,self.surname,self.birthdate,self.gender)
        Student.cursor.execute(sql,value)
        try:
            Student.connection.commit()
            print(f"{Student.cursor.rowcount} tane kayıt eklendi.")
            print(f"Son eklenen kaydın id numarası: {Student.cursor.lastrowid}")
        except mysql.connector.Error as err:
            print("Kayıt Eklenemedi",err)
        finally:
            Student.connection.close()
    @staticmethod
    def saveStudents(students):
        sql = "INSERT INTO student(studentNumber,name,surname,birthdate,gender,class_id) VALUES(%s,%s,%s,%s,%s,%s)"
        values = students
        Student.cursor.executemany(sql,values)
        try:
            Student.connection.commit()
            print(f"{Student.cursor.rowcount} tane kayıt başarıyla eklendi.")
        except mysql.connector.Error as err:
            print("Kayıt Hatası",err)
        finally:
            Student.connection.close()
    
    @staticmethod
    def querys():
        # 1- Tüm öğrenci kayıtlarını alınız.
        sql = "SELECT * FROM student"
        # 2- Öğrencilerin sadece no, ad ve soyad bilgilerini alınız.
        sql = "SELECT student.id, student.name, student.surname FROM student"
        # 3- Sadece kız öğrencilerin adını soyadını alınız.
        sql = "SELECT student.name, student.surname FROM student WHERE student.gender='K'"
        # 4- Sadece 2003 doğumlu öğrencilerin bilgilerini alın.
        sql = "SELECT * FROM student WHERE EXTRACT(YEAR FROM student.birthdate) = 2003"
        # 5- İsmi ali ve doğum tarihi 2005 olan öğrencileri alınız.
        sql = "SELECT * FROM student WHERE student.name = 'Ali' AND EXTRACT(YEAR FROM student.birthdate) = 2005"
        # 6- Adı veya soyadı içerisinde an ifadesi geçen kayıtları alınız.
        sql = "SELECT * FROM student WHERE student.name LIKE '%an%' OR student.surname LIKE '%an'"
        # 7- Kaç erkek öğrenci vardır ? 
        sql = "SELECT COUNT(*) FROM student WHERE student.gender = 'E'"
        # 8 - Kız öğrencileri harf sırasına göre getiriniz.
        sql = "SELECT * FROM student WHERE student.gender = 'K' ORDER BY student.name,student.surname ASC"
        Student.cursor.execute(sql)
        result = Student.cursor.fetchall()
        for x in result:
            # print(f"{x[0]} {x[1]} {x[2]} {x[3]} {x[4]}")
            # print(f"{x[0]} {x[1]} {x[2]}")
            # print(f"{x[0]} {x[1]} {x[2]} {x[3]} {x[4]} ")  
            # print(f"{x[0]}")
            print(f"{x[0]} {x[1]} {x[2]} {x[3]} {x[4]} ")
        Student.connection.close()
    @staticmethod
    def getStudentById(id):
        sql = "SELECT * FROM student where student.id=%s"
        value = (id,)
        Student.cursor.execute(sql,value)
        obj = Student.cursor.fetchone()
        return Student(obj[0],obj[1],obj[2],obj[3],obj[4])
    def updateStudent(self):
        sql = "UPDATE student SET name=%s,surname=%s,birthdate=%s,gender=%s WHERE id=%s"
        values = (self.name,self.surname,self.birthdate,self.gender,self.id)
        Student.cursor.execute(sql,values)
        try:
            Student.connection.commit()
            print("Kayıt Güncellendi")
        except mysql.connector.Error as err:
            print("Kayıt Güncellenemedi",err)
        finally:
            Student.connection.close()
    
    @staticmethod
    def getStudentsByGender(gender):
        sql = "SELECT * FROM student where student.gender=%s"
        value = (gender,)
        Student.cursor.execute(sql,value)
        return Student.cursor.fetchall()
        
    def updateStudents(ogrenciler):
        sql = "UPDATE student SET name=%s,surname=%s,birthdate=%s,gender=%s WHERE id=%s"
        values = []
        sira = [1,2,3,4,0]
        for row in ogrenciler:
            row = [row[i] for i in sira]
            values.append(row)
        Student.cursor.executemany(sql,values)

        try:
            Student.connection.commit()
            print(f"{Student.cursor.rowcount} tane kayıt güncellendi")
        except mysql.connector.Error as err:
            print("Kayıt Güncellenemedi",err)
        finally:
            Student.connection.close()
    

# ogrenci1 = Student("Emre","Tekin",datetime.datetime(2001,7,22),"E")
# ogrenci1.saveStudent()
ogrenciler = [
    (101,"Emre","Tekin",datetime.datetime(2001,7,22),"E",1),
    (102,"Elif","Tekin",datetime.datetime(1997,8,25),"K",2),
    (103,"Nermin","Tekin",datetime.datetime(1977,6,30),"K",3),
    (104,"Sadi","Tekin",datetime.datetime(1975,9,15),"E",1),
    (105,"Tuğba","Aktaş",datetime.datetime(2001,3,21),"E",2),
    (106,"Zeynep","Ferzan",datetime.datetime(2001,8,14),"K",3),
]
Student.saveStudents(ogrenciler)
# Student.querys()
# student = Student.getStudentById(5)
# student.name = "Mauro"
# student.surname = "Icardi"
# student.updateStudent()
# students = Student.getStudentsByGender("K")
# boslist = []
# for ogrenci in students:
#     ogrenci = list(ogrenci)
#     ogrenci[1] = "Simge"
#     boslist.append(ogrenci)
# Student.updateStudents(boslist)