from django.db import models
from django.db.models.aggregates import Count
from random import randint

# Create your models here.
class QuizUser(models.Model):
    name = models.CharField(max_length=250)

# class QuesManager(models.Manager):
#     def random(self):
#         count = self.aggregate(count=Count('id'))['count']
#         random_index = randint(0, count - 1)
#         return super().get_queryset().filter(id = random_index)

class Ques(models.Model):
    quiz_user = models.ForeignKey(QuizUser,on_delete=models.CASCADE,null = True)
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)

# class RelationTable(models.Model):
#     quiz_user = models.ForeignKey(QuizUser,on_delete=models.CASCADE,null = True)
#     ques = models.ForeignKey(Ques,on_delete=models.CASCADE,null = True)
