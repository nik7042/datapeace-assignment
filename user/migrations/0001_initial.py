# Generated by Django 4.2 on 2025-05-07 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("company_name", models.CharField(max_length=255)),
                ("age", models.PositiveIntegerField()),
                ("city", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=100)),
                ("zip", models.PositiveBigIntegerField()),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("web", models.URLField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "User",
                "verbose_name_plural": "Users",
                "ordering": ["last_name", "first_name"],
            },
        ),
    ]
