# core/urls.py

from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.home, name='index'),
    path('profile/', views.profile, name='profile'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('news/<int:pk>/like/', views.toggle_like, name='toggle_like'),
    path('tea_gardens/', views.tea_gardens, name='tea_gardens'),  # Tea Gardens page
    path('tea_history/', views.tea_history, name='tea_history'),  # Tea History page
    path('tinymce/', include('tinymce.urls')),
    path('tea-category/', views.tea_category, name='tea_category'),
    path('tea-category/<int:pk>/', views.tea_detail, name='tea_detail'),
    path('tea-history/<int:pk>/', views.tea_history_detail, name='tea_history_detail'),
    path('tea-gardens/<int:pk>/', views.tea_garden_detail, name='tea_garden_detail'),
]