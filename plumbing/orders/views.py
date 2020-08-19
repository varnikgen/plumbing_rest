from django.shortcuts import render

from cart.cart import Cart
from orders.forms import OrderCreateForm
from orders.models import OrderItem


def order_create(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'],
                                         quantity=item['quantity'])
                # очистка корзины
                cart.clear()
                return render(request, 'orders/order_created.html', {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/order_create.html', {'cart': cart, 'form': form})
