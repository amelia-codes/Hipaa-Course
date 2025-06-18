from django.db import models

# Create your models here.
#from django.db import models
class Ques(models.Model):
    question = models.CharField(max_length = 500) #check if null True by default
    option1 = models.CharField(max_length = 500)
    option2 = models.CharField(max_length = 500)
    option3 = models.CharField(max_length = 500)
    option4 = models.CharField(max_length = 500)
    correctanswer = models.CharField(max_length = 500)
    def __str__(self):
        return self.question
class ValidUser(models.Model):
    email=models.CharField(max_length=255)
