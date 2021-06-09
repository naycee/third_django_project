from django.db import models
from django.db.models import Model


# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=400)
    address = models.CharField(max_length=400)
    zip_code = models.IntegerField()


    def __str__(self):
        return self.name


class Certificate_type(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        verbose_name = 'Certificate Type'
        verbose_name_plural = 'Certificate Types'


    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=40)
    

    def __str__(self):
        return self.name


class Faculty(models.Model):
    name = models.CharField(max_length=40)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Grade(models.Model):
    type = models.CharField(max_length=40)

    def __str__(self):
        return self.type


class Student(models.Model):
    full_name = models.CharField(max_length=40)
    year_of_graduation = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    certificate_type = models.ForeignKey(Certificate_type, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name