from django.shortcuts import render
from .models import Article
# Create your views here.

def article_list(request):
    articles = Article.objects.all().order_by('date')
    # pass the articles / convert first to a dictionary
    context = {'articlesOLO' : articles}
    return render(request, 'articles/article_list.html', context)