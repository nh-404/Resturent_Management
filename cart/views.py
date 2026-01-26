from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import User
from menu.models import Online_menu
from cart.models import Cart, CarfItem



@login_required(login_url='login')
def add_to_cart(request, item_id):
    food = get_object_or_404(Online_menu, id=item_id)

    cart, _ = Cart.objects.get_or_create(
        user=request.user,
        is_active=True
    )

    item, created = CarfItem.objects.get_or_create(
        cart=cart,
        food=food
    )

    if not created:
        item.quantity += 1
        item.save()

    return redirect('cart_detail')



@login_required(login_url='login')
def cart_detail(request):
    
    cart = Cart.objects.filter(
        user=request.user,
        is_active=True
    ).first()

    return render(request, 'cart/cart_detail.html', {'cart': cart})



@login_required(login_url='login')
def cart_increment(request, item_id):
    item = get_object_or_404(CarfItem, id=item_id)
    item.quantity += 1
    item.save()
    return redirect('cart_detail')



@login_required(login_url='login')
def cart_decrement(request, item_id):
    item = get_object_or_404(CarfItem, id=item_id)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()
    return redirect('cart_detail')



@login_required(login_url='login')
def cart_remove(request, item_id):
    item = get_object_or_404(CarfItem, id=item_id)
    item.delete()
    return redirect('cart_detail')