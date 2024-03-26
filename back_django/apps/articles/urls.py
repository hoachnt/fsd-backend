from django.urls import path

from . import views


app_name = 'articles'
urlpatterns = [
    path('api/', views.api, name = 'api'),
    path('comment/api/', views.comment_api, name = 'comment_api'),
    path('', views.index, name = 'index'),
    path('<int:article_id>/', views.detail, name = 'detail'),
    path('<int:article_id>/create_comment', views.create_comment, name = 'create_comment')
]