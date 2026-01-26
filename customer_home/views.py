from django.shortcuts import render
from menu.models import Offline_menu
from order.models import Order_food



def home(request):

    offline_menus = Offline_menu.objects.all()

    #top_selling_food = (Order_food.objects.values('foods__id', 'foods__food_name').annotate(total_sold=sum('quantity')).order_by('-total_sold')[:5])


    context = {
        'offline_menus' : offline_menus,
        #'top_selling_food':top_selling_food,
    }


    return render(request, 'customer/customer_home.html', context)





def menu(request):

    return render(request, 'customer/menu.html')






def contact(request):

    return render(request, 'customer/contact.html')




def book_table(request):

    return render(request, 'customer/order/book_table.html')