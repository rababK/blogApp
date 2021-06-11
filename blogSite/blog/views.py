from django.views import generic
from .models import Article

class ArticleList(generic.ListView):
    model = Article
    queryset = Article.objects.all()
    context_object_name = 'Article_list'
    template_name = 'home.html'

class ArticleDetaill(generic.DetailView):
    model = Article
    template_name = 'Article_detail.html'