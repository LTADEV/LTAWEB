# Generated by Django 4.2 on 2023-09-07 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Gallery",
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
                ("gallery_title", models.CharField(max_length=50)),
                (
                    "gallery_tag",
                    models.CharField(
                        choices=[
                            ("campus", "Campus"),
                            ("transportation", "Transportation"),
                            ("infra", "Infrastructure"),
                            ("lab", "Lab"),
                            ("activity", "Activity"),
                        ],
                        default="campus",
                        max_length=50,
                    ),
                ),
                (
                    "gallery_image",
                    models.FileField(
                        default=None, max_length=250, upload_to="gallery/"
                    ),
                ),
            ],
        ),
    ]
