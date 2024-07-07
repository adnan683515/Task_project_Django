from django.db import models

# Create your models here.

class Task_cetagory(models.Model):
    cetagory_name = models.CharField(max_length=100)
    
    
    
    def __str__(self):
        return self.cetagory_name
    