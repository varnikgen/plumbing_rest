from rest_framework import serializers

from .models import Product, Review


class ProductListSerializer(serializers.ModelSerializer):
    """Список товаров"""

    class Meta:
        model = Product
        fields = ("name", "price", "category")


class ReviewCreateSerializer(serializers.ModelSerializer):
    """Добавление отзыва"""

    class Meta:
        model = Review
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    """Вывод отзыва"""

    class Meta:
        model = Review
        fields = ("name", "text", "parent")


class ProductDetailSerializer(serializers.ModelSerializer):
    """Карточка товара"""
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)  # Вывод имени категории вместо id
    reviews = ReviewSerializer(many=True)  # Вывод отзывов

    class Meta:
        model = Product
        exclude = ("available",)
