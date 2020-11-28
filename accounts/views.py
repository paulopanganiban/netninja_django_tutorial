from django.shortcuts import render
from django.http.response import Http404, HttpResponse
# Create your views here.


def signup_view(request):
    # return HttpResponse('test')
    str = "HOLLA"
    context = {'str' : str}
    return render(request, 'accounts/signup_view.html')
