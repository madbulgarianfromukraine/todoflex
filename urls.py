from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name= 'index'),
    path('add', views.addTodoItem, name = 'add'),
    path('completed/<todo_id>', views.completedTodo, name = 'completed'),
    path('deletecompleted/<todo_id>', views.deleteCompleted, name = 'deletecompleted'),
    path('deleteall/<todo_id>', views.deleteAll, name = 'deleteall'),
    path('completed/<todo_id>', views.completedTodo, name = 'completedTodo')

]