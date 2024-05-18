from django.urls import path
from .views import TaskList, Task

urlpatterns = [
    path('', TaskList.as_view(), name="todos"),
    path('todo/<uuid:pk>/', Task.as_view(), name="todo")
]