# Generated by Django 4.0.3 on 2022-03-15 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character_builder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classstartingstats',
            name='base_lv',
            field=models.IntegerField(),
        ),
    ]
