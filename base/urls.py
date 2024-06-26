from django.urls import path
from .views import TodoList, TodoDetail, CreateTodo, UpdateTodo, DeleteTodo, CustomLoginView, CreateUser

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("signup/", CreateUser.as_view(), name="signup"),
    path("", TodoList.as_view(), name="todos"),
    path("todo/<uuid:pk>/", TodoDetail.as_view(), name="todo"),
    path("create-todo/", CreateTodo.as_view(), name="create-todo"),
    path("update-todo/<uuid:pk>/", UpdateTodo.as_view(), name="update-todo"),
    path("delete-todo/<uuid:pk>/", DeleteTodo.as_view(), name="delete-todo"),
]