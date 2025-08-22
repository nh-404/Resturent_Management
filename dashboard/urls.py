from dashboard import views
from django.urls import path

urlpatterns = [
    
    path('dashboard-home/', views.dashboard_home, name='dashboard_home'),
]