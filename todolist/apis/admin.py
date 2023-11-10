from django.contrib import admin
from apis.models import *

# Register your models here.

@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    list_display = ('id','detail','complete','create_date')
    readonly_fields = ["create_date"]