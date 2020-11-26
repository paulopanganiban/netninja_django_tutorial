from django.contrib import admin
from .models import Article
# it means get the .models file in the current directory
# Register your models here.

admin.site.register(Article)