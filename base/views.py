from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from .models import Todo


class CustomLoginView(LoginView):
    template_name = "base/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("todos")


class TodoList(ListView):
    model = Todo
    context_object_name = "todos"
    template_name = "base/todos.html"


class TodoDetail(DetailView):
    model = Todo
    context_object_name = "todo"
    template_name = "base/todo_detail.html"


class CreateTodo(CreateView):
    model = Todo
    fields = "__all__"
    success_url = reverse_lazy("todos")
    template_name = "base/create_todo.html"


class UpdateTodo(UpdateView):
    model = Todo
    fields = "__all__"
    success_url = reverse_lazy("todos")
    template_name = "base/create_todo.html"


class DeleteTodo(DeleteView):
    model = Todo
    context_object_name = "todo"
    success_url = reverse_lazy("todos")
    template_name = "base/confirm_delete_todo.html"
