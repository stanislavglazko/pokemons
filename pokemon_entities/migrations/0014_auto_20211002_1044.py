# Generated by Django 3.1.7 on 2021-10-02 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0013_auto_20211002_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='description',
            field=models.TextField(blank=True, default='pokemon'),
        ),
    ]
