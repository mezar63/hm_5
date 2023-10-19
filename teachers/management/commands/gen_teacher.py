import sys

from django.core.management.base import BaseCommand

from teachers.models import Subject

SUBJECTS_DEMO = (
    "Математика",
    "География",
    "Биология",
    "Химия",
)


class Command(BaseCommand):
    help = "Add subjects"

    def handle(self, *args, **options):
        for subject in SUBJECTS_DEMO:
            Subject.objects.create(name=subject)

            self.stdout.write(self.style.SUCCESS("Successfully added"))
