from django.db import models

# Create your models here.

class quotations(models.Model):
    name=models.CharField(max_length=50,null=False)
    mail=models.EmailField(max_length=50,null=False)
    contact=models.BigIntegerField(null=False)
    service=models.CharField(max_length=50,null=False)
    budget=models.IntegerField(null=True)
    note=models.CharField(max_length=200,null=True)