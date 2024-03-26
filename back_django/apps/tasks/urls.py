from django.urls import path

from . import views

app_name = 'tasks'
urlpatterns = [
    path('api/', views.api, name = 'api'),
]