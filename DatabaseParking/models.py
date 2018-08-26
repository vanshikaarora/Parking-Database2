from django.db import models


class Post(models.Model):
    number=models.CharField(max_length=10,primary_key=True)
    date=models.CharField(max_length=20)
    type = models.CharField(max_length=15)
    amount=models.IntegerField()
    total=models.IntegerField()

class DatePost(models.Model):
    number=models.ForeignKey(Post,on_delete=models.CASCADE,max_length=10)
    date=models.CharField(max_length=20)
    amount=models.IntegerField(max_length=5)