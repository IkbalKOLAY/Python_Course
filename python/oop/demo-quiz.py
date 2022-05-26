# question

class Question:
    def __init__(self,text,choices,answer) -> None:
        self.text=text
        self.choices=choices
        self.answer=answer

    def checkAnswer(self,answer):
        return self.answer == answer



# quiz

class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score=0 # kac soruya cevap verildiği 
        self.questionIndex=0 # 0 -->q1

    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        question = self.getQuestion()
        print("")

q1 = Question("q1: elma hangi renk ?",["kırmızı","mor","turuncu"],"kırmızı")
q2 = Question("q2: muz hangi renk ?",["kırmızı","sarı","siyah"],"sarı")
q3 = Question("q3: kivi hangi renk ?",["yeşil","mor","pembe"],"yeşil")
questions = [q1,q2,q3]

quiz = Quiz(questions)
question = quiz.getQuestion()
print(question.text) # indexine göre soruları gösterir



# print(q1.text)
# print((q1.choices))
# answer_ = input("")
# print(q1.checkAnswer(answer_))