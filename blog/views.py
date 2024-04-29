from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse
from .models import Article, Comment, ArticleType
from .forms import CommentForm
from .utils import get_number_of_pages
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    template = loader.get_template("pages/index.html")
    articles = Article.objects.order_by('-created_at')[:25]

    # pagination

    paginator = Paginator(articles, 25)
    page_obj = paginator.get_page(1)
    
    slides = Article.objects.filter(article_type = 1).order_by('-created_at')[:5]
    context = {
        'current_page': 'index',
        'last_articles':page_obj,
        'slides':slides,
    }
    return HttpResponse(template.render(context, request))


def article(request, article_id, comment_status):
    template = loader.get_template("pages/article.html")
    article = get_object_or_404(Article, pk = article_id)
    comments = article.comment_set.all()
    context = {
        'current_page': 'article_list',
        'article_id':article_id,
        'article': article,
        'comments_length': len(comments),
        'comments_list': comments,
        'comment_status': comment_status,
    }
    return HttpResponse(template.render(context, request))

def articleList(request, page):
    
    # template
    template = loader.get_template("pages/articleList.html")

    # get all the articles

    all_articles =  Article.objects.order_by("-created_at")

    # paginator

    paginator = Paginator(all_articles, 25)
    page_obj = paginator.get_page(page)
    number_of_pages = paginator.num_pages

    context = {
        'current_page': 'article_list',
        'article_page':page_obj,
        'page':page,
        'number_of_pages': get_number_of_pages(number_of_pages),
        'has_next': page < number_of_pages,
        'has_prev': page > 1,
        'next_page': page + 1,
        'prev_page': page - 1
    }

    return HttpResponse(template.render(context, request))

def resourceList(request, page):
     # template
    template = loader.get_template("pages/articleList.html")

    # get all the articles

    all_articles =  Article.objects.order_by("-created_at")

    # paginator

    paginator = Paginator(all_articles, 25)
    page_obj = paginator.get_page(page)
    number_of_pages = paginator.num_pages

    context = {
        'current_page': 'resource_list',
        'article_page':page_obj,
        'page':page,
        'number_of_pages': get_number_of_pages(number_of_pages),
        'has_next': page < number_of_pages,
        'has_prev': page > 1,
        'next_page': page + 1,
        'prev_page': page - 1
    }

    return HttpResponse(template.render(context, request))

def category(request, category, page):
    template = loader.get_template("pages/articleList.html")

    # get all the articles

    all_articles =  Article.objects.order_by("-created_at")

    # paginator

    paginator = Paginator(all_articles, 25)
    page_obj = paginator.get_page(page)
    number_of_pages = paginator.num_pages

    context = {
        'current_page': 'category',
        'article_page':page_obj,
        'page':page,
        'number_of_pages': get_number_of_pages(number_of_pages),
        'has_next': page < number_of_pages,
        'has_prev': page > 1,
        'next_page': page + 1,
        'prev_page': page - 1
    }

    return HttpResponse(template.render(context, request))

def about(request):
    template = loader.get_template("pages/about.html")
    context = {
        'current_page': 'about',
    }
    return HttpResponse(template.render(context, request))

def helpUs(request):
    template = loader.get_template("pages/helpUs.html")
    context = {
         'current_page': 'help_us',
    }
    return HttpResponse(template.render(context, request))

def resource(request, resource_id):
    template = loader.get_template("pages/resource.html")
    context = {
        'current_page': 'resource_list',
        'resource_id': resource_id
    }
    return HttpResponse(template.render(context, request))

def author(request, author_id):
    template = loader.get_template("pages/author.html")
    context = {
        'current_page': 'about',
        'author_id': author_id
    }
    return HttpResponse(template.render(context, request))

def create_comment(request):
    if request.method != 'POST':
        raise Http404("Acceso restringido.") 
    try:
        article_id = request.POST['article']
        article = Article.objects.get(pk=article_id) 
    except Article.DoesNotExist:
        raise Http404("Artículo no encontrado.")

    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)  # Avoid extra save if form is invalid
        comment.article = article  # Assign article to comment
        comment.save()
        return HttpResponseRedirect(f'/article/{article_id}/1/#commentForm')
    else: 
        return HttpResponseRedirect(f'/article/{article_id}/2/#commentForm')
   