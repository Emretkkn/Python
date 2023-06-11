import json
import os
class User:
    def __init__(self, username ,password, email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}
        self.loadUsers()

    def login(self,username,password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print("Login Yapıldı.")
                break
        else:
            print("Lütfen kullanıcı adı ve şifrenizi kontrol ediniz.")
    def loadUsers(self):
        if os.path.exists("users.json"):
            with open("users.json","r",encoding="utf-8") as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    newUser = User(username=user["username"],password=user["password"],email=user["email"])
                    self.users.append(newUser)

    def register(self, user: User):
        self.users.append(user)
        self.savetoFile()
        print("Kullanıcı Oluşturuldu.")
    
    def savetoFile(self):
        liste = []
        for user in self.users:
            liste.append(json.dumps(user.__dict__))
        with open("users.json",'w',encoding="utf-8") as file:
           json.dump(liste, file) 

    def logout(self):
        if self.isLoggedIn == True:
            self.isLoggedIn = False
            self.currentUser = {}
            print("Çıkış Yapıldı.")
        else:
            print("Lütfen önce giriş yapınız.")

    def identity(self):
        if self.isLoggedIn == True:
            print(f"Kullanıcı adınız: {self.currentUser.username}\nE-postanız: {self.currentUser.email}")
        else:
            print("Lütfen Giriş Yapınız.")
repository = UserRepository()

while True:
    print("Menü".center(50,'*'))
    secim = int(input("1-Register\n2-Login\n3-Logout\n4-Identity\n5-Exit\nLütfen yapmak istediğiniz işlemin numarasını tuşlayınız: "))
    if secim == 5:
        break
    else:
        if secim == 1:
            username = input("Lütfen kullanmak istediğiniz kullanıcı adını yazınız: ")
            username = username.strip()
            password = input("Lütfen kullanmak istediğiniz şifreyi yazınız: ")
            password.strip()
            while len(password) <= 8:
                print("Lütfen 8 karakterden uzun bir şifre giriniz.")
                password = input("Lütfen kullanmak istediğiniz şifreyi yazınız: ")
            email = input("Lütfen e-postanızı yazınız: ")
            email.strip()
            while '@' not in email:
                print("Lütfen e-postanızı @ karakteri ile yazınız.")
                email = input("Lütfen e-postanızı yazınız: ")
            user = User(username=username,password=password,email=email)
            repository.register(user)
        elif secim == 2:
            if repository.isLoggedIn == True:
                print("Zaten giriş yaptınız.")
            else:
                username = input("Kullanıcı adını giriniz: ")
                password = input("Şifrenizi giriniz: ")
                repository.login(username,password)
        elif secim == 3:
            repository.logout()
        elif secim == 4:
            repository.identity()
        else:
            print("Yanlış bir değer girdiniz.")