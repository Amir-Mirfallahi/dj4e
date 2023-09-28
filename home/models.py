from django.db import models


class Question(models.Model):
    question = models.CharField(max_length=512)

    def __str__(self):
        return self.question


class Answer(models.Model):
    question = models.ForeignKey(Question, models.CASCADE)
    choice_text = models.CharField(max_length=128)
    votes = models.IntegerField(default=1)
