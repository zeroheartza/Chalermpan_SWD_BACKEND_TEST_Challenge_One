from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from ..serializers import TodolistSerializer,CreateTodolistSerializer,DeleteTodolistSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from apis.models import ToDoList

class GetTodoList(APIView):
 
    @staticmethod
    def get(request, *args, **kwargs):
        queryset = ToDoList.objects.all().order_by('-create_date')
        todolistSerializer = TodolistSerializer(queryset,many=True).data
        return Response(todolistSerializer, status=status.HTTP_200_OK)

class CreateTodoList(APIView):

    @staticmethod
    def post(request, *args, **kwargs):
        """
        test create
        {"detail":"work","complete":true}
        """
        createTodolistSerializer = CreateTodolistSerializer(request.data)
        queryset = ToDoList.objects.create(
        detail = createTodolistSerializer.data['detail'],
        complete = createTodolistSerializer.data['complete']
        )
        
        todolistSerializer = TodolistSerializer(queryset).data
        return Response(todolistSerializer, status=status.HTTP_200_OK)


class DeleteTodoList(APIView):
  
    @staticmethod
    def delete(request, *args, **kwargs):
        todolist_id = request.GET.get('todolist_id', None)
        # deleteTodolistSerializer = DeleteTodolistSerializer(request.data)  
        queryset = ToDoList.objects.get(id=todolist_id)
        queryset.delete()
    
        return Response({"data":"Delete todolist id {} success".format(str(todolist_id))}, status=status.HTTP_200_OK)

class EditTodoList(APIView):
  
    @staticmethod
    def post(request, *args, **kwargs):
        todolist_id = request.GET.get('todolist_id', None)
        rData = request.data
 
        queryset = ToDoList.objects.get(id=todolist_id)
        if('detail' in rData):
            queryset.detail = rData['detail']
        if('complete' in rData):
            queryset.complete = rData['complete']
        queryset.save()
        return Response({"data":"Edit todolist id {} success".format(str(queryset.id))}, status=status.HTTP_200_OK)