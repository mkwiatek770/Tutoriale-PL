from django.http import HttpResponse
from django.shortcuts import render
from my_app.models import Article


def home_view(request):
    return HttpResponse("<h1>Hello World!</h1>")


def articles(request):
    articles = Article.objects.all()
    return render(request, "articles.html", {
        "articles": articles
    })
