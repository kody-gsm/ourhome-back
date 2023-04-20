from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title + self.answerCheck()
    
    def answerCheck(self):
        if self.answer_set.all():
            return ""
        else:
            return " : X"
    

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()

    def __str__(self):
        return str(self.question) + " : " + str(self.answer)




