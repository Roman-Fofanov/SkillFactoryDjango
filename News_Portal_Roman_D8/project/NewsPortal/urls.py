from django.urls import path
from .views import (
    NewsList, NewsDetail, NewsCreate, NewsDelete, NewsUpdate, SearchList, ArticlesCreate
)

urlpatterns = [
    path('', NewsList.as_view(), name='news_list'),
    path('<int:pk>', NewsDetail.as_view(), name='news_detail'),
    path('create/', NewsCreate.as_view(), name='news_create'),
    path('<int:pk>/edit/', NewsUpdate.as_view(), name='news_update'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('search/', SearchList.as_view(), name='search_publications'),
    path('articles/create/', ArticlesCreate.as_view(), name='articles_create'),
]
