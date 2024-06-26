from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Todo


class CustomLoginView(LoginView):
    template_name = "base/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("todos")
    

class CreateUser(FormView):
    template_name = "base/sign_up.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("todos")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(CreateUser, self).form_valid(form)
    
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("todos")
        return super(CreateUser, self).get(*args, **kwargs)


class TodoList(LoginRequiredMixin, ListView):
    model = Todo
    context_object_name = "todos"
    template_name = "base/todos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todos"] = context["todos"].filter(user=self.request.user)
        context["count"] = context["todos"].filter(completed=False).count()

        search_input = self.request.GET.get("search-area") or ""
        if search_input:
            context["todos"] = context["todos"].filter(Q(title__icontains=search_input) | Q(description__icontains=search_input))
        context["search_input"] = search_input
        return context

class TodoDetail(LoginRequiredMixin, DetailView):
    model = Todo
    context_object_name = "todo"
    template_name = "base/todo_detail.html"


class CreateTodo(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ["title", "description", "completed"]
    success_url = reverse_lazy("todos")
    template_name = "base/create_todo.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTodo, self).form_valid(form)


class UpdateTodo(LoginRequiredMixin, UpdateView):
    model = Todo
    fields = ["title", "description", "completed"]
    success_url = reverse_lazy("todos")
    template_name = "base/create_todo.html"


class DeleteTodo(LoginRequiredMixin, DeleteView):
    model = Todo
    context_object_name = "todo"
    success_url = reverse_lazy("todos")
    template_name = "base/confirm_delete_todo.html"
