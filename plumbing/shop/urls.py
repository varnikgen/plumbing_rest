from django.urls import path

from . import views


app_name = 'shop'
urlpatterns = [
    path("category/", views.CategoryListView.as_view()),
    path("category/<int:pk>", views.CategoryProductsView.as_view()),
    path("product/", views.ProductListView.as_view()),
    path("product/<int:pk>", views.ProductDetailView.as_view()),
    path("review/", views.ReviewCreateView.as_view()),
    path("rating/", views.AddStartRatingView.as_view()),
]
