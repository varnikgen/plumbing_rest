from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.views.generic.base import View

from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm


class CartAddView(View):
    """Добавление товара в корзину"""
    def post(self, request, pk):
        cart = Cart(request)
        product = Product.objects.get(id=pk)
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
        return redirect('cart:cart_detail')


class CartRemoveView(View):
    def get(self, request, pk):
        """Удаление товара из корзины"""
        cart = Cart(request)
        product = Product.objects.get(id=pk)
        cart.remove(product)
        return redirect('cart:cart_detail')


class CartDetailView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'cart/cart_detail.html', {'cart': cart})
