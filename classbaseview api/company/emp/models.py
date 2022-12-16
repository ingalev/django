from django.db import models

# Create your models here.
class employee(models.Model):
    name=models.CharField(max_length=50)
    salary=models.IntegerField()
    email=models.EmailField()
    