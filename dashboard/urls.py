from dashboard import views
from django.urls import path

urlpatterns = [
    
    path('dashboard-home/', views.dashboard_home, name='dashboard_home'),
    path('dashboard-menu/', views.dashboard_offline_menu, name='dashboard_offline_menu'),
    #path('dashboard-home/', views.dashboard_home, name='dashboard_home'),
]