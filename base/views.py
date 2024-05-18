from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Todo

class TaskList(ListView):
    model = Todo
    context_object_name = "todos"
    template_name = "base/todos.html"


class Task(DetailView):
    model = Todo
    context_object_name = "todo"
    template_name = "base/todo.html"