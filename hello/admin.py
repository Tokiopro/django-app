from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Article # models.py から Article クラスをインポート

admin.site.register(Article) # DjangoAdmin に Article クラスを登録
