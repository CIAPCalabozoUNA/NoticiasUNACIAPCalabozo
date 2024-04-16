from django.contrib import admin
from .models import Article, ArticleType, Resource

# Register your models here.

admin.site.register(Article)
admin.site.register(ArticleType)
admin.site.register(Resource)
