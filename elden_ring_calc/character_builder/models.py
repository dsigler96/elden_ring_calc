from django.db import models

class ClassStartingStats(models.Model):
    name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    base_lv  = models.IntegerField()
    base_vig = models.IntegerField()
    base_mnd = models.IntegerField()
    base_end = models.IntegerField()
    base_str = models.IntegerField()
    base_dex = models.IntegerField()
    base_int = models.IntegerField()
    base_fai = models.IntegerField()
    base_arc = models.IntegerField()
    
    #Copy line above for all stats



# python manage.py makemigrations (file directory) this line updates the database with the changes you made to the code (django side of things)
# python manage.py migrate  this line populates the database (sqlite side of things) - these two functions are sequential

# python manage.py makemigrations --empty character_builder  This code makes a new file in migrations that we can use for whatever -
# In this case it will be to populate the names of classes and levels since that is what we are working on now