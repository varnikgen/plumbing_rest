from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


app_name = 'shop'
urlpatterns = format_suffix_patterns([
    path("category/", views.CategoryListView.as_view()),
    path("category/<int:pk>", views.CategoryProductsView.as_view()),
    path("product/", views.ProductViewSet.as_view({'get': 'list'})),
    path("product/<int:pk>", views.ProductViewSet.as_view({'get': 'retrieve'})),
    path("review/", views.ReviewCreateViewSet.as_view({'post': 'create'})),
    path("rating/", views.AddStartRatingViewSet.as_view({'post': 'create'})),
])
# urlpatterns = [
#     path("category/", views.CategoryListView.as_view()),
#     path("category/<int:pk>", views.CategoryProductsView.as_view()),
#     # path("product/", views.ProductListView.as_view()),
#     # path("product/<int:pk>", views.ProductDetailView.as_view()),
#     path("product/", views.ProductViewSet.as_view()),
#     path("product/<int:pk>", views.ProductDetailView.as_view()),
#     path("review/", views.ReviewCreateView.as_view()),
#     path("rating/", views.AddStartRatingView.as_view()),
# ]
