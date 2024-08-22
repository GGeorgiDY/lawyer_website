from django.urls import path
from lawyer_website.news.views import article_list, article_detail

urlpatterns = [
    path('', article_list, name='article_list'),
    path('<int:pk>/', article_detail, name='article_detail'),
]

