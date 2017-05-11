from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Role(models.Model):
    movie = models.ForeignKey(Movie)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Actor(models.Model):
    role = models.ForeignKey(Role)
    full_name = models.CharField(max_length=250)
    gender = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name


class Salary(models.Model):
    role = models.ForeignKey(Role)
    amount = models.IntegerField()

    def __str__(self):
        return "{} php".format(self.amount)
