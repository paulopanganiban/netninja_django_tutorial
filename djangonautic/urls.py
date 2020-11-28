"""djangonautic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import  views

#static files
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#media files upload the static folders
from django.conf.urls.static import static
from django.conf import settings #we have access sa properties na mediaurls
#from django.confs.urls import url
# 1.11 vs 3.1.3 
urlpatterns = [
    #url(r'^admin/', admin.site.urls) 1.11
    path('admin/', admin.site.urls),
    #path('polls/', include('polls.urls'))
    path('about/', views.about),
    path('', views.homepage),
    path('articles/', include('articles.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)