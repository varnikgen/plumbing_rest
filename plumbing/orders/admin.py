from django.contrib import admin

from orders.models import OrderItem, Order


class OrderItemInline(admin.TabularInline):
    """Содержание заказа"""
    model = OrderItem
    raw_id_fields = ['product']
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Заказы в административной панели"""
    list_display = ["id", "first_name", "middle_name", "last_name", "email", "phone", "paid", "created", "updated"]
    list_filter = ["paid", "created", "updated"]
    inlines = [OrderItemInline]
