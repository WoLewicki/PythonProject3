from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Question(models.Model):
    topic = models.CharField(max_length=20, default="No topic given.")
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)
    question_text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.topic


class Response(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    question = models.ForeignKey(Question, on_delete=models.CASCADE,)
    message_text = models.CharField(max_length=2000)
    like_counter = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published',)
