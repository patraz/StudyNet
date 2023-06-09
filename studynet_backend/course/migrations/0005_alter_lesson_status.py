# Generated by Django 4.2.1 on 2023-05-21 20:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("course", "0004_rename_lessons_lesson"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="status",
            field=models.CharField(
                choices=[("draft", "Draft"), ("published", "Published")],
                default="published",
                max_length=20,
            ),
        ),
    ]
