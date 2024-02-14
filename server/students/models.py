from django.db import models

# Create your models h

class Student(models.Model):
    Id = models.IntegerField(primary_key=True,null=False,default=0)
    Text =models.CharField(max_length=100)
    File = models.FileField(upload_to='uploads/',null=True)

class Result(models.Model):
    Id = models.IntegerField(primary_key=True,null=False,default=0)
    Result =models.CharField(max_length=100)

    

