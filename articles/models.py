from django.db import models
from django.db.models.fields import SlugField

# Create your models here.
# class Article(models.Model): // table name: Article, columns = yung variables 
# https://docs.djangoproject.com/en/3.1/ref/models/fields/#model-field-types
class Article(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True) # auto add time 
    # add in thumbnail
    thumbnail = models.ImageField(default='default.png', blank=True)
    # add in author later

    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.body[:50] + "..." # says 0-50 characters + concatenation ...