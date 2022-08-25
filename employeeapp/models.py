from django.db import models

# Create your models here.

class Department(models.Model):
    department=models.CharField(max_length=120)

    def __str__(self):
        return self.department

class Employee(models.Model):
    name=models.CharField(max_length=120)
    salary=models.PositiveIntegerField()
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=12)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)


    def __str__(self):
        return self.name
