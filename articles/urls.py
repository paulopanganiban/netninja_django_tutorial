from django.urls import path, include
from . import  views

app_name = 'articles'
# bakit importante tong namespace? para hindi matanga si template.
# para pag nag call ng url, articles:detail
# so parang sa html, app_name:name / articles:detail
urlpatterns = [
    path('', views.article_list, name='list'),
                                # {% url 'list' %}
    path('<slug:slug>', views.article_detail, name='detail'),
    # '<slug: is the TYPE of the PASSED parameter
    # <slug ay yung pinasa ng user
    # :slug> name ng parameter na gagamitin sa url na pwedeng articles/detail/asdasdasd --> asdasd iqquery natin sa views.py

    # para saan yung name? para magets ng HTML template! fucking cool.
]