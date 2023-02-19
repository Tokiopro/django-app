# from django.shortcuts import render
# from django.http import HttpResponse
from django.views import generic
from .models import Article

# Create your views here.
# def index(request):関数ベース
#     # articles = Article.objects.all()
#     articles = Article.objects.filter(content__icontains='h')
#     context = {
#         'articles': articles,
#     }
#     #templateエンジンを介して下記のファイルを返す。
#     return render (request, 'hello/index.html', context)
#クラスビュー（汎用ビュー）
class IndexView(generic.ListView):
    model=Article
    template_name='hello/index.html'
