from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #templateエンジンを介して下記のファイルを返す。
    return render (request, 'hello/index.html')
