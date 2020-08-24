from rest_framework import serializers

from .models import Product, Review, Rating


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


class CreateRatingSerializer(serializers.ModelSerializer):
    """Добавление рейтинга пользователем"""
    class Meta:
        model = Rating
        fields = ("star", "product")

    def create(self, validated_data):
        rating = Rating.objects.update_or_create(
            ip=validated_data.get('ip', None),
            product=validated_data.get('product', None),
            defaults={'star': validated_data.get("star")}
        )
        return rating
