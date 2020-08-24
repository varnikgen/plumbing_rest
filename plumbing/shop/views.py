from django.db import models
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .models import Product
from .serializers import ProductListSerializer, ProductDetailSerializer, ReviewCreateSerializer, CreateRatingSerializer
from .service import get_client_ip


class ProductListView(APIView):
    """Вывод списка товаров"""
    def get(self, request):
        products = Product.objects.filter(available=True).annotate(
            rating_user=models.Count("ratings", filter=models.Q(ratings__ip=get_client_ip(request))),
        ).annotate(
            middle_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings'))
        )
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetailView(APIView):
    """Вывод карточки товара"""
    def get(self, request, pk):
        product = Product.objects.get(id=pk, available=True)
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)


class ReviewCreateView(APIView):
    """Добавление отзыва к товару"""
    def post(self, request):
        review = ReviewCreateSerializer(data=request.data)
        if review.is_valid():
            review.save()
        return Response(status=201)


class AddStartRatingView(APIView):
    """Добавление рейтинга товару"""

    def post(self, request):
        serializer = CreateRatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(ip=get_client_ip(request))
            return Response(status=201)
        else:
            return Response(status=400)
