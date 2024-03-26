from django.urls import path

from . import views

app_name = 'tasks'
urlpatterns = [
    path('api/', views.api, name = 'api'),
    path('api/<int:task_id>/', views.task_by_id, name = 'task_by_id'),
]