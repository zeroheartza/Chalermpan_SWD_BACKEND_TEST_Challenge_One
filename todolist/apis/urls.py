
from django.urls import path
from apis.views import todolistapi

urlpatterns = [

    path("get_todo_list/", todolistapi.GetTodoList.as_view(), name="get_todo_list"),
    path("create_todo_list/", todolistapi.CreateTodoList.as_view(), name="create_todo_list"),
    path("delete_todo_list/", todolistapi.DeleteTodoList.as_view(), name="create_todo_list"),
    path("edit_todo_list/", todolistapi.EditTodoList.as_view(), name="edit_todo_list"),

]
