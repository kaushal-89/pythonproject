from rest_framework import serializers
from .models import Comment, Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title',)
class CommentSerializer(serializers.ModelSerializer):
    article = ArticleSerializer('article')
    #article = article.title
    class Meta:
        model = Comment
        fields = ('id', 'article', 'name', 'comment', 'date')