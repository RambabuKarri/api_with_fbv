from django.db import models

# Create your models here.
class Employe(models.Model):
    
    Ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    sal=models.IntegerField()