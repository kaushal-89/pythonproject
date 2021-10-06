from django.contrib import admin

from .models import Article, Comment

class ArticleAdmin(admin.ModelAdmin):
    fields = ['title', 'author', 'excerpt', 'content', 'publication_date', 'status', 'allow_comment']
    list_display = ('title', 'author', 'excerpt', 'publication_date', 'status', 'allow_comment')

class CommentAdmin(admin.ModelAdmin):
    fields = ['name', 'comment', 'article', 'date']
    list_display = ('name', 'comment', 'article', 'date')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
