from django.db import models


def give_like(like):
    return like+1


def give_dislike(like):
    return like-1


class User(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Users"


class Question(models.Model):
    topic = models.CharField(max_length=10, default="No topic given.")
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    question_text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    
    def __str__(self):
        return self.topic


class Response(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    message_text = models.CharField(max_length=2000)
    like_counter = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published', auto_now_add=True)


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"
