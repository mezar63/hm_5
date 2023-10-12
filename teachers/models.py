from django.db import models


class Subject(models.Model):
    name = models.CharField("Название предмета", max_length=75, default="")

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField("ФИО", max_length=255, default="")
    birth_date = models.DateField("Дата рождения", default="")
    subjects = models.CharField(max_length=100, default='Математика')

    def __str__(self):
        return self.name