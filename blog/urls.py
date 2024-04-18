from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name= 'index'),
    path('article/<int:article_id>/', views.article , name= 'article'),
    path('article_list/', views.articleList , name= 'article_list'),
    path('about/', views.about , name= 'about'),
    path('help_us/', views.helpUs , name= 'help_us'),
    path('resource/<int:resourse_id>/', views.resource , name= 'resource'),
    path('author/<int:author_id>/', views.author , name= 'author'),
]