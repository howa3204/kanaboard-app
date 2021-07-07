from django.shortcuts import render

from .models import Article

# Create your views here.

# Display blog.
def blog(request):
    context = {'blog':blog}
    return render(request, 'blog/blog.html', context)

def article(request, article_id):
    article = Article.objects.get(id=article_id)
    context = {'article':article}
    return render(request, 'blog/article.html', context)
