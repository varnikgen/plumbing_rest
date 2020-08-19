from django import template

from shop.models import Category, Product

register = template.Library()


@register.simple_tag()
def get_categories():
    """Вывод всех категорий"""
    return Category.objects.all()


@register.inclusion_tag('shop/tags/last_products.html')
def get_last_products(count=5):
    """Вывод последних поступлений"""
    products = Product.objects.order_by("id")[count+1:]
    return {"last_products": products}
