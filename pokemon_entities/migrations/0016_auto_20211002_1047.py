# Generated by Django 3.1.7 on 2021-10-02 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0015_auto_20211002_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='description',
            field=models.TextField(default='pokemon'),
        ),
    ]
