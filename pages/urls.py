from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutUsPageView.as_view(), name='about'),
]
