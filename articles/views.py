from django.http.response import Http404, HttpResponse
from django.shortcuts import redirect, render
from .models import Article
from django.http.response import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.


def article_list(request):
    articles = Article.objects.all().order_by('date')
    # pass the articles / convert first to a dictionary
    context = {'articlesOLO': articles}
    return render(request, 'articles/article_list.html', context)


def article_detail(request, slug_id):
    article = Article.objects.get(pk=slug_id)
    context = {'article': article}
    return render(request, 'articles/article_detail.html', context)
    #
    # gagamit tayo ng query
    # try:
    #     detail = Article.objects.get(pk=slug)
    # except Article.DoesNotExist:
    #     raise Http404
    # context = {'detail': detail}
    # return render(request, 'articles/article_detail.html', context)
    # return HttpResponse(slug)


@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', { 'form': form })
