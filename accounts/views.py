from django.shortcuts import render, redirect
from django.http.response import Http404, HttpResponse

# Django auth
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def signup_view(request):
    if request.method == "POST":
        # take the data and validate
        # create an instance and access the request.POST's data
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # if true
            form.save()  # save that data to the database @_@ wowowowowow!
            # log the user in
            # app_name='articles' url name='list'
            return redirect('articles:list')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/signup_view.html', context)
