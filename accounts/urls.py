from django.urls import path
from accounts import views

urlpatterns = [

    path('profile/', views.user_profile, name='profile'),
    path('edit-profile/<int:id>/', views.edit_profile, name='edit_profile'),

    path('signUp/', views.signUp, name='signUp'),
    path('login/', views.signIn, name='login'),
    path('logout/', views.signOut, name='logout'),

    path('change-password/', views.change_password, name='change_password'),
    path('verify-otp/', views.send_otp, name='send_otp'),

    path('reset-password/', views.reset_password, name='reset_password'),
    path('reset-password/<uidb64>/<token>/', views.reset_password_confirm, name='reset_password_confirm'),
]
