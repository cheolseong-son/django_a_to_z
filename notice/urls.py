from django.urls import path
from . import views

urlpatterns= [
    path('<int:pk>', views.notice_page),
    path('', views.notice),
]