from django.db import models

# Create
class modelclass(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.EmailField()