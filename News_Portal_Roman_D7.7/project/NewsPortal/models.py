from django.db import models  # импорт
from django.contrib.auth.models import User
from django.db.models import Sum, DateTimeField
from django.core.validators import MinValueValidator
from django import forms
from django.urls import reverse


class Author(models.Model):
    user_author = models.OneToOneField(User, on_delete=models.CASCADE)
    user_rating = models.FloatField(default=0)

    def update_rating(self):
        rating_posts_author = Post.objects.filter(author_post_id=self.pk).aggregate(rating_news=Sum('rating_news'))[
            'rating_news']
        rating_comments_author = \
            Comment.objects.filter(user_comment_id=self.user_author).aggregate(rating_comment=Sum('rating_comment'))[
                'rating_comment']
        rating_comments_posts = \
            Comment.objects.filter(post_comment__author_post=self.user_author).aggregate(
                rating_comment=Sum('rating_comment'))[
                'rating_comment']
        self.user_rating = rating_posts_author * 3 + rating_comments_author + rating_comments_posts
        self.save()

class Category(models.Model):

    science = 'SC'
    politics = 'PO'
    games = 'GA'
    sport = 'SP'

    CATEGORYS = [
        (science, 'Наука'),
        (politics, 'Политика'),
        (games, 'Игры'),
        (sport, 'Спорт')
    ]
    category_new = models.CharField(max_length=2, choices=CATEGORYS, unique=True)

class Post(models.Model):
    news = 'NE'
    article = 'AR'
    FIELD = [
        (news, 'Новость'),
        (article, 'Статья')
    ]

    author_post = models.ForeignKey(Author, on_delete=models.CASCADE)
    article_or_news = models.CharField(max_length=2, choices=FIELD)
    creation_datetime = models.DateTimeField(auto_now_add = True)
    header = models.CharField(max_length=64, default="Текст заголовка")
    article_text = models.TextField()
    rating_news = models.IntegerField(default=0)
    post_category = models.ManyToManyField(Category, through='PostCategory')

    def like_post(self):
        self.rating_news += 1
        self.save()

    def dislike_post(self):
        self.rating_news -= 1
        self.save()

    def preview(self):
        return self.article_text[0:124] + '...'

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    text_comment = models.TextField()
    data_time_comment = models.DateTimeField(auto_now_add=True)
    rating_comment = models.IntegerField(default=0)
    post_comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_comment = models.ForeignKey(User, on_delete=models.CASCADE)

    def like_comment(self):
        self.rating_comment += 1
        self.save()

    def dislike_comment(self):
        self.rating_comment -= 1
        self.save()

class News(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=1)
    datetime = models.DateTimeField(auto_now_add = True)
    category = models.ForeignKey(
        to='NewsCategory',
        on_delete=models.CASCADE,
        related_name='news',
    )

    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])

class NewsCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()