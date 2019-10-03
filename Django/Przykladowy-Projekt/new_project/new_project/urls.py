from django.contrib import admin
from django.urls import path

from my_app import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home_view, name="home"),
    path("articles/", views.articles, name="articles"),
    path("articles/<int:id>/", views.article_detail, name="article_detail"),
    path("create-article/", views.ArticleCreate.as_view(), name="article_create"),
]
