from django import template

register = template.Library()

@register.filter
def cart_total(cart):
    return sum(item.total_price for item in cart.items.all())
