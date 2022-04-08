from django.urls import path
from . import views # 현재 폴더에 있는 views.py를 사용할 수 있게 가져오라는 것

# FBV (function based view) : 함수에 기반을 둔 방법
# CBV (class based view) : 장고가 제공하는 클래스를 활용해 구현하는 방법

urlpatterns = [
    path('', views.index),
]