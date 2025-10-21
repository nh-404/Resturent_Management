from django.shortcuts import render
from menu.models import Offline_menu



def online_menu(request):

    return render(request, 'customer/order/online_order.html')



def offline_menu(request):

    offline_menus = Offline_menu.objects.all()



    context = {
        'offline_menus' : offline_menus,
    }



    return render(request, 'customer/order/offline_order.html',context)
