from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import messages
from my_app.models import Article


def home_view(request):
    return render(request, "home.html")

def articles(request):
    articles = Article.objects.all().order_by("-publised_date")
    return render(request, "articles.html", {
        "articles": articles
    })


def article_detail(request, id):
    article = get_object_or_404(Article, pk=id)
    return render(request, "article_detail.html", {
        "article": article
    })


class ArticleCreate(View):

    def get(self, request):
        users = User.objects.all()
        return render(request, "article_create.html", {"users": users})

    def post(self, request):
        title = request.POST.get("title")
        description = request.POST.get("description")
        author = request.POST.get("author")
        author_object = User.objects.get(username=author)

        try:
            article = Article.objects.create(
                title=title,
                description=description,
                author=author_object,
            )
            messages.success(request, "Article with title {} has been created!".format(title))
        except Exception as err:
            messages.success(request, "There was an error: {}".format(err))
        
        return redirect("articles")


class ArticleUpdate(View):

    def get(self, request, id):
        article = get_object_or_404(Article, id=id)
        return render(request, "article_update.html", {"article": article})
    
    def post(self, request, id):
        article = get_object_or_404(Article, id=id)

        new_title = request.POST.get("title")
        description = request.POST.get("description")
