from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/profile/', views.UserProfile, name='UserProfile'),
    path('accounts/login/', auth_views.LoginView.as_view(next_page=''), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('<int:id>/', views.MakeRequestView, name='makerequest'),
    path('user/', views.ManagerAllocation, name='ManagerSchedule'),
    path('request/pending/all', views.pending_request, name='PendingRequest'),
    path('request/all/view/<int:id>', views.RequestView, name='RequestDetailedView'),
    path('request/approved/all', views.approved_list, name='ApprovedList'),
    
    
]
