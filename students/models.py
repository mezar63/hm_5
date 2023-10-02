from django.db import models


# Create your models here.
class Student(models.Model):
    first_name = models.CharField("Ім'я", max_length=255, default="")
    last_name = models.CharField("Прізвище", max_length=255, default="")
    birth_date = models.DateField("Дата народження", default="")

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенти"
