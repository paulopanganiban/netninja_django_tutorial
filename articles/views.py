from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from .models import Article
from django.http.response import HttpResponse, Http404
# Create your views here.


def article_list(request):
    articles = Article.objects.all().order_by('date')
    # pass the articles / convert first to a dictionary
    context = {'articlesOLO': articles}
    return render(request, 'articles/article_list.html', context)


def article_detail(request, slug):
    # 
    # gagamit tayo ng query
    # try:
    #     detail = Article.objects.get(pk=slug)
    # except Article.DoesNotExist:
    #     raise Http404
    # context = {'detail': detail}
    # return render(request, 'articles/article_detail.html', context)
    return HttpResponse(slug)
