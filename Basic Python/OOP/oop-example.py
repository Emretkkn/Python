# Question
class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    
    def checkAnswer(self,answer):
        return self.answer == answer

q1 = Question("En iyi programlama dili hangisidir ?",["Python","Javascript","R","PHP","Kotlin"],"Python")
q2 = Question("En popüler programlama dili hangisidir ?",["Python","Javascript","R","PHP","Kotlin"],"PHP")
q3 = Question("En fazla kullanılan kütüphane hangisidir",["datetime","Numpy","Pandas","Pyqt5"],"Pyqt5")

# Quiz
class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0
    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        soru = self.getQuestion()
        print(f"Soru {self.questionIndex + 1}: {soru.text} ")

        for i in soru.choices:
            print("-" + i)
        answer = input("Cevap: ")
        self.tahmin(answer)
        self.loadQuestion() 

    def tahmin(self,answer):
        soru = self.getQuestion()
        if soru.checkAnswer(answer):
            self.score += 1
        self.questionIndex +=1

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()
    
    def showScore(self):
        print(f"Score: {self.score}")
        
    def displayProgress(self):
        toplamSoru = len(self.questions)
        soruNo = self.questionIndex + 1
        if soruNo > toplamSoru:
            print("Quiz bitti.")
        else:
            print(f"{soruNo}/{toplamSoru}")

# print(q1.checkAnswer("Python"))
# print(q2.checkAnswer("Javascript"))

sorular = [q1,q2,q3]
quiz = Quiz(sorular)  
quiz.displayQuestion()