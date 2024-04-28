from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Article

# Create your views here.
def index(request):
    template = loader.get_template("pages/index.html")
    context = {}
    return HttpResponse(template.render(context, request))

def article(request, article_id):
    template = loader.get_template("pages/article.html")
    article = Article.objects.get(pk=article_id)
    comments = article.comment_set.all()
    context = {
        'article_id':article_id,
        'article': article,
        'comments_length': len(comments),
        'comments_list': comments
    }
    return HttpResponse(template.render(context, request))

def articleList(request):
    template = loader.get_template("pages/articleList.html")
    context = {}
    return HttpResponse(template.render(context, request))

def about(request):
    template = loader.get_template("pages/about.html")
    context = {}
    return HttpResponse(template.render(context, request))

def helpUs(request):
    template = loader.get_template("pages/helpUs.html")
    context = {}
    return HttpResponse(template.render(context, request))

def resource(request, resource_id):
    template = loader.get_template("pages/resource.html")
    context = {
        'resource_id': resource_id
    }
    return HttpResponse(template.render(context, request))

def author(request, author_id):
    template = loader.get_template("pages/author.html")
    context = {
        'author_id': author_id
    }
    return HttpResponse(template.render(context, request))