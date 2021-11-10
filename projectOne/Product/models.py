from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import DO_NOTHING


class Employees(models.Model):
    emp_name = models.CharField(max_length=100)
    emp_age = models.IntegerField()
    emp_sex = models.CharField(max_length=100)
    emp_department = models.CharField(max_length=100)
    emp_title = models.CharField(max_length=100)
    emp_salary = models.DecimalField(max_digits=8, decimal_places=2)
    ownner = models.ForeignKey(User, on_delete=DO_NOTHING, null=True)


    def __str__(self):
        return self.emp_name

class Album(models.Model):
    title = models.CharField(max_length=200)
    artiste = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.title}'

class Songs(models.Model):
    title = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=DO_NOTHING)

    def __str__(self):
        return f'{self.title}'

class Author(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.name}'

class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    author = models.ManyToManyField(Author)

    def __str__(self):
        return f'{self.title}'


    