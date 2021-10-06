from django.urls import path
from .views import index, ArticleListView, ArticleDetailView, add_comment, Comment_API, CommentForm

urlpatterns =[
    #path('', index, name='index'),
    path('', ArticleListView.as_view(), name='article'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_details'),
    path('add_comment/', add_comment, name='add_comment'),
    path('comment_api', Comment_API.as_view(), name='comment API'),
    path('comment_form/', CommentForm.as_view(), name='comment form')
]