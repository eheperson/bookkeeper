# Generated by Django 4.0.4 on 2022-05-12 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktracker', '0012_alter_author_date_of_death_alter_book_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
