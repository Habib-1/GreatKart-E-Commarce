from django.urls import path
from .views import home, CategoryBasedView, ProductDetailView

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('store/', CategoryBasedView.as_view(), name='store'),
    path('store/<slug:category_slug>/', CategoryBasedView.as_view(), name='category_based'),
    path('store/<slug:category_slug>/<slug:product_slug>/', ProductDetailView.as_view(), name='product_detail'),
]
