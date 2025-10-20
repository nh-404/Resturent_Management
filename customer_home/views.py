from django.shortcuts import render

def home(request):

    return render(request, 'customer/customer_home.html')





def menu(request):

    return render(request, 'customer/menu.html')






def contact(request):

    return render(request, 'customer/contact.html')





def online_order(request):

    return render(request, 'customer/order/online_order.html')



def offline_order(request):

    return render(request, 'customer/order/offline_order.html')



def book_table(request):

    return render(request, 'customer/order/book_table.html')