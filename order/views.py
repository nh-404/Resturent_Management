from django.shortcuts import render
from django.db import transaction
from cart.models import Cart, CarfItem
from django.contrib.auth.decorators import login_required



@login_required(login_url='login')
@transaction.atomic
def place_order(request):
    user = request.user
    cart = Cart.objects.get(user=user, is_active=True)

    # Calculate subtotal
    subtotal = sum(item.food.price * item.quantity for item in cart.items.all())

    order = Order.objects.create(
        user=user,
        subtotal=subtotal,
        vat=0,
        service_charge=0,
        discount=0,
        total=subtotal,  # temporary, can calculate later
        status='pending'
    )

    # Create order items
    for item in cart.items.all():
        Order_food.objects.create(
            order=order,
            foods=item.food,
            quantity=item.quantity,
            price=item.food.price,
            total_price=item.food.price * item.quantity
        )

    # Deactivate cart
    cart.is_active = False
    cart.save()

    context = {
        'order': order,
        'items': order.food.all(),
    }
    return render(request, 'customer/order/order_success.html', context)
