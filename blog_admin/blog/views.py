from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, HttpResponseRedirect
from django.views import generic, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin
from .models import Article, Comment
from .forms import CommentForm
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import CommentSerializer
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView
import datetime

# Create your views here.

def index(request):
    text = 'This is my first blog'
    return HttpResponse(text)

class ArticleListView(generic.ListView):
    model = Article

class ArticleDetailView(FormMixin, DetailView):
    template_name = 'blog/article_detail.html'
    model = Article
    form_class = CommentForm

    def get_success_url(self):
        return reverse('article_detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = form = self.form_class()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(ArticleDetailView, self).form_valid(form)

class CommentForm(View):
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def get(self, request, *args, **kwargs):
        submitted = False
        form = self.form_class()
        if 'submitted' in request.GET:
            submitted = True
        return render(request, self.template_name, {'form': form, 'submitted': submitted, 'message': 'This is done'})


def add_comment(request):
    authorname = 'amba' #request.GET.get('authorname', None)
    comment = 'nice article' #request.GET.get('comment', None)
    now = '2020-10-19 12:57:14' #datetime.datetime.now()
    article = Article.objects.get(id=1)

    c = Comment(name=authorname, comment=comment, article=article, date=now )
    c.save()
    return HttpResponseRedirect('/article/1/')

class Comment_API(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    #comment = Comment.objects.values('name','comment','article','date','article__title')
    #print(comment)
    #print(str(comment.query))
