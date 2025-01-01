from django.urls import path
from .views import cartView,add_to_cart,remove_from_cart,increment,decrement
urlpatterns = [
    path('', cartView.as_view(),name='cart'),
    path('add_to_cart/<int:product_id>/',add_to_cart,name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/',remove_from_cart,name='remove_from_cart'),
    path('increment/<int:id>/',increment,name='increment'),
    path('decrement/<int:id>/',decrement,name='decrement'),
]