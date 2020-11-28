from django.shortcuts import render
from django.http.response import Http404, HttpResponse

# Django auth 
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def signup_view(request):
    form = UserCreationForm()
    context = {'form' : form}
    return render(request, 'accounts/signup_view.html', context)
