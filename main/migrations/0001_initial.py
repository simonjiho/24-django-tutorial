# Generated by Django 5.1 on 2024-10-13 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Study",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=500, verbose_name="스터디 이름")),
                (
                    "description",
                    models.CharField(max_length=2000, verbose_name="스터디 설명"),
                ),
            ],
            options={
                "verbose_name": "스터디",
                "db_table": "study",
            },
        ),
    ]