from django.urls import path
from . import views

urlpatterns = [
 #as_view() はクラスベースのビューをビュー関数化するメソッドです。
 path('', views.IndexView.as_view(), name='index'),
]
