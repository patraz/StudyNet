# Generated by Django 4.2.1 on 2023-05-21 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("course", "0002_course"),
    ]

    operations = [
        migrations.CreateModel(
            name="Lessons",
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
                ("title", models.CharField(max_length=255)),
                ("slug", models.SlugField()),
                ("short_description", models.TextField(blank=True, null=True)),
                ("long_description", models.TextField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("draft", "Draft"), ("published", "Draft")],
                        default="published",
                        max_length=20,
                    ),
                ),
                (
                    "lsson_type",
                    models.CharField(
                        choices=[("article", "Article"), ("quiz", "quiz")],
                        default="article",
                        max_length=20,
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lessons",
                        to="course.course",
                    ),
                ),
            ],
        ),
    ]
