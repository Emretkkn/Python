'''
Moduül hakkında bilgilendirme

'''

number = 35
liste = ["Emre",3,4,(1,2,3),True]
person = {
    "Name": "Emre",
    "Surname": "Tekin",
    "Age": 22,
    "City": "İzmir",
    "Gender" : "Male"
}

def kareal(x):
    '''
    Fonksiyon hakkında bilgilendirme.

    '''
    x = x**2
    print(f"Girilen x değerinin karesi {x}")

class Brand:
    def speak(self):
        print("I'm speaking")