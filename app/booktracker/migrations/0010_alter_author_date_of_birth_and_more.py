# Generated by Django 4.0.4 on 2022-05-12 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktracker', '0009_alter_book_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='date_of_birth',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='date_of_death',
            field=models.DateField(auto_now=True),
        ),
    ]
