from customer_home import views
from django.urls import path

urlpatterns = [
    
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('contact/', views.contact, name='contact'),
    path('book-table/', views.book_table, name='book_table'),

]