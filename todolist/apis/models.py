from django.db import models

# Create your models here.

class ToDoList(models.Model):
    detail = models.CharField(max_length=300,null=True,blank=True)
    complete = models.BooleanField(default=False)
    create_date = models.DateTimeField(null=True,blank=True,auto_now_add=True)
