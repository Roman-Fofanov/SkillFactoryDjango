from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import News


class NewsList(ListView):
    model = News
    ordering = 'datetime'
    template_name = 'news.html'
    context_object_name = 'news'

class NewsDetail(DetailView):
    model = News
    template_name = 'new.html'
    context_object_name = 'new'