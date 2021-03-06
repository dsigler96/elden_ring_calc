# Generated by Django 4.0.3 on 2022-03-15 23:02

from msilib.schema import Class
from django.db import migrations

#from character_builder you have to import each class that you are going to be using to add a table
from character_builder.models import ClassStartingStats


def populate(apps, schema_editor):
    yeet = ClassStartingStats.objects.get(name="Prophet")
    # Say you make a mistake and need to change a row, follow format below
    #var = ClassStartingStats.objects.get(name='mistaken_row')
    #var.base_lvl = 24
    #var.name = "Vagabond"
    #var.save()
    #From there run python manage.py makemigrations character_builder
    #Then python manage.py migrate
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('character_builder', '0002_alter_classstartingstats_base_lv'),
    ]

    operations = [
        migrations.RunPython(populate)
    ]
