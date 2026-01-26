from django.shortcuts import render
from menu.models import Offline_menu, Online_menu
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def online_menu(request):

    online_menu = Online_menu.objects.all()



    context = {
        'online_menu' : online_menu,
    }

    return render(request, 'customer/menu/online_menu.html', context)



def offline_menu(request):

    offline_menus = Offline_menu.objects.all()



    context = {
        'offline_menus' : offline_menus,
    }



    return render(request, 'customer/order/offline_order.html',context)
