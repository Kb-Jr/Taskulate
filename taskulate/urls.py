from django.urls import path, re_path

from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, TaskReorder
from . import views
from django.views.generic.base import RedirectView
favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)


urlpatterns = [
    re_path(r'^favicon\.ico$', favicon_view),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-reorder/', TaskReorder.as_view(), name='task-reorder'),
]
