from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.serializers import *
from .models import ToDoList

class TodolistSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ('id', 'detail', 'complete','create_date')

class CreateTodolistSerializer(serializers.Serializer):
    detail = CharField(allow_null=True,allow_blank=True)
    complete = BooleanField(default=False)

class DeleteTodolistSerializer(serializers.Serializer):

    todolist_id = IntegerField(allow_null=False)

