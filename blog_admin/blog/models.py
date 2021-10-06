from django.db import models
from django.urls import reverse, reverse_lazy


# Create your models here.


class Article(models.Model):
    STATUS_CHOICES = [
        ('1', 'Active'),
        ('0', 'Inactive'),
    ]
    ALLOW_COMMENT_CHOICES = [
        ('1', 'Yes'),
        ('0', 'No'),
    ]
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=150)
    excerpt = models.TextField(blank=True)
    content = models.TextField(blank=True)
    publication_date = models.DateTimeField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='1')
    allow_comment = models.CharField(max_length=1, choices= ALLOW_COMMENT_CHOICES, default='1')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('article_details', args=[str(self.id)])


class Comment(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField(blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return self.name