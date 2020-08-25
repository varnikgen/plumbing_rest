from django.db import models
from rest_framework import generics

from .models import Product
from .serializers import ProductListSerializer, ProductDetailSerializer, ReviewCreateSerializer, CreateRatingSerializer
from .service import get_client_ip


class ProductListView(generics.ListAPIView):
    """Вывод списка товаров"""
    serializer_class = ProductListSerializer

    def get_queryset(self):
        products = Product.objects.filter(available=True).annotate(
            rating_user=models.Count("ratings", filter=models.Q(ratings__ip=get_client_ip(self.request))),
        ).annotate(
            middle_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings'))
        )
        return products


class ProductDetailView(generics.RetrieveAPIView):
    """Вывод карточки товара"""
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductDetailSerializer


class ReviewCreateView(generics.CreateAPIView):
    """Добавление отзыва к товару"""
    serializer_class = ReviewCreateSerializer


class AddStartRatingView(generics.CreateAPIView):
    """Добавление рейтинга товару"""
    serializer_class = CreateRatingSerializer

    def perform_create(self, serializer):
        serializer.save(ip=get_client_ip(self.request))
