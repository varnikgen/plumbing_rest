from rest_framework import serializers

from .models import Product


class ProductListSerializer(serializers.ModelSerializer):
    """Список товаров"""

    class Meta:
        model = Product
        fields = ("name", "price", "category")


class ProductDetailSerializer(serializers.ModelSerializer):
    """Карточка товара"""
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)  # Вывод имени категории вместо id

    class Meta:
        model = Product
        exclude = ("available",)
