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
    
    
    
    path('request/cto/pending/all', views.cto_pending_list, name='CTOPendingRequest'),
        #--------------------------------CT0--------------------------------------------#
    path('request/cto/pending/all', views.cto_pending_list, name='cto_pending_requestlist'),
    path('request/cto/approved/all', views.cto_approved_list, name='cto_approved_requestlist'),
    path('request/cto/unapprove/<int:id>/',views.cto_approve_request,name='cto_approve'),
    path('request/cto/all/view/<int:id>', views.cto_request_view, name='cto_all_request_view'),
    path('request/cto/reject/<int:id>', views.cto_reject_request, name='cto_reject'),
    path('request/cto/all/view/<int:id>', views.cto_request_view, name='cto_all_request_view'),

    
    #--------------------------------CTO--------------------------------------------#
    path('request/all/view/<int:id>', views.RequestView, name='all_request_view'),
    path('request/reject/<int:id>', views.reject_request, name='reject'),
    path('request/approve/<int:id>', views.approve_request, name='approve'),
    path('accounts/login/', auth_views.LoginView.as_view( next_page='PendingRequest'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    
]
