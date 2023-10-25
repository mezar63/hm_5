from django.db import models


class Subject(models.Model):
    name = models.CharField("Название педмета", max_length=100, default="")

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField("ФИО", max_length=255, default="")
    birth_date = models.DateField()
    subjects = models.ForeignKey(
        Subject, verbose_name="Предметы", on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.name
