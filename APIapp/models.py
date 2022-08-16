from django.db import models

# Create your models here.
class Drink(models.Model):
    name = models.CharField(max_length= 100)
    description = models.TextField(max_length= 100)


    def __str__(self):
        return "%s %s" %(self.name, self.description)