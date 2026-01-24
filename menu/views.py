from django.shortcuts import render
from menu.models import Offline_menu, Online_menu



def online_menu(request):

    online_menu = Online_menu.objects.all()



    context = {
        'online_menu' : online_menu,
    }

    return render(request, 'customer/order/online_order.html', context)



def offline_menu(request):

    offline_menus = Offline_menu.objects.all()



    context = {
        'offline_menus' : offline_menus,
    }



    return render(request, 'customer/order/offline_order.html',context)
