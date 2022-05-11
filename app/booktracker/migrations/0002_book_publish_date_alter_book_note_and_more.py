# Generated by Django 4.0.4 on 2022-05-10 20:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('booktracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='note',
            field=models.TextField(),
        ),
        migrations.AlterUniqueTogether(
            name='book',
            unique_together={('author', 'title')},
        ),
        migrations.DeleteModel(
            name='Notebook',
        ),
    ]