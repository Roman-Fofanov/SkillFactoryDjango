from django.urls import path
# Импортируем созданное нами представление
from .views import PostsList, PostDetail, NewsCreate, NewsUpdate, PostDelete, SearchList
from .views import upgrade_me
from .views import IndexView
from django.views.decorators.cache import cache_page

urlpatterns = [
   path('', cache_page(60)(PostsList.as_view()), name='post_list'),
   path('<int:pk>', cache_page(300)(PostDetail.as_view()), name='post_detail'),
   path('create/', NewsCreate.as_view(), name='create_news'),
   path('<int:pk>/edit/', NewsUpdate.as_view(), name='edit_news'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('search/', SearchList.as_view(), name='search_publications'),
   path('upgrade/', upgrade_me, name = 'upgrade'),
]