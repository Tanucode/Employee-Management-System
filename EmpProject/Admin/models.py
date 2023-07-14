from django.db import models

# Create your models here.
class Role(models.Model):
    name = models.CharField(null=False,max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    username = models.CharField(max_length=1000,null=False,unique=True)
    email=models.CharField(max_length=20)
    empid=models.CharField(max_length=100,null=False,unique=True)
    desig=models.CharField(max_length=30)
    salary=models.IntegerField(default=0)
    exp=models.IntegerField()
    skill=models.CharField(max_length=20)
    aow=models.ForeignKey(Role,on_delete=models.CASCADE)
    phone=models.IntegerField()
    dob=models.DateField(max_length=10)
    gender=models.CharField(max_length=20)
    address=models.TextField(max_length=40000)
    # password = models.CharField(max_length=1000,)

    def __str__(self):
        return "%s ,%s" %(self.username,self.aow)