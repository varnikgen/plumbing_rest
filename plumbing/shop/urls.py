from django.urls import path

from . import views


app_name = 'shop'
urlpatterns = [
    path("product/", views.ProductListView.as_view()),
    path("product/<int:pk>", views.ProductDetailView.as_view()),
]
