from django.shortcuts import render
from menu.models import Offline_menu

def dashboard_home(request):

    return render(request, 'dashboard/dasboard_home.html')



def dashboard_offline_menu(request):

    total_dishes = Offline_menu.objects.count()
    offline_menus = Offline_menu.objects.all()



    context = {
        'offline_menus' : offline_menus,
        'total_dishes' : total_dishes,
        
    }
    

    return render(request, 'dashboard/dashboard_menu.html', context)