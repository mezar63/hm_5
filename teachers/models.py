from django.db import models


# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField("Имя", max_length=55, default="")
    last_name = models.CharField("Фамилия", max_length=55, default="")
    subject = models.CharField("Придмет", max_length=75, default="")

    def __str__(self):
        return f"{self.last_name} {self.first_name} ({self.subject})"

    class Meta:
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"


from django.db.models.signals import post_migrate
from django.dispatch import receiver

from faker import Faker

fake = Faker("uk")
SUBJECT_NAMES = ("Математика", "Георгафия", "Экономика", "Философия", "Биология")


@receiver(post_migrate)
def add_initial_data(sender, **kwargs):
    if sender.name == "teachers":
        for i in range(5):
            Teacher.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                subject=fake.random_element(elements=SUBJECT_NAMES),
            )
