from django.db import models


class Post(models.Model):
    number=models.CharField(max_length=10,primary_key=True)
    date=models.CharField(max_length=30)