# Generated by Django 4.2 on 2023-09-07 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Career",
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
                ("career_title", models.CharField(max_length=50)),
                ("career_exp", models.CharField(max_length=50)),
                (
                    "career_type",
                    models.CharField(
                        choices=[("FT", "Full Time"), ("PT", "Part Time")],
                        default="FT",
                        max_length=40,
                    ),
                ),
                ("career_position", models.CharField(max_length=50)),
                ("career_location", models.CharField(max_length=50)),
            ],
        ),
    ]
