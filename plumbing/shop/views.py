from django.db import models
from rest_framework import generics, permissions, viewsets

from .models import Product, Category
from .serializers import (
    ProductListSerializer,
    ProductDetailSerializer,
    ReviewCreateSerializer,
    CreateRatingSerializer,
    CategoryListSerializer)
from .service import get_client_ip


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """Вывод списка товаров или описание конкретного товара"""
    serializer_class = ProductListSerializer

    def get_queryset(self):
        products = Product.objects.filter(available=True).annotate(
            rating_user=models.Count("ratings", filter=models.Q(ratings__ip=get_client_ip(self.request))),
        ).annotate(
            middle_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings'))
        )
        return products

    def get_serializer_class(self):
        if self.action == "list":
            return ProductListSerializer
        elif self.action == "retrieve":
            return ProductDetailSerializer


class ReviewCreateViewSet(viewsets.ModelViewSet):
    """Добавление отзыва к товару"""
    serializer_class = ReviewCreateSerializer


class AddStartRatingViewSet(viewsets.ModelViewSet):
    """Добавление рейтинга товару"""
    serializer_class = CreateRatingSerializer

    def perform_create(self, serializer):
        serializer.save(ip=get_client_ip(self.request))



class CategoryListView(generics.ListAPIView):
    """Вывод списка категорий"""
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class CategoryProductsView(generics.ListAPIView):
    """Вывод товаров категории"""
    serializer_class = CategoryListSerializer

    def get_queryset(self):
        products = Product.objects.filter(available=True, category_id=self.kwargs.get('pk')).annotate(
            rating_user=models.Count("ratings", filter=models.Q(ratings__ip=get_client_ip(self.request))),
        ).annotate(
            middle_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings'))
        )
        return products


# class ProductListView(generics.ListAPIView):
#     """Вывод списка товаров"""
#     serializer_class = ProductListSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get_queryset(self):
#         products = Product.objects.filter(available=True).annotate(
#             rating_user=models.Count("ratings", filter=models.Q(ratings__ip=get_client_ip(self.request))),
#         ).annotate(
#             middle_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings'))
#         )
#         return products
#
#
# class ProductDetailView(generics.RetrieveAPIView):
#     """Вывод карточки товара"""
#     queryset = Product.objects.filter(available=True)
#     serializer_class = ProductDetailSerializer
#
#
# class ReviewCreateView(generics.CreateAPIView):
#     """Добавление отзыва к товару"""
#     serializer_class = ReviewCreateSerializer
#
#
# class AddStartRatingView(generics.CreateAPIView):
#     """Добавление рейтинга товару"""
#     serializer_class = CreateRatingSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(ip=get_client_ip(self.request))
