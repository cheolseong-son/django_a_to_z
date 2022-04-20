from django.urls import path
from . import views

urlpatterns= [
    path('search/<str:q>/', views.NoticeSearch.as_view()),
    path('create_notice/', views.NoticeCreate.as_view()),
    path('<int:pk>', views.NoticeDetail.as_view()),
    path('', views.NoticeList.as_view()),
]