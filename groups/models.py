from django.db import models

from teachers.models import Teacher


class Group(models.Model):
    name = models.CharField("Назва групи", max_length=255, default="")
    teacher = models.ForeignKey(
        Teacher, verbose_name="Вчитель", on_delete=models.PROTECT
    )

    def __str__(self):
        return self.name
