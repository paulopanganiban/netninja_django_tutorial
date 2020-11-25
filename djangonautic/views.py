from django.http.response import HttpResponse

def homepage(request):
    return HttpResponse('home page')

def about(request):
    # request has the information about the request made by the user
    return HttpResponse('about')