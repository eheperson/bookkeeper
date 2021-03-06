# Generated by Django 4.0.4 on 2022-05-11 00:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booktracker', '0003_alter_author_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_info', to='booktracker.author'),
        ),
    ]
