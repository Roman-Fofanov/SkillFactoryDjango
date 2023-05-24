from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class Post(models.Model):
    CATEGORY_CHOICES = [
        ('Tanks', 'Танки'),
        ('Healers', 'Хилы'),
        ('DD', 'ДД'),
        ('Guildmasters', 'Гилдмастеры'),
        ('Questgivers', 'Квестгиверы'),
        ('Smiths', 'Кузнецы'),
        ('Tanners', 'Кожевники'),
        ('Potionbrewers', 'Зельевары'),
        ('Spellmasters', 'Мастера заклинаний')
    ]

    title = models.CharField(max_length=254)
    body = RichTextField()
    category = models.CharField(max_length=254, choices=CATEGORY_CHOICES,)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])


class Response(models.Model):
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, null=True, choices=[('A', 'Принят'),
                                                                ('D', 'Отклонён')])
