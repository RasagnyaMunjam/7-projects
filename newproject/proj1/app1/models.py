from django.db import models

# Create your models here.
class First(models.Model):
    name=models.CharField(max_length=50)
    address=models.TextField(max_length=50)
    age=models.IntegerField()
