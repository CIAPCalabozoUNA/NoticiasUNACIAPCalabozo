from django.contrib import admin
from .models import Article, ArticleType, Resource, Image, Author, Comment

# Register your models here.

admin.site.register(Image)
admin.site.register(Article)
admin.site.register(ArticleType)
admin.site.register(Resource)
admin.site.register(Author)
admin.site.register(Comment)
