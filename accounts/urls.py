from django.urls import path
from accounts import views

urlpatterns = [
    path('signUp/', views.signUp, name='signUp'),
    path('login/', views.signIn, name='login'),
    path('logout/', views.signOut, name='logout'),
    path('reset-password/', views.reset_password, name='reset_password'),
    path('reset-password/<uidb64>/<token>/', views.reset_password_confirm, name='reset_password_confirm'),
]
