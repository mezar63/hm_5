# Generated by Django 4.2.5 on 2023-10-26 16:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("students", "0003_alter_student_year"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="phone",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
