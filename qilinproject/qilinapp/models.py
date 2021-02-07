from django.db import models

# Create your models here.
class Restaurant(models.Model):

   foodCategory = models.CharField(max_length = 50)
   foodItems = models.CharField(max_length = 50)
   foodAttribute = models.CharField(max_length = 50)
   price = models.IntegerField(default=0)

   class Meta:
      db_table = "restaurant"