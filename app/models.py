from django.db import models

# Create your models here.

class DEPT(models.Model):
    DNAME= models.CharField(max_length= 100)
    LOCATION= models.CharField(max_length=100)
    DEPTNO= models.IntegerField(primary_key=True)

    def __str__(self):
        return self.DNAME


class EMP(models.Model):
    EMPNO= models.IntegerField(primary_key=True)
    ENAME= models.CharField(max_length=100)
    JOB= models.CharField(max_length=100)
    HIREDATE= models.DateField()
    SAL= models.IntegerField()
    COMM= models.IntegerField(null=True, blank=True)
    DEPTNO= models.ForeignKey(DEPT, on_delete= models.CASCADE)

    def __str__(self):
        return self.ENAME