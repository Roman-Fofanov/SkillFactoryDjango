from datetime import datetime
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, UpdateView, DeleteView, CreateView
)
from .models import News
from .filters import NewsFilter
from .forms import NewsForm

class NewsList(ListView):
    model = News
    ordering = 'datetime'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10


    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class NewsDetail(DetailView):
    model = News
    template_name = 'new.html'
    context_object_name = 'new'

class NewsCreate(CreateView):
    form_class = NewsForm
    model = News
    template_name = 'news_edit.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.article_or_news = 'NE'
        return super().form_valid(form)

class NewsUpdate(UpdateView):
    form_class = NewsForm
    model = News
    template_name = 'news_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        if post.post_type == 'AR':
            return HttpResponse('Такой новости не существует')
        post.save()
        return super().form_valid(form)

class NewsDelete(DeleteView):
    model = News
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')

class SearchList(ListView):
    model = News
    template_name = 'search_page.html'
    context_object_name = 'news'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['time_now'] = datetime.utcnow()
        return context

class ArticlesCreate(CreateView):
    form_class = NewsForm
    model = News
    template_name = 'articles_create.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.article_or_news = 'AR'
        return super().form_valid(form)