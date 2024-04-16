# Generated by Django 5.0 on 2024-04-15 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="StreamingVariable",
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
                ("name", models.CharField(max_length=100)),
                ("value", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("NEG", "Negative"),
                            ("POS", "Positive"),
                            ("VOL", "Volatile"),
                        ],
                        default="POS",
                        max_length=3,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
