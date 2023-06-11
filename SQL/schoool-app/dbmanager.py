import mysql.connector
from datetime import datetime
from student import Student
from connection import connection
from teacher import Teacher
from classes import Class
class DbManager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()
    
    def getStudentById(self,id):
        sql = "SELECT * FROM student WHERE student.id = %s"
        value = (id,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchone()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print("Hata",err)

    def getStudentsByClassId(self,classid):
        sql = "SELECT * FROM student WHERE student.class_id = %s"
        value = (classid,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchall()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print("Hata",err)
    def addStudent(self,student:Student):
        sql = "INSERT INTO student(studentNumber,name,surname,birthdate,gender,class_id) VALUES(%s,%s,%s,%s,%s,%s)"
        value = (student.studentNumber,student.name,student.surname,student.birthdate,student.gender,student.classid)
        self.cursor.execute(sql,value)
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt eklendi.")
            print(f"Son eklenen kaydın id numarası: {self.cursor.lastrowid}")
        except mysql.connector.Error as err:
            print("Kayıt Eklenemedi",err)

    def editStudent(self,student:Student):
        sql = "UPDATE student SET studentNumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s,class_id=%s WHERE id=%s"
        values = (student.studentNumber,student.name,student.surname,student.birthdate,student.gender,student.classid,student.id)
        self.cursor.execute(sql,values)
        try:
            self.connection.commit()
            print("Kayıt Güncellendi")
        except mysql.connector.Error as err:
            print("Kayıt Güncellenemedi",err)
        finally:
            self.connection.close()

    def getTeacherById(self,id):
        sql = "SELECT * FROM teacher WHERE teacher.id=%s"
        value = (id,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchone()
            return Teacher.CreateTeacher(obj)
        except mysql.connector.Error as err:
            print("Error: ",err)

    def addTeacher(self,teacher:Teacher):
        sql = "INSERT INTO teacher(branch,name,surname,birthdate,gender) VALUES(%s,%s,%s,%s,%s)"
        values = (teacher.branch,teacher.name,teacher.surname,teacher.birthdate,teacher.gender)
        self.cursor.execute(sql,values)
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt eklendi.")
            print(f"Son eklenen kaydın id numarası: {self.cursor.lastrowid}")
        except mysql.connector.Error as err:
            print("Error: ",err)
    def editTeacher(self,teacher:Teacher):
        sql = "UPDATE teacher SET branch=%s,name=%s,surname=%s,birthdate=%s,gender=%s WHERE id=%s"
        values = (teacher.branch,teacher.name,teacher.surname,teacher.birthdate,teacher.gender,teacher.id)
        self.cursor.execute(sql,values)
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt güncellendi.")
        except mysql.connector.Error as err:
            print("Hata: ",err)

    def getClassList(self):
        sql = "SELECT * FROM class"
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Class.createClass(obj)
        except mysql.connector.Error as err:
            print("Hata",err)       

db = DbManager()
# student = db.getStudentById(2)
# print(student.name)
# print(student.surname)
# students = db.getStudentsByClassId(1)
# print(students[0].name)
# student[0].name = "Elifnur"
# student[0].studentNumber = 107
# db.addStudent(student[0])
# db.editStudent(student[0])
# teacher = db.getTeacherById(1)
# teacher[0].name = "Kaan"
# teacher[0].surname = "Yaralıoğlu"
# teacher[0].branch = "Yöneylem Araştırması"
# teacher[0].birthdate = datetime(1955,9,17)
# teacher[0].gender = "E"
# db.addTeacher(teacher[0])
# teacher[0].name = "Vahap"
# db.editTeacher(teacher[0])

