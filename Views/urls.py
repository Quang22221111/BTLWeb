from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:item_id>/',views.product,name='product_detail'),
    path('overview/',views.product_overview),
    path('cart/',views.cart,name = "cart"),
]