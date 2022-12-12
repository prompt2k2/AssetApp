from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/profile/', views.UserProfile, name='UserProfile'),
    path('accounts/login/', auth_views.LoginView.as_view(next_page=''), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
