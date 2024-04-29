from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name= 'index'),
    path('article/<int:article_id>/<int:comment_status>/', views.article , name= 'article'),
    path('article_list/<int:page>/', views.articleList , name= 'article_list'),
    path('resource_list/<int:page>/', views.resourceList , name= 'resource_list'),
    path('category/<int:category>/<int:page>/', views.category, name= 'category'),
    path('about/', views.about , name= 'about'),
    path('help_us/', views.helpUs , name= 'help_us'),
    path('resource/<int:resourse_id>/', views.resource , name= 'resource'),
    path('author/<int:author_id>/', views.author , name= 'author'),
    path('create_comment/', views.create_comment, name = 'create_comment')
]