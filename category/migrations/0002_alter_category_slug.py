# Generated by Django 3.2.22 on 2023-10-27 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=60, unique=True),
        ),
    ]
