from menu import views
from django.urls import path

urlpatterns = [
    

    path('online-order/', views.online_menu, name='online_order'),
    path('offline-order/', views.offline_menu, name='offline_order'),
    
    #path('online_menu/', views.online_menu, name='online_menu'),
    # path('online-order/', views.online_order, name='online_order'),
    # path('offline-order/', views.offline_order, name='offline_order'),
    # path('book-table/', views.book_table, name='book_table'),

]