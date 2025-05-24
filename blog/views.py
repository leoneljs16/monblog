from django.shortcuts import render
from .models import Article

def accueil(request):
    articles = Article.objects.all().order_by('-date_publication')
    return render(request, 'blog/accueil.html', {'articles': articles})
