from . import views
from django.urls import path

urlpatterns = [
    path('', views.ArticleList.as_view(), name='ArticleList'),
    path('<slug:slug>/', views.ArticleDetaill.as_view(), name='ArticleDetaill'),
]