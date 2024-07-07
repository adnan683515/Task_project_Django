from django.db import models
from cetagory_app.models import Task_cetagory
# Create your models here.
class task(models.Model):
    Title = models.CharField(max_length=50)
    Description = models.TextField()
    is_completed = models.BooleanField()
    Task_Assign_Date = models.DateField()
    cetagory = models.ManyToManyField(Task_cetagory)
    
    def __str__(self):
        return self.Title
    