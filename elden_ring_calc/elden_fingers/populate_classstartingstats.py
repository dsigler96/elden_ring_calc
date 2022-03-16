import sys
import os, django
from django.conf import settings
os.environ["DJANGO_SETTINGS_MODULE"] = "elden_fingers.settings"
django.setup()
from character_builder.models import ClassStartingStats

#sys.path.append("..")

hero_dict = {
    "name" : "Hero",
    "base_lv" : 7,
    "base_vig" : 14,
    "base_mnd" : 9,
    "base_end" : 12,
    "base_str" : 16,
    "base_dex" : 9,
    "base_int" : 7,
    "base_fai" : 8,
    "base_arc" : 11,
}

bandit_dict = {
    "name" : "Bandit",
    "base_lv" : 5,
    "base_vig" : 10,
    "base_mnd" : 11,
    "base_end" : 10,
    "base_str" : 9,
    "base_dex" : 13,
    "base_int" : 9,
    "base_fai" : 8,
    "base_arc" : 14
}

astrologer_dict = {
    "name" : "Astrologer",
    "base_lv" : 6,
    "base_vig" : 9,
    "base_mnd" : 15,
    "base_end" : 9,
    "base_str" : 8,
    "base_dex" : 12,
    "base_int" : 16,
    "base_fai" : 7,
    "base_arc" : 9
}

warrior_dict = {
    "name" : "Warrior",
    "base_lv" : 8,
    "base_vig" : 11,
    "base_mnd" : 12,
    "base_end" : 11,
    "base_str" : 10,
    "base_dex" : 16,
    "base_int" : 10,
    "base_fai" : 8,
    "base_arc" : 9
}

prisoner_dict = {
    "name" : "Prisoner",
    "base_lv" : 9,
    "base_vig" : 11,
    "base_mnd" : 12,
    "base_end" : 11,
    "base_str" : 11,
    "base_dex" : 14,
    "base_int" : 14,
    "base_fai" : 6,
    "base_arc" : 9
}

confessor_dict = {
    "name" : "Confessor",
    "base_lv" : 10,
    "base_vig" : 10,
    "base_mnd" : 13,
    "base_end" : 10,
    "base_str" : 12,
    "base_dex" : 12,
    "base_int" : 9,
    "base_fai" : 14,
    "base_arc" : 9
}

wretch_dict = {
    "name" : "Wretch",
    "base_lv" : 1,
    "base_vig" : 10,
    "base_mnd" : 10,
    "base_end" : 10,
    "base_str" : 10,
    "base_dex" : 10,
    "base_int" : 10,
    "base_fai" : 10,
    "base_arc" : 10
}

vagabond_dict = {
    "name" : "Vagabond",
    "base_lv" : 9,
    "base_vig" : 15,
    "base_mnd" : 10,
    "base_end" : 11,
    "base_str" : 14,
    "base_dex" : 13,
    "base_int" : 9,
    "base_fai" : 9,
    "base_arc" : 7
}

prophet_dict = {
    "name" : "Prophet",
    "base_lv" : 7,
    "base_vig" : 10,
    "base_mnd" : 14,
    "base_end" : 8,
    "base_str" : 11,
    "base_dex" : 10,
    "base_int" : 7,
    "base_fai" : 16,
    "base_arc" : 10
}

samurai_dict = {
    "name" : "Samurai",
    "base_lv" : 9,
    "base_vig" : 12,
    "base_mnd" : 11,
    "base_end" : 13,
    "base_str" : 12,
    "base_dex" : 15,
    "base_int" : 9,
    "base_fai" : 8,
    "base_arc" : 8
}

lyst = [hero_dict, bandit_dict, astrologer_dict, warrior_dict, 
        prisoner_dict, confessor_dict, wretch_dict, vagabond_dict, 
        prophet_dict, samurai_dict]

def populate():



    # code below used for populating base stat list
    # for item in lyst:
    #     entry = ClassStartingStats(name = "")
    #     for key, value in item.items():
    #         setattr(entry, key, value)
    #     entry.save()

    # Say you make a mistake and need to change a row, follow format below
    #var = ClassStartingStats.objects.get(name='mistaken_row')
    #var.base_lvl = 24
    #var.name = "Vagabond"
    #var.save()
    #From there run python manage.py makemigrations character_builder
    #Then python manage.py migrate
    pass

populate()